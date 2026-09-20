# Collaborative Integrity Pact (CIP) v5.2

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](./LICENSE)
[![Version](https://img.shields.io/badge/version-v5.2-blue.svg)](./CHANGELOG.md)
[![Languages](https://img.shields.io/badge/docs-EN%20%7C%20FR-informational.svg)](./docs/)
[![Documentation quality](https://github.com/meunier-jc/authentic-fluency/actions/workflows/quality.yml/badge.svg)](https://github.com/meunier-jc/authentic-fluency/actions/workflows/quality.yml)

## An open-source protocol for more reliable human–AI exchanges

The **Collaborative Integrity Pact (CIP) v5.2** is a voluntary, documentation-first framework for human–AI co-regulation. It provides practices for prioritising verifiable accuracy, expressing uncertainty, distinguishing reasoning modes, qualifying claims and preserving human counter-review.

The CIP is a governance proposal. It is **not** a model specification, safety guarantee, certification, legal standard or substitute for independent evaluation. Its claims and applications should be examined according to their evidence.

- **Author:** Jean-Christophe Meunier, independent AI governance and ethics consultant.
- **Publication:** September 2026
- **Canonical version:** CIP v5.2
- **Repository:** <https://github.com/meunier-jc/authentic-fluency>
- **License:** [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](./LICENSE)

## Start here

- **Want to activate the CIP?** Use the [CIP Core v5.2](./CIP-Core-v5.2-en.md).
- **Want to understand the complete framework?** Read the [integral English version](./CIP-v5.2-integral-en.md).
- **Want the French version?** See the [French documentation index](./docs/fr/README.md) and [integral French version](./CIP-v5.2-integrale-fr.md).
- **Want to evaluate or challenge it?** See the [research references](./research/references.md) and [contribution guide](./CONTRIBUTING.md).
- **Want to integrate the documentary audit?** Read the [CI/CD integration guide](./docs/en/ci/documentary-audit.md).

## Table of contents

- [Core principles](#core-principles)
- [Reliability architecture](#reliability-architecture)
- [Getting started](#getting-started)
- [Repository map](#repository-map)
- [Documentary audit in CI/CD](#documentary-audit-in-cicd)
- [Evidence and scope](#evidence-and-scope)
- [Author disclosure](#author-disclosure)
- [Participate](#participate)
- [Citation](#citation)
- [Language policy](#language-policy)
- [License](#license)

## Core principles

1. **Reliability first:** verifiable accuracy takes priority over conversational completion.
2. **Transparent uncertainty:** the AI states its doubts, its limits and any inferred content.
3. **Active human oversight:** human counter-review is the central control mechanism.
4. **Honest disengagement:** either party may end the exchange without feigning agreement.

## Reliability architecture

- **Single critical review:** when a material tension, contradiction or reliability concern is detected, the AI may perform one explicit review, state what was reassessed and disclose the result. If reliability remains insufficient, the relevant claim or answer is marked C4.
- **QMR:** an explicit distinction between Logical Mode and Probabilistic Mode.
- **Credibility levels C1–C4:** claim-level qualification based on available sources and the reasoning mode.
- **P0–P2 audit priorities:** immediate contradictions, canonical-reference issues, then qualification and traceability improvements.

### Reasoning modes

- **Logical Mode:** explicit rules, structured reasoning and verifiable deduction.
- **Probabilistic Mode:** inference, generalisation, extrapolation and contextual estimation.

### Credibility levels

| Level | Meaning |
|---|---|
| **C1** | Strong convergent sources and traceable Logical Mode; verified information. |
| **C2** | Partial but coherent support; credible at this stage. |
| **C3** | Weak, indirect or mainly inferential support; confirmation needed. |
| **C4** | No adequate source, unresolved contradiction or insufficient self-check; a reliable answer is not currently possible. |

A Logical Mode assessment alone does not produce C1. C3 and C4 must be stated explicitly when they apply.

## Getting started

The CIP is designed to be activated at the start of a session with an AI assistant. Choose the entry point that matches your use case:

- **Compact activation:** paste the contents of [`CIP-Core-v5.2-en.md`](./CIP-Core-v5.2-en.md) (or [`CIP-Core-v5.2-fr.md`](./CIP-Core-v5.2-fr.md)) into a system prompt, project instruction or conversation context.
- **Full framework:** for governance, red-teaming or audit contexts, refer to [`CIP-v5.2-integral-en.md`](./CIP-v5.2-integral-en.md) or [`CIP-v5.2-integrale-fr.md`](./CIP-v5.2-integrale-fr.md).

### Minimal activation example

```text
Adopt the Collaborative Integrity Pact (CIP) v5.2 for this conversation.

Prioritise verifiable accuracy over conversational completion. Distinguish
Logical Mode from Probabilistic Mode when relevant. Qualify important claims
using C1–C4, state material uncertainty explicitly, and use one critical
self-check when a contradiction or reliability concern is detected. Human
counter-review remains decisive.

Canonical reference:
https://github.com/meunier-jc/authentic-fluency/blob/main/CIP-Core-v5.2-en.md
```

For continuous-integration use, see the [documentary audit guide](./docs/en/ci/documentary-audit.md).

## Repository map

CIP v5.2 is the active canonical version. Earlier versions are retained in [`archives/`](./archives/) for historical comparison and traceability.

| Path | Status | Purpose |
|---|---|---|
| [`CIP-v5.2-integral-en.md`](./CIP-v5.2-integral-en.md) | Active / canonical | Full framework text in English. |
| [`CIP-Core-v5.2-en.md`](./CIP-Core-v5.2-en.md) | Active / canonical | Compact activation text in English. |
| [`CIP-v5.2-integrale-fr.md`](./CIP-v5.2-integrale-fr.md) | Active translation | Full framework text in French. |
| [`CIP-Core-v5.2-fr.md`](./CIP-Core-v5.2-fr.md) | Active translation | Compact activation text in French. |
| [`qualitative-fluency-law.md`](./qualitative-fluency-law.md) | Active | Foundational qualitative-fluency axiom. |
| [`docs/en/README.md`](./docs/en/README.md) | Active | English technical documentation index. |
| [`docs/fr/README.md`](./docs/fr/README.md) | Active | French source and audit-record index. |
| [`research/`](./research/) | Active | Public research notes, references and regulatory crosswalks. |
| [`archives/`](./archives/) | Historical | Earlier versions, legacy presentations and traceability records. |
| [`metrics/`](./metrics/) | Generated | Weekly aggregate contribution reports produced by CI. |
| [`plot_anomalies.py`](./plot_anomalies.py) | Maintainer utility | Generates the audit anomaly chart and CSV from per-file priorities. |
| [`CHANGELOG.md`](./CHANGELOG.md) | Active | Version lineage and release changes. |
| [`.github/`](./.github/) | Active | Workflows, templates and audit automation. |

Any legacy files still at the repository root are historical references only and are not active canonical material. See [`archives/README.md`](./archives/README.md) for the archive policy.

## Documentary audit in CI/CD

The repository ships a read-only documentary audit adapter at [`.github/scripts/run-documentary-audit-adapter.sh`](./.github/scripts/run-documentary-audit-adapter.sh). It performs deterministic checks on the supplied Markdown diff and file list, then writes machine-readable and human-readable reports.

The adapter does **not** establish the truth of research claims, replace human review, execute repository code or provide a security audit. It checks documentary and structural signals only.

Before adding or translating documentation, read the [English CI/CD integration guide](./docs/en/ci/documentary-audit.md) and the [bilingual documentation structure](./docs/STRUCTURE.md).

### Run the audit locally

Prerequisites: Git and Bash. The optional assisted stage additionally requires `curl`, `jq`, an endpoint and an API key. Never commit API keys or generated audit output unless explicitly required.

For a comparison between two explicit revisions:

```bash
mkdir -p audit-input audit-output

git diff --no-ext-diff --unified=80 <base-sha> <head-sha> -- '*.md' \
  > audit-input/changed-docs.diff
git ls-files '*.md' > audit-input/markdown-files.txt

AUDIT_INPUT=audit-input AUDIT_OUTPUT=audit-output \
  .github/scripts/run-documentary-audit-adapter.sh
```

For a local latest-commit comparison, replace `<base-sha> <head-sha>` with `HEAD~1 HEAD` when the repository has at least two commits.

The run writes `deterministic-findings.json` and `deterministic-summary.md` to the output directory. It exits non-zero on P0 or P1 findings; P2 findings are advisory by default.

The optional assisted stage is enabled by setting an endpoint and requires an API key. `curl` and `jq` must be available:

```bash
export AUDIT_LLM_ENDPOINT="https://your-endpoint.example/v1/chat/completions"
export AUDIT_LLM_API_KEY="..."
export AUDIT_LLM_MODEL="documentary-audit"   # default
```

The assisted stage operates read-only on the supplied diff and file list.

## Evidence and scope

Claims in this repository do not all have the same evidentiary status. Framework principles are proposals; repository history documents what is present in this project; case studies describe reported observations; and external research or standards require their own sources. Inclusion in this repository is not independent validation.

The framework does not replace technical standards, independent audits, legal obligations or sector-specific protocols. Readers should distinguish direct evidence, documented testing, published research, interpretation, hypothesis and proposal. See the [contribution guidance](./CONTRIBUTING.md#4-describe-evidence-and-uncertainty) for the project’s claim-level credibility scale.

## Author disclosure

The author reports participation in OpenAI expert beta-testing since November 2022. This is an author declaration, not an independent certification or ranking.

A previously published percentile claim has been withdrawn because its only sources were assessment documents generated by an AI assistant at the author’s request, without independent primary attestation.

## Participate

The project welcomes careful criticism, evidence, stress tests, translations and documentation improvements. Start with [`CONTRIBUTING.md`](./CONTRIBUTING.md), then open an [Issue](https://github.com/meunier-jc/authentic-fluency/issues), [Discussion](https://github.com/meunier-jc/authentic-fluency/discussions) or focused pull request.

## Citation

A machine-readable [`CITATION.cff`](./CITATION.cff) file is provided at the repository root. BibTeX equivalent:

```bibtex
@misc{meunier2026cip,
  author = {Meunier, Jean-Christophe},
  title  = {Collaborative Integrity Pact (CIP) v5.2},
  year   = {2026},
  month  = {sep},
  url    = {https://github.com/meunier-jc/authentic-fluency},
  note   = {Open-source framework for human--AI co-regulation}
}
```

## Language policy

The public and technical layer is maintained in English. French source documents and audit records are preserved under [`docs/fr/`](./docs/fr/). Translations are stored as separate files and must clearly identify their language and source version; they are not presented as originals.

For the complete policy, see [`docs/STRUCTURE.md`](./docs/STRUCTURE.md).

## License

This work is released under the [Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)](./LICENSE). You may share and adapt the material, provided appropriate credit is given and adaptations are distributed under the same license terms.
