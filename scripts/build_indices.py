"""Build thematic index files from processed papers.

Generates browsable markdown indices in the analysis/ directory:
  - analysis/by_topic/{tag}.md   — one file per topic tag
  - analysis/by_method/{tag}.md  — one file per methodology tag
  - analysis/by_claim/{claim}.md — one file per quantum advantage claim value
  - analysis/overview.md         — dashboard with summary statistics

Usage examples:
    # Rebuild all indices
    python scripts/build_indices.py

    # Rebuild all indices (explicit)
    python scripts/build_indices.py --rebuild

    # Generate only one topic index
    python scripts/build_indices.py --topic portfolio-optimisation

    # Generate only the overview dashboard
    python scripts/build_indices.py --overview-only
"""

import argparse
import json
import os
import re
import sys
from collections import Counter
from datetime import datetime, timezone

# Ensure project root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from scripts.utils.frontmatter import read_frontmatter  # noqa: E402
from scripts.utils.logger import get_logger  # noqa: E402

logger = get_logger("build_indices")


def _find_project_root() -> str:
    """Walk up from this file to find the directory containing CLAUDE.md."""
    current = os.path.dirname(os.path.abspath(__file__))
    for _ in range(10):
        if os.path.isfile(os.path.join(current, "CLAUDE.md")):
            return current
        current = os.path.dirname(current)
    return os.getcwd()


PROJECT_ROOT = _find_project_root()
PROCESSED_DIR = os.path.join(PROJECT_ROOT, "papers", "processed")
ANALYSIS_DIR = os.path.join(PROJECT_ROOT, "analysis")
CITATION_INDEX_PATH = os.path.join(ANALYSIS_DIR, "citation_index.json")

SKIP_FILES = {".gitkeep"}

# Acronyms that should remain uppercase in display names
_ACRONYMS = {"qaoa", "vqe", "hhl", "qubo", "svm", "ml"}


def _tag_display_name(tag: str) -> str:
    """Convert a hyphenated tag to a title-cased display name, preserving acronyms."""
    words = tag.replace("-", " ").split()
    result = []
    for w in words:
        if w.lower() in _ACRONYMS:
            result.append(w.upper())
        else:
            result.append(w.capitalize())
    return " ".join(result)


def _wiki_link(filename: str) -> str:
    """Return an Obsidian wiki-link for a paper filename (no .md extension)."""
    return f"[[{filename.removesuffix('.md')}]]"


def _escape_pipe(text: str) -> str:
    """Escape pipe characters for markdown table cells."""
    return str(text).replace("|", "\\|")


def _extract_section(body: str, section_name: str) -> str:
    """Extract a ## section from markdown body. Returns empty string if not found."""
    pattern = re.compile(
        rf"^## {re.escape(section_name)}\s*\n(.*?)(?=^## |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(body)
    if match:
        content = match.group(1).strip()
        # Skip placeholder comments
        if content.startswith("<!--") and content.endswith("-->"):
            return ""
        return content
    return ""


def _extract_findings_bullets(body: str) -> list[str]:
    """Extract bullet points from the ## Findings section."""
    section = _extract_section(body, "Findings")
    if not section:
        return []
    bullets = []
    for line in section.splitlines():
        stripped = line.strip()
        if stripped.startswith("- ["):
            bullets.append(stripped)
    return bullets


def _extract_open_questions(body: str) -> list[str]:
    """Extract bullet points from the ## Open questions section."""
    section = _extract_section(body, "Open questions")
    if not section:
        return []
    bullets = []
    for line in section.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            bullets.append(stripped)
    return bullets


def _list_papers() -> list[str]:
    """List paper .md files in processed dir, filtering out non-paper files."""
    papers = sorted(
        f
        for f in os.listdir(PROCESSED_DIR)
        if f.endswith(".md")
        and f not in SKIP_FILES
        and not f.startswith(".")
        and not f.startswith("Untitled")
    )
    return papers


def _load_citation_data() -> dict:
    """Load citation index if available. Returns paper -> citation info mapping."""
    if not os.path.isfile(CITATION_INDEX_PATH):
        return {}
    try:
        with open(CITATION_INDEX_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("papers", {})
    except (json.JSONDecodeError, OSError):
        logger.warning("Could not load citation index from %s", CITATION_INDEX_PATH)
        return {}


# ---------------------------------------------------------------------------
# Data collection
# ---------------------------------------------------------------------------

def _collect_paper_data(papers: list[str]) -> list[dict]:
    """Read frontmatter and body sections for all papers. Returns list of dicts."""
    all_data = []
    for filename in papers:
        filepath = os.path.join(PROCESSED_DIR, filename)
        meta, body = read_frontmatter(filepath)
        if not meta:
            logger.warning("Skipping %s — no frontmatter", filename)
            continue

        topic_tags = meta.get("topic_tags") or []
        methodology_tags = meta.get("methodology_tags") or []
        idea_tags = meta.get("idea_tags") or []
        contradiction_flags = meta.get("contradiction_flags") or []

        paper = {
            "filename": filename,
            "title": meta.get("title", ""),
            "authors": meta.get("authors") or [],
            "year": meta.get("year"),
            "source_type": meta.get("source_type", ""),
            "evidence_type": meta.get("evidence_type", ""),
            "topic_tags": [t for t in topic_tags if isinstance(t, str)],
            "methodology_tags": [t for t in methodology_tags if isinstance(t, str)],
            "idea_tags": [t for t in idea_tags if isinstance(t, str)],
            "contradiction_flags": [t for t in contradiction_flags if isinstance(t, str)],
            "quantum_advantage_claim": meta.get("quantum_advantage_claim", ""),
            "relevance_phase1": meta.get("relevance_phase1", ""),
            "findings_bullets": _extract_findings_bullets(body),
            "open_questions": _extract_open_questions(body),
            "has_experiment_details": bool(_extract_section(body, "Experiment details")),
        }
        all_data.append(paper)
    return all_data


# ---------------------------------------------------------------------------
# Index builders
# ---------------------------------------------------------------------------

def _sort_findings(bullets: list[tuple[str, str]]) -> list[tuple[str, str]]:
    """Sort findings: [supported] first, then [speculative], then [disputed], limit 20."""
    priority = {"[supported]": 0, "[speculative]": 1, "[disputed]": 2}

    def key(item: tuple[str, str]) -> int:
        bullet = item[0]
        for tag, rank in priority.items():
            if tag in bullet:
                return rank
        return 3

    sorted_bullets = sorted(bullets, key=key)
    return sorted_bullets[:20]


def _paper_row_topic(paper: dict) -> str:
    """Build a paper table row for topic indices."""
    link = _wiki_link(paper["filename"])
    year = paper["year"] or "—"
    source = _escape_pipe(paper["source_type"] or "—")
    methods = ", ".join(paper["methodology_tags"]) or "—"
    qa = paper["quantum_advantage_claim"] or "—"
    rel = paper["relevance_phase1"] or "—"
    return f"| {link} | {year} | {source} | {methods} | {qa} | {rel} |"


def _paper_row_method(paper: dict) -> str:
    """Build a paper table row for method indices."""
    link = _wiki_link(paper["filename"])
    year = paper["year"] or "—"
    source = _escape_pipe(paper["source_type"] or "—")
    topics = ", ".join(paper["topic_tags"]) or "—"
    qa = paper["quantum_advantage_claim"] or "—"
    rel = paper["relevance_phase1"] or "—"
    return f"| {link} | {year} | {source} | {topics} | {qa} | {rel} |"


def _paper_row_claim(paper: dict) -> str:
    """Build a paper table row for claim indices."""
    link = _wiki_link(paper["filename"])
    year = paper["year"] or "—"
    source = _escape_pipe(paper["source_type"] or "—")
    topics = ", ".join(paper["topic_tags"]) or "—"
    methods = ", ".join(paper["methodology_tags"]) or "—"
    return f"| {link} | {year} | {source} | {topics} | {methods} |"


def _count_evidence_types(papers: list[dict]) -> dict[str, int]:
    """Count evidence types among a list of papers."""
    counts: dict[str, int] = Counter()
    for p in papers:
        st = p["source_type"]
        if "empirical" in st:
            counts["Empirical"] += 1
        elif "theoretical" in st:
            counts["Theoretical"] += 1
        elif "review" in st:
            counts["Review"] += 1
        else:
            counts["Other"] += 1
    return dict(counts)


def _sort_papers_by_year(papers: list[dict]) -> list[dict]:
    """Sort papers by year descending (newest first)."""
    return sorted(papers, key=lambda p: p.get("year") or 0, reverse=True)


def build_topic_index(tag: str, papers: list[dict]) -> str:
    """Generate a topic index markdown string for one tag."""
    display = _tag_display_name(tag)
    tagged = [p for p in papers if tag in p["topic_tags"]]
    tagged = _sort_papers_by_year(tagged)

    ev = _count_evidence_types(tagged)
    header_parts = [f"**Papers:** {len(tagged)}"]
    for label in ["Empirical", "Theoretical", "Review"]:
        if ev.get(label, 0) > 0:
            header_parts.append(f"**{label}:** {ev[label]}")

    lines = [
        f"# {display}",
        "",
        " | ".join(header_parts),
        "",
        "## Papers",
        "",
        "| Paper | Year | Source Type | Methods | QA Claim | Relevance |",
        "|-------|------|-------------|---------|----------|-----------|",
    ]
    for p in tagged:
        lines.append(_paper_row_topic(p))

    # Key Findings
    all_findings: list[tuple[str, str]] = []
    for p in tagged:
        for bullet in p["findings_bullets"]:
            all_findings.append((bullet, p["filename"]))
    sorted_findings = _sort_findings(all_findings)

    if sorted_findings:
        lines.append("")
        lines.append("## Key Findings")
        lines.append("")
        for bullet, filename in sorted_findings:
            attribution = _wiki_link(filename)
            lines.append(f"{bullet} — {attribution}")

    # Methods table
    method_counts: Counter = Counter()
    for p in tagged:
        for m in p["methodology_tags"]:
            method_counts[m] += 1

    if method_counts:
        lines.append("")
        lines.append("## Methodologies Used")
        lines.append("")
        lines.append("| Method | Papers |")
        lines.append("|--------|--------|")
        for method, count in method_counts.most_common():
            lines.append(f"| {method} | {count} |")

    # Open Questions
    all_questions: list[tuple[str, str]] = []
    for p in tagged:
        for q in p["open_questions"]:
            all_questions.append((q, p["filename"]))

    if all_questions:
        lines.append("")
        lines.append("## Open Questions")
        lines.append("")
        for q, filename in all_questions[:10]:
            attribution = _wiki_link(filename)
            # Strip leading "- " if present
            q_text = q.lstrip("- ")
            lines.append(f"- {q_text} — {attribution}")

    lines.append("")
    return "\n".join(lines)


def build_method_index(tag: str, papers: list[dict]) -> str:
    """Generate a method index markdown string for one tag."""
    display = _tag_display_name(tag)
    tagged = [p for p in papers if tag in p["methodology_tags"]]
    tagged = _sort_papers_by_year(tagged)

    ev = _count_evidence_types(tagged)
    header_parts = [f"**Papers:** {len(tagged)}"]
    for label in ["Empirical", "Theoretical", "Review"]:
        if ev.get(label, 0) > 0:
            header_parts.append(f"**{label}:** {ev[label]}")

    lines = [
        f"# {display}",
        "",
        " | ".join(header_parts),
        "",
        "## Papers",
        "",
        "| Paper | Year | Source Type | Topics | QA Claim | Relevance |",
        "|-------|------|-------------|--------|----------|-----------|",
    ]
    for p in tagged:
        lines.append(_paper_row_method(p))

    # Topics using this method
    topic_counts: Counter = Counter()
    for p in tagged:
        for t in p["topic_tags"]:
            topic_counts[t] += 1

    if topic_counts:
        lines.append("")
        lines.append("## Topics Using This Method")
        lines.append("")
        lines.append("| Topic | Papers |")
        lines.append("|-------|--------|")
        for topic, count in topic_counts.most_common():
            lines.append(f"| {topic} | {count} |")

    # Key Findings
    all_findings: list[tuple[str, str]] = []
    for p in tagged:
        for bullet in p["findings_bullets"]:
            all_findings.append((bullet, p["filename"]))
    sorted_findings = _sort_findings(all_findings)

    if sorted_findings:
        lines.append("")
        lines.append("## Key Findings")
        lines.append("")
        for bullet, filename in sorted_findings:
            attribution = _wiki_link(filename)
            lines.append(f"{bullet} — {attribution}")

    lines.append("")
    return "\n".join(lines)


def build_claim_index(claim: str, papers: list[dict], citation_data: dict) -> str:
    """Generate a claim index markdown string for one QA claim value."""
    display = f"Quantum Advantage: {_tag_display_name(claim)}"
    tagged = [p for p in papers if p["quantum_advantage_claim"] == claim]
    tagged = _sort_papers_by_year(tagged)

    lines = [
        f"# {display}",
        "",
        f"**Papers:** {len(tagged)}",
        "",
        "## Papers",
        "",
        "| Paper | Year | Source Type | Topics | Methods |",
        "|-------|------|-------------|--------|---------|",
    ]
    for p in tagged:
        lines.append(_paper_row_claim(p))

    # Evidence summary
    sim_only = sum(
        1 for p in tagged
        if any(t in p.get("idea_tags", []) for t in ["limitation:simulation-only"])
        or "simulation" in " ".join(p.get("methodology_tags", [])).lower()
    )
    real_qpu = sum(
        1 for p in tagged
        if any("qpu" in t.lower() or "hardware" in t.lower() for t in p.get("methodology_tags", []))
    )
    empirical = sum(1 for p in tagged if "empirical" in (p.get("source_type") or ""))
    theoretical = sum(1 for p in tagged if "theoretical" in (p.get("source_type") or ""))

    lines.append("")
    lines.append("## Evidence Summary")
    lines.append("")
    lines.append(f"- {empirical} empirical papers")
    lines.append(f"- {theoretical} theoretical papers")
    if sim_only:
        lines.append(f"- {sim_only} papers rely on simulation only")
    if real_qpu:
        lines.append(f"- {real_qpu} papers tested on real QPU")

    lines.append("")
    return "\n".join(lines)


def build_overview(papers: list[dict], citation_data: dict) -> str:
    """Generate the overview dashboard markdown."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    total = len(papers)

    years = [p["year"] for p in papers if p.get("year")]
    year_range = f"{min(years)}–{max(years)}" if years else "—"
    experiment_count = sum(1 for p in papers if p["has_experiment_details"])

    lines = [
        "# SLR Overview Dashboard",
        "",
        f"Generated: {now}",
        "",
        "## Summary",
        "",
        f"- **Total papers:** {total}",
        f"- **Year range:** {year_range}",
        f"- **Papers with experiment details:** {experiment_count}",
        "",
    ]

    # Source Type Distribution
    source_counts: Counter = Counter()
    for p in papers:
        st = p["source_type"] or "unknown"
        source_counts[st] += 1

    lines.append("## Source Type Distribution")
    lines.append("")
    lines.append("| Source Type | Count |")
    lines.append("|-------------|-------|")
    for st, count in source_counts.most_common():
        lines.append(f"| {st} | {count} |")
    lines.append("")

    # Topic Distribution
    topic_counts: Counter = Counter()
    topic_methods: dict[str, Counter] = {}
    for p in papers:
        for t in p["topic_tags"]:
            topic_counts[t] += 1
            if t not in topic_methods:
                topic_methods[t] = Counter()
            for m in p["methodology_tags"]:
                topic_methods[t][m] += 1

    lines.append("## Topic Distribution")
    lines.append("")
    lines.append("| Topic | Papers | Most Common Method |")
    lines.append("|-------|--------|--------------------|")
    for topic, count in topic_counts.most_common():
        mc = topic_methods[topic].most_common(1)
        top_method = mc[0][0] if mc else "—"
        lines.append(f"| {topic} | {count} | {top_method} |")
    lines.append("")

    # Methodology Distribution
    method_counts: Counter = Counter()
    method_topics: dict[str, Counter] = {}
    for p in papers:
        for m in p["methodology_tags"]:
            method_counts[m] += 1
            if m not in method_topics:
                method_topics[m] = Counter()
            for t in p["topic_tags"]:
                method_topics[m][t] += 1

    lines.append("## Methodology Distribution")
    lines.append("")
    lines.append("| Method | Papers | Most Common Topic |")
    lines.append("|--------|--------|--------------------|")
    for method, count in method_counts.most_common():
        mc = method_topics[method].most_common(1)
        top_topic = mc[0][0] if mc else "—"
        lines.append(f"| {method} | {count} | {top_topic} |")
    lines.append("")

    # Quantum Advantage Claims
    qa_counts: Counter = Counter()
    for p in papers:
        qa = p["quantum_advantage_claim"] or "unknown"
        qa_counts[qa] += 1

    lines.append("## Quantum Advantage Claims")
    lines.append("")
    lines.append("| Claim | Count |")
    lines.append("|-------|-------|")
    for claim, count in qa_counts.most_common():
        lines.append(f"| {claim} | {count} |")
    lines.append("")

    # Year Distribution
    year_counts: Counter = Counter()
    for p in papers:
        if p.get("year"):
            year_counts[p["year"]] += 1

    lines.append("## Year Distribution")
    lines.append("")
    lines.append("| Year | Papers |")
    lines.append("|------|--------|")
    for year in sorted(year_counts.keys(), reverse=True):
        lines.append(f"| {year} | {year_counts[year]} |")
    lines.append("")

    # Research Gaps
    sparse_topics = [t for t, c in topic_counts.items() if c < 3]
    no_empirical_methods = [
        m for m in method_counts
        if not any(
            "empirical" in p.get("source_type", "")
            for p in papers
            if m in p["methodology_tags"]
        )
    ]
    demonstrated_topics = set()
    for p in papers:
        if p["quantum_advantage_claim"] == "demonstrated":
            for t in p["topic_tags"]:
                demonstrated_topics.add(t)
    no_demonstrated = [t for t in topic_counts if t not in demonstrated_topics]

    lines.append("## Research Gaps")
    lines.append("")
    if sparse_topics:
        lines.append(f"- Topics with < 3 papers: {', '.join(sorted(sparse_topics))}")
    else:
        lines.append("- Topics with < 3 papers: none")
    if no_empirical_methods:
        lines.append(f"- Methods with no empirical validation: {', '.join(sorted(no_empirical_methods))}")
    else:
        lines.append("- Methods with no empirical validation: none")
    if no_demonstrated:
        lines.append(f'- Topics with no "demonstrated" quantum advantage: {", ".join(sorted(no_demonstrated))}')
    else:
        lines.append('- Topics with no "demonstrated" quantum advantage: none')
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# File writers
# ---------------------------------------------------------------------------

def _write_file(path: str, content: str) -> None:
    """Write content to a file, creating directories as needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build thematic index files from processed papers."
    )
    parser.add_argument(
        "--rebuild",
        action="store_true",
        default=False,
        help="Regenerate all index files (default behavior when run with no flags).",
    )
    parser.add_argument(
        "--topic",
        type=str,
        default=None,
        help="Generate only one topic index (e.g. portfolio-optimisation).",
    )
    parser.add_argument(
        "--overview-only",
        action="store_true",
        default=False,
        help="Generate only the overview dashboard.",
    )
    args = parser.parse_args()

    # Collect data from all papers
    paper_files = _list_papers()
    if not paper_files:
        print("No processed papers found.")
        return

    print(f"Reading {len(paper_files)} papers...")
    all_papers = _collect_paper_data(paper_files)
    logger.info("Collected data from %d papers", len(all_papers))

    citation_data = _load_citation_data()

    # Determine what to build
    build_all = not args.topic and not args.overview_only

    topic_count = 0
    method_count = 0
    claim_count = 0

    if args.topic:
        # Single topic
        content = build_topic_index(args.topic, all_papers)
        out_path = os.path.join(ANALYSIS_DIR, "by_topic", f"{args.topic}.md")
        _write_file(out_path, content)
        tagged = [p for p in all_papers if args.topic in p["topic_tags"]]
        print(f"Generated topic index: {args.topic} ({len(tagged)} papers)")
        topic_count = 1

    if build_all:
        # Collect all unique tags
        all_topics: set[str] = set()
        all_methods: set[str] = set()
        all_claims: set[str] = set()

        for p in all_papers:
            all_topics.update(p["topic_tags"])
            all_methods.update(p["methodology_tags"])
            qa = p["quantum_advantage_claim"]
            if qa:
                all_claims.add(qa)

        # Topic indices
        print(f"Building topic indices... ({len(all_topics)} tags)")
        for tag in sorted(all_topics):
            content = build_topic_index(tag, all_papers)
            out_path = os.path.join(ANALYSIS_DIR, "by_topic", f"{tag}.md")
            _write_file(out_path, content)
            topic_count += 1

        # Method indices
        print(f"Building method indices... ({len(all_methods)} tags)")
        for tag in sorted(all_methods):
            content = build_method_index(tag, all_papers)
            out_path = os.path.join(ANALYSIS_DIR, "by_method", f"{tag}.md")
            _write_file(out_path, content)
            method_count += 1

        # Claim indices
        print(f"Building claim indices... ({len(all_claims)} claims)")
        for claim in sorted(all_claims):
            content = build_claim_index(claim, all_papers, citation_data)
            out_path = os.path.join(ANALYSIS_DIR, "by_claim", f"{claim}.md")
            _write_file(out_path, content)
            claim_count += 1

    # Overview dashboard
    if build_all or args.overview_only:
        print("Building overview dashboard...")
        content = build_overview(all_papers, citation_data)
        out_path = os.path.join(ANALYSIS_DIR, "overview.md")
        _write_file(out_path, content)

    # Summary
    parts = []
    if topic_count:
        parts.append(f"{topic_count} topic indices")
    if method_count:
        parts.append(f"{method_count} method indices")
    if claim_count:
        parts.append(f"{claim_count} claim indices")
    if build_all or args.overview_only:
        parts.append("1 overview dashboard")

    print(f"Generated {', '.join(parts)}")
    logger.info("Index generation complete: %s", ", ".join(parts))


if __name__ == "__main__":
    main()
