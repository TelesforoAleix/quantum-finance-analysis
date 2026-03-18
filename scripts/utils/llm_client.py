"""Model-agnostic LLM call wrapper supporting Anthropic and OpenAI."""

import os
import time

import anthropic
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


class LLMClient:
    """Model-agnostic LLM call wrapper supporting Anthropic and OpenAI.

    Dispatches to the appropriate SDK based on model name prefix.
    Implements exponential backoff (3 retries: 2s, 4s, 8s).
    """

    _MAX_RETRIES = 3
    _BASE_DELAY = 2  # seconds

    def __init__(self) -> None:
        self._anthropic_client: anthropic.Anthropic | None = None
        self._openai_client: openai.OpenAI | None = None

    @property
    def anthropic_client(self) -> anthropic.Anthropic:
        if self._anthropic_client is None:
            self._anthropic_client = anthropic.Anthropic()
        return self._anthropic_client

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
        """Call an LLM model and return the response text.

        Routes to Anthropic for 'claude*' models, OpenAI for 'gpt*' models.
        Retries up to 3 times with exponential backoff on transient errors.

        Raises:
            ValueError: If the model name prefix is unrecognised.
            RuntimeError: If all retries are exhausted.
        """
        if model.startswith("claude"):
            call_fn = self._call_anthropic
        elif model.startswith("gpt"):
            call_fn = self._call_openai
        else:
            raise ValueError(
                f"Unrecognised model prefix: {model!r}. "
                "Model name must start with 'claude' or 'gpt'."
            )

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
                anthropic.RateLimitError,
                anthropic.APIStatusError,
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

    def _call_anthropic(
        self, model: str, prompt: str, temperature: float, max_tokens: int
    ) -> str:
        response = self.anthropic_client.messages.create(
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.content[0].text

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
