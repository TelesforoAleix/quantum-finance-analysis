# Quantum Finance SLR — Extraction Pipeline

Automated extraction pipeline for a systematic literature review on quantum computing in financial services. Part of an MSc thesis at Copenhagen Business School.

The system fetches PDFs from Zotero, extracts structured knowledge using LLMs (6 modular steps), and outputs queryable markdown files for an Obsidian vault.

## Quick start

```bash
# Clone and enter repo
git clone https://github.com/TelesforoAleix/quantum-finance-analysis.git
cd quantum-finance-analysis

# Install dependencies
pip install -r requirements.txt

# Configure API keys
cp .env.example .env
# Edit .env with your Anthropic, OpenAI, and Zotero API keys
```

## Usage

```bash
# Process a single paper (all 6 steps)
python scripts/extract_paper.py --pdf papers/raw_pdfs/sample.pdf

# Run a specific extraction step
python scripts/run_extraction_step.py --paper 2023_Bova_QuantumFinance.md --step 4

# Re-run from a step onwards (after editing step 3)
python scripts/run_extraction_step.py --paper 2023_Bova_QuantumFinance.md --from-step 4

# Batch re-run step 6 on all papers
python scripts/run_extraction_step.py --batch --step 6

# Validate all processed papers against schema
python scripts/validate_markdown.py --batch
```

## Repository structure

```
CLAUDE.md                    # Full project spec (single source of truth)
.github/agents/              # VS Code Copilot agents (orchestrator, designer, coder, tester)
config/                      # JSON configs (extraction steps, tags, source types)
templates/                   # Markdown templates for paper files
prompts/                     # LLM prompt templates for each extraction step
scripts/                     # Python CLI tools and pipeline scripts
scripts/utils/               # Shared utilities (LLM client, frontmatter, logging)
papers/raw_pdfs/             # Incoming PDFs from Zotero (git-ignored)
papers/processed/            # Generated markdown files (Obsidian vault)
tests/                       # Test suites and sample papers
logs/                        # Pipeline run logs (git-ignored)
```

## Development

This project uses VS Code with GitHub Copilot. Four custom agents coordinate development:

- **@orchestrator** — primary agent, coordinates tasks and manages commits
- **@designer** — creates configs, schemas, templates
- **@coder** — writes Python implementation
- **@tester** — validates outputs and runs tests

Start with `@orchestrator` in VS Code chat. See `CLAUDE.md` for the full specification.

## Research phases

1. **Broad SLR** — ~2,800 → ~400–500 papers, LLM-extracted to Obsidian
2. **Expert interviews** — validate clusters, select use case
3. **Focused deep-dive** — re-filter knowledge base for selected use case
4. **Experiment** — reproduce or extend key findings

## Development progress

### Milestone 1 — Foundation (complete)
Repository structure, configuration files, core utilities (LLM client, frontmatter, structured logging), PDF text extraction, paper template, schema validation, and processing log. All infrastructure needed for the extraction pipeline is in place.
