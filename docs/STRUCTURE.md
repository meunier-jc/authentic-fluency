# Bilingual documentation structure

This repository uses a non-destructive bilingual policy.

## Language rules

- Public and technical documentation is written in English.
- French source material and audit records remain in French.
- Translations are separate files and are never presented as originals.
- Historical documents retain their original date and version.

## Directory layout

```text
.
├── README.md                         # English public entry point
├── CIP-v5.1.md                       # English canonical full text
├── CIP-Core-v5.1.md                  # English compact activation text
├── .github/                          # English CI/CD and contribution automation
├── docs/
│   ├── STRUCTURE.md                  # This bilingual policy and directory map
│   ├── en/
│   │   ├── README.md                 # English technical documentation index
│   │   └── ci/
│   │       └── documentary-audit.md  # English CI/CD integration guide
│   └── fr/
│       ├── README.md                 # French source and audit-record index
│       ├── source/                   # Preserved French source documents
│       └── audit/                    # French audit records and source reports
├── research/                         # English public research documentation
└── archives/                         # Versioned historical material
```

The root-level files required by GitHub and agent tooling remain at the root. They are kept in English so that the public and technical control layer has one stable language and one stable path.

French source documents are preserved under `docs/fr/source/`, while French audit records are grouped under `docs/fr/audit/`. A translated document must use a distinct filename and explicitly identify its source document, translation status and translation date. The root README is the English public entry point; its former French content is preserved at `docs/fr/source/README.fr.md`.

## Change protocol

When adding a public document, write it in English and link it from the English index. When adding or revising a French source document, store it under `docs/fr/` and preserve its original wording. Do not overwrite a French source with an English translation. Run Markdown lint, link checks and a language/path review before merging.
