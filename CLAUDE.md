# CLAUDE.md — quantum finance SLR automation system

> This file is the single source of truth for the project. It is read by GitHub Copilot (claude-opus-4-6) at the start of every session. It defines the research context, the system to be built, the data architecture, the extraction pipeline, the agent roles, and the development process. Do not modify this file without updating all affected sections.

---

## 1. Project context

### 1.1 Research goal

This project supports an MSc thesis at Copenhagen Business School on **quantum computing in financial services**. The thesis follows a four-phase research structure:

- **Phase 1 — Broad systematic literature review (SLR):** Map the landscape of quantum computing applications in finance across ~400–500 screened papers. Identify use cases, methodologies, and emerging themes.
- **Phase 2 — Expert interviews:** Validate Phase 1 findings with practitioners and researchers. Narrow focus to one specific use case or vertical.
- **Phase 3 — Deep-dive review:** Re-examine the knowledge base filtered to the selected use case. Build the theoretical and methodological foundation for the experiment.
- **Phase 4 — Experiment:** Design and execute a focused experiment based on the selected use case. Reproduce or extend findings from key papers.

### 1.2 The problem this system solves

The researcher will screen ~2,800 papers and work intensively with ~400–500 of them. Manually extracting and linking insights across that volume is not feasible. This system automates the extraction of structured knowledge from PDFs using LLMs, stores the results as queryable markdown files, and enables the researcher to synthesize findings across heterogeneous sources — comparing claims, surfacing contradictions, and grouping papers by idea, method, use case, or limitation.

### 1.3 What success looks like

At the end of the build, the researcher should be able to:

1. Import a list of DOIs into Zotero, trigger the pipeline, and receive structured markdown files for each paper in an Obsidian vault.
2. Run individual extraction steps on a single paper, review the output, edit it if needed, and re-run downstream steps without touching the rest of the batch.
3. Query the knowledge base by tag (e.g. "all papers mentioning portfolio optimisation as a use case") and get a list of papers with their relevant extracted sections.
4. See which papers support, contradict, or are silent on a given idea or claim.

---

## 2. Technical architecture

### 2.1 Three-layer system

The system has three layers. Each layer has a single responsibility and clean handoffs between them.

```
Layer 1: Zotero (reference management)
  └─ Stores all paper metadata and PDF attachments
  └─ Shared group library for collaboration
  └─ Zotero Web API is the programmatic entry point

Layer 2: LLM extraction pipeline (the system to build)
  └─ Fetches PDFs from Zotero via API
  └─ Extracts plain text from PDFs
  └─ Runs modular LLM extraction steps
  └─ Writes structured markdown files to the Obsidian vault

Layer 3: Obsidian vault (knowledge synthesis)
  └─ Receives markdown files from the pipeline
  └─ Researcher navigates, links, and annotates
  └─ Tags and wiki-links enable cross-paper synthesis
```

### 2.2 Data flow

```
[DOI list]
  → Zotero (import by DOI, auto-fetch metadata + PDF)
    → Zotero Web API (fetch attachment)
      → PDF text extraction (PyMuPDF or pdfplumber)
        → Step 1: Source classification
        → Step 2: Metadata extraction
        → Step 3: Methodology extraction
        → Step 4: Findings extraction
        → Step 5: Limitations extraction
        → Step 6: Synthesis and tagging
          → Structured .md file written to Obsidian vault
            → Researcher reviews, edits, re-runs steps as needed
```

**v2/v3 cross-paper analysis flow:**

```
[Processed .md files in papers/processed/]
  → Tag discovery (LLM suggests new tags → researcher approves)
  → Enhanced experiment details (Step 3 expanded)
  → Citation graph (OpenAlex API → analysis/citation_index.json)
  → Thematic indices (analysis/by_topic/, analysis/by_method/, analysis/by_claim/)
    → Contradiction detection (LLM compares claims across papers)
      → Experiment design assistant (interactive agent)
```

### 2.3 Technology stack

| Component | Tool | Notes |
|-----------|------|-------|
| Reference management | Zotero (shared group library) | Import by DOI, PDF storage, citation export |
| PDF text extraction | PyMuPDF or pdfplumber | Convert PDF to plain text for LLM input |
| LLM provider | Anthropic Claude (claude-opus-4-6) primary | Model-agnostic — OpenAI fallback supported |
| Knowledge base | Obsidian vault | Markdown files, wiki-links, tag graph |
| Version control | Git | Vault tracked, PDFs not committed |
| IDE | VS Code + GitHub Copilot | Copilot uses claude-opus-4-6 |

### 2.4 Important Zotero API limitation

The Zotero API returns attachment metadata and download links but does not extract full text from PDFs. Full-text extraction requires a separate parsing step after PDF retrieval. The pipeline must handle this explicitly.

---

## 3. Modular extraction pipeline

### 3.1 Design principles

- **Modular:** Each extraction step is independent. Steps can be run individually, re-run selectively, or skipped.
- **Editable:** Every step outputs to a named section in the markdown file. The researcher can edit any section and re-run downstream steps without re-running upstream ones.
- **Source-type-aware:** Extraction prompts are parameterized by source type. A peer-reviewed empirical paper uses different extraction logic than a whitepaper.
- **Model-agnostic:** The pipeline can route different steps to different LLM providers for quality benchmarking.
- **Auditable:** Each markdown file records which model ran each step and when.

### 3.2 The six extraction steps

#### Step 1 — Source classification

- **Input:** PDF full text (first 2,000 tokens sufficient)
- **Output fields:**
  - `source_type`: one of the values below
  - `source_type_confidence`: `high`, `medium`, `low`
  - `auto_detected`: `true` (flipped to `false` if researcher manually corrects)
- **Edit behaviour:** If researcher changes `source_type`, flip `auto_detected: false`. Re-running steps 2–6 will use the corrected source type.
- **Notes:** Zotero's `itemType` is a starting signal but not reliable enough to depend on alone. LLM should assess based on PDF content structure (does it have an abstract, methods section, peer-review indicators, etc.).

**Source type classification signatures:**

| Source type | Key signals |
|-------------|-------------|
| `peer-reviewed-empirical` | Methods section, results section, statistical analysis, peer review indicators (journal/conference), novel data or experiments |
| `peer-reviewed-theoretical` | Formal proofs, propositions, theoretical framework, no experimental section or simulated only |
| `preprint` | arXiv, SSRN, or similar preprint server DOI; no journal assignment; may lack peer review statement |
| `conference-paper` | Conference proceedings, workshop paper, symposium presentation |
| `review-article` | Explicit inclusion/exclusion criteria, PRISMA or similar protocol, synthesis of existing literature rather than novel contribution |
| `technical-report` | Government, standards body, or institutional authorship; technical depth without academic peer review |
| `industry-whitepaper` | No methods section, vendor or organisation authorship, advocacy tone, limited citations |
| `industry-report` | Market research, consulting firm, or industry body authorship; data often proprietary |
| `other` | Does not fit the above categories |

#### Step 2 — Metadata extraction

- **Input:** PDF full text + `source_type`
- **Output fields:** `title`, `authors`, `year`, `journal_or_venue`, `doi`, `abstract_summary`
- **Notes:** Most of this is also in Zotero — this step reconciles and supplements. Flag discrepancies.
- **Edit behaviour:** Editable. Re-run steps 3–6 if corrected.

#### Step 3 — Methodology extraction

- **Input:** PDF full text + `source_type`
- **Output fields:** `methodology_description`, `algorithms_used`, `frameworks`, `experimental_setup`, `dataset_used`
- **Experiment detail fields (v2):**
  - `experiment_input`: dataset details (source, size, features, preprocessing)
  - `experiment_process`: algorithm pipeline, parameter choices, convergence criteria
  - `experiment_output`: result format, metrics reported, baselines
  - `experiment_parameters`: qubit count, circuit depth, shots, optimizer, hyperparameters
  - `hardware_details`: simulator name, QPU model, cloud provider
  - `reproducibility_notes`: code availability, data availability, replication feasibility
- **Edit behaviour:** Editable. Re-run steps 5–6 if corrected.

**Source-type extraction emphasis for Step 3:**

| Source type | Extraction focus |
|-------------|------------------|
| `peer-reviewed-empirical` | Research design, quantum algorithm(s) used (QAOA, VQE, HHL, etc.), hardware (simulator vs. real QPU), dataset, evaluation metrics, baseline comparisons |
| `peer-reviewed-theoretical` | Theoretical framework, formal model, proof technique, assumptions, propositions |
| `preprint` | Treat as empirical or theoretical based on content. Flag as preprint in frontmatter |
| `conference-paper` | Same as empirical/theoretical; note if short paper or workshop paper |
| `review-article` | Search strategy, inclusion/exclusion criteria, number of papers included, synthesis method, classification taxonomy |
| `technical-report` | Technical specifications, standards referenced, scope of analysis |
| `industry-whitepaper` | Claimed approach or framework. Note absence of formal methods section. Identify supporting evidence (if any) |
| `industry-report` | Market methodology, data sources, analytical framework |

#### Step 4 — Findings extraction

- **Input:** PDF full text + `source_type`
- **Output fields:** `key_findings`, `results_summary`, `performance_claims`, `quantum_advantage_claim`
- **Quantum advantage claim values:** `demonstrated`, `theoretical`, `speculative`, `disputed`, `not-applicable`
- **Edit behaviour:** Editable. Re-run steps 5–6 if corrected.

**Inline claim tagging:** Every claim in the Findings section must be tagged inline:
- `[supported]` — claim backed by empirical results in this paper
- `[speculative]` — argued theoretically, not empirically validated
- `[disputed]` — contradicts findings in other known literature

**Source-type extraction emphasis for Step 4:**

| Source type | Extraction focus |
|-------------|------------------|
| `peer-reviewed-empirical` | Quantified results with confidence intervals if available. Flag quantum advantage claims. Note whether results are from simulation or real hardware |
| `peer-reviewed-theoretical` | Key propositions or theorems, claimed complexity advantages, conditions under which claims hold |
| `preprint` | Default quantum advantage claims to `[speculative]` unless strong empirical support is present |
| `conference-paper` | Same as empirical/theoretical |
| `review-article` | Key themes identified, consensus findings, areas of disagreement across reviewed literature |
| `technical-report` | Recommendations, technical conclusions, policy implications |
| `industry-whitepaper` | Claims made. Default all to `[speculative]` unless backed by cited peer-reviewed evidence. Note vendor context |
| `industry-report` | Market findings, trend claims, projections. Note proprietary data context |

#### Step 5 — Limitations extraction

- **Input:** PDF full text + `source_type`
- **Output fields:** `limitations`, `open_questions`, `future_work`
- **Notes:** Capture both author-stated limitations and limitations the LLM identifies that the authors do not mention explicitly (flag the latter as `[inferred]`).
- **Edit behaviour:** Editable. Re-run step 6 if corrected.

**Source-type extraction emphasis for Step 5:**

| Source type | Extraction focus |
|-------------|------------------|
| `peer-reviewed-empirical` | Internal validity, hardware noise, qubit count constraints, dataset size, scalability to production, reproducibility |
| `peer-reviewed-theoretical` | Assumptions required, gap between theoretical and practical performance, missing empirical validation |
| `preprint` | Same as empirical/theoretical; additionally flag lack of peer review |
| `conference-paper` | Same as empirical/theoretical; note page-limit constraints |
| `review-article` | Search coverage gaps, recency, language bias, grey literature exclusion |
| `technical-report` | Scope constraints, institutional mandate limitations, currency of data |
| `industry-whitepaper` | Lack of peer review, potential vendor bias, missing reproducibility, proprietary data |
| `industry-report` | Proprietary methodology, potential bias, limited reproducibility |

#### Step 6 — Synthesis and tagging

- **Input:** All sections from steps 1–5 (reads existing markdown, not the PDF)
- **Output fields:** `topic_tags`, `methodology_tags`, `idea_tags`, `contradiction_flags`, `related_papers`, `relevance_phase1`, `relevance_phase3`
- **Notes:** This step reads the already-extracted sections and applies the unified tag vocabulary. It also looks for potential contradictions with other papers if a cross-paper index is available.
- **Edit behaviour:** Fully editable. This step can always be re-run without touching steps 1–5.

### 3.3 Selective re-run logic

The pipeline must support:

```bash
# Re-run a specific step on a specific paper
python run_extraction_step.py --paper 2023_Bova_QuantumFinance.md --step 4

# Re-run from a step onwards (e.g. after editing step 3)
python run_extraction_step.py --paper 2023_Bova_QuantumFinance.md --from-step 4

# Re-run only papers where source type was manually corrected
python run_extraction_step.py --batch --filter auto_detected=false --from-step 2

# Re-run step 6 (synthesis) on all papers
python run_extraction_step.py --batch --step 6
```

---

## 4. Markdown schema

### 4.1 File naming

```
YYYY_FirstAuthorLastname_ShortTitle.md
Example: 2023_Bova_QuantumFinanceReview.md
```

### 4.2 Full frontmatter spec

```yaml
---
zotero_key: ""
title: ""
authors: []
year:
journal_or_venue: ""
doi: ""
paper_type: ""
source_type: ""
source_type_confidence: high | medium | low
auto_detected: true
topic_tags: []
methodology_tags: []
idea_tags: []
classification: generic | application-specific
evidence_type: empirical | theoretical | mixed
quantum_advantage_claim: demonstrated | theoretical | speculative | disputed | not-applicable
relevance_phase1: high | medium | low
relevance_phase3: high | medium | low | not-yet-assessed
related_papers: []
contradiction_flags: []
steps_completed: []
step1_model: ""
step2_model: ""
step3_model: ""
step4_model: ""
step5_model: ""
step6_model: ""
step1_date: ""
step2_date: ""
step3_date: ""
step4_date: ""
step5_date: ""
step6_date: ""
---
```

### 4.3 Body sections

```markdown
## Abstract summary
[Step 2 output — plain language summary]

## Methodology
[Step 3 output — varies by source type]

## Experiment details
[Step 3 output — structured experiment replication details]

## Findings
[Step 4 output — results, claims, performance]

## Quantum advantage claim
[Step 4 output — stated claim + classification tag]

## Limitations
[Step 5 output — author-stated + [inferred] limitations]

## Open questions
[Step 5 output]

## Key ideas
[Step 6 output — bullet list with idea tags]
- #idea:portfolio-optimisation — statement of idea as paper frames it

## Contradictions
[Step 6 output — where this paper contradicts others]
- #idea:quantum-advantage — contradicts [[2022_Other_Paper]] which claims X

## Notable quotes
[Researcher-added — verbatim quotes with page references]
> "Quote here." (p. 12)

## Researcher notes
[Researcher-added — not LLM generated. Personal synthesis, connections to interviews, Phase 3 flags.]
```

### 4.4 Tag vocabulary

All tags use lowercase hyphenated format. Tags are defined in `config/tag_registry.json` — do not use undeclared tags.

**Topic tags (use cases)**

| Tag | Description |
|-----|-------------|
| `#portfolio-optimisation` | Asset allocation, portfolio construction, QUBO formulations, Markowitz variants |
| `#risk-modelling` | VaR, CVaR, credit risk, market risk, stress testing |
| `#derivatives-pricing` | Options pricing, Monte Carlo, structured products |
| `#fraud-detection` | Anomaly detection, classification, transaction monitoring |
| `#credit-scoring` | Loan approval, default prediction, creditworthiness assessment |
| `#high-frequency-trading` | Execution optimisation, latency, algorithmic trading |
| `#asset-pricing` | Factor models, pricing of financial instruments |
| `#quantum-cryptography` | QKD, post-quantum cryptography in financial contexts |
| `#regulatory-compliance` | AML, KYC, reporting automation |
| `#market-simulation` | Agent-based models, market microstructure, scenario generation |

**Methodology tags**

| Tag | Description |
|-----|-------------|
| `#QAOA` | Quantum Approximate Optimisation Algorithm |
| `#VQE` | Variational Quantum Eigensolver |
| `#quantum-annealing` | D-Wave or similar annealing-based approaches |
| `#HHL` | Harrow-Hassidim-Lloyd algorithm for linear systems |
| `#quantum-ML` | Quantum machine learning, QNNs, quantum kernel methods |
| `#quantum-SVM` | Quantum support vector machines |
| `#amplitude-estimation` | Quantum amplitude estimation for Monte Carlo speedup |
| `#QUBO` | Quadratic Unconstrained Binary Optimisation formulation |
| `#variational` | General variational quantum algorithms (covers QAOA and VQE) |
| `#grover` | Grover's search algorithm and variants |
| `#quantum-walk` | Quantum walk algorithms |
| `#quantum-simulation` | Hamiltonian simulation for financial models |
| `#classical-simulation` | Classical simulation of quantum circuits |

**Synthesis tags (pre-registered idea, contradiction, and limitation tags)**

| Tag | Description |
|-----|-------------|
| `#idea:quantum-advantage` | A claim about where quantum outperforms classical |
| `#idea:near-term-feasibility` | Claims about NISQ-era applicability |
| `#idea:hybrid-approach` | Quantum-classical hybrid as the practical path |
| `#contradiction:classical-vs-quantum` | Paper contradicts claims about quantum superiority |
| `#contradiction:scalability` | Paper contradicts claims about scaling to real problems |
| `#limitation:qubit-count` | Insufficient qubits for practical problems |
| `#limitation:noise` | Hardware noise degrades results |
| `#limitation:data-encoding` | Cost of encoding classical financial data into quantum states |
| `#limitation:no-empirical-validation` | Theoretical claims not backed by experiment |
| `#limitation:simulation-only` | Results from classical simulation, not real QPU |

**Custom tags**

New idea, contradiction, or limitation tags may be added following these formats. Tags should be lowercase and hyphenated. Prefer reusable categories over one-off labels.
- Idea tags: `#idea:[concept]`
- Contradiction tags: `#contradiction:[concept]`
- Limitation tags: `#limitation:[concept]`

All new tags must be registered in `config/tag_registry.json` before use.

---

## 5. Agent architecture

The system uses five agent roles implemented as VS Code custom agents in `.github/agents/`. The **orchestrator** is the primary user-facing agent that coordinates development. It delegates work to three specialist agents (designer, coder, tester) and pauses for human approval at each transition.

### Orchestrator agent

- **File:** `.github/agents/orchestrator.agent.md`
- **Tools:** `read`, `search`, `agent`, `execute` (git only), `todo`
- **Responsibility:** Drive the development plan forward. Read the project spec, identify the next task, delegate to the appropriate specialist agent, commit and push after each completed task.
- **Checkpoints:** Pauses for human approval before every subagent delegation, at each new milestone, and when researcher action is required.

### Designer agent

- **File:** `.github/agents/designer.agent.md`
- **Tools:** `read`, `edit`, `search`
- **Responsibility:** Create and maintain config files, JSON schemas, markdown templates, validation rules.
- **Does not:** write Python implementation code.

### Coder agent

- **File:** `.github/agents/coder.agent.md`
- **Tools:** `read`, `edit`, `search`, `execute`
- **Responsibility:** Write, refine, and debug Python scripts and CLI tools.
- **Does not:** make architecture decisions — escalates to the orchestrator.

### Tester agent

- **File:** `.github/agents/tester.agent.md`
- **Tools:** `read`, `search`, `execute`
- **Responsibility:** Validate pipeline outputs, check schema compliance, run tests, report issues.
- **Does not:** fix code — reports findings for the coder to address.

### Explore agent (built-in)

- **Responsibility:** Fast read-only codebase research. Used by other agents to gather context across many files.

### Workflow

```
User opens chat with @orchestrator
  → Orchestrator reads CLAUDE.md + identifies next task
  → Proposes delegation → waits for approval
  → Delegates to @designer / @coder / @tester
  → Summarises result → commits and pushes
  → Proposes next task → waits for approval
```

### Commit convention

Format: `Task {N.M}: {descriptive title}` — managed by the orchestrator.

---

## 6. Repository structure

```
project-root/
├── CLAUDE.md                        # This file — single source of truth
├── README.md                        # How to set up and run the system
├── .gitignore                       # Excludes PDFs, .env, logs, __pycache__
├── .env.example                     # Template for API keys (never commit .env)
├── requirements.txt                 # Python dependencies
├── processing_log.json              # Tracks per-paper step completion
│
├── .github/
│   ├── copilot-instructions.md      # Workspace instructions for all agents
│   └── agents/
│       ├── orchestrator.agent.md    # Primary coordinator agent
│       ├── designer.agent.md        # Config/schema/template specialist
│       ├── coder.agent.md           # Python implementation agent
│       ├── tester.agent.md          # Validation and QA agent
│       └── experiment-designer.agent.md  # Interactive experiment design assistant
│
├── config/
│   ├── extraction_config.json       # Step parameters, model selections, token limits
│   ├── tag_registry.json            # All approved tags with descriptions
│   └── source_types.json            # Source type definitions and template mappings
│
├── templates/
│   ├── paper_base.md                # Blank paper template
│   ├── peer_reviewed_empirical.md   # Source-type-specific extraction hints
│   ├── peer_reviewed_theoretical.md
│   ├── preprint.md
│   ├── review_article.md
│   ├── conference_paper.md
│   ├── industry_whitepaper.md
│   └── industry_report.md
│
├── scripts/
│   ├── extract_paper.py             # Main orchestrator — runs all 6 steps on one paper
│   ├── run_extraction_step.py       # Run or re-run individual steps (--paper, --step, --from-step, --batch)
│   ├── fetch_from_zotero.py         # Fetch PDFs from Zotero API by key or collection
│   ├── extract_pdf_text.py          # PDF to plain text (PyMuPDF wrapper)
│   ├── validate_markdown.py         # Check paper files against schema
│   ├── sync_obsidian.py             # Push processed files to Obsidian vault path
│   ├── discover_tags.py             # LLM-based tag suggestion across papers
│   ├── approve_tags.py              # Merge approved tag suggestions into registry
│   ├── build_citation_graph.py      # Build citation network via OpenAlex API
│   ├── report_missing_papers.py     # Report frequently-cited papers not in collection
│   ├── build_indices.py             # Generate thematic index files
│   ├── detect_contradictions.py     # Cross-paper contradiction detection
│   └── utils/
│       ├── __init__.py
│       ├── llm_client.py            # Model-agnostic LLM call wrapper
│       ├── frontmatter.py           # Read/write YAML frontmatter in markdown files
│       ├── logger.py                # Structured logging for all pipeline steps
│       ├── text_chunker.py          # Token-aware text truncation and chunking
│       ├── step_runner.py           # Step dispatch: load prompt, call LLM, parse, write
│       ├── tag_validator.py         # Validate tags against registry
│       ├── paper_index.py           # Cross-paper index builder (idea-tags → papers)
│       └── openalex_client.py       # OpenAlex API wrapper with caching
│
├── prompts/
│   ├── step1_classify.txt           # LLM prompt template for source classification
│   ├── step2_metadata.txt           # LLM prompt template for metadata extraction
│   ├── step3_methodology.txt        # LLM prompt template (parameterized by source_type)
│   ├── step4_findings.txt           # LLM prompt template (parameterized by source_type)
│   ├── step5_limitations.txt        # LLM prompt template
│   ├── step6_synthesis.txt          # LLM prompt template (reads all prior sections)
│   ├── tag_discovery.txt            # LLM prompt for suggesting new tags
│   ├── contradiction_detection.txt  # LLM prompt for cross-paper contradiction analysis
│   └── experiment_design_system.txt # System prompt for experiment design agent
│
├── papers/
│   ├── raw_pdfs/                    # Incoming PDFs from Zotero (not committed to git)
│   └── processed/                   # Generated markdown files (Obsidian vault)
│
├── analysis/                        # Cross-paper analysis outputs
│   ├── overview.md                  # Dashboard: tag frequencies, evidence breakdown
│   ├── tag_suggestions.json         # LLM-suggested tags for review
│   ├── citation_index.json          # Citation graph data
│   ├── missing_papers.md            # Papers cited frequently but not in collection
│   ├── contradictions_index.json    # Cross-paper contradiction data
│   ├── contradictions.md            # Human-readable contradiction report
│   ├── experiment_landscape.md      # Aggregated experiment details
│   ├── openalex_cache/              # API response cache (git-ignored)
│   ├── by_topic/                    # Index files by topic tag
│   ├── by_method/                   # Index files by methodology tag
│   └── by_claim/                    # Index files by QA claim type
│
├── logs/                            # Pipeline run logs (not committed to git)
│
└── tests/
    ├── test_extraction_steps.py     # Unit tests for each step
    ├── test_schema_validation.py    # Validate markdown files against spec
    └── sample_papers/               # Small set of PDFs for testing (not committed)
```

---

## 7. Configuration files

### 7.1 `config/extraction_config.json` structure

```json
{
  "default_model": "claude-opus-4-6",
  "fallback_model": "gpt-4o",
  "zotero_group_id": "YOUR_GROUP_ID",
  "obsidian_vault_path": "/absolute/path/to/vault",
  "pdf_output_path": "papers/raw_pdfs",
  "markdown_output_path": "papers/processed",
  "steps": {
    "step1": {
      "name": "source_classification",
      "model": "claude-opus-4-6",
      "temperature": 0.2,
      "max_tokens": 500,
      "prompt_file": "prompts/step1_classify.txt",
      "input_tokens": 2000
    },
    "step2": {
      "name": "metadata_extraction",
      "model": "claude-opus-4-6",
      "temperature": 0.1,
      "max_tokens": 800,
      "prompt_file": "prompts/step2_metadata.txt",
      "input_tokens": 3000
    },
    "step3": {
      "name": "methodology_extraction",
      "model": "claude-opus-4-6",
      "temperature": 0.3,
      "max_tokens": 1500,
      "prompt_file": "prompts/step3_methodology.txt",
      "input_tokens": 8000
    },
    "step4": {
      "name": "findings_extraction",
      "model": "claude-opus-4-6",
      "temperature": 0.3,
      "max_tokens": 1500,
      "prompt_file": "prompts/step4_findings.txt",
      "input_tokens": 8000
    },
    "step5": {
      "name": "limitations_extraction",
      "model": "claude-opus-4-6",
      "temperature": 0.3,
      "max_tokens": 1000,
      "prompt_file": "prompts/step5_limitations.txt",
      "input_tokens": 8000
    },
    "step6": {
      "name": "synthesis_tagging",
      "model": "claude-opus-4-6",
      "temperature": 0.2,
      "max_tokens": 1500,
      "prompt_file": "prompts/step6_synthesis.txt",
      "input_tokens": 0
    }
  }
}
```

---

## 8. Development process

### 8.1 Principles

- **Plan before coding.** Every feature starts with a plan produced by the Planner agent. No code is written until the plan is reviewed and approved.
- **One step at a time.** Build and test each extraction step before moving to the next. Do not build all six steps at once.
- **Test on sample papers.** Always validate new scripts against 3–5 sample papers in `tests/sample_papers/` before running on the full batch.
- **Selective re-run is non-negotiable.** Every script must support running on a single paper or a filtered subset. Batch-only tools are not acceptable.
- **Schema first.** If a script's output does not conform to the markdown schema in Section 4, fix the script — not the schema.
- **Secrets never in code.** All API keys and credentials go in `.env`. The `.env` file is in `.gitignore`.

### 8.2 Phased development milestones

#### Milestone 1 — Foundation
Build the infrastructure that every subsequent step depends on.

- [x] Repository structure created as per Section 6
- [x] `config/extraction_config.json` populated with all step definitions
- [x] `config/tag_registry.json` populated with initial tag vocabulary
- [x] `utils/llm_client.py` — model-agnostic wrapper supporting Anthropic and OpenAI APIs
- [x] `utils/frontmatter.py` — read and write YAML frontmatter in markdown files
- [x] `scripts/extract_pdf_text.py` — PDF to plain text via PyMuPDF
- [x] `scripts/fetch_from_zotero.py` — fetch attachment by Zotero item key
- [x] `templates/paper_base.md` — blank paper template with all sections
- [x] `.env.example` with all required variable names
- [x] `tests/test_schema_validation.py` — validates a markdown file against the frontmatter spec

#### Milestone 2 — Step 1 and step 2 (classification and metadata)
Get the first two steps working end-to-end on a single paper.

- [x] `prompts/step1_classify.txt` — source classification prompt
- [x] `prompts/step2_metadata.txt` — metadata extraction prompt
- [x] `scripts/run_extraction_step.py` — supports `--paper`, `--step`, `--from-step`
- [x] Step 1 tested on 5 sample papers — validate source type detection accuracy
- [x] Step 2 tested on 5 sample papers — validate metadata accuracy vs. Zotero
- [x] `tests/test_extraction_steps.py` — unit tests for steps 1 and 2

#### Milestone 3 — Steps 3, 4, 5 (core extraction)
The substantive extraction steps with source-type parameterization.

- [x] `prompts/step3_methodology.txt` — parameterized by `{source_type}`
- [x] `prompts/step4_findings.txt` — parameterized by `{source_type}`
- [x] `prompts/step5_limitations.txt`
- [x] Source-type template files for each type in `templates/`
- [x] Steps 3–5 tested on sample papers across at least 3 different source types
- [x] Selective re-run tested: edit step 3 output, re-run from step 4, confirm step 3 is unchanged

#### Milestone 4 — Step 6 (synthesis and tagging)
Cross-paper synthesis and the unified tag layer.

- [x] `prompts/step6_synthesis.txt` — reads all prior sections, outputs tags
- [x] Tag validation against `config/tag_registry.json` — reject unknown tags
- [x] Step 6 tested on 10 processed papers
- [x] Verify tag output is consistent across similar papers

#### Milestone 5 — Batch processing and orchestration
Run the full pipeline at scale.

- [x] `scripts/extract_paper.py` — orchestrator running all 6 steps on one paper
- [x] `scripts/run_extraction_step.py` — `--batch` flag with `--filter` support
- [x] Batch test on 20 papers — log errors, track step completion per paper
- [x] `scripts/validate_markdown.py` — batch validation of all processed papers
- [x] `scripts/sync_obsidian.py` — copy processed files to Obsidian vault path

#### Milestone 6 — Zotero integration
Connect the pipeline to the live Zotero group library.

- [x] `scripts/fetch_from_zotero.py` — fetch by collection tag (`phase1-included`)
- [x] End-to-end test: DOI → Zotero → PDF → pipeline → Obsidian markdown
- [x] Handle missing PDFs gracefully (log, skip, flag in frontmatter)
- [x] Handle API rate limits and retries

#### Milestone 7 — v2: Data enrichment (tag discovery + experiment details + citation graph)
- [ ] Phase 2.1: Tag discovery pipeline complete and tested
- [ ] Phase 2.2: Step 3 enhanced with experiment details, all papers re-processed
- [ ] Phase 2.3: Citation graph built, missing papers report generated

#### Milestone 8 — v2: Cross-paper indexing (thematic indices)
- [ ] Phase 2.4: Thematic indices generated (by_topic, by_method, by_claim, overview dashboard)
- [ ] All analysis files committed to `analysis/` directory

#### Milestone 9 — v3: Cross-paper intelligence (contradiction detection + experiment assistant)
- [ ] Phase 3.1: Contradiction detection complete, contradiction index and report generated
- [ ] Phase 3.2: Experiment design agent operational and tested

### 8.3 Definition of done for each milestone

A milestone is complete when:
1. All checklist items are implemented
2. All tests pass on sample papers
3. At least one real paper from the research corpus has been processed end-to-end
4. No hardcoded API keys, paths, or credentials exist in any script
5. A brief note is added to README.md describing what the milestone added

### 8.4 Known constraints and edge cases to handle

- **PDFs with no extractable text:** Some papers are scanned images. The system must detect this and log a warning rather than silently failing.
- **Very long papers:** Papers exceeding the LLM context window must be chunked. Steps 3–5 are most likely to hit this — chunk by section (intro, methods, results, discussion).
- **Papers without DOIs:** Some preprints or reports may not have DOIs. The pipeline must support manual addition to Zotero and still process them.
- **Rate limits:** Both Zotero API and LLM APIs have rate limits. All API calls must use exponential backoff and retry logic.
- **Duplicate papers:** The same paper may appear under different DOIs (preprint + published version). Flag duplicates during Zotero import.
- **Non-English papers:** Flag and skip — scope is English-language sources only.

---

## 9. Resolved decisions

The following decisions were made during the planning phase and apply to all development:

| Decision | Choice | Rationale |
|----------|--------|----------|
| Python version | 3.11 | Stable, wide library support |
| Dependency management | pip + requirements.txt | Simple, universally supported |
| LLM client | Direct SDKs (anthropic + openai) | Minimal dependencies, full control, simpler debugging |
| CLI framework | argparse | Standard library, no extra dependency |
| Processing log | Flat JSON file (`processing_log.json`) | Simple, git-trackable, no extra dependency |
| Obsidian vault path | Same repo (`papers/processed/`) | No sync step needed — Obsidian opens the folder directly |
| Prompt templating | Python `str.format()` | Simple variable substitution, no extra dependency |
| Experiment details location | Enhance Step 3 | Reuses re-run infrastructure, avoids pipeline complexity |
| Analysis outputs directory | `analysis/` (committed) | Separates generated analysis from Obsidian paper data |
| Citation data source | OpenAlex API (free) | More accurate than LLM extraction, no cost per query |
| Experiment design tool | Interactive VS Code agent | Conversational interface for iterative research design |
| Tag discovery output | `analysis/tag_suggestions.json` | Researcher reviews before any tags enter the registry |

---

## 10. v2/v3 Development roadmap

v1 (complete) handles per-paper extraction. v2 adds cross-paper data enrichment and indexing. v3 adds intelligence layers for contradiction detection and experiment design.

### 10.1 Design decisions for v2/v3

| Decision | Choice | Rationale |
|----------|--------|----------|
| Experiment details | Enhance Step 3 (not new step) | Reuses existing re-run infrastructure, avoids pipeline complexity |
| Thematic indices | `analysis/` directory | Separates generated analysis from primary paper data in Obsidian |
| Citation data source | OpenAlex API | Free, no API key needed, more accurate than LLM extraction from PDF references |
| Experiment design assistant | Interactive VS Code agent | Conversational interface better for iterative research design |
| Analysis outputs | Committed to git (except cache) | Enables version tracking and collaboration |

### 10.2 Phase 2.1 — Tag discovery pipeline

Batch LLM analysis suggests new tags not in the registry, aggregated with frequency counts for researcher review.

- [ ] `prompts/tag_discovery.txt` — prompt for suggesting new tags given paper content + existing registry
- [ ] `scripts/discover_tags.py` — CLI: reads all papers, calls LLM, writes `analysis/tag_suggestions.json`
- [ ] `scripts/approve_tags.py` — CLI: merges approved suggestions into `config/tag_registry.json` and updates `prompts/step6_synthesis.txt`
- [ ] Test: run on 10 papers, verify suggestions are novel, approval workflow works, step 6 re-run picks up new tags

### 10.3 Phase 2.2 — Enhanced experiment details (Step 3)

Expand Step 3 to capture replication-grade experiment details for empirical papers.

- [ ] Update `prompts/step3_methodology.txt` with experiment detail fields (input, process, output, parameters, hardware, reproducibility)
- [ ] Update `scripts/utils/step_runner.py` `_write_step3_results()` to write `## Experiment details` section
- [ ] Update `templates/paper_base.md` to include `## Experiment details` placeholder
- [ ] Update `config/extraction_config.json` step3: `max_tokens` 4000→6000, `input_tokens` 13000→15000
- [ ] Re-run step 3 on all papers (`--batch --step 3`)
- [ ] Test: 3 empirical papers have details populated, 1 review paper has empty/N/A fields

### 10.4 Phase 2.3 — Citation graph (API-based)

Build citation network via OpenAlex API. Identify frequently-cited papers missing from the collection.

- [ ] `scripts/utils/openalex_client.py` — API wrapper with rate limiting, caching to `analysis/openalex_cache/`
- [ ] `scripts/build_citation_graph.py` — CLI: reads DOIs from frontmatter, queries OpenAlex, outputs `analysis/citation_index.json`
- [ ] `scripts/report_missing_papers.py` — CLI: generates `analysis/missing_papers.md` (papers cited by ≥N collection papers but absent)
- [ ] Test: 5 papers with known DOIs, verify citation data matches OpenAlex, papers without DOIs gracefully skipped

### 10.5 Phase 2.4 — Thematic indices

Auto-generate browsable markdown index files organized by topic, methodology, and claim type.

- [ ] `scripts/build_indices.py` — CLI: generates `analysis/by_topic/`, `analysis/by_method/`, `analysis/by_claim/`, `analysis/overview.md`
- [ ] Index format: paper table (year, method, QA claim, evidence), aggregated findings, open questions
- [ ] Dashboard (`overview.md`): counts, tag frequencies, year distribution, evidence breakdown, gaps
- [ ] Test: every paper appears in at least one topic index, overview counts match paper count

### 10.6 Phase 3.1 — Contradiction detection

LLM compares claims across papers within each topic to systematically identify contradictions.

- [ ] `prompts/contradiction_detection.txt` — prompt receiving grouped claims from papers in same topic
- [ ] `scripts/detect_contradictions.py` — CLI: groups papers by topic (via indices), sends claims to LLM, outputs `analysis/contradictions_index.json` + `analysis/contradictions.md`
- [ ] Severity levels: high (direct contradiction), medium (tension), low (different emphasis)
- [ ] Optional `--update-papers` flag: enriches individual paper `## Contradictions` sections
- [ ] Test: run on topics with known disagreements, verify at least some contradictions detected

### 10.7 Phase 3.2 — Experiment design assistant

Interactive VS Code agent that reads all analysis outputs to help design Phase 4 experiments.

- [ ] `.github/agents/experiment-designer.agent.md` — read-only tools (`read`, `search`)
- [ ] `prompts/experiment_design_system.txt` — system prompt with research landscape context
- [ ] Extend `scripts/build_indices.py` to generate `analysis/experiment_landscape.md`
- [ ] Capabilities: suggest experiments for a topic, identify methodology gaps, propose designs to resolve contradictions
- [ ] Test: agent cites real papers, suggests methods present in literature, doesn't hallucinate

### 10.8 Dependencies and parallelism

```
Phase 2.1: Tag Discovery ──────────────────────┐
Phase 2.2: Experiment Details ─────────────┐    │
Phase 2.3: Citation Graph ────────────┐    │    │
                                      ▼    ▼    ▼
Phase 2.4: Thematic Indices ─────────── (enriched by all above)
                                      │
                                      ▼
Phase 3.1: Contradiction Detection ─── (needs 2.4 grouping)
                                      │
                                      ▼
Phase 3.2: Experiment Design Agent ─── (needs 2.2 + 2.4 + 3.1)
```

Phases 2.1, 2.2, 2.3 are fully independent. Critical path: 2.4 → 3.1 → 3.2.
