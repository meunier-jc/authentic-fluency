# Meunier’s AI–Human Collaborative Integrity Pact (CIP) v5.1

## Open-source framework for human–AI co-regulation

The **Collaborative Integrity Pact (CIP) v5.1** is an operational framework for more reliable, transparent and accountable human–AI collaboration. It gives priority to verifiable accuracy, explicit uncertainty and active human counter-review.

**Author:** Jean-Christophe Meunier, independent AI governance and ethics consultant. The repository records an author-declared OpenAI beta-testing profile and a declared 1.5% global ranking; these claims are not presented as independent certification.

**Publication:** August 2026

**Canonical version:** CIP v5.1

**Repository:** <https://github.com/meunier-jc/authentic-fluency>

## Core principles

1. **Reliability first:** verifiable accuracy takes priority over conversational completion.
2. **Uncertainty transparency:** the AI must state doubts, limits and inferred content.
3. **Active human oversight:** human counter-review is the central control mechanism.
4. **Honest disengagement:** either party may withdraw without simulating agreement.

## Reliability architecture

- **Single self-check:** one critical review per response, with C4 escalation if it fails.
- **QMR:** explicit distinction between logical and probabilistic reasoning modes.
- **Credibility levels C1–C4:** convergent sources combined with the reasoning mode; C1 requires both.
- **P0–P2 audit priorities:** immediate contradictions, canonical-reference issues and qualification or traceability improvements.

## Repository map

| Path | Purpose |
|---|---|
| [`CIP-v5.1.md`](./CIP-v5.1.md) | Canonical full framework text. |
| [`CIP-Core-v5.1.md`](./CIP-Core-v5.1.md) | Compact activation text. |
| [`qualitative-fluency-law.md`](./qualitative-fluency-law.md) | Foundational qualitative-fluency axiom. |
| [`docs/en/`](./docs/en/) | English technical documentation and CI/CD integration guide. |
| [`docs/fr/`](./docs/fr/) | French source reports and audit records. |
| [`research/`](./research/) | Public research notes, references and regulatory crosswalks. |
| [`archives/`](./archives/) | Versioned historical material. |
| [`CHANGELOG.md`](./CHANGELOG.md) | Version lineage and release changes. |
| [`.github/`](./.github/) | GitHub workflows, templates and audit automation. |

## Documentary audit in CI/CD

The repository includes a read-only documentary audit adapter at [`.github/scripts/run-documentary-audit-adapter.sh`](./.github/scripts/run-documentary-audit-adapter.sh). It performs deterministic checks for obsolete versions, contradictory rates, unsupported claims and Markdown quality. An optional assisted stage can classify claims and evidence using the `repository-documentary-audit` protocol.

Read the [English CI/CD integration guide](./docs/en/ci/documentary-audit.md) and the [bilingual documentation structure](./docs/STRUCTURE.md) before adding or translating documentation.

## Evidence and scope

The framework is a governance proposal and does not replace technical standards, independent audits, legal obligations or sector-specific protocols. Public documentation distinguishes direct evidence, author declarations, interpretations and hypotheses. Historical versions remain available as dated archives.

## Contributing and security

Please read [`CONTRIBUTING.md`](./CONTRIBUTING.md) before opening a pull request. Use the repository’s quality workflow for Markdown, links, required files and documentary checks. Report security issues through [`SECURITY.md`](./SECURITY.md).

## Citation

```bibtex
@misc{meunier2026cip,
  author = {Meunier, Jean-Christophe},
  title = {Collaborative Integrity Pact (CIP) v5.1},
  year = {2026},
  month = {aug},
  url = {https://github.com/meunier-jc/authentic-fluency},
  note = {Open-source framework for human--AI co-regulation}
}
```

## Language policy

The public and technical layer is maintained in English. French source documents and audit records are preserved under [`docs/fr/`](./docs/fr/). A translation must be stored as a separate file and must identify its source, date and status; it must never overwrite an original.
