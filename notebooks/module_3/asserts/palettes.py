"""Generates palettes.png – the three kinds of colour palettes for choropleth maps.

Sequential, diverging and qualitative palettes from matplotlib, five classes
each, as they would appear in a map legend.

Run from this folder:  python palettes.py
"""

import matplotlib.pyplot as plt
import numpy as np

INK = "#1A1A1A"
GREY = "#5A5A5A"

GROUPS = [
    ("Последовательные", "от меньшего к большему", ["BuPu", "YlOrRd", "Greens"]),
    ("Расходящиеся", "отклонение от центра", ["RdBu", "PuOr", "BrBG"]),
    ("Качественные", "категории без порядка", ["Set2", "tab10", "Pastel1"]),
]
N_CLASSES = 5

fig, axes = plt.subplots(3, 3, figsize=(10, 3.6))

for col, (title, subtitle, names) in enumerate(GROUPS):
    for row, name in enumerate(names):
        ax = axes[row, col]
        cmap = plt.get_cmap(name)
        if name in ("Set2", "tab10", "Pastel1"):
            colors = [cmap(i) for i in range(N_CLASSES)]
        else:
            colors = [cmap(x) for x in np.linspace(0.08, 0.92, N_CLASSES)]
        for i, color in enumerate(colors):
            ax.add_patch(plt.Rectangle((i, 0), 0.92, 1, color=color))
        ax.set_xlim(0, N_CLASSES)
        ax.set_ylim(0, 1)
        ax.set_axis_off()
        ax.text(N_CLASSES / 2, -0.2, name, ha="center", va="top",
                fontsize=9, color=GREY, family="monospace")
    axes[0, col].set_title(f"{title}\n", fontsize=12, color=INK, weight="bold")
    axes[0, col].text(N_CLASSES / 2, 1.15, subtitle, ha="center", va="bottom",
                      fontsize=10, color=GREY)

plt.subplots_adjust(hspace=0.9, wspace=0.15, top=0.8, bottom=0.08, left=0.02, right=0.98)
plt.savefig("palettes.png", dpi=150, facecolor="white")
