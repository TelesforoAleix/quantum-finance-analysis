# System Overview — Quantum Finance SLR Extraction Pipeline

> This document explains how the entire extraction pipeline works, from a PDF entering the system to a structured markdown file appearing in your Obsidian vault. Written for researchers and collaborators who want to understand the system without reading the code.

---

## Table of contents

1. [What the system does](#1-what-the-system-does)
2. [Architecture](#2-architecture)
3. [Data flow: life of a paper](#3-data-flow-life-of-a-paper)
4. [The 6 extraction steps](#4-the-6-extraction-steps)
5. [How prompts work](#5-how-prompts-work)
6. [Source-type awareness](#6-source-type-awareness)
7. [Tag system](#7-tag-system)
8. [Output format: the markdown file](#8-output-format-the-markdown-file)
9. [LLM integration](#9-llm-integration)
10. [Configuration layer](#10-configuration-layer)
11. [Processing log](#11-processing-log)
12. [CLI tools reference](#12-cli-tools-reference)
13. [File map](#13-file-map)

---

## 1. What the system does

The system takes academic PDFs about quantum computing in finance and produces structured, queryable markdown files for an Obsidian vault. Each file contains:

- Bibliographic metadata (title, authors, year, DOI)
- Source classification (e.g., peer-reviewed empirical, preprint, industry whitepaper)
- Methodology summary (algorithms, datasets, experimental setup)
- Key findings with inline evidence tags (`[supported]`, `[speculative]`, `[disputed]`)
- Limitations (author-stated and LLM-inferred)
- Synthesis tags that connect papers by topic, method, and idea

This enables the researcher to query across hundreds of papers by tag, idea, or claim — comparing what different papers say about the same topic.

---

## 2. Architecture

The system has three layers:

```
┌─────────────────────────────────────────────────────────┐
│  Layer 1: Zotero (Reference Management)                 │
│  ┌───────────────────────────────────────────────────┐  │
│  │ • Stores paper metadata and PDF attachments       │  │
│  │ • Group library: ID 6475432                       │  │
│  │ • Collection: PVDPVINK (initial-screening)        │  │
│  │ • Accessed via Zotero Web API                     │  │
│  └───────────────────────────────────────────────────┘  │
│                         │                                │
│                    PDF download                          │
│                         ▼                                │
│  Layer 2: LLM Extraction Pipeline (this system)         │
│  ┌───────────────────────────────────────────────────┐  │
│  │ fetch_from_zotero.py → extract_pdf_text.py        │  │
│  │         │                                         │  │
│  │         ▼                                         │  │
│  │ ┌─────────────────────────────────────────────┐   │  │
│  │ │ Step 1: Source classification               │   │  │
│  │ │ Step 2: Metadata extraction                 │   │  │
│  │ │ Step 3: Methodology extraction              │   │  │
│  │ │ Step 4: Findings extraction                 │   │  │
│  │ │ Step 5: Limitations extraction              │   │  │
│  │ │ Step 6: Synthesis and tagging               │   │  │
│  │ └─────────────────────────────────────────────┘   │  │
│  │         │                                         │  │
│  │         ▼                                         │  │
│  │ Structured .md file → papers/processed/           │  │
│  └───────────────────────────────────────────────────┘  │
│                         │                                │
│                    same folder                           │
│                         ▼                                │
│  Layer 3: Obsidian Vault (Knowledge Synthesis)          │
│  ┌───────────────────────────────────────────────────┐  │
│  │ • Researcher navigates, links, annotates          │  │
│  │ • Tags and wiki-links enable cross-paper queries  │  │
│  │ • Graph view shows connections between papers     │  │
│  └───────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

The Obsidian vault points directly at `papers/processed/` — there's no separate sync step.

---

## 3. Data flow: life of a paper

Here's what happens when a new paper enters the system:

```
DOI
 └→ Added to Zotero (manually or by import)
     └→ Zotero auto-fetches metadata + PDF attachment
         └→ fetch_from_zotero.py downloads PDF to papers/raw_pdfs/
             └→ extract_pdf_text.py converts PDF → plain text (.txt cache)
                 └→ Step 1: LLM classifies source type (e.g., "preprint")
                     └→ Step 2: LLM extracts metadata (title, authors, year, DOI, abstract)
                         └→ Step 3: LLM extracts methodology (algorithms, setup, dataset)
                             └→ Step 4: LLM extracts findings (claims, results, quantum advantage)
                                 └→ Step 5: LLM extracts limitations (stated + inferred)
                                     └→ Step 6: LLM reads all prior sections, assigns tags
                                         └→ Final .md file in papers/processed/
                                             └→ Visible in Obsidian immediately
```

Each step writes to the **same markdown file**, progressively filling in frontmatter fields and body sections. If a step fails, the pipeline stops and earlier sections are preserved.

### Text extraction details

- **Tool:** PyMuPDF (fitz library)
- **Caching:** Extracted text is saved as `papers/raw_pdfs/{name}.txt` — subsequent runs skip re-extraction
- **Image-only PDFs:** Detected when extracted text < 100 characters. Logged as a warning and skipped.

---

## 4. The 6 extraction steps

Each step is an independent LLM call. Steps can be run individually, re-run selectively, or skipped.

### Step 1 — Source classification

| Property | Value |
|----------|-------|
| **Reads** | First ~2,000 tokens of PDF text |
| **Writes to frontmatter** | `source_type`, `source_type_confidence`, `auto_detected` |
| **Writes to body** | — |
| **Purpose** | Classify the paper into one of 9 source types |

The 9 source types: `peer-reviewed-empirical`, `peer-reviewed-theoretical`, `preprint`, `conference-paper`, `review-article`, `technical-report`, `industry-whitepaper`, `industry-report`, `other`.

If the researcher manually corrects the source type, `auto_detected` flips to `false`. Subsequent steps use the corrected type.

### Step 2 — Metadata extraction

| Property | Value |
|----------|-------|
| **Reads** | First ~3,000 tokens of PDF text + `source_type` from step 1 |
| **Writes to frontmatter** | `title`, `authors`, `year`, `journal_or_venue`, `doi`, `aliases` |
| **Writes to body** | **Abstract summary** section |
| **Purpose** | Extract bibliographic metadata and generate an abstract summary |

Also generates Obsidian `aliases` (the full title + a short version) so the paper can be found by multiple names.

### Step 3 — Methodology extraction

| Property | Value |
|----------|-------|
| **Reads** | ~8,000 tokens of PDF text + `source_type` |
| **Writes to frontmatter** | — |
| **Writes to body** | **Methodology** section |
| **Purpose** | Describe research methods, algorithms, experimental setup, datasets |

The extraction focus changes based on source type. For an empirical paper, it emphasises algorithms and datasets. For a review article, it looks for search strategy and inclusion criteria. See [Source-type awareness](#6-source-type-awareness).

### Step 4 — Findings extraction

| Property | Value |
|----------|-------|
| **Reads** | ~8,000 tokens of PDF text + `source_type` |
| **Writes to frontmatter** | `quantum_advantage_claim` |
| **Writes to body** | **Findings** and **Quantum advantage claim** sections |
| **Purpose** | Extract key findings with inline evidence tags |

Every claim is tagged inline:
- `[supported]` — backed by empirical results in this paper
- `[speculative]` — argued theoretically, not empirically validated
- `[disputed]` — contradicts findings in other known literature

The `quantum_advantage_claim` field is set to one of: `demonstrated`, `theoretical`, `speculative`, `disputed`, `not-applicable`.

### Step 5 — Limitations extraction

| Property | Value |
|----------|-------|
| **Reads** | ~8,000 tokens of PDF text + `source_type` |
| **Writes to frontmatter** | — |
| **Writes to body** | **Limitations** and **Open questions** sections |
| **Purpose** | Capture limitations (author-stated and LLM-inferred) plus future work |

Limitations the LLM identifies that the authors did not mention are flagged with `[inferred]`.

### Step 6 — Synthesis and tagging

| Property | Value |
|----------|-------|
| **Reads** | All body sections from steps 1–5 (not the PDF — reads the markdown) |
| **Writes to frontmatter** | `topic_tags`, `methodology_tags`, `idea_tags`, `tags`, `relevance_phase1`, `relevance_phase3` |
| **Writes to body** | **Key ideas** and **Contradictions** sections |
| **Purpose** | Assign tags from controlled vocabulary, identify key ideas and contradictions |

The `tags` field uses a hierarchical format for Obsidian: `topic/portfolio-optimisation`, `method/QAOA`, `idea/quantum-advantage`, etc.

---

## 5. How prompts work

Each step has a prompt template file in `prompts/`:

| Step | Prompt file | Template variables |
|------|-------------|-------------------|
| 1 | `prompts/step1_classify.txt` | `{paper_text}` |
| 2 | `prompts/step2_metadata.txt` | `{paper_text}`, `{source_type}` |
| 3 | `prompts/step3_methodology.txt` | `{paper_text}`, `{source_type}` |
| 4 | `prompts/step4_findings.txt` | `{paper_text}`, `{source_type}` |
| 5 | `prompts/step5_limitations.txt` | `{paper_text}`, `{source_type}` |
| 6 | `prompts/step6_synthesis.txt` | `{extracted_content}` |

### How template variables are filled

- `{paper_text}` — The PDF's extracted plain text, truncated to the step's `input_tokens` limit (configured in `config/extraction_config.json`). Truncation uses a heuristic of 1 token ≈ 4 characters.
- `{source_type}` — The source type from step 1 (or manually corrected). Read from the markdown file's frontmatter.
- `{extracted_content}` — All body sections from the markdown file (Abstract summary through Open questions). Used only by step 6, which reads what earlier steps wrote rather than the raw PDF.

### How the LLM is called

1. The step runner loads the prompt template from `prompts/`
2. It substitutes the template variables using Python string formatting
3. The completed prompt is sent to the LLM as a single user message
4. The LLM response is expected to be JSON
5. The JSON is parsed (with fallback handling for markdown code fences)
6. Parsed fields are written to the appropriate frontmatter fields and body sections

### What happens if the LLM returns bad JSON

The parser tries several recovery strategies:
1. Strip markdown code fences (```json ... ```)
2. Extract content between first `{` and last `}`
3. If all parsing fails, the step is marked as failed and the pipeline stops (for `extract_paper.py`) or continues to the next paper (for batch mode)

---

## 6. Source-type awareness

Steps 3, 4, and 5 change their extraction focus based on the paper's source type. This is embedded directly in the prompt text — the prompt contains a table of per-type instructions, and the `{source_type}` variable tells the LLM which row to follow.

For example, for methodology extraction (step 3):

| Source type | Extraction focus |
|-------------|------------------|
| `peer-reviewed-empirical` | Research design, quantum algorithms, hardware (simulator vs. QPU), dataset, metrics, baselines |
| `peer-reviewed-theoretical` | Theoretical framework, formal model, proof technique, assumptions |
| `review-article` | Search strategy, inclusion/exclusion criteria, number of papers, synthesis method |
| `industry-whitepaper` | Claimed approach, note absence of methods, identify supporting evidence |

The full per-type extraction guidance for all 9 types is defined in two places:
- **`config/source_types.json`** — Structured data with `step3_focus`, `step4_focus`, `step5_focus` fields
- **`prompts/step{3,4,5}_*.txt`** — The same guidance embedded in the prompts as natural language instructions

---

## 7. Tag system

Tags connect papers across the vault. All tags must exist in `config/tag_registry.json` — unknown tags are rejected during validation.

### Tag categories

**Topic tags** (10 tags) — Financial use cases:
`portfolio-optimisation`, `risk-modelling`, `derivatives-pricing`, `fraud-detection`, `credit-scoring`, `high-frequency-trading`, `asset-pricing`, `quantum-cryptography`, `regulatory-compliance`, `market-simulation`

**Methodology tags** (13 tags) — Quantum algorithms and techniques:
`QAOA`, `VQE`, `quantum-annealing`, `HHL`, `quantum-ML`, `quantum-SVM`, `amplitude-estimation`, `QUBO`, `variational`, `grover`, `quantum-walk`, `quantum-simulation`, `classical-simulation`

**Synthesis tags** (10 tags) — Ideas, contradictions, and limitations:
- Ideas: `idea:quantum-advantage`, `idea:near-term-feasibility`, `idea:hybrid-approach`
- Contradictions: `contradiction:classical-vs-quantum`, `contradiction:scalability`
- Limitations: `limitation:qubit-count`, `limitation:noise`, `limitation:data-encoding`, `limitation:no-empirical-validation`, `limitation:simulation-only`

### How tags appear in Obsidian

In the YAML frontmatter, tags use a hierarchical format with `/` separators:

```yaml
tags:
  - topic/portfolio-optimisation
  - method/QAOA
  - method/variational
  - idea/quantum-advantage
  - limitation/simulation-only
```

This creates a browsable tag tree in Obsidian's tag pane. Separate `topic_tags`, `methodology_tags`, and `idea_tags` fields also store the raw tag names for programmatic access.

### Custom tags

New tags can be added following these formats:
- `idea:[concept]` (e.g., `idea:error-mitigation`)
- `contradiction:[concept]` (e.g., `contradiction:encoding-overhead`)
- `limitation:[concept]` (e.g., `limitation:training-instability`)

All new tags must be registered in `config/tag_registry.json` before use. See the [Tuning Guide](TUNING_GUIDE.md) for instructions.

---

## 8. Output format: the markdown file

Each processed paper produces a single `.md` file in `papers/processed/`.

### File naming

```
YYYY_FirstAuthorLastname_ShortTitle.md
Example: 2023_Bova_QuantumFinanceReview.md
```

### Frontmatter fields (YAML header)

| Field | Set by | Description |
|-------|--------|-------------|
| `zotero_key` | Zotero fetch | Zotero item key |
| `title` | Step 2 | Full paper title |
| `authors` | Step 2 | List of author names |
| `year` | Step 2 | Publication year |
| `journal_or_venue` | Step 2 | Journal, conference, or platform name |
| `doi` | Step 2 | DOI string |
| `aliases` | Step 2 | Obsidian aliases (full title + short form) |
| `source_type` | Step 1 | One of 9 source types |
| `source_type_confidence` | Step 1 | `high`, `medium`, or `low` |
| `auto_detected` | Step 1 | `true` unless researcher manually corrected |
| `topic_tags` | Step 6 | List of topic tags |
| `methodology_tags` | Step 6 | List of methodology tags |
| `idea_tags` | Step 6 | List of idea/synthesis tags |
| `tags` | Step 6 | Unified hierarchical tags for Obsidian |
| `quantum_advantage_claim` | Step 4 | `demonstrated`, `theoretical`, `speculative`, `disputed`, or `not-applicable` |
| `relevance_phase1` | Step 6 | `high`, `medium`, or `low` |
| `relevance_phase3` | Step 6 | `high`, `medium`, `low`, or `not-yet-assessed` |
| `related_papers` | Step 6 | Links to related papers |
| `contradiction_flags` | Step 6 | Contradiction indicators |
| `steps_completed` | All steps | List of completed step numbers `[1, 2, 3, 4, 5, 6]` |
| `step{N}_model` | Each step | LLM model used |
| `step{N}_date` | Each step | ISO timestamp of extraction |

### Body sections

| Section | Written by | Content |
|---------|-----------|---------|
| **Abstract summary** | Step 2 | Plain-language summary of the paper |
| **Methodology** | Step 3 | Research methods, algorithms, setup, datasets |
| **Findings** | Step 4 | Key results with `[supported]`/`[speculative]`/`[disputed]` tags |
| **Quantum advantage claim** | Step 4 | Classification and explanation |
| **Limitations** | Step 5 | Author-stated + `[inferred]` limitations |
| **Open questions** | Step 5 | Unresolved questions and future work |
| **Key ideas** | Step 6 | Bullet list with `#idea:` and `#limitation:` tags |
| **Contradictions** | Step 6 | Where this paper contradicts others |
| **Notable quotes** | Researcher | Manually added verbatim quotes with page references |
| **Researcher notes** | Researcher | Personal synthesis, connections, flags |

The last two sections are never overwritten by the pipeline — they're reserved for the researcher.

---

## 9. LLM integration

### Current setup

The pipeline uses **Azure AI Foundry** with the **Mistral-Large-3** model deployment.

| Component | Detail |
|-----------|--------|
| Provider | Azure AI Foundry |
| Model | Mistral-Large-3 (all 6 steps) |
| API | OpenAI-compatible via `openai.AzureOpenAI` client |
| Rate limit | 20 requests per minute (client-enforced) + 20K tokens per minute (Azure-enforced) |
| Retries | 3 attempts with exponential backoff (2s → 4s → 8s) |

### Model routing

The LLM client routes calls based on the model name:
- If the model name is in the `AZURE_DEPLOYMENTS` environment variable → Azure AI Foundry
- If the model name starts with `gpt` → Standard OpenAI API
- Otherwise → Azure AI Foundry (default)

This allows mixing models — for example, using Mistral-Large-3 for most steps but GPT-4o for synthesis.

### Rate limiting

A sliding-window rate limiter tracks the last 60 seconds of requests. If 20 requests have been made in the last minute, the client blocks until a slot opens. This prevents Azure 429 (Too Many Requests) errors.

Azure also enforces a 20,000 tokens-per-minute limit server-side. When hit, the client's retry logic (exponential backoff) handles the delay.

---

## 10. Configuration layer

Three JSON files control the pipeline's behaviour:

### `config/extraction_config.json`

Central configuration for all extraction steps. Contains:
- **Global settings:** `default_model`, `fallback_model`, `zotero_group_id`, paths
- **Per-step settings:** For each step (1–6):
  - `model` — Which LLM to use
  - `temperature` — Sampling temperature (lower = more deterministic)
  - `max_tokens` — Maximum response length
  - `prompt_file` — Path to the prompt template
  - `input_tokens` — How many tokens of PDF text to include (0 = no truncation)

### `config/tag_registry.json`

The controlled vocabulary of all valid tags. Organised into three sections:
- `topic_tags` — 10 financial use case tags
- `methodology_tags` — 13 quantum algorithm/technique tags
- `synthesis_tags` — 10 idea, contradiction, and limitation tags

Any tag not in this file is rejected during validation.

### `config/source_types.json`

Defines the 9 source types with:
- `template_file` — Path to a source-type-specific markdown template
- `classification_signals` — Text patterns that indicate this source type
- `step3_focus`, `step4_focus`, `step5_focus` — Per-type extraction guidance

---

## 11. Processing log

`processing_log.json` in the project root tracks which steps have been completed for each paper. Example:

```json
{
  "papers": {
    "2023_Bova_QuantumFinance.md": {
      "steps_completed": [1, 2, 3, 4, 5, 6],
      "step1_date": "2026-03-18T20:37:29.695922",
      "step1_model": "Mistral-Large-3",
      "step2_date": "2026-03-18T20:37:35.123456",
      "step2_model": "Mistral-Large-3",
      "last_updated": "2026-03-18T20:40:15.789123"
    }
  }
}
```

This log enables:
- Resuming interrupted batch runs (skip papers that already completed a step)
- Filtering papers by completion status
- Auditing which model was used for each step and when

---

## 12. CLI tools reference

| Script | Purpose | Example |
|--------|---------|---------|
| `scripts/fetch_from_zotero.py` | Download PDFs from Zotero | `python scripts/fetch_from_zotero.py --collection PVDPVINK` |
| `scripts/extract_pdf_text.py` | Extract text from a PDF | `python scripts/extract_pdf_text.py --file paper.pdf` |
| `scripts/extract_paper.py` | Run full pipeline on one paper | `python scripts/extract_paper.py --pdf papers/raw_pdfs/paper.pdf --name 2024_Author_Title.md` |
| `scripts/run_extraction_step.py` | Run specific step(s) | `python scripts/run_extraction_step.py --paper file.md --step 4` |
| `scripts/validate_markdown.py` | Validate schema compliance | `python scripts/validate_markdown.py --batch` |
| `scripts/sync_obsidian.py` | Sync to Obsidian vault | `python scripts/sync_obsidian.py` |

### Key CLI patterns

```bash
# Process a new paper (all 6 steps)
python scripts/extract_paper.py --pdf papers/raw_pdfs/paper.pdf --name 2024_Author_Title.md

# Re-run a single step on a paper
python scripts/run_extraction_step.py --paper 2024_Author_Title.md --step 4

# Re-run from step 3 onwards (after editing step 2 output)
python scripts/run_extraction_step.py --paper 2024_Author_Title.md --from-step 3

# Batch re-run step 6 on all papers (after changing tag vocabulary)
python scripts/run_extraction_step.py --batch --step 6

# Fetch from Zotero and auto-process new papers
python scripts/fetch_from_zotero.py --collection PVDPVINK --process

# Validate all papers
python scripts/validate_markdown.py --batch
```

---

## 13. File map

```
project-root/
├── CLAUDE.md                           # Full project specification
├── README.md                           # Setup and usage guide
├── docs/
│   ├── SYSTEM_OVERVIEW.md              # This file
│   └── TUNING_GUIDE.md                 # How to modify the system
│
├── .env                                # API keys (not in git)
├── .env.example                        # Template for .env
├── requirements.txt                    # Python dependencies
├── processing_log.json                 # Per-paper step completion tracker
│
├── config/
│   ├── extraction_config.json          # Step parameters, models, token limits
│   ├── tag_registry.json               # Controlled tag vocabulary
│   └── source_types.json               # Source type definitions
│
├── prompts/
│   ├── step1_classify.txt              # Source classification prompt
│   ├── step2_metadata.txt              # Metadata extraction prompt
│   ├── step3_methodology.txt           # Methodology prompt (source-type-aware)
│   ├── step4_findings.txt              # Findings prompt (source-type-aware)
│   ├── step5_limitations.txt           # Limitations prompt (source-type-aware)
│   └── step6_synthesis.txt             # Synthesis prompt (reads prior sections)
│
├── templates/
│   └── paper_base.md                   # Blank paper template (all fields + sections)
│
├── scripts/
│   ├── extract_paper.py                # Full pipeline orchestrator
│   ├── run_extraction_step.py          # Run/re-run individual steps
│   ├── fetch_from_zotero.py            # Download PDFs from Zotero API
│   ├── extract_pdf_text.py             # PDF → plain text
│   ├── validate_markdown.py            # Schema validation
│   ├── sync_obsidian.py                # Vault sync (no-op if same directory)
│   └── utils/
│       ├── llm_client.py               # LLM API wrapper (Azure + OpenAI)
│       ├── step_runner.py              # Step dispatch engine
│       ├── frontmatter.py              # YAML frontmatter read/write
│       ├── text_chunker.py             # Token-aware text truncation
│       ├── tag_validator.py            # Tag registry validation
│       ├── processing_log.py           # Processing log management
│       └── logger.py                   # Structured JSON logging
│
├── papers/
│   ├── raw_pdfs/                       # Downloaded PDFs + text cache (not in git)
│   └── processed/                      # Output markdown files (Obsidian vault)
│
└── tests/
    └── test_schema_validation.py       # 25 pytest tests for schema compliance
```
