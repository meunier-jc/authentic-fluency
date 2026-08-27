# Rapport de validation — CIP v5.1

**Dépôt :** `meunier-jc/authentic-fluency`  
**Branche contrôlée :** `main`  
**Date du contrôle :** 27 août 2026  
**Périmètre :** commits CIP v5.1, fichiers Markdown, métadonnées de citation, workflows CI/CD et scripts automatisés.

## 1. Résultat exécutif

Les corrections documentaires P0 et P1 ont été publiées dans la branche `main`. La valeur de référence est désormais **1,5 % mondial**, qualifiée comme classement déclaré. La recherche exhaustive des fichiers Markdown ne trouve plus aucune occurrence textuelle de `1,2 %` ou `1.2%`.

Les références actives ont été harmonisées sur **CIP v5.1**. Les mentions de v5.0 qui subsistent sont historiques, notamment dans les intitulés d’archives, la lignée des versions et les descriptions des évolutions introduites en v5.0.

Les workflows CI/CD ne contiennent pas de référence active obsolète à v5.0. Les premiers contrôles associés aux commits P0 et P1 ont échoué sur des erreurs de formatage Markdown indépendantes des corrections de version ; ces erreurs ont ensuite été corrigées et les workflows associés aux commits `c0ba7f2` et `de3ca1a` sont au vert.

## 2. Commits réalisés pour CIP v5.1

| Commit | Date UTC | Auteur | Portée | Résultat |
|---|---:|---|---|---|
| `36c4138075a635fd6debe0259c8523804b1063c2` | 2026-08-27 12:05:55 | `meunier-jc` | Corrections P0 : alignement du percentile sur 1,5 %, qualification du classement et des formulations associées dans `CIP-v5.0.md`, `CIP-v5.1.md`, `README.md` et `archives/CIP-v4.4.md` | Publié sur `main` |
| `2e34d896c89521f8b99b688e0bcd3546f3859c5d` | 2026-08-27 12:17:21 | `meunier-jc` | Corrections P1 : harmonisation des références canoniques v5.1 dans `AGENTS.md`, `CLAUDE.md`, `llms.txt`, `research/references.md` et le crosswalk réglementaire ; mise à jour de `CITATION.cff` | Publié sur `main` |

### Détail du commit P0

Le commit `36c4138` a remplacé la formulation obsolète du percentile dans `CIP-v5.0.md`, qualifié la valeur dans le texte v5.1 et le README, et annoté l’archive v4.4. Aucune archive n’a été réécrite silencieusement.

### Détail du commit P1

Le commit `2e34d89` a établi v5.1 comme référence active dans les instructions d’agents, l’index destiné aux LLM, la lignée documentaire et le crosswalk réglementaire. Les métadonnées `CITATION.cff` indiquent désormais le titre, la version `5.1` et la date de publication du 27 août 2026.

## 3. Contrôle des mentions obsolètes

La commande de recherche appliquée à tous les fichiers Markdown suivis est :

```bash
git grep -n -E '1[,.]2[[:space:]]*%|1[,.]2%' -- '*.md'
```

**Résultat : aucune occurrence.** Les chaînes `1.2.0` et `section 1.2` avaient été identifiées auparavant comme faux positifs, mais elles ne correspondent pas au taux obsolète.

Les références v5.0 restantes sont limitées à des usages historiques ou descriptifs : la version précédente est conservée dans la lignée, les archives et les explications des changements v5.0. Elles ne désignent plus la référence opérationnelle actuelle.

## 4. Contrôle des workflows et tests automatisés

Les workflows contrôlés sont :

| Fichier | Contrôle observé | Référence active v5.0 résiduelle |
|---|---|---:|
| `.github/workflows/quality.yml` | Markdown lint, liens, fichiers requis, contrôle de contenu et secrets | Non |
| `.github/workflows/triage.yml` | Triage automatisé via GitHub Script | Non |
| `.github/workflows/weekly-metrics.yml` | Collecte hebdomadaire et publication de métriques agrégées | Non |
| `.github/scripts/collect_metrics.py` | Script de collecte GitHub et génération Markdown | Non |

Les workflows ne ciblent pas explicitement `CIP-v5.0.md` ni `CIP-Core-v5.0-en.md`. Ils effectuent des contrôles génériques du dépôt, ce qui est préférable pour éviter de figer la CI sur une version historique.

### Exécutions CI associées

| Run | Commit | Conclusion | Observation |
|---:|---|---|---|
| `33070299681` | `36c4138` | `failure` | Échec initial du job Markdown lint sur plusieurs fichiers de recherche et de sécurité. |
| `33071164380` | `2e34d89` | `failure` | Même famille d’erreurs Markdown ; aucune indication d’un échec causé par une référence active v5.0. |
| `33072484266` | `c0ba7f2` | `success` | Lint Markdown vert après correction des titres, listes, citations et espaces finaux. |
| `33072563287` | `de3ca1a` | `success` | Workflow Documentation quality entièrement vert après publication de l’addendum du rapport. |

Les erreurs observées comprennent notamment des titres ou listes sans ligne blanche, des URL nues et une emphase utilisée comme titre. Elles concernent entre autres `research/hallucinatory-inception.md`, `research/references.md`, `research/regulatory-crosswalk-eu-ai-act-oecd.md` et `SECURITY.md`. Ces erreurs constituent un chantier distinct de priorité P2 ou P1 qualité, mais empêchent la CI de passer au vert.

## 5. Validation des liens et références canoniques

Les chemins actifs suivants sont désormais cohérents :

```text
CIP-v5.1.md
CIP-Core-v5.1.md
```

Les liens vers les anciennes versions et le dépôt historique `Human-AI-Moral-Contract` sont conservés lorsqu’ils documentent la généalogie du projet. Ils doivent toutefois rester explicitement étiquetés comme historiques et ne pas être utilisés comme source canonique dans les index ou instructions courantes.

## 6. État de conformité documentaire

| Contrôle | État | Commentaire |
|---|---|---|
| Valeur active fixée à 1,5 % | Conforme | Formulation qualifiée comme classement déclaré. |
| Occurrence active de 1,2 % dans Markdown | Conforme | Aucune occurrence détectée. |
| Instructions agents alignées sur v5.1 | Conforme | `AGENTS.md` et `CLAUDE.md` mis à jour. |
| Index LLM aligné sur v5.1 | Conforme | `llms.txt` mis à jour. |
| Lignée et crosswalk alignés | Conforme | v5.1 actif ; v5.0 historique. |
| Métadonnées de citation | Conforme | `CITATION.cff` indique v5.1. |
| Workflow CI/CD vert | Conforme | Runs `33072484266` et `33072563287` terminés avec succès. |
| Validation indépendante du percentile | Non démontrée | Une attestation primaire et une méthode restent requises pour C1. |

## 7. Actions restantes

La correction technique du lint est terminée. Les contrôles locaux et distants sont verts ; maintenir désormais la vérification du lint et des liens à chaque modification documentaire.

La prochaine action documentaire consiste à maintenir la formulation « classement déclaré de 1,5 % mondial » jusqu’à obtention d’une attestation primaire, de la méthode de calcul, de la population de référence, de la date de mesure et d’une corroboration indépendante.

## Conclusion

Les commits P0 et P1 ont bien été réalisés et publiés. Le dépôt ne contient plus de taux Markdown obsolète de 1,2 %, ses références opérationnelles pointent vers v5.1 et les workflows CI/CD sont désormais verts.

## Addendum — validation finale du lint

Après la première publication du rapport et des notes de présentation, le workflow local `markdownlint-cli2` a été exécuté sur les 22 fichiers Markdown suivis. Résultat : **0 erreur**.

Les corrections finales ont porté sur les séparations autour des listes, les titres d’emphase, les niveaux de titres, les blocs de citation et les espaces finaux. Elles ont été publiées dans le commit `c0ba7f2` (`docs: clear markdown lint checks`). La nouvelle version du rapport et des notes est incluse dans l’état final du dépôt.

Le run GitHub déclenché par `c0ba7f2` est terminé avec succès (`33072484266`). Le run suivant déclenché par `de3ca1a` est également terminé avec succès (`33072563287`).

## Commits consolidés

La séquence complète de l’état CIP v5.1 est donc : `36c4138` (P0), `2e34d89` (P1), `db7e042` (rapport et notes publiés), `c0ba7f2` (correction finale du lint Markdown), puis `de3ca1a` (addendum final et validation CI consolidée).

La compétence réutilisable `repository-documentary-audit` a également été améliorée avec une procédure de reprise idempotente afin d’éviter de refaire les étapes déjà validées.

## État CI final

Le contrôle local est vert et les deux derniers runs GitHub associés à `c0ba7f2` et `de3ca1a` sont terminés avec succès. La chaîne Documentation quality est donc stable sur l’état courant du dépôt.

## Références

- [Dépôt authentic-fluency](https://github.com/meunier-jc/authentic-fluency)
- [Workflow Documentation quality](https://github.com/meunier-jc/authentic-fluency/blob/main/.github/workflows/quality.yml)
- [Commit c0ba7f2](https://github.com/meunier-jc/authentic-fluency/commit/c0ba7f2)
- [Commit 2e34d89](https://github.com/meunier-jc/authentic-fluency/commit/2e34d89)
- [Commit 36c4138](https://github.com/meunier-jc/authentic-fluency/commit/36c4138)
