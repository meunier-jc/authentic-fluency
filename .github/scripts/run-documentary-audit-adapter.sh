#!/usr/bin/env bash
set -euo pipefail

# Adapter read-only for CI/CD documentary audits.
# Required: AUDIT_INPUT, AUDIT_OUTPUT
# Optional assisted mode: AUDIT_LLM_ENDPOINT, AUDIT_LLM_API_KEY, AUDIT_LLM_MODEL

INPUT_DIR="${AUDIT_INPUT:-audit-input}"
OUTPUT_DIR="${AUDIT_OUTPUT:-audit-output}"
MODEL="${AUDIT_LLM_MODEL:-documentary-audit}"
mkdir -p "$OUTPUT_DIR"

for required in "$INPUT_DIR/changed-docs.diff" "$INPUT_DIR/markdown-files.txt"; do
  test -f "$required" || { echo "Missing audit input: $required" >&2; exit 2; }
done

REPORT="$OUTPUT_DIR/deterministic-findings.json"
SUMMARY="$OUTPUT_DIR/deterministic-summary.md"

python3 - "$INPUT_DIR" "$REPORT" "$SUMMARY" <<'PY'
import json, pathlib, re, sys

input_dir = pathlib.Path(sys.argv[1])
report_path = pathlib.Path(sys.argv[2])
summary_path = pathlib.Path(sys.argv[3])
diff = (input_dir / "changed-docs.diff").read_text(errors="replace")
files = (input_dir / "markdown-files.txt").read_text(errors="replace").splitlines()
findings = []
changed_lines = []
current_file = None
current_line = 0
for raw in diff.splitlines():
    if raw.startswith("+++ b/"):
        current_file = raw[6:]
        current_line = 0
    elif raw.startswith("@@"):
        match = re.search(r"\+(\d+)", raw)
        current_line = int(match.group(1)) - 1 if match else current_line
    elif current_file and raw.startswith("+") and not raw.startswith("+++"):
        current_line += 1
        changed_lines.append((current_file, current_line, raw[1:]))
    elif current_file and not raw.startswith("-"):
        current_line += 1

patterns = [
    (r"CIP[- ]v5\.0|CIP-Core[- ]v5\.0", "P1", "Obsolete active version reference"),
    (r"1[,.]2\s*%|1\.2%", "P0", "Obsolete percentile reference"),
    (r"\b(unique|first formal|discoverer|inédit|découvreur)\b", "P2", "Unqualified novelty claim"),
    (r"\b(major systemic risk|global financial crisis|risque systémique majeur|crise financière mondiale)\b", "P2", "Unqualified causal or systemic claim"),
    (r"\b(97%|>95%|<3%)\b", "P2", "Metric without visible protocol"),
    (r"INPI Soleau envelope filed", "P2", "Unverified filing claim"),
]

for filename, line_no, line in changed_lines:
    if not filename.endswith(".md"):
        continue
    # French source/audit records and dated archives preserve historical evidence;
    # they are intentionally non-blocking and are reviewed through their own audit trail.
    if filename.startswith("docs/fr/") or filename.startswith("archives/"):
        continue
    for pattern, priority, message in patterns:
        if re.search(pattern, line, re.IGNORECASE):
            findings.append({"file": filename, "line": line_no, "priority": priority, "message": message, "evidence": line.strip()[:500]})

report_path.write_text(json.dumps({"mode": "deterministic", "findings": findings}, ensure_ascii=False, indent=2) + "\n")
counts = {p: sum(1 for x in findings if x["priority"] == p) for p in ("P0", "P1", "P2")}
summary = ["# Deterministic documentary audit", "", f"Findings: {len(findings)}", "", "| Priority | Count |", "|---|---:|"]
summary += [f"| {p} | {counts[p]} |" for p in ("P0", "P1", "P2")]
summary += ["", "The adapter is read-only. No file, commit, branch or remote was modified.", ""]
summary_path.write_text("\n".join(summary))
PY

if [[ -n "${AUDIT_LLM_ENDPOINT:-}" ]]; then
  command -v curl >/dev/null || { echo "curl is required for assisted mode" >&2; exit 2; }
  command -v jq >/dev/null || { echo "jq is required for assisted mode" >&2; exit 2; }
  test -n "${AUDIT_LLM_API_KEY:-}" || { echo "AUDIT_LLM_API_KEY is required when AUDIT_LLM_ENDPOINT is set" >&2; exit 2; }

  prompt_file="$OUTPUT_DIR/assisted-audit-prompt.txt"
  {
    echo "You are a documentary audit agent. Work in READ-ONLY mode. Do not modify files, create commits, push, comment, or expose secrets. Analyze only the supplied diff and file list. Return strict JSON with a top-level findings array. Each finding must contain: finding_id, file, line, priority (P0/P1/P2), claim, evidence, recommendation, status. Distinguish direct evidence, author declaration, interpretation, and missing evidence."
    echo
    echo "=== CHANGED DOCUMENTS DIFF ==="
    cat "$INPUT_DIR/changed-docs.diff"
    echo
    echo "=== MARKDOWN FILE LIST ==="
    cat "$INPUT_DIR/markdown-files.txt"
  } > "$prompt_file"

  jq -n --arg model "$MODEL" --rawfile prompt "$prompt_file" \
    '{model:$model,temperature:0,messages:[{role:"user",content:$prompt}]}' \
    | curl --fail-with-body --silent --show-error \
        -H "Authorization: Bearer ${AUDIT_LLM_API_KEY}" \
        -H "Content-Type: application/json" \
        --data-binary @- "${AUDIT_LLM_ENDPOINT}" \
    | tee "$OUTPUT_DIR/assisted-audit-response.json" >/dev/null
else
  cat > "$OUTPUT_DIR/assisted-audit-disabled.md" <<'EOF'
# Assisted documentary audit

Assisted mode was not enabled. Set `AUDIT_LLM_ENDPOINT`, `AUDIT_LLM_API_KEY` and optionally `AUDIT_LLM_MODEL` to run the agent review. Deterministic checks completed independently.
EOF
fi

# Block only on deterministic P0/P1 findings; P2 remains advisory by default.
python3 - "$REPORT" <<'PY'
import json, sys
report = json.load(open(sys.argv[1]))
blocking = [f for f in report["findings"] if f["priority"] in {"P0", "P1"}]
if blocking:
    print(f"Blocking documentary findings: {len(blocking)}", file=sys.stderr)
    for f in blocking[:20]:
        print(f"{f['priority']} {f['file']}:{f['line']} — {f['message']}", file=sys.stderr)
    sys.exit(1)
print("No blocking deterministic documentary findings.")
PY
