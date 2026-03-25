#!/usr/bin/env bash
# run_full_pipeline.sh — Run the complete SLR pipeline end-to-end.
#
# Usage:
#   ./run_full_pipeline.sh                    # Full run (Zotero fetch + extract + analysis)
#   ./run_full_pipeline.sh --skip-fetch       # Skip Zotero, use existing PDFs
#   ./run_full_pipeline.sh --skip-extract     # Skip extraction, only run analysis
#   ./run_full_pipeline.sh --limit 10         # Limit Zotero fetch to 10 papers
#   ./run_full_pipeline.sh --rebuild          # Force rebuild of all analysis caches
#   ./run_full_pipeline.sh --dry-run          # Print commands without executing

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

PYTHON="${PYTHON:-python}"
COLLECTION="${ZOTERO_COLLECTION:-PVDPVINK}"
WORKERS="${WORKERS:-10}"

# Defaults
SKIP_FETCH=false
SKIP_EXTRACT=false
LIMIT=0
REBUILD=""
DRY_RUN=false

# Parse arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --skip-fetch)    SKIP_FETCH=true; shift ;;
        --skip-extract)  SKIP_EXTRACT=true; shift ;;
        --limit)         LIMIT="$2"; shift 2 ;;
        --rebuild)       REBUILD="--rebuild"; shift ;;
        --workers)       WORKERS="$2"; shift 2 ;;
        --dry-run)       DRY_RUN=true; shift ;;
        -h|--help)
            head -10 "$0" | tail -7
            exit 0
            ;;
        *) echo "Unknown option: $1"; exit 1 ;;
    esac
done

run() {
    echo ""
    echo "================================================================"
    echo ">> $*"
    echo "================================================================"
    if [ "$DRY_RUN" = true ]; then
        echo "   (dry-run — skipped)"
    else
        "$@"
    fi
}

FAILED=()

run_safe() {
    if ! run "$@"; then
        FAILED+=("$*")
        echo "!! FAILED: $* (continuing...)"
    fi
}

# -----------------------------------------------------------------------
# Phase 1: Fetch PDFs from Zotero
# -----------------------------------------------------------------------
if [ "$SKIP_FETCH" = false ] && [ "$SKIP_EXTRACT" = false ]; then
    FETCH_ARGS=("$PYTHON" scripts/fetch_from_zotero.py --collection "$COLLECTION" --process)
    if [ "$LIMIT" -gt 0 ]; then
        FETCH_ARGS+=(--limit "$LIMIT")
    fi
    run_safe "${FETCH_ARGS[@]}"

# -----------------------------------------------------------------------
# Phase 2: Batch extraction only (if skipping fetch but not extract)
# -----------------------------------------------------------------------
elif [ "$SKIP_FETCH" = true ] && [ "$SKIP_EXTRACT" = false ]; then
    run_safe "$PYTHON" scripts/run_extraction_step.py --batch --from-step 1 --workers "$WORKERS"
fi

# -----------------------------------------------------------------------
# Phase 3: Validate all processed papers
# -----------------------------------------------------------------------
if [ "$SKIP_EXTRACT" = false ]; then
    run_safe "$PYTHON" scripts/validate_markdown.py --batch
fi

# -----------------------------------------------------------------------
# Phase 4: Analysis (no LLM — API/local only)
# -----------------------------------------------------------------------
run_safe "$PYTHON" scripts/build_citation_graph.py $REBUILD
run_safe "$PYTHON" scripts/report_missing_papers.py

# -----------------------------------------------------------------------
# Phase 5: Analysis (LLM-powered)
# -----------------------------------------------------------------------
run_safe "$PYTHON" scripts/discover_tags.py
run_safe "$PYTHON" scripts/detect_contradictions.py $REBUILD

# -----------------------------------------------------------------------
# Phase 6: Build all indices (reads local data, no LLM)
# -----------------------------------------------------------------------
run_safe "$PYTHON" scripts/build_indices.py $REBUILD

# -----------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------
echo ""
echo "================================================================"
echo "Pipeline complete."
echo "================================================================"

if [ ${#FAILED[@]} -gt 0 ]; then
    echo ""
    echo "WARNING: ${#FAILED[@]} step(s) failed:"
    for cmd in "${FAILED[@]}"; do
        echo "  - $cmd"
    done
    exit 1
else
    echo "All steps succeeded."
fi
