# Bilingual documentation structure

This repository uses a non-destructive bilingual policy.

## Language rules

- English is the public and technical access language; it does not determine interpretative authority.
- CIP v5.2 is the active framework. The French full text, `CIP-v5.2-integrale-fr.md`, takes precedence in case of interpretative divergence, as stated in `CHANGELOG.md`.
- `CIP-v5.2-integral-en.md` is the English full version. The English and French Core files are compact activation texts linked to the full framework.
- French source material, audit records and the existing French `CHANGELOG.md` are preserved in their original language. The changelog is an explicit exception to the English public-documentation default.
- Translations are separate files and are never presented as originals.
- Historical documents retain their original dates and version identifiers. Distinguish composition dates, observations, filings, releases and repository publication dates; do not infer one from another.
- Historical material is identified as legacy and organized under `archives/`.

## Directory layout

```text
.
├── README.md                         # English public entry point
├── CHANGELOG.md                      # Preserved French version history
├── CIP-v5.2-integrale-fr.md           # French full text; interpretative reference
├── CIP-v5.2-integral-en.md            # English full version
├── CIP-Core-v5.2-fr.md                # French compact activation text
├── CIP-Core-v5.2-en.md                # English compact activation text
├── .github/                          # CI/CD and contribution automation
├── docs/
│   ├── STRUCTURE.md                  # This policy
│   ├── en/                           # English technical documentation
│   │   ├── README.md
│   │   └── ci/documentary-audit.md
│   └── fr/                           # French sources and records
│       ├── README.md
│       ├── recherche/                # French research source
│       ├── source/
│       └── audit/
├── research/                         # Research documentation; preserved French sources may coexist
├── archives/
│   ├── README.md
│   ├── CIP-v3.8.md                   # Preserved legacy path
│   ├── CIP-v4.4.md                   # Preserved legacy path
│   ├── cip/
│   │   ├── README.md
│   │   ├── v5.0/
│   │   └── v5.1/
│   ├── legacy-outputs/
│   └── presentations/
└── metrics/                          # Current generated contribution reports
```

Root-level files used by GitHub and agent tooling remain at the root. English provides a stable public and technical entry point; French interpretative priority is a separate rule, not a competing technical path.

Existing legacy paths are retained to avoid breaking references. New historical CIP versions should be organized under `archives/cip/`. Material under `archives/` must not be presented as the active framework.

French sources are preserved under `docs/fr/source/` and `docs/fr/recherche/`; audit records are grouped under `docs/fr/audit/`. Existing French research files may remain at their established paths. A translation must identify its source, translation status, translation date and version lineage. It must not replace the original source document.

## Change protocol

Write new public and technical documentation in English and link it from the English index. Preserve the wording, dates and version identifiers of historical French source documents. When correcting active documentation, record the correction separately from historical release dates. Verify relative links, Markdown formatting and language/authority labels before merging. Do not change historical dates without a traceable source.
