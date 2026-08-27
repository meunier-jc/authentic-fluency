# Documentary audit in CI/CD

## Purpose

`repository-documentary-audit` turns documentary quality into a repeatable pull-request control. The pipeline detects obsolete versions, contradictory figures, broken links, unsupported metrics and over-strong claims while keeping the repository read-only by default.

## Two-stage architecture

The pipeline has two separate stages.

The **deterministic stage** runs on every pull request. It performs Markdown linting, link checks, required-file checks, forbidden active-version checks, obsolete-value checks and `git diff --check`. These checks are fast, reproducible and independent of an AI service.

The **assisted stage** is optional. It receives only the documentary diff and the approved Markdown file list. It applies the `repository-documentary-audit` protocol to identify claims, evidence types, priorities P0–P2 and credibility levels C1–C4. Its output is advisory unless the repository maintainers explicitly configure a blocking threshold.

## Adapter contract

The adapter is available at `.github/scripts/run-documentary-audit-adapter.sh` and in the reusable skill package.

Required environment variables:

- `AUDIT_INPUT`: directory containing `changed-docs.diff` and `markdown-files.txt`.
- `AUDIT_OUTPUT`: directory where reports are written.

Optional assisted-mode variables:

- `AUDIT_LLM_ENDPOINT`: OpenAI-compatible chat-completions endpoint.
- `AUDIT_LLM_API_KEY`: service key stored in GitHub Actions secrets.
- `AUDIT_LLM_MODEL`: model identifier used by the endpoint.

The adapter writes `deterministic-findings.json` and `deterministic-summary.md`. It fails on deterministic P0 or P1 findings and leaves P2 findings advisory by default. It never creates a commit, pushes a branch, modifies a file or marks a notification as read.

## Recommended workflow permissions

```yaml
permissions:
  contents: read
  pull-requests: read
```

Use the `pull_request` event for untrusted contribution code. Do not expose service secrets to forked pull requests. Do not use `pull_request_target` to execute or checkout untrusted code.

## Example workflow steps

```yaml
- uses: actions/checkout@v4
  with:
    fetch-depth: 0

- name: Build documentary inputs
  shell: bash
  run: |
    set -euo pipefail
    mkdir -p audit-input audit-output
    git diff --no-ext-diff --unified=80 \
      "${{ github.event.pull_request.base.sha || github.event.before }}" \
      "${{ github.sha }}" -- '*.md' > audit-input/changed-docs.diff
    git ls-files '*.md' > audit-input/markdown-files.txt

- name: Run documentary adapter
  env:
    AUDIT_INPUT: audit-input
    AUDIT_OUTPUT: audit-output
  run: .github/scripts/run-documentary-audit-adapter.sh

- name: Upload audit evidence
  if: always()
  uses: actions/upload-artifact@v4
  with:
    name: documentary-audit-report
    path: audit-output/
```

## Rollout

Start in advisory mode and measure false positives. After maintainers review the reports, make P0 blocking, normally require review for P1 and keep P2 as tracked recommendations. Re-run the deterministic checks after every change to the adapter, the Markdown rules or the canonical documentation paths.

## Data handling

Send the smallest possible input to an assisted service: the diff and the relevant documentation only. Never send personal access tokens, unrelated private files or authentication cookies. Store service keys only in GitHub Actions secrets, and keep the assisted job separate from any job that can write to the repository.
