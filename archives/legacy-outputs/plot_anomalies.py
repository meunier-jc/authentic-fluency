from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

files = [
    "README.md",
    "CIP-v5.1.md",
    "CIP-v5.0.md",
    "archives/CIP-v4.4.md",
    "AGENTS.md",
    "CLAUDE.md",
    "llms.txt",
    "research/references.md",
    "research/regulatory-crosswalk...md",
    "research/hallucinatory-inception.md",
]
# Counts are audit findings, not line counts: P0 = immediate factual/public correction;
# P1 = canonical version/reference harmonization; P2 = qualification or historical cleanup.
p0 = np.array([2, 1, 1, 1, 0, 0, 0, 0, 0, 0])
p1 = np.array([0, 0, 0, 0, 1, 1, 1, 2, 2, 0])
p2 = np.array([0, 0, 0, 0, 0, 0, 0, 1, 1, 5])

plt.style.use("seaborn-v0_8-whitegrid")
fig, ax = plt.subplots(figsize=(13, 7.5), dpi=180)
y = np.arange(len(files))
left = np.zeros(len(files))
colors = {"P0": "#b42318", "P1": "#d97706", "P2": "#2563eb"}
for label, values in [("P0 — immédiat", p0), ("P1 — harmonisation", p1), ("P2 — qualification", p2)]:
    ax.barh(y, values, left=left, height=0.62, label=label, color=colors[label.split()[0]])
    left += values

ax.set_yticks(y)
ax.set_yticklabels(files, fontsize=9)
ax.invert_yaxis()
ax.set_xlabel("Nombre de constats d’anomalie", fontsize=11)
ax.set_title("Dépôt authentic-fluency — répartition des anomalies par fichier et priorité", fontsize=14, weight="bold", pad=14)
ax.legend(loc="lower right", frameon=True)
ax.set_xlim(0, max(left) + 1)
for i, total in enumerate(left):
    if total:
        ax.text(total + 0.08, i, f"{int(total)}", va="center", fontsize=9, weight="bold")
ax.text(0, -0.08, "Source : audit documentaire du dépôt, branche main, 27 août 2026. Les occurrences 1.2.0 et section 1.2 sont exclues comme faux positifs.", transform=ax.transAxes, fontsize=8, color="#4b5563")
fig.tight_layout(rect=[0, 0.04, 1, 1])
out = Path("/home/ubuntu/authentic-fluency-audit/anomalies_par_fichier_priorite.png")
fig.savefig(out, bbox_inches="tight")
print(out)
print({"P0": int(p0.sum()), "P1": int(p1.sum()), "P2": int(p2.sum()), "total": int((p0+p1+p2).sum())})
plt.close(fig)

# Compact data export for slide notes and reproducibility.
rows = ["fichier,P0,P1,P2,total"]
rows += [f"{f},{a},{b},{c},{a+b+c}" for f, a, b, c in zip(files, p0, p1, p2)]
Path("/home/ubuntu/authentic-fluency-audit/anomalies_par_fichier_priorite.csv").write_text("\n".join(rows) + "\n", encoding="utf-8")
print("/home/ubuntu/authentic-fluency-audit/anomalies_par_fichier_priorite.csv")
  
