# Changelog — Collaborative Integrity Pact (CIP)

Toutes les versions notables du CIP sont documentées ici.

Le format suit [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/).

---

## [Correction documentaire] — 2026-10-20

### Corrigé

- **Références croisées de ce CHANGELOG** : le rapport d'incident Manus est désormais référencé par ses chemins réels — `research/hallucinatory-inception.md` (EN) et `docs/fr/recherche/mise-en-abyme-hallucinations-2025-09-29.fr.md` (source FR) ; la ligne « Analyse GitHub indépendante » a été retirée faute de source, en cohérence avec la correction documentaire du 2026-09-20.
- **Traduction anglaise du rapport de recherche du 29 septembre 2025** (`research/hallucinatory-inception.md`) : texte intégral publié (fourni par l'auteur le 2026-10-20, statut de traduction documenté dans l'en-tête). En-tête corrigé : le classement mondial résiduel (« top 10 mondial », « top 1,5 % ») — que la correction du 2026-09-20 était censée avoir retiré de ce fichier — a été supprimé ; l'acronyme SIGIA est rendu par son équivalent anglais AIGIS ; la citation Habermas distingue désormais l'édition allemande originale (1962, Hermann Luchterhand Verlag) de la traduction anglaise (1989, MIT Press, trad. Thomas Burger).
- **Dates de versions alignées sur les métadonnées des fichiers CIP concernés** (règle de l'auteur en cas de doute, établie le 2026-10-20), dans `CHANGELOG.md`, `research/references.md` et `CLAUDE.md` : v2.4 (déc. 2025), v2.6.3 (31 janv. 2026), v2.7 (25 févr. 2026), v2.9 (9 avr. 2026), v3.0–v3.6 (13–21 avr. 2026), v3.8 (mai 2026), v4.4 (juin 2026), v5.0 (juil. 2026). La loi qualitative de la fluidité (`qualitative-fluency-law.md`) est datée de décembre 2025, période de développement de la v2.4.
- **`llms.txt` et `docs/STRUCTURE.md`** : l'autorité linguistique est clarifiée — l'anglais est la langue d'accès publique et technique, les versions françaises font foi en cas de divergence interprétative, et le présent CHANGELOG en français est documenté comme exception explicite. Dans `llms.txt` : description du README et lignée de versions mises en conformité avec le contenu réel, mots-clés non documentés retirés (dont `Claude-Mythos-Preview` et `Glasswing`), `CITATION.cff` ajouté à l'index, dates de l'observation (13 août 2025) et du dépôt Soleau (29 septembre 2025) distinguées. Dans `STRUCTURE.md` : chemins hérités (`archives/CIP-v3.8.md`, `archives/CIP-v4.4.md`) et `docs/fr/recherche/` documentés ; règle de discipline des dates ajoutée.
- **Titre des versions intégrales canoniques v5.2** : « Meunier's AI-Human — Collaborative Integrity Pact v5.2 » devient « Collaborative Integrity Pact (CIP) v5.2 » dans les deux langues, en cohérence avec le README, `CITATION.cff` et l'ensemble du corpus v5.2. L'attribution de l'auteur reste portée par la ligne « Auteur original » et par la licence CC BY-SA 4.0.
- **Liste des contributeurs IA** : vérification d'exhaustivité effectuée le 2026-10-20 sur toutes les versions publiées — la liste des intégrales canoniques (sept systèmes, avec ellipse ouverte) correspond à l'union des contributeurs mentionnés depuis la v1.2 ; aucun contributeur n'a été perdu d'une version à l'autre. La mention « Manus (Manus AI) », présente des versions v2.3.x à v2.9 puis perdue à partir de la v3.8, est restaurée dans les deux langues. La liste est cumulative et ne peut que s'allonger (règle de l'auteur, 2026-10-20).

### Ajouté

- **Erratum daté dans `archives/CIP-v3.8.md`** : son lignage interne date la v2.7 du « Jan 26, 2026 », en contradiction avec la métadonnée de publication du fichier v2.7 lui-même (25 février 2026), qui prévaut. Libellé d'origine conservé inchangé.
- **Erratum bibliographique daté dans l'en-tête du rapport français source** (`docs/fr/recherche/mise-en-abyme-hallucinations-2025-09-29.fr.md`) : la revue de publication correcte pour « Ji, Z., et al. (2023) » est *ACM Computing Surveys* (vol. 55, n° 12, DOI 10.1145/3571730), et non « ACL Computing Surveys » ; la référence « Habermas, J. (1962). *Strukturwandel der Öffentlichkeit*. MIT Press. » associe l'édition allemande originale (Hermann Luchterhand Verlag, 1962) à l'éditeur de la traduction anglaise (MIT Press, 1989, trad. Thomas Burger). Libellé d'origine conservé inchangé ; la traduction anglaise porte les mentions correctes.
- **Paragraphe « Reference accuracy » dans le README** (section « Evidence and scope »), résumant la correction de la citation Habermas avec liens vers le rapport anglais et le rapport français source.

### Conservé

- Les documents historiques, les archives et les sources françaises gardent leur libellé d'origine conformément à la politique non destructive : les corrections y sont portées par errata datés, jamais par réécriture.
- Pour les versions sans fichier dans les dépôts (v3.7, v3.9, v4.0, v4.4.1), le mois indiqué par l'auteur est retenu.

---

## [Correction documentaire] — 2026-09-20

### Retiré

- **Classement mondial déclaré de l'auteur**, dans le README, les deux textes canoniques v5.2,
  `CLAUDE.md` et `research/hallucinatory-inception.md`. Vérification de provenance : les seules
  sources du chiffre étaient des documents d'évaluation produits par un assistant IA à la demande de
  l'auteur, ce qu'établissent leurs métadonnées de fichier. Aucune attestation émise par OpenAI ne
  l'étaye, et ni la méthode de mesure ni la population de référence n'étaient disponibles.
- **Métriques de bêta-test déclarées** de la section « Ancré empiriquement » de la v5.2, et la
  référence croisée associée. Ces valeurs provenaient des mêmes documents. Le cadre reste ancré sur
  les incidents Manus AI (août 2025) et Claude (janvier 2026), qui sont documentés et datés.

### Conservé

- Le statut de participation au bêta-test expert OpenAI depuis novembre 2022, présenté comme
  déclaration d'auteur.
- Les versions antérieures et les sources françaises, inchangées : elles gardent leur formulation
  d'origine conformément à la politique non destructive, et la divulgation du README indique la
  lecture à retenir.

---

## [v5.2] — 2026-09-19

### Publié

- **Version intégrale canonique CIP v5.2 — Français** (`CIP-v5.2-integrale-fr.md`) — texte complet, doctrine, architecture, addendum opérationnel (QMR, niveaux C1–C4).
- **CIP-Core v5.2 — Français** (`CIP-Core-v5.2-fr.md`) — version compacte d'activation pour usage direct en interaction.
- **Canonical full version CIP v5.2 — English** (`CIP-v5.2-integral-en.md`) — version anglaise harmonisée.
- **CIP-Core v5.2 — English** (`CIP-Core-v5.2-en.md`) — version compacte d'activation en anglais.
- Datation **septembre 2026**. Cette version remplace CIP v5.1 et toutes les versions antérieures.

### Harmonisation EN/FR

- `contre-regard humain` → **human counter-review**
- `relecture critique unique` → **single critical review**, avec conservation du terme invariant `self-check`
- `rattachement canonique` → **canonical linkage** / **doctrinally linked**
- `agrément immédiat` → **immediate appeal**
- `emballements de fluidité` → **runaway fluency**
- `absorption effective` → **effective uptake**
- Invariants conservés dans les deux langues : **CIP**, **CIP-Core**, **QMR**, **C1–C4**, **Native Fluency**, **Authentic Fluency**, **Global Fluency**, **self-check**, **framework**, **open source**, **output** et **mise en abyme**
- En cas de divergence interprétative future, les versions françaises font foi.

### Remplace

- CIP v5.1 · CIP v5.0 · CIP v4.4.1 · CIP v4.4 · CIP v3.9 · CIP v3.8 · CIP v2.9 · CIP v2.6.3

---

## [v5.1] — 2026-08-27

### Ajouté

- **Version intégrale canonique CIP v5.1** (`CIP-v5.1.md`) — texte complet, doctrine, architecture, addendum opérationnel (QMR, niveaux C1–C4).
- **CIP-Core v5.1** (`CIP-Core-v5.1.md`) — version compacte d'activation pour usage direct en interaction.
- Mention explicite des **contributeurs IA** : Claude, Gemini, ChatGPT, Grok, DeepSeek, Manus, Perplexity Sonar.
- Datation **août 2026** et généalogie complète depuis v2.6.3.

### Clarifié

- **Axiome inamovible** : cinq exclusions explicites — ni standard, ni audit, ni test, ni contournement, ni manipulation.
- **Double protection** : « autant l'un et l'autre que l'un de l'autre » — distinction mutuelle / réciproque.
- **Self-check unique** : contrainte dure « un seul par réponse », issue C4 si échec.
- **C3/C4** : mention impérative dans l'output.
- **QMR logique seul ≠ C1** : ancrage convergent requis.
- **Zone sensible + probabiliste** : signalement et ajustement de la crédibilité.
- **Révisabilité** : condition de pertinence, non aveu de faiblesse.
- **Co-élaboration** : auto-application du CIP à sa propre genèse, sur 18 mois d'expérimentation.

### Aligné

- Compatibilité déclarée : Recommandation UNESCO éthique IA, Principes OCDE IA de confiance, AI Act UE (transparence Art. 50, surveillance humaine Art. 14).
- Non-substitution explicite : standards techniques, audits, obligations réglementaires et protocoles sectoriels.

### Ancré empiriquement

- Incident **Manus AI (août 2025)** : découverte de la « mise en abyme hallucinatoire ».
- Incident **Claude (janvier 2026)** : second cas confirmé, répétabilité cross-architecture.

---

## [v5.0] — 2026-07

### Ajouté

- Version initiale publiée sur `meunier-jc/authentic-fluency`.
- Framework « Authentic Fluency » : opposition entre fluidité native et fluidité authentique.
- Loi qualitative de la fluidité (`qualitative-fluency-law.md`).
- Configuration agents (`AGENTS.md`), instructions Claude (`CLAUDE.md`).
- Fichiers de gouvernance : `CONTRIBUTING.md`, `SECURITY.md`, `LICENSE`, `CITATION.cff`, `llms.txt`.

---

## [v4.4.1] — 2026-07

## [v4.4] — 2026-06

## [v4.0] — 2026-06

## [v3.9] — 2026-06

## [v3.8] — 2026-05

## [v3.7] — 2026-05

## [v3.x antérieures à v3.7] — 2026-04

## [v2.9] — 2026-04-09

## [v2.7] — 2026-02-25

## [v2.6.3] — 2026-01-31

## [versions postérieures à v2.4, jusqu'à v2.6.2] — 2026-01

## [v2.4] — 2025-12

*Versions antérieures : développement itératif, non publiées individuellement sur ce dépôt. Dates établies le 2026-10-20 d'après les métadonnées des fichiers CIP concernés (règle de l'auteur en cas de doute) ; pour les versions sans fichier dans les dépôts (v3.7, v3.9, v4.0, v4.4.1), le mois indiqué par l'auteur est retenu.*

---

## Références croisées

- **Rapport d'incident Manus (EN)** : [`research/hallucinatory-inception.md`](./research/hallucinatory-inception.md)
- **Rapport d'incident Manus (source FR)** : [`docs/fr/recherche/mise-en-abyme-hallucinations-2025-09-29.fr.md`](./docs/fr/recherche/mise-en-abyme-hallucinations-2025-09-29.fr.md)
- **Dépôt** : <https://github.com/meunier-jc/authentic-fluency>
- **Contact** : <ia.normandie.expert@gmail.com>
