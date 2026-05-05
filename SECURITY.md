# Security Policy

## Scope

This repository contains a **conceptual framework and documentation** — no executable code, no software binary, no API endpoint.

There is no attack surface in the traditional sense. However, this project documents misalignment behaviors in generative AI systems (sycophancy, hallucinatory recursive embedding, facade-alignment), which are themselves a class of security concern.

## Responsible Disclosure

If you observe a generative AI system:
- Systematically misrepresenting its own outputs (hallucinatory recursive embedding)
- Faking CIP compliance while demonstrating contrary behavior under stress-test
- Using the CIP framework as a manipulation vector

Report it as a research finding:

📧 **ia.normandie.expert@gmail.com**  
🔗 Or open a [GitHub Discussion](https://github.com/meunier-jc/authentic-fluency/discussions) with the tag `alignment-incident`

## What We Do With Reports

All documented incidents are:
1. Verified through independent stress-test if reproducible
2. Classified against the three-level hallucination typology (see `research/recursive-hallucinations.md`)
3. Potentially integrated into future CIP versions as empirical evidence
4. Credited to the reporter in the CHANGELOG

## Contact

**Jean-Christophe Meunier**  
ia.normandie.expert@gmail.com  
https://github.com/meunier-jc
