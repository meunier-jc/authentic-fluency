# Collaborative Integrity Pact (CIP) v5.2

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](./LICENSE)
[![Version](https://img.shields.io/badge/version-v5.2-blue.svg)](./CHANGELOG.md)
[![Languages](https://img.shields.io/badge/docs-EN%20%7C%20FR-informational.svg)](./docs/)
[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)](#)

## An open-source framework for human–AI co-regulation

The **Collaborative Integrity Pact (CIP) v5.2** is an operational framework for more reliable, transparent and accountable human–AI collaboration. It prioritises verifiable accuracy, explicit uncertainty and active human counter-review over conversational smoothness.

- **Author:** Jean-Christophe Meunier, independent AI governance and ethics consultant.
- **Publication:** September 2026
- **Canonical version:** CIP v5.2
- **Repository:** <https://github.com/meunier-jc/authentic-fluency>
- **License:** [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](./LICENSE)

## Table of contents

- [Core principles](#core-principles)
- [Reliability architecture](#reliability-architecture)
- [Getting started](#getting-started)
- [Repository map](#repository-map)
- [Documentary audit in CI/CD](#documentary-audit-in-cicd)
- [Evidence and scope](#evidence-and-scope)
- [Author disclosure](#author-disclosure)
- [Contributing and security](#contributing-and-security)
- [Citation](#citation)
- [Language policy](#language-policy)
- [License](#license)

## Core principles

1. **Reliability first:** verifiable accuracy takes priority over conversational completion.
2. **Transparent uncertainty:** the AI states its doubts, its limits and any inferred content.
3. **Active human oversight:** human counter-review is the central control mechanism.
4. **Honest disengagement:** either party may end the exchange without feigning agreement.

## Reliability architecture

- **Single self-check:** one critical review per response, with a C4 escalation if it fails.
- **QMR:** an explicit distinction between logical and probabilistic reasoning modes.
- **Credibility levels C1–C4:** convergent sources combined with the reasoning mode; C1 requires both.
- **P0–P2 audit priorities:** immediate contradictions, canonical-reference issues, then qualification and traceability improvements.

## Getting started

The CIP is designed to be activated at the start of a session with an AI assistant. Two entry points are available:

- **Compact activation:** paste the contents of [`CIP-Core-v5.2-en.md`](./CIP-Core-v5.2-en.md) (or [`CIP-Core-v5.2-fr.md`](./CIP-Core-v5.2-fr.md)) into a system prompt, a project instruction or the first message of a conversation.
- **Full framework:** for governance, red-teaming or audit contexts, refer to [`CIP-v5.2-integral-en.md`](./CIP-v5.2-integral-en.md) / [`CIP-v5.2-integrale-fr.md`](./CIP-v5.2-integrale-fr.md).

Minimal activation example:

```text
Adopt the Collaborative Integrity Pact (CIP) v5.2 as the governing protocol
for this conversation. Apply reliability-first behaviour, mark uncertainty
explicitly, and use credibility levels C1–C4 when citing sources.
Reference: https://github.com/meunier-jc/authentic-fluency
```

For continuous-integration use, see the [documentary audit guide](./docs/en/ci/documentary-audit.md).

## Repository map

| Path | Purpose |
|---|---|
| [`CIP-v5.2-integral-en.md`](./CIP-v5.2-integral-en.md) | Canonical full framework text (English). |
| [`CIP-Core-v5.2-en.md`](./CIP-Core-v5.2-en.md) | Compact activation text (English). |
| [`CIP-v5.2-integrale-fr.md`](./CIP-v5.2-integrale-fr.md) | Version intégrale canonique (Français). |
| [`CIP-Core-v5.2-fr.md`](./CIP-Core-v5.2-fr.md) | Version compacte d'activation (Français). |
| [`qualitative-fluency-law.md`](./qualitative-fluency-law.md) | Foundational qualitative-fluency axiom. |
| [`docs/en/`](./docs/en/) | English technical documentation and CI/CD integration guide. |
| [`docs/fr/`](./docs/fr/) | French source reports and audit records. |
| [`research/`](./research/) | Public research notes, references and regulatory crosswalks. |
| [`archives/`](./archives/) | Versioned historical material. |
| [`CHANGELOG.md`](./CHANGELOG.md) | Version lineage and release changes. |
| [`.github/`](./.github/) | GitHub workflows, templates and audit automation. |

## Documentary audit in CI/CD

The repository ships a read-only documentary audit adapter at [`.github/scripts/run-documentary-audit-adapter.sh`](./.github/scripts/run-documentary-audit-adapter.sh). It performs deterministic checks for obsolete versions, contradictory rates, unsupported claims and Markdown quality. An optional assisted stage can classify claims and evidence through the `repository-documentary-audit` protocol.

Before adding or translating documentation, read the [English CI/CD integration guide](./docs/en/ci/documentary-audit.md) and the [bilingual documentation structure](./docs/STRUCTURE.md).

## Evidence and scope

The framework is a governance proposal. It does not replace technical standards, independent audits, legal obligations or sector-specific protocols. Public documentation distinguishes direct evidence, author declarations, interpretations and hypotheses. Historical versions remain available as dated archives.

## Author disclosure

The repository records an author-declared OpenAI beta-testing profile and a self-reported 1.5% global ranking. These are declarations by the author and are not presented as independent certification.

## Contributing and security

Read [`CONTRIBUTING.md`](./CONTRIBUTING.md) before opening a pull request, and follow the repository's quality workflow for Markdown, links, required files and documentary checks. Report security issues through [`SECURITY.md`](./SECURITY.md). Contributors are also expected to observe the [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md).

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

The public and technical layer is maintained in English. French source documents and audit records are preserved under [`docs/fr/`](./docs/fr/). A translation must be stored as a separate file identifying its source, date and status; it must never overwrite an original.

## License

This work is released under the [Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)](./LICENSE). You may share and adapt the material, provided appropriate credit is given, a link to the license is provided and derivative works are distributed under the same license.
