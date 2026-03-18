# Quantum Finance SLR — Workspace Instructions

## Authoritative Spec

`CLAUDE.md` in the project root is the single source of truth for all requirements, schemas, and architecture decisions. Always reference it before creating or modifying files.

## Project Conventions

- **Python**: 3.11, pip + requirements.txt, argparse for CLIs
- **LLM SDKs**: anthropic + openai directly (no LangChain)
- **Secrets**: `.env` file, loaded via python-dotenv. Never hardcode API keys.
- **Logging**: Use `scripts/utils/logger.py` for all pipeline logging
- **Frontmatter**: Use `scripts/utils/frontmatter.py` for reading/writing YAML in markdown files
- **Tags**: All tags must exist in `config/tag_registry.json`. Reject unknown tags.
- **File naming**: Papers follow `YYYY_FirstAuthorLastname_ShortTitle.md` format

## Key Paths

| Path | Purpose |
|------|---------|
| `config/` | JSON configs (extraction steps, tags, source types) |
| `templates/` | Markdown templates for paper files |
| `prompts/` | LLM prompt templates for each extraction step |
| `scripts/` | Python CLI tools and pipeline scripts |
| `scripts/utils/` | Shared utilities (LLM client, frontmatter, logging) |
| `papers/raw_pdfs/` | Incoming PDFs (git-ignored) |
| `papers/processed/` | Generated markdown files (Obsidian vault) |
| `tests/` | Test suites and sample papers |
| `logs/` | Pipeline run logs (git-ignored) |

## Commit Convention

Format: `Task {N.M}: {descriptive title}` — managed by the orchestrator agent.
