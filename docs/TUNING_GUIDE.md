# Tuning Guide — How to Modify the Extraction Pipeline

> This document explains how to change prompts, tags, models, extraction features, and parameters to improve the quality of your analysis. Every section tells you exactly which file to edit and what to change.
>
> For an understanding of how the system works, read [SYSTEM_OVERVIEW.md](SYSTEM_OVERVIEW.md) first.

---

## Table of contents

1. [Quick reference: "I want to change X"](#1-quick-reference)
2. [Changing LLM models](#2-changing-llm-models)
3. [Modifying prompts](#3-modifying-prompts)
4. [Adding or removing tags](#4-adding-or-removing-tags)
5. [Adding a new source type](#5-adding-a-new-source-type)
6. [Changing what gets extracted](#6-changing-what-gets-extracted)
7. [Tuning model parameters](#7-tuning-model-parameters)
8. [Re-running after changes](#8-re-running-after-changes)
9. [Validating your changes](#9-validating-your-changes)
10. [Common tuning scenarios](#10-common-tuning-scenarios)

---

## 1. Quick reference

| I want to... | Edit this file | Section/field |
|---------------|---------------|---------------|
| Use a different LLM model | `config/extraction_config.json` | `steps.step{N}.model` |
| Add a new Azure model deployment | `.env` | `AZURE_DEPLOYMENTS` |
| Change what the LLM extracts | `prompts/step{N}_*.txt` | Prompt instructions |
| Add a new topic tag | `config/tag_registry.json` | `topic_tags` |
| Add a new methodology tag | `config/tag_registry.json` | `methodology_tags` |
| Add a new idea/limitation tag | `config/tag_registry.json` | `synthesis_tags` |
| Update the tag vocabulary in step 6 | `prompts/step6_synthesis.txt` | Tag list section |
| Add a new source type | `config/source_types.json` + `prompts/step1_classify.txt` | See [section 5](#5-adding-a-new-source-type) |
| Change extraction focus for a source type | `prompts/step{3,4,5}_*.txt` | Source-type table |
| Increase/decrease output length | `config/extraction_config.json` | `steps.step{N}.max_tokens` |
| Include more/less of the PDF | `config/extraction_config.json` | `steps.step{N}.input_tokens` |
| Make output more/less creative | `config/extraction_config.json` | `steps.step{N}.temperature` |
| Add a new frontmatter field | `scripts/utils/step_runner.py` | `_write_step{N}_results()` |
| Change the output template | `templates/paper_base.md` | YAML header + body sections |
| Change API rate limits | `scripts/utils/llm_client.py` | `RateLimiter.__init__()` |
| Re-run one step on one paper | Terminal | `python scripts/run_extraction_step.py --paper file.md --step N` |
| Re-run one step on all papers | Terminal | `python scripts/run_extraction_step.py --batch --step N` |

---

## 2. Changing LLM models

### Switch model for a specific step

Edit `config/extraction_config.json`. Each step has a `model` field:

```json
"step4": {
  "name": "findings_extraction",
  "model": "Mistral-Large-3",    ← change this
  "temperature": 0.3,
  "max_tokens": 1500,
  "prompt_file": "prompts/step4_findings.txt",
  "input_tokens": 8000
}
```

You can use different models for different steps — for example, a cheaper model for classification (step 1) and a more powerful model for findings (step 4).

### Add a new Azure deployment

1. Deploy the model in your Azure AI Foundry portal
2. Add the deployment name to `.env`:

```
AZURE_DEPLOYMENTS=Kimi-K2.5,Mistral-Large-3,GPT-4o-mini
```

3. Use the deployment name in `config/extraction_config.json`:

```json
"step1": {
  "model": "GPT-4o-mini",
  ...
}
```

### Use standard OpenAI instead of Azure

Models whose names start with `gpt` are automatically routed to the OpenAI API. Set your OpenAI key in `.env`:

```
OPENAI_API_KEY=sk-...
```

Then use the model name directly:

```json
"step4": {
  "model": "gpt-4o",
  ...
}
```

### After changing models

Re-run the affected steps to update the papers:

```bash
# Re-run step 4 on all papers with the new model
python scripts/run_extraction_step.py --batch --step 4
```

The `step{N}_model` field in each paper's frontmatter records which model was used, so you can track which papers were processed with which model.

---

## 3. Modifying prompts

Prompts are plain text files in `prompts/`. This is the most impactful way to improve extraction quality.

### File locations

| Step | File | Template variables |
|------|------|-------------------|
| 1 — Classification | `prompts/step1_classify.txt` | `{paper_text}` |
| 2 — Metadata | `prompts/step2_metadata.txt` | `{paper_text}`, `{source_type}` |
| 3 — Methodology | `prompts/step3_methodology.txt` | `{paper_text}`, `{source_type}` |
| 4 — Findings | `prompts/step4_findings.txt` | `{paper_text}`, `{source_type}` |
| 5 — Limitations | `prompts/step5_limitations.txt` | `{paper_text}`, `{source_type}` |
| 6 — Synthesis | `prompts/step6_synthesis.txt` | `{extracted_content}` |

### How prompts are structured

Each prompt follows this pattern:

1. **Role statement** — "You are a research assistant..."
2. **Task description** — "Your task: Given the paper text, extract..."
3. **Source-type-specific guidance** (steps 3–5) — A table telling the LLM what to focus on per source type
4. **Output format** — JSON schema the LLM must follow
5. **Examples** (optional) — Sample JSON output
6. **Input data** — The template variable (`{paper_text}` or `{extracted_content}`)

### Tips for prompt iteration

**Start small:** Change one section of the prompt, re-run on 2–3 papers, compare outputs, iterate.

```bash
# Test a prompt change on one paper
python scripts/run_extraction_step.py --paper 2024_Ghysels_QuantumFinance.md --step 3
```

**Be specific about what you want:** Instead of "extract methodology," say "identify the quantum algorithm by name (e.g., QAOA, VQE, HHL), whether it was run on a simulator or real QPU, and the number of qubits used."

**Control output structure via JSON schema:** The prompt defines the JSON keys the LLM must return. If you want a new field, add it to the JSON schema in the prompt and update the step runner (see [section 6](#6-changing-what-gets-extracted)).

**Manage length:** If outputs are too short, add "Provide detailed descriptions" or increase `max_tokens`. If too verbose, add "Be concise — use bullet points" or decrease `max_tokens`.

### Editing source-type-specific guidance

Steps 3, 4, and 5 contain per-type extraction tables. For example, in `prompts/step3_methodology.txt`:

```
Source type: peer-reviewed-empirical
Focus: Research design, quantum algorithm(s) used, hardware (simulator vs. real QPU),
       dataset, evaluation metrics, baseline comparisons

Source type: industry-whitepaper
Focus: Claimed approach or framework. Note absence of formal methods section.
       Identify supporting evidence (if any)
```

To change what gets extracted for a source type, edit the relevant row in the prompt.

### Important: keep the JSON output format consistent

The step runner expects specific JSON keys from each step. If you rename or remove a key, you must also update the corresponding `_write_step{N}_results()` function in `scripts/utils/step_runner.py`. See [section 6](#6-changing-what-gets-extracted).

---

## 4. Adding or removing tags

### Edit the tag registry

All tags live in `config/tag_registry.json`. The file has three sections:

```json
{
  "topic_tags": {
    "portfolio-optimisation": "Asset allocation, QUBO, Markowitz variants",
    "risk-modelling": "VaR, CVaR, credit risk, market risk"
  },
  "methodology_tags": {
    "QAOA": "Quantum Approximate Optimisation Algorithm",
    "VQE": "Variational Quantum Eigensolver"
  },
  "synthesis_tags": {
    "idea:quantum-advantage": "A claim about where quantum outperforms classical",
    "limitation:noise": "Hardware noise degrades results"
  }
}
```

### To add a new tag

1. Add the tag to the appropriate section in `config/tag_registry.json`:

```json
"methodology_tags": {
  "QAOA": "Quantum Approximate Optimisation Algorithm",
  "quantum-error-correction": "Error correction codes and techniques"   ← new
}
```

2. **Also update `prompts/step6_synthesis.txt`** — Step 6's prompt contains a copy of the tag vocabulary that tells the LLM which tags to use. If you add a tag to the registry but not the prompt, the LLM won't know to use it.

Search for the tag list section in the prompt (it starts with "**Tag vocabulary**") and add your new tag there.

3. Re-run step 6 on all papers so the LLM can apply the new tag:

```bash
python scripts/run_extraction_step.py --batch --step 6
```

### To remove a tag

1. Remove it from `config/tag_registry.json`
2. Remove it from `prompts/step6_synthesis.txt`
3. Manually remove the tag from any papers that already use it, or re-run step 6 on all papers

### Tag format rules

- All lowercase
- Hyphens instead of spaces (`quantum-annealing`, not `quantum annealing`)
- Ideas: `idea:[concept]`
- Contradictions: `contradiction:[concept]`
- Limitations: `limitation:[concept]`

### How tags flow to Obsidian

Step 6 writes tags in two formats:
- **Flat lists** (`topic_tags`, `methodology_tags`, `idea_tags`) — for programmatic filtering
- **Unified hierarchical** (`tags`) — for Obsidian's tag pane, using `/` separators:
  - `topic/portfolio-optimisation`
  - `method/QAOA`
  - `idea/quantum-advantage`
  - `limitation/noise`

---

## 5. Adding a new source type

This requires changes in three places:

### Step 1: Define the source type

Edit `config/source_types.json` and add a new entry:

```json
"government-policy": {
  "template_file": "templates/government_policy.md",
  "classification_signals": "Government authorship, policy language, regulatory citations",
  "step3_focus": "Policy framework, regulatory references, scope of recommendations",
  "step4_focus": "Policy recommendations, projected impacts, regulatory implications",
  "step5_focus": "Jurisdiction limits, political context, implementation challenges"
}
```

### Step 2: Update the classification prompt

Edit `prompts/step1_classify.txt` and add the new source type to the classification table:

```
| government-policy | Government authorship, policy language, regulatory citations |
```

### Step 3: Update extraction prompts

Edit the source-type-specific tables in `prompts/step3_methodology.txt`, `prompts/step4_findings.txt`, and `prompts/step5_limitations.txt` to include extraction guidance for the new type.

### Step 4 (optional): Create a template

Create `templates/government_policy.md` if you want a type-specific template. Otherwise, `templates/paper_base.md` is used as the default.

### After adding

Re-run step 1 on all papers so the LLM can detect the new type:

```bash
python scripts/run_extraction_step.py --batch --step 1
```

Papers reclassified to the new type should then be re-run from step 2 onwards:

```bash
python scripts/run_extraction_step.py --batch --filter source_type=government-policy --from-step 2
```

---

## 6. Changing what gets extracted

### Which step writes which fields

Understanding this mapping is essential for adding new extraction features.

**Step 1 writes to frontmatter:**
- `source_type`, `source_type_confidence`, `auto_detected`

**Step 2 writes to frontmatter:**
- `title`, `authors`, `year`, `journal_or_venue`, `doi`, `aliases`

**Step 2 writes to body:**
- `## Abstract summary`

**Step 3 writes to body:**
- `## Methodology`

**Step 4 writes to frontmatter:**
- `quantum_advantage_claim`

**Step 4 writes to body:**
- `## Findings`
- `## Quantum advantage claim`

**Step 5 writes to body:**
- `## Limitations`
- `## Open questions`

**Step 6 writes to frontmatter:**
- `topic_tags`, `methodology_tags`, `idea_tags`, `tags`, `relevance_phase1`, `relevance_phase3`, `contradiction_flags`, `related_papers`

**Step 6 writes to body:**
- `## Key ideas`
- `## Contradictions`

### To add a new frontmatter field

Example: you want to add an `industry_sector` field to track which financial sector each paper focuses on.

1. **Add the field to the prompt** (`prompts/step2_metadata.txt`):

   Add `"industry_sector"` to the JSON output schema in the prompt.

2. **Add the field to the template** (`templates/paper_base.md`):

   ```yaml
   industry_sector: ""
   ```

3. **Add the field to the step runner** (`scripts/utils/step_runner.py`):

   Find the function `_write_step2_results()` and add a line to write the new field:

   ```python
   updates["industry_sector"] = results.get("industry_sector", "")
   ```

4. **Add validation** (optional, in `tests/test_schema_validation.py`):

   Add the field to the required frontmatter fields list.

5. **Re-run step 2** on papers you want the new field for:

   ```bash
   python scripts/run_extraction_step.py --batch --step 2
   ```

### To add a new body section

1. Add the section to `templates/paper_base.md`:

   ```markdown
   ## Industry context
   <!-- Step 3 output — industry-specific context -->
   ```

2. Update the relevant prompt to produce content for this section.

3. Update the relevant `_write_step{N}_results()` in `scripts/utils/step_runner.py` to call `_write_body_section()` with the new section heading.

---

## 7. Tuning model parameters

Each step in `config/extraction_config.json` has three key knobs:

### Temperature

Controls randomness in LLM output.

| Value | Effect | Best for |
|-------|--------|----------|
| 0.0–0.1 | Very deterministic, consistent | Metadata extraction (step 2) |
| 0.2 | Balanced | Classification (step 1), synthesis (step 6) |
| 0.3 | Slightly creative | Methodology, findings, limitations (steps 3–5) |
| 0.5+ | More varied | Not recommended for structured extraction |

Current defaults: 0.1 (step 2), 0.2 (steps 1, 6), 0.3 (steps 3, 4, 5)

### max_tokens

Maximum number of tokens the LLM can generate in its response.

| Step | Current | Effect of increasing | Effect of decreasing |
|------|---------|---------------------|---------------------|
| 1 | 500 | Longer reasoning in classification | May truncate output |
| 2 | 800 | Longer abstract summaries | Shorter abstracts |
| 3 | 1500 | More detailed methodology | Less detail |
| 4 | 1500 | More detailed findings | Fewer findings listed |
| 5 | 1000 | More limitations identified | Fewer limitations |
| 6 | 1500 | More tags and key ideas | Fewer tags assigned |

If you're getting truncated JSON responses (parsing failures), increase `max_tokens` for that step.

### input_tokens

How many tokens of the PDF text to include in the prompt. Uses a heuristic of 1 token ≈ 4 characters.

| Step | Current | Rationale |
|------|---------|-----------|
| 1 | 2000 | Only needs the opening pages to classify |
| 2 | 3000 | Title, authors, abstract are near the start |
| 3 | 8000 | Methods section can be deep in the paper |
| 4 | 8000 | Results section can be deep in the paper |
| 5 | 8000 | Limitations are often near the end |
| 6 | 0 | Reads the markdown file, not the PDF |

Setting `input_tokens` to `0` disables truncation (full text). Be cautious — very long papers may exceed the model's context window.

---

## 8. Re-running after changes

The pipeline supports selective re-runs so you don't have to reprocess everything.

### After changing a prompt

```bash
# Re-run the changed step on all papers
python scripts/run_extraction_step.py --batch --step 3

# Or test on one paper first
python scripts/run_extraction_step.py --paper 2024_Ghysels_QuantumFinance.md --step 3
```

### After changing tags (step 6 prompt + tag registry)

```bash
# Re-run step 6 on all papers
python scripts/run_extraction_step.py --batch --step 6
```

### After editing a paper's step 3 output manually

```bash
# Re-run from step 4 onwards (step 3 is preserved)
python scripts/run_extraction_step.py --paper 2024_Author_Title.md --from-step 4
```

### After correcting a source type manually

```bash
# Re-run from step 2 onwards for papers where source type was manually corrected
python scripts/run_extraction_step.py --batch --filter auto_detected=false --from-step 2
```

### After changing models

```bash
# Re-run all steps with the new model
python scripts/run_extraction_step.py --batch --from-step 1

# Or just re-run the step that uses the new model
python scripts/run_extraction_step.py --batch --step 4
```

### Step dependency chain

Changes to earlier steps may require re-running later steps:

```
Step 1 (source type) → affects steps 2, 3, 4, 5 (they use {source_type})
Step 2 (metadata)    → does not affect steps 3-6
Step 3 (methodology) → does not affect steps 4-6 directly
Step 4 (findings)    → does not affect steps 5-6 directly
Step 5 (limitations) → does not affect step 6 directly
Step 6 (synthesis)   → reads ALL prior sections, so any change upstream may affect it
```

**Rule of thumb:** If you change a prompt for step N, re-run step N. If you also want step 6 to reflect the new output, re-run step 6 too.

---

## 9. Validating your changes

### Schema validation

After any change, validate all papers against the schema:

```bash
python scripts/validate_markdown.py --batch
```

This checks:
- All required frontmatter fields exist
- All tags are in `config/tag_registry.json`
- All required body sections exist

### Run tests

```bash
python -m pytest tests/ -v
```

The test suite (`tests/test_schema_validation.py`) has 25 tests covering frontmatter fields, body sections, and tag validation. If you've added new fields or tags, update the tests accordingly.

### Manual spot-check

After changing a prompt, compare the output of 3–5 papers to assess quality:

```bash
# Re-run on a few papers
python scripts/run_extraction_step.py --paper 2024_Ghysels_QuantumFinance.md --step 3
python scripts/run_extraction_step.py --paper 2021_Stamatopoulos_TowardsQuantumAdvantage.md --step 3
python scripts/run_extraction_step.py --paper 2026_Ganguly_AutonomousQuantumAgents.md --step 3
```

Then open the files in Obsidian and review the sections you changed.

---

## 10. Common tuning scenarios

### "Findings are too vague — I want more specific quantitative results"

1. Edit `prompts/step4_findings.txt`
2. Add instructions like: "Always include specific numbers, percentages, confidence intervals, and error bars when available. State the exact metric names and values."
3. Test on 2–3 papers:
```bash
python scripts/run_extraction_step.py --paper 2021_Stamatopoulos_TowardsQuantumAdvantage.md --step 4
```
4. If satisfied, batch re-run: `python scripts/run_extraction_step.py --batch --step 4`

### "Too many tags are being assigned — papers get 8+ tags that aren't all relevant"

1. Edit `prompts/step6_synthesis.txt`
2. Add a constraint: "Assign only the 3–5 most relevant tags. Only include a tag if there is strong evidence for it in the extracted content."
3. Re-run: `python scripts/run_extraction_step.py --batch --step 6`

### "I want to track which quantum hardware each paper uses"

1. Add to `prompts/step3_methodology.txt` JSON schema: `"quantum_hardware": "Name of QPU or simulator used (e.g., IBM Eagle, D-Wave Advantage, Qiskit Aer)"`
2. Add `quantum_hardware: ""` to `templates/paper_base.md` frontmatter
3. Add to `scripts/utils/step_runner.py` in `_write_step3_results()`:
   ```python
   updates["quantum_hardware"] = results.get("quantum_hardware", "")
   ```
4. Re-run step 3: `python scripts/run_extraction_step.py --batch --step 3`

### "I want to add a new financial use case tag (e.g., insurance)"

1. Add to `config/tag_registry.json`:
   ```json
   "insurance": "Insurance pricing, actuarial models, claims prediction"
   ```
2. Add to the tag list in `prompts/step6_synthesis.txt`
3. Re-run step 6: `python scripts/run_extraction_step.py --batch --step 6`
4. Validate: `python scripts/validate_markdown.py --batch`

### "I want to use a different model for the most important steps"

Edit `config/extraction_config.json`:

```json
"step1": { "model": "GPT-4o-mini", ... },
"step2": { "model": "GPT-4o-mini", ... },
"step3": { "model": "Mistral-Large-3", ... },
"step4": { "model": "GPT-4o", ... },
"step5": { "model": "Mistral-Large-3", ... },
"step6": { "model": "GPT-4o", ... }
```

If the new model is an Azure deployment, add it to `.env`:
```
AZURE_DEPLOYMENTS=Kimi-K2.5,Mistral-Large-3,GPT-4o,GPT-4o-mini
```

If it's a standard OpenAI model (name starts with `gpt`), it routes automatically — just ensure `OPENAI_API_KEY` is set in `.env`.

### "Step 4 keeps failing with JSON parsing errors on certain papers"

This usually means the LLM response exceeds `max_tokens` and gets cut off mid-JSON.

1. Increase `max_tokens` in `config/extraction_config.json`:
   ```json
   "step4": { "max_tokens": 2500, ... }
   ```
2. Re-run the failing paper:
   ```bash
   python scripts/run_extraction_step.py --paper failing_paper.md --step 4
   ```

If the issue persists, the prompt may be requesting too many output fields. Simplify the JSON schema in `prompts/step4_findings.txt`.
