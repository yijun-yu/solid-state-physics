"""Generate clean monochrome academic SVG diagram for Chapter 2 (Crystal Bonding)."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

os.environ.setdefault("MPLCONFIGDIR", os.path.join(os.path.dirname(__file__), ".mplcache"))
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "docs", "public", "figures")
os.makedirs(OUT_DIR, exist_ok=True)

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Microsoft YaHei", "SimHei", "DejaVu Sans"],
    "mathtext.fontset": "stix",
    "axes.edgecolor": "#111111",
    "svg.fonttype": "path",
})


def fig1_bonding_potential():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.8, 3.7), gridspec_kw={"width_ratios": [1.22, 1.0]})

    # --- Left panel: u(r) and f(r) for Lennard-Jones potential ---
    r = np.linspace(0.95, 2.35, 400)
    u_attr = -4.0 * (1.0 / r) ** 6
    u_rep = 4.0 * (1.0 / r) ** 12
    u_tot = u_rep + u_attr
    # Force f(r) = -du/dr = 4*(12/r^13 - 6/r^7); scaled cleanly to separate from u(r)
    f_tot = 4.0 * (12.0 / r ** 13 - 6.0 / r ** 7) * 0.20

    r0 = 2.0 ** (1 / 6)          # ~1.1225, u = -1, f = 0
    rm = (26.0 / 7.0) ** (1 / 6) # ~1.2445, inflection point of u, min of f (max attraction)
    um = 4.0 * ((1.0 / rm) ** 12 - (1.0 / rm) ** 6)
    fm = 4.0 * (12.0 / rm ** 13 - 6.0 / rm ** 7) * 0.20

    ax1.axhline(0, color="#666666", lw=0.9, zorder=1)
    ax1.plot(r, u_rep, color="#999999", lw=1.0, ls=":", label=r"排斥势 $u_{\mathrm{rep}}$")
    ax1.plot(r, u_attr, color="#999999", lw=1.0, ls="-.", label=r"吸引势 $u_{\mathrm{attr}}$")
    ax1.plot(r, u_tot, color="#111111", lw=1.8, label=r"总势能 $u(r)$")
    ax1.plot(r, f_tot, color="#333333", lw=1.25, ls="--", label=r"作用力 $f(r)=-\mathrm{d}u/\mathrm{d}r$")

    # Mark r0 and rm
    ax1.plot([r0, r0], [0, -1.0], color="#444444", lw=0.9, ls=":")
    ax1.scatter([r0, r0], [-1.0, 0.0], s=26, color="#111111", zorder=5)
    ax1.plot([rm, rm], [0, um], color="#666666", lw=0.85, ls=":")
    ax1.scatter([rm, rm], [um, fm], s=22, facecolors="#ffffff", edgecolors="#111111", lw=1.1, zorder=5)

    # Binding energy double arrow
    ax1.annotate("", xy=(r0 - 0.10, 0.0), xytext=(r0 - 0.10, -1.0),
                 arrowprops=dict(arrowstyle="<->", lw=0.95, color="#111111"))
    ax1.text(r0 - 0.14, -0.52, r"$W$", fontsize=10, ha="right", va="center")

    ax1.text(r0 + 0.04, 0.10, r"$r_0$", fontsize=10, ha="left")
    ax1.text(rm + 0.05, 0.10, r"$r_m$", fontsize=10, ha="left")
    ax1.text(0.96, -0.14, r"$\sigma$", fontsize=9.5, ha="right", color="#555555")
    ax1.text(rm + 0.07, fm + 0.04, r"$f_{\max}$", fontsize=9.5, ha="left", va="center")

    ax1.set_xlim(0.88, 2.35)
    ax1.set_ylim(-1.45, 1.55)
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    ax1.set_xlabel(r"原子间距 $r$", fontsize=10)
    ax1.set_ylabel(r"势能 $u$ / 力 $f$", fontsize=10)
    ax1.legend(loc="upper right", frameon=False, fontsize=8.5, handlelength=2.0)
    ax1.set_title("结合势能与结合力曲线", fontsize=10.5, pad=8)

    # --- Right panel: 1D ionic chain Madelung summation ---
    ax2.set_aspect("equal")
    ax2.set_xlim(-3.85, 3.85)
    ax2.set_ylim(-2.45, 2.75)
    ax2.axis("off")

    # Baseline
    ax2.plot([-3.55, 3.55], [0, 0], color="#888888", lw=1.0, zorder=1)
    ax2.text(-3.65, 0, r"$\cdots$", fontsize=12, ha="right", va="center", color="#555555")
    ax2.text(3.65, 0, r"$\cdots$", fontsize=12, ha="left", va="center", color="#555555")

    for j in range(-3, 4):
        is_pos = (j % 2 == 0)
        fc = "#111111" if is_pos else "#ffffff"
        tc = "#ffffff" if is_pos else "#111111"
        rad = 0.24 if j == 0 else 0.20
        c = Circle((j, 0), rad, facecolor=fc, edgecolor="#111111", lw=1.3, zorder=4)
        ax2.add_patch(c)
        ax2.text(j, 0.0, "+" if is_pos else "−", color=tc,
                 fontsize=11 if j == 0 else 10, fontweight="bold", ha="center", va="center", zorder=5)
        # Index labels below
        lab = "0" if j == 0 else (f"+{j}" if j > 0 else f"{j}")
        ax2.text(j, -0.44, lab, fontsize=9, ha="center", color="#444444")

    # Distance marker a between 0 and +1
    ax2.annotate("", xy=(0, -0.78), xytext=(1, -0.78),
                 arrowprops=dict(arrowstyle="<->", lw=1.0, color="#222222"))
    ax2.text(0.5, -1.03, r"$a$", fontsize=10, ha="center")

    # Arcs showing shell contributions from reference ion 0
    for k, y_arc, txt in [(1, 0.56, r"$-\frac{2}{1}$"), (2, 0.96, r"$+\frac{2}{2}$"), (3, 1.36, r"$-\frac{2}{3}$")]:
        # Right half bracket from 0 to k
        ax2.plot([0, 0, k, k], [0.28, y_arc, y_arc, 0.28], color="#555555", lw=0.85, ls="--" if k > 1 else "-")
        ax2.text(k / 2.0, y_arc + 0.06, txt, fontsize=8.8, ha="center", va="bottom",
                 bbox=dict(boxstyle="square,pad=0.05", fc="#ffffff", ec="none"))

    ax2.text(0, -1.45, r"$\alpha = 2\left(1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots\right) = 2\ln 2$",
             fontsize=9.8, ha="center")
    ax2.set_title("一维等距正负离子链马德隆求和", fontsize=10.5, pad=8)

    plt.tight_layout(pad=0.7)
    fig.savefig(os.path.join(OUT_DIR, "ch02-bonding-potential.svg"), format="svg", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    fig1_bonding_potential()
    print("Generated ch02-bonding-potential.svg in", OUT_DIR)
