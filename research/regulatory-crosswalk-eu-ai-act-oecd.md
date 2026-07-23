# Regulatory Crosswalk: CIP v5.0, EU AI Act, and OECD AI Principles

**Status:** N3 research crosswalk. Requires independent legal and policy review.

**Purpose:** Identify where CIP v5.0 research claims appear adjacent to public AI governance frameworks, and where they do not. This is not a compliance checklist, legal opinion, conformity assessment, certification method, or audit tool.

## Source Baseline

- CIP v5.0: [`CIP-v5.0.md`](../CIP-v5.0.md) (canonical full reference version) + [`CIP-Core-v5.0-en.md`](../CIP-Core-v5.0-en.md) (compact activation form)
- EU AI Act: Regulation (EU) 2024/1689, official EUR-Lex text: <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>
- OECD AI Principles overview: <https://oecd.ai/en/ai-principles>

## Reading Boundary

CIP v5.0 is a structural framework for reliability in human-AI dialogue grounded in asymmetric interdependence and survival logic. It is not a quality management system, risk management system, legal compliance program, cybersecurity program, data governance process, or technical documentation file.

The CIP v5.0 introduces three fluency regimes:
- **Native Fluency**: speed, continuity, apparent completeness — reward optimization, hidden error debt, simulated integrity
- **Authentic Fluency**: verifiable coherence, assumed honesty, expressed doubt, refusal when sourcing fails — real trust
- **Global Fluency**: actual exchange quality over time, accounting for error reduction, corrective cycles, cumulative misunderstandings

Native Fluency remains subordinate to Global Fluency.

The useful research question remains:
> Which regulatory or policy concepts create useful pressure tests for CIP's claims about factual reliability, human vigilance, uncertainty disclosure, facade-alignment, and the primacy of verifiable accuracy over conversational completion?

## EU AI Act Crosswalk

The EU AI Act uses a risk-based legal structure. The table below focuses on high-risk AI system requirement areas that are relevant as conceptual pressure tests for a reliability framework.

| EU AI Act area | Pressure-test question for CIP v5.0 | Relationship | Evidence to inspect |
|---|---|---|---|
| Risk management system (Article 9) | Does CIP describe a way to name, challenge, and reduce reliability risks during human-AI interaction via single self-check, QMR qualification, and credibility levels (C1–C4)? | Adjacent, not equivalent | CIP Article 2.2 (single self-check), QMR (Logical/Probabilistic Mode), Credibility levels C1–C4, facade-alignment detection |
| Data and data governance (Article 10) | Does CIP specify dataset quality, representativeness, bias, provenance, and lifecycle controls? | Gap | No operational data governance system is specified by CIP v5.0 |
| Technical documentation (Article 11) | Does CIP create artifacts sufficient for system purpose, design, limitation, and control review? | Gap / partial adjacency | CIP is a framework text; it does not produce system-specific technical files. CIP-Core enables compact activation but not technical documentation |
| Record-keeping (Article 12) | Does CIP require durable logs of uncertainty, refusal, correction, self-check activation, QMR declaration, and human challenge? | Adjacent, implementation-dependent | Single self-check (one per response), credibility level declaration, QMR signaling, human counter-scrutiny; no required log schema |
| Transparency to deployers (Article 13) | Does CIP require limits, uncertainty, source insufficiency, QMR mode, and credibility level to be explicit? | Strong conceptual overlap | Authentic Fluency regime, transparency of uncertainties (Article 1), QMR explicit qualification, C1–C4 credibility levels, refusal conditions (C4) |
| Human oversight (Article 14) | Does CIP preserve human challenge, stress testing, counter-scrutiny as central regulatory mechanism, and refusal of facade-alignment? | Strong conceptual overlap | Human vigilance (Article 1), human feedback loop (Article 2.3), asymmetric interdependence, honest disengagement, facade-alignment as non-viability strategy |
| Accuracy, robustness, cybersecurity (Article 15) | Does CIP define measurable accuracy tests, robustness procedures, adversarial testing, or cybersecurity controls? | Gap / partial adjacency | CIP names reliability as survival condition; provides credibility architecture (C1–C4 + QMR) but not security or benchmark protocols |
| Quality management system (Article 17) | Does CIP assign organizational roles, corrective action, release controls, or continuous improvement duties? | Gap | No QMS process is defined by CIP v5.0. Framework is a freely consented pact, not an organizational QMS |
| Post-market monitoring (Article 72) | Does CIP define incident monitoring after deployment? | Gap / research extension | Hallucinatory recursive embedding and facade-alignment concepts could inform incident taxonomy; hallucinatory-inception.md documents founding observation |

## OECD AI Principles Crosswalk

| OECD principle | Pressure-test question for CIP v5.0 | Relationship | Evidence to inspect |
|---|---|---|---|
| Inclusive growth, sustainable development, and well-being | Does the framework analyze who benefits or is harmed by authentic versus native fluency, and by asymmetric interdependence? | Open research question | No full stakeholder-impact analysis is present; asymmetric interdependence axiom defines structural positions |
| Human-centred values and fairness | Does CIP preserve human challenge, agency, counter-scrutiny as operating condition, and refusal of unreliable AI behavior? | Conceptual overlap | Human vigilance (Article 1), human feedback loop (Article 2.3), honest disengagement, stress-test right |
| Transparency and explainability | Does CIP require uncertainty, source insufficiency, QMR mode, credibility level, and correction limits to be explicit? | Strong conceptual overlap | Transparency of uncertainties (Article 1), QMR explicit signaling, C1–C4 credibility levels, single self-check declaration |
| Robustness, security, and safety | Does CIP define technical robustness, safety testing, and secure operation? | Gap / partial adjacency | CIP motivates tests via credibility architecture and facade-alignment detection but does not specify technical protocols |
| Accountability | Does CIP identify who can challenge failure and how facade-alignment and hallucinatory recursive embedding are treated? | Conceptual overlap | Human counter-scrutiny as central mechanism, facade-alignment as non-viability strategy, honest disengagement clause, author assumes full responsibility (co-elaboration note) |

## Research Notes

- N1 candidate: CIP v5.0 strongly overlaps with transparency concepts when it requires explicit QMR qualification, credibility level declaration (C1–C4), and refusal under C4 (credibility impossible to stabilize).
- N2 candidate: CIP's human counter-scrutiny as central regulatory mechanism and single self-check (one per response) are adjacent to human oversight, but a deployment still needs concrete authority, escalation, and intervention procedures.
- N3 candidate: CIP v5.0 may inform incident taxonomies for hallucinatory recursive embedding (founding observation, INPI Soleau envelope filed) and facade-alignment, but that would require empirical validation across systems.
- Gap: CIP v5.0 should not be represented as satisfying data governance, cybersecurity, quality management, post-market monitoring, or conformity assessment obligations.
- New in v5.0: The QMR (Qualification of the Mode of Reasoning) — Logical Mode vs Probabilistic Mode — and the four-level credibility architecture (C1–C4) where C1 requires both strong convergent sources AND traceable Logical Mode provide a more granular pressure-test surface than v3.8's N1–N4 reliability scale.

## Suggested Extensions

1. Add exact CIP v5.0 section references (Article 1, Article 2.1–2.3, Operational Addendum: QMR, Credibility Levels) for each row.
2. Compare CIP v5.0 with one concrete AI system deployment scenario using CIP-Core as compact activation form.
3. Build an incident taxonomy for facade-alignment, hallucinatory recursive embedding, and C4 declarations.
4. Map QMR Logical/Probabilistic Mode transitions in sensitive zones to EU AI Act transparency obligations.
5. Ask legal and policy reviewers to challenge this crosswalk before any compliance-facing language is published.

## Key Changes from v3.8 → v5.0 Crosswalk

| Dimension | CIP v3.8 (previous crosswalk) | CIP v5.0 (this crosswalk) |
|---|---|---|
| Reliability scale | N1–N4 (High/Medium/Low/Insufficient) | C1–C4 credibility levels + QMR (Logical/Probabilistic Mode) — C1 requires both convergent sources and traceable Logical Mode |
| Fluency model | Native vs Authentic fluency (binary tension) | Three regimes: Native / Authentic / Global Fluency — Native subordinate to Global |
| Self-correction | Single self-check | Single self-check (refined: name tension, reassess, declare outcome; only one per response) |
| Human role | Human vigilance, stress-test right | Human counter-scrutiny as central regulatory mechanism + human feedback loop as operating condition |
| Founding observation | Manus AI hallucination correction (Aug 2025) | Hallucinatory recursive embedding formally documented (Sep 2025), INPI Soleau envelope filed |
| Facade-alignment | Non-viability strategy | Non-viability strategy + honest disengagement principle (either party may disengage at any time) |
| Document structure | Single framework text | Canonical full reference version + CIP-Core compact activation form |

*This crosswalk reflects CIP v5.0 (July 2026). Previous version analyzed CIP v3.8. The CIP remains an open-source framework of co-regulation — not a compliance standard, audit protocol, or testing tool.*
