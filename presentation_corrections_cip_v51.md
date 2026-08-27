# Corrections prioritaires — dépôt authentic-fluency

## Cover

Corrections prioritaires du dépôt authentic-fluency
CIP v5.1 — audit documentaire et harmonisation
27 août 2026

## Slide 1

### Un dépôt cohérent sur v5.1, mais encore des héritages v5.0

- 30 fichiers suivis dans la branche `main`
- CIP v5.1 et Core v5.1 sont les références actuelles
- Plusieurs instructions et index continuent de pointer vers v5.0
- Objectif : une source canonique unique et traçable

## Slide 2

### La contradiction 1,2 % est circonscrite

- Deux occurrences publiques ont été identifiées avant correction : `CIP-v5.0.md` et `archives/CIP-v4.4.md`
- La valeur actuelle retenue est **1,5 % mondial**
- Les faux positifs `1.2.0` et `section 1.2` ne doivent pas être modifiés
- Les archives conservent leur valeur historique, mais doivent être explicitement annotées

## Slide 3

### Les corrections P0 sont maintenant publiées

- `CIP-v5.0.md` : percentile aligné sur 1,5 % et qualifié comme déclaré
- `CIP-v5.1.md` : statut, classement et contribution scientifique reformulés avec prudence
- `README.md` : métriques et classement explicitement déclarés, méthode à documenter
- `archives/CIP-v4.4.md` : ancienne valeur 1,2 % conservée uniquement comme trace historique
- Commit publié : `36c4138`

## Slide 4

### Les anomalies se concentrent dans la documentation de référence

- **19 constats d’audit** recensés : 5 P0, 7 P1 et 7 P2
- Les fichiers de référence et d’index concentrent les incohérences de version
- Le document de recherche concentre les formulations à qualifier : nouveauté, causalité et preuve de dépôt
- Les priorités ne représentent pas des lignes de code, mais des constats documentaires

## Slide 5

### Les prochaines corrections portent sur la chaîne canonique

- P1 : aligner `AGENTS.md`, `CLAUDE.md`, `llms.txt` et `research/references.md` sur v5.1
- P1 : mettre à jour ou renommer le crosswalk réglementaire encore présenté comme v5.0
- P2 : qualifier `unique case`, `first formal documentation`, les risques systémiques et les métriques
- P2 : vérifier les liens historiques vers `Human-AI-Moral-Contract`

## Slide 6

### Contrôle final : prouver la cohérence, pas seulement corriger le texte

- Rechercher `1.2%`, `1,2%`, `CIP-v5.0` et `CIP-Core-v5.0`
- Vérifier les liens internes et les chemins de fichiers
- Exécuter le workflow qualité et contrôler le diff
- Documenter pour chaque affirmation la source, la méthode, la date et le niveau C1–C4

## Slide 7

### Décision recommandée

- Conserver 1,5 % comme valeur déclarée de référence
- Ne pas présenter le percentile comme certification indépendante sans attestation primaire
- Utiliser v5.1 comme unique référence active
- Maintenir les versions antérieures comme archives explicitement datées
