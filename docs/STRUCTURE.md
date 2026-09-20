# Bilingual documentation structure

This repository uses a non-destructive bilingual policy.

## Language rules

- Public and technical documentation is written in English.
- French source material and audit records remain in French.
- Translations are separate files and are never presented as originals.
- Historical documents retain their original dates and version identifiers.
- CIP v5.2 is the active canonical framework. Historical material is identified as legacy and organized under `archives/`.

## Directory layout

```text
.
├── README.md                         # English public entry point
├── CIP-v5.2-integral-en.md           # English canonical full text
├── CIP-Core-v5.2-en.md               # English compact activation text
├── .github/                          # English CI/CD and contribution automation
├── docs/
│   ├── STRUCTURE.md                  # This bilingual policy and directory map
│   ├── en/
│   │   ├── README.md                 # English technical documentation index
│   │   └── ci/
│   │       └── documentary-audit.md  # English CI/CD integration guide
│   └── fr/
│       ├── README.md                 # French source and audit-record index
│       ├── source/                    # Preserved French source documents
│       └── audit/                     # French audit records and source reports
├── research/                          # English public research documentation
├── archives/                          # Historical versions and legacy artifacts
│   ├── README.md                      # Archive policy and active-version reference
│   ├── cip/
│   │   ├── README.md                  # Historical CIP index
│   │   ├── v5.0/                      # Historical v5.0 documents
│   │   └── v5.1/                      # Historical v5.1 documents
│   ├── legacy-outputs/                # Historical generated reports and artifacts
│   │   └── metrics/
│   └── presentations/                 # Historical presentation materials
│       ├── README.md
│       ├── corrections-cip-v5.1/
│       └── documentary-audit/
└── metrics/                           # Current CI metrics and generated reports
```

The root-level files required by GitHub and agent tooling remain at the root. The active public and technical control layer is maintained in English so that it has one stable language and one stable path. All historical material has been organized under `archives/` and must not be treated as the active framework.

French source documents are preserved under `docs/fr/source/`, while French audit records are grouped under `docs/fr/audit/`. A translation must use a distinct filename and clearly identify its source, translation status, translation date, and version lineage. It must not replace the original source document.

## Change protocol

When adding a public document, write it in English and link it from the English index. When adding or revising a French source document, store it under `docs/fr/` and preserve its original wording, date, and version. Legacy versions and historical artifacts belong under `archives/`; they must retain their original metadata and must not be presented as current framework material. Run Markdown lint, link checks, and a language/path review before merging.
