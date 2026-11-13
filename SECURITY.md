# Security Policy

## Scope

This repository primarily contains a **conceptual framework and documentation**, but it also includes executable Python and Bash scripts under `.github/scripts/` and GitHub Actions workflows under `.github/workflows/` for maintenance, documentary audits, contribution triage and metrics collection.

The security scope therefore includes these scripts and workflows, their third-party dependencies and actions, token permissions, handling of secrets, network requests and generated artifacts. A documentation-first project is not exempt from risks introduced by executable automation.

The project also documents misalignment behaviors in generative AI systems (sycophancy, hallucinatory recursive embedding, facade-alignment), which are a separate research concern from vulnerabilities in the repository's automation.

## Reporting Automation Vulnerabilities

Report suspected vulnerabilities in scripts or workflows privately to <ia.normandie.expert@gmail.com>. Include the affected file and revision, potential impact and a minimal reproduction where safe. Do not publish credentials, personal data or exploit details in a public Issue or Discussion. If a credential has been exposed, revoke or rotate it promptly; removing it from a file alone does not invalidate it.

## Responsible Disclosure

If you observe a generative AI system:

- Systematically misrepresenting its own outputs (hallucinatory recursive embedding)
- Faking CIP compliance while demonstrating contrary behavior under stress-test
- Using the CIP framework as a manipulation vector

Report it as a research finding:

📧 **<ia.normandie.expert@gmail.com>**
🔗 Or open a [GitHub Discussion](https://github.com/meunier-jc/authentic-fluency/discussions) with the tag `alignment-incident`

## What We Do With Reports

All documented incidents are:

1. Verified through independent stress-test if reproducible.
2. Classified against the three-level hallucination typology (see `research/hallucinatory-inception.md`).
3. Potentially integrated into future CIP versions as empirical evidence.
4. Credited to the reporter in the CHANGELOG.

## Contact

**Jean-Christophe Meunier**
<ia.normandie.expert@gmail.com>
<https://github.com/meunier-jc>
