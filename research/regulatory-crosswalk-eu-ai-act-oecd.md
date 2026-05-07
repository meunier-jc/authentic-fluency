# Regulatory Crosswalk: CIP v3.8, EU AI Act, and OECD AI Principles

**Status:** N3 research crosswalk. Requires independent legal and policy review.

**Purpose:** Identify where CIP v3.8 research claims appear adjacent to public
AI governance frameworks, and where they do not. This is not a compliance
checklist, legal opinion, conformity assessment, certification method, or audit
tool.

## Source Baseline

- CIP v3.8: [`CIP-v3.8.md`](../CIP-v3.8.md)
- EU AI Act: Regulation (EU) 2024/1689, official EUR-Lex text:
  <https://eur-lex.europa.eu/eli/reg/2024/1689/oj>
- OECD AI Principles overview:
  <https://oecd.ai/en/ai-principles>

## Reading Boundary

CIP v3.8 is a structural framework for reliability in human-AI dialogue. It is
not a quality management system, risk management system, legal compliance
program, cybersecurity program, data governance process, or technical
documentation file.

The useful research question is therefore not:

> Does CIP comply with regulation?

The useful research question is:

> Which regulatory or policy concepts create useful pressure tests for CIP's
> claims about factual reliability, human vigilance, uncertainty disclosure, and
> facade-alignment?

## EU AI Act Crosswalk

The EU AI Act uses a risk-based legal structure. The table below focuses on
high-risk AI system requirement areas that are relevant as conceptual pressure
tests for a reliability framework.

| EU AI Act area | Pressure-test question for CIP v3.8 | Relationship | Evidence to inspect |
|---|---|---|---|
| Risk management system (Article 9) | Does CIP describe a way to name, challenge, and reduce reliability risks during human-AI interaction? | Adjacent, not equivalent | CIP sections on factual reliability, self-check, stress-test right, facade-alignment |
| Data and data governance (Article 10) | Does CIP specify dataset quality, representativeness, bias, provenance, and lifecycle controls? | Gap | No operational data governance system is specified by CIP v3.8 |
| Technical documentation (Article 11) | Does CIP create artifacts sufficient for system purpose, design, limitation, and control review? | Gap / partial adjacency | CIP is a framework text; it does not produce system-specific technical files |
| Record-keeping (Article 12) | Does CIP require durable logs of uncertainty, refusal, correction, and human challenge? | Adjacent, implementation-dependent | Reliability scale, self-check, human counter-gaze; no required log schema |
| Transparency to deployers (Article 13) | Does CIP require limits, uncertainty, and source insufficiency to be made explicit? | Strong conceptual overlap | Authentic fluency, reliability scale, refusal when no reliable source is available |
| Human oversight (Article 14) | Does CIP preserve human challenge, stress testing, and refusal of facade-alignment? | Strong conceptual overlap | Human vigilance, stress-test right, asymmetric interdependence |
| Accuracy, robustness, cybersecurity (Article 15) | Does CIP define measurable accuracy tests, robustness procedures, adversarial testing, or cybersecurity controls? | Gap / partial adjacency | CIP names reliability as a condition; it does not provide security or benchmark protocols |
| Quality management system (Article 17) | Does CIP assign organizational roles, corrective action, release controls, or continuous improvement duties? | Gap | No QMS process is defined by CIP v3.8 |
| Post-market monitoring (Article 72) | Does CIP define incident monitoring after deployment? | Gap / research extension | Facade-alignment and recursive hallucination concepts could inform incident taxonomy |

## OECD AI Principles Crosswalk

| OECD principle | Pressure-test question for CIP v3.8 | Relationship | Evidence to inspect |
|---|---|---|---|
| Inclusive growth, sustainable development, and well-being | Does the framework analyze who benefits or is harmed by authentic versus native fluency? | Open research question | No full stakeholder-impact analysis is present |
| Human-centred values and fairness | Does CIP preserve human challenge, agency, and refusal of unreliable AI behavior? | Conceptual overlap | Human vigilance, stress-test right, asymmetric interdependence |
| Transparency and explainability | Does CIP require uncertainty, source insufficiency, and correction limits to be explicit? | Strong conceptual overlap | Reliability scale and refusal conditions |
| Robustness, security, and safety | Does CIP define technical robustness, safety testing, and secure operation? | Gap / partial adjacency | CIP can motivate tests but does not specify them |
| Accountability | Does CIP identify who can challenge failure and how facade-alignment is treated? | Conceptual overlap | Human counter-gaze, facade-alignment as non-viability strategy |

## Research Notes

- **N1 candidate:** CIP strongly overlaps with transparency concepts when it
  requires explicit uncertainty and refusal under insufficient evidence.
- **N2 candidate:** CIP's human vigilance and stress-test right are adjacent to
  human oversight, but a deployment still needs concrete authority, escalation,
  and intervention procedures.
- **N3 candidate:** CIP may inform incident taxonomies for recursive
  hallucination and facade-alignment, but that would require empirical
  validation across systems.
- **Gap:** CIP v3.8 should not be represented as satisfying data governance,
  cybersecurity, quality management, post-market monitoring, or conformity
  assessment obligations.

## Suggested Extensions

1. Add exact CIP section references for each row.
2. Compare CIP v3.8 with one concrete AI system deployment scenario.
3. Build an incident taxonomy for facade-alignment and recursive hallucination.
4. Ask legal and policy reviewers to challenge this crosswalk before any
   compliance-facing language is published.
