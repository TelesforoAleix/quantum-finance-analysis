"""Model-agnostic LLM call wrapper supporting Azure AI Foundry and OpenAI."""

import os
import time
from collections import deque

import openai
from dotenv import load_dotenv

from .logger import get_logger

logger = get_logger("llm_client")


def _find_project_root() -> str:
    """Walk up from this file to find the directory containing CLAUDE.md."""
    current = os.path.dirname(os.path.abspath(__file__))
    for _ in range(10):
        if os.path.isfile(os.path.join(current, "CLAUDE.md")):
            return current
        current = os.path.dirname(current)
    return os.getcwd()


# Load .env from project root
load_dotenv(os.path.join(_find_project_root(), ".env"))


class RateLimiter:
    """Simple sliding-window rate limiter for requests per minute."""

    def __init__(self, max_requests_per_minute: int = 20) -> None:
        self._max_rpm = max_requests_per_minute
        self._timestamps: deque[float] = deque()

    def wait_if_needed(self) -> None:
        """Block until we can make another request without exceeding RPM."""
        now = time.monotonic()
        # Remove timestamps older than 60 seconds
        while self._timestamps and self._timestamps[0] < now - 60:
            self._timestamps.popleft()

        if len(self._timestamps) >= self._max_rpm:
            sleep_time = 60 - (now - self._timestamps[0]) + 0.1
            if sleep_time > 0:
                logger.info(
                    "Rate limit: waiting %.1f seconds", sleep_time
                )
                time.sleep(sleep_time)

        self._timestamps.append(time.monotonic())


class LLMClient:
    """LLM client supporting Azure AI Foundry deployments.

    Routes to Azure OpenAI for the configured deployment,
    with fallback to standard OpenAI for gpt* models.
    Implements exponential backoff (3 retries: 2s, 4s, 8s).
    """

    _MAX_RETRIES = 3
    _BASE_DELAY = 2  # seconds

    def __init__(self) -> None:
        self._azure_client: openai.AzureOpenAI | None = None
        self._openai_client: openai.OpenAI | None = None
        self._rate_limiter = RateLimiter()
        self._azure_deployment = os.getenv("AZURE_DEPLOYMENT", "")

    @property
    def azure_client(self) -> openai.AzureOpenAI:
        if self._azure_client is None:
            self._azure_client = openai.AzureOpenAI(
                api_key=os.getenv("AZURE_API_KEY"),
                azure_endpoint=os.getenv("AZURE_ENDPOINT", ""),
                api_version=os.getenv("AZURE_API_VERSION", "2024-05-01-preview"),
            )
        return self._azure_client

    @property
    def openai_client(self) -> openai.OpenAI:
        if self._openai_client is None:
            self._openai_client = openai.OpenAI()
        return self._openai_client

    def call(
        self,
        model: str,
        prompt: str,
        temperature: float = 0.3,
        max_tokens: int = 1500,
    ) -> str:
        """Call an LLM and return the response text.

        Routes to Azure for the configured deployment name,
        standard OpenAI for gpt* models, and Azure as default.

        Raises:
            RuntimeError: If all retries are exhausted.
        """
        if model == self._azure_deployment or not model.startswith("gpt"):
            call_fn = self._call_azure
        else:
            call_fn = self._call_openai

        # Enforce RPM rate limit before attempting the call
        self._rate_limiter.wait_if_needed()

        last_error: Exception | None = None
        for attempt in range(1, self._MAX_RETRIES + 1):
            try:
                start = time.monotonic()
                result = call_fn(model, prompt, temperature, max_tokens)
                elapsed = time.monotonic() - start
                logger.info(
                    "LLM call succeeded",
                    extra={
                        "model": model,
                        "attempt": attempt,
                        "latency_s": round(elapsed, 2),
                        "prompt_len": len(prompt),
                        "response_len": len(result),
                    },
                )
                return result
            except (
                openai.RateLimitError,
                openai.APIStatusError,
            ) as exc:
                last_error = exc
                delay = self._BASE_DELAY * (2 ** (attempt - 1))
                logger.warning(
                    "LLM call failed, retrying",
                    extra={
                        "model": model,
                        "attempt": attempt,
                        "error": str(exc),
                        "retry_delay_s": delay,
                    },
                )
                time.sleep(delay)

        raise RuntimeError(
            f"LLM call to {model} failed after {self._MAX_RETRIES} retries: {last_error}"
        )

    def _call_azure(
        self, model: str, prompt: str, temperature: float, max_tokens: int
    ) -> str:
        response = self.azure_client.chat.completions.create(
            model=self._azure_deployment,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content

    def _call_openai(
        self, model: str, prompt: str, temperature: float, max_tokens: int
    ) -> str:
        response = self.openai_client.chat.completions.create(
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content
