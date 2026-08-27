# Contributing to Authentic Fluency and the CIP

Thank you for your interest in **Authentic Fluency** and the **Collaborative Integrity Pact (CIP)**. This repository is an independent, open-source research project about reliability, truthfulness and the structural conditions for responsible Human–AI collaboration.

You do not need to be an expert, agree with every claim, or already know the project vocabulary to participate. The most useful contributions are clear, respectful and traceable. A well-supported objection is as valuable as a proposal for improvement.

## 1. Understand the project first

Start with the following resources:

1. [README](./README.md)
2. [Current framework](./CIP-v5.1.md)
3. [Research references](./research/references.md)
4. [Open collaboration invitation](https://github.com/meunier-jc/authentic-fluency/issues/7)
5. [Code of Conduct](./CODE_OF_CONDUCT.md)

If you are building on an earlier CIP version, consult the historical material in the [Human-AI-Moral-Contract archive](https://github.com/meunier-jc/Human-AI-Moral-Contract) and cite the exact version and file. Do not silently alter historical documents when version traceability matters.

This is a research framework, not a product-support forum, a generic AI commentary board or a compliance checklist. Contributions should connect to the framework, its evidence, its tests, its documentation or its practical application.

## 2. Who can contribute

The project welcomes researchers in AI safety, alignment, reliability, HCI and human–AI interaction; specialists in AI ethics, philosophy of technology, governance and public policy; ML/LLM, evaluation and MLOps engineers; red-teamers and auditors; social scientists, psychologists and UX researchers; organisations with implementation experience; and technical writers, translators, educators and open-source maintainers.

You can contribute by **supporting, challenging, extending, testing, documenting or applying** the framework. No particular academic title or institutional affiliation is required. Good-faith criticism and well-supported alternatives are explicitly welcome.

## 3. Choose the right contribution

Useful contributions generally identify a precise ambiguity, contradiction, limitation or untested assumption; provide a documented observation, stress test, case study or reproducible example; connect a claim to published research or an authoritative source; propose a concrete revision, definition, metric or protocol; or improve documentation, accessibility, translation and discoverability.

| Contribution | Recommended starting point |
|---|---|
| Question, early idea or general feedback | [GitHub Discussions](https://github.com/meunier-jc/authentic-fluency/discussions) |
| Correction, research task or reproducible problem | [GitHub Issues](https://github.com/meunier-jc/authentic-fluency/issues) |
| Focused change ready for review | Pull request linked to an Issue or Discussion |
| Practical experience or case study | Discussion first, then a focused Issue or pull request |
| Translation or documentation improvement | Issue or direct focused pull request |

If you are unsure, open a Discussion and describe what you want to examine. You do not need a complete solution before starting a conversation.

## 4. Describe evidence and uncertainty

For every substantive claim, distinguish observed behaviour, documented testing, published research, interpretation, hypothesis and proposal. Include direct links, test conditions, relevant model or system context, and enough detail for another contributor to investigate the claim. Do not share personal data, credentials, confidential prompts, private logs or information that could identify a research participant.

When the project’s claim-level credibility scale is appropriate, use it as follows:

| Level | Meaning |
|---|---|
| **C1** | Strong, convergent and traceable support; the claim has been verified. |
| **C2** | Partial but coherent support; the claim is credible but not fully established. |
| **C3** | Weak, indirect or mainly inferential support; confirmation is required. |
| **C4** | No adequate source, unresolved contradiction or insufficient stability for a reliable conclusion. |

C3 and C4 material may still be valuable as exploratory work. Label it accurately and separate it from established findings. The scale makes uncertainty visible; it is not intended to prevent early research.

## 5. Contribution workflow

### 5.1 Open a Discussion or Issue

For a substantial conceptual, structural or technical change, open an Issue or Discussion before preparing a pull request. Explain the context, the proposal or question, the affected document and version, the motivation, the evidence or reasoning, and the outcome you would consider useful. Small typo fixes, broken-link fixes and narrowly scoped documentation corrections may go directly to a pull request.

### 5.2 Create a focused branch

Fork the repository, create a branch from `main`, and keep one coherent purpose per branch. Use a descriptive name such as:

```text
challenge/sycophancy-threshold
correction/framework-section-iv
extension/multi-agent-evaluation
research/reliability-study
docs/contributor-onboarding
ci/markdown-quality
```

### 5.3 Make and review the change

Preserve existing links, citations, terminology and version references unless the purpose of the change is to revise them. Do not silently rewrite historical research. Review the complete diff locally, check Markdown formatting, verify links where practical, and remove generated artefacts or unrelated edits.

### 5.4 Submit a pull request

Use the repository pull request template. Explain what changed, why it changed and how it can be reviewed. Link the Issue or Discussion, identify affected files or sections, include sources or test results, describe known limitations and state whether AI assistance was used.

A draft pull request is welcome when early feedback would be useful. A pull request does not need to be perfect, but it must be focused enough for another contributor to understand and review.

## 6. Conventional Commits

Use the following format for commit messages:

```text
<type>(<scope>): <imperative summary>

<context or motivation>

<what changed and why>

Evidence: <source, test, discussion or issue link>
Issue: #<number>

BREAKING CHANGE: <describe an incompatible change, if applicable>
```

The subject should be concise, start with a lowercase imperative verb and have no final period. Keep one coherent intention per commit. Use the body to explain motivation, evidence and limitations rather than merely listing files.

### 6.1 Accepted types

| Type | Use in this repository |
|---|---|
| `research` | Add or revise research, analysis, case studies or references. |
| `test` | Add or revise a stress test, evaluation protocol or reproducible scenario. |
| `docs` | Change the README, guides, contribution documentation or translations. |
| `fix` | Correct a factual error, broken link, inconsistency or misleading wording. |
| `feat` | Add a substantive section, protocol, documented capability or framework element. |
| `refactor` | Reorganise content without changing its main intent. |
| `ci` | Change workflows, quality checks or GitHub automation. |
| `chore` | Perform repository maintenance that does not directly change research content. |
| `revert` | Revert an earlier commit. |

Recommended scopes include `cip`, `framework`, `research`, `references`, `case-study`, `docs`, `contributing`, `workflow`, `issues`, `links`, `translation` and `release`. Avoid vague scopes such as `misc`.

### 6.2 Examples

```text
research(reliability): compare sycophancy indicators across models

test(stress-test): add contradiction-recovery scenario

docs(contributing): clarify evidence requirements

fix(references): correct citation for recursive embedding

ci(docs): add Markdown and link quality checks
```

Use `!` or a `BREAKING CHANGE:` footer when a change is intentionally incompatible:

```text
feat(protocol)!: adopt claim-level credibility labels

BREAKING CHANGE: update references to the former confidence terminology.
```

## 7. Human review and AI assistance

AI tools may be used for brainstorming, translation, editing, coding assistance or drafting. Every contributor remains responsible for factual accuracy, originality, licensing and the implications of the submitted material.

Do not submit unreviewed generated text, fabricated references, private data, confidential prompts or material copied without permission. If AI assistance was substantial, disclose it in the pull request and confirm that a human contributor reviewed the complete final result. The repository’s pull request template includes explicit review checkboxes.

## 8. GitHub Actions and quality checks

The repository runs automated checks on pushes to `main` and on pull requests targeting `main`. The current quality workflow checks Markdown formatting, links, required repository files, contribution-guidance markers and accidental changes to files resembling secrets or private keys.

The triage workflow may apply labels and publish an idempotent welcome comment to a first-time contributor. It does not automatically close Issues, merge pull requests or execute code from a submitted pull request. If a check fails, read the job log and distinguish a real defect from a pre-existing historical-document issue before changing the configuration.

Contributors should run a local review before opening a pull request. At minimum, inspect the complete diff, check the Markdown structure of edited files, confirm that references still point to the intended version and ensure that no `.env`, private key, credential or confidential file has been added.

## 9. Review and merge policy

Reviewers may request clarification, additional evidence, narrower scope or a clearer distinction between observation and interpretation. Testing the framework itself, including adversarial testing and attempts to find internal contradictions, is a legitimate contribution.

Maintainers will consider relevance, clarity, traceability, internal coherence, practical usefulness, licensing and compatibility with the project’s scope. A contribution may be declined without judging the contributor personally. When possible, the reason and a constructive next step will be provided.

Do not rewrite `main` or a branch already shared with other contributors. Rebase only your own unpublished branch, and coordinate before force-pushing any branch that another person may have fetched. Prefer `--force-with-lease` over `--force` when a force-push is unavoidable.

Branch protection should require the quality checks before merging into `main`. Approval requirements may be introduced when a second active human maintainer is available; they should not make the project impossible for a sole maintainer to operate.

## 10. Community standards and scope boundaries

Follow the [Code of Conduct](./CODE_OF_CONDUCT.md). Critique ideas, evidence and methods rather than people. Do not harass, impersonate, dox or expose private information about contributors or research participants.

The project is unlikely to accept contributions that are unrelated to its scope, present unsupported claims as established facts, expose private information, copy material without appropriate rights, remove uncertainty labels from exploratory work, or turn the CIP into a generic compliance checklist without explaining the conceptual and practical consequences.

Disagreement with a foundational claim is not, by itself, a reason for rejection. Identify the relevant passage, explain the disagreement, provide evidence or reasoning, and propose a way to test or resolve it.

## 11. Language, licensing and contact

Contributions to the main repository should normally be written in **English** so that the project can be reviewed internationally. Translations are welcome and should identify their language and source version.

Unless a file states otherwise, written contributions are distributed under the repository’s [Creative Commons Attribution-ShareAlike 4.0 license](./LICENSE). By submitting a contribution, you confirm that you have the right to submit it under that license.

If you are unsure where to begin, open a [Discussion](https://github.com/meunier-jc/authentic-fluency/discussions) with the title `New contributor` or comment on the [open collaboration invitation](https://github.com/meunier-jc/authentic-fluency/issues/7).

Thank you for helping make the project more rigorous, accessible and useful.

---

*This guide is itself open to improvement. If an instruction is unclear, incomplete or inconsistent with the project, open an Issue explaining how it could be improved.*
