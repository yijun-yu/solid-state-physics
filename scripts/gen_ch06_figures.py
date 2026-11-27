"""Generate clean monochrome academic SVG diagrams for Chapter 6 (Semiconductors)."""
import os
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

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


def fig1_semiconductor_stats(preview_dir=None):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.0, 3.95))

    # --- Left: Direct vs Indirect Bandgap Schematic ---
    kx_d = np.linspace(-1.0, 1.0, 200)
    ec_d = 2.55 + 1.10 * (kx_d ** 2)
    ev_d = 1.15 - 0.80 * (kx_d ** 2)

    ax1.plot(1.6 + kx_d, ec_d, color="#111111", lw=1.8, zorder=3)
    ax1.plot(1.6 + kx_d, ev_d, color="#111111", lw=1.8, zorder=3)
    ax1.fill_between(1.6 + kx_d, 0.25, ev_d, color="#e6e6e6", zorder=1)
    ax1.plot([1.6, 1.6], [0.25, 3.95], color="#888888", lw=0.8, ls=":", zorder=2)

    # Vertical photon transition arrow
    ax1.annotate("", xy=(1.6, 2.53), xytext=(1.6, 1.17),
                 arrowprops=dict(arrowstyle="-|>", lw=1.35, color="#111111"), zorder=5)
    ax1.scatter([1.6, 1.6], [2.55, 1.15], s=24, color="#111111", zorder=6)
    ax1.text(1.75, 1.85, r"$h\nu = E_g$", fontsize=8.8, va="center", ha="left")
    ax1.text(1.6, 4.32, "直接带隙（如 GaAs）", fontsize=9.2, ha="center")
    ax1.text(1.6, 3.45, "导带", fontsize=8.4, ha="center", color="#333333",
             bbox=dict(facecolor="white", edgecolor="none", pad=1.0))
    ax1.text(1.6, 0.58, "价带", fontsize=8.4, ha="center", color="#333333")

    # Center vertical divider
    ax1.plot([3.40, 3.40], [0.15, 4.45], color="#aaaaaa", lw=0.85, ls="--")

    # Indirect gap: VB max at x=4.95, CB min at x=5.95 (clipped cleanly to avoid tall spill)
    kx_iv = np.linspace(-0.98, 0.98, 200)
    ev_i = 1.15 - 0.80 * (kx_iv ** 2)
    kx_ic = np.linspace(-0.95, 0.95, 200)
    ec_i = 2.55 + 1.10 * (kx_ic ** 2)

    ax1.plot(5.95 + kx_ic, ec_i, color="#111111", lw=1.8, zorder=3)
    ax1.plot(4.95 + kx_iv, ev_i, color="#111111", lw=1.8, zorder=3)
    ax1.fill_between(4.95 + kx_iv, 0.25, ev_i, color="#e6e6e6", zorder=1)
    ax1.plot([4.95, 4.95], [0.25, 3.95], color="#888888", lw=0.8, ls=":", zorder=2)

    # Photon (vertical) + Phonon (horizontal) indirect transition
    ax1.annotate("", xy=(4.95, 2.55), xytext=(4.95, 1.17),
                 arrowprops=dict(arrowstyle="-|>", lw=1.25, color="#333333", ls="--"), zorder=5)
    ax1.annotate("", xy=(5.93, 2.55), xytext=(4.95, 2.55),
                 arrowprops=dict(arrowstyle="-|>", lw=1.35, color="#111111"), zorder=5)
    ax1.scatter([4.95, 5.95], [1.15, 2.55], s=24, color="#111111", zorder=6)
    ax1.text(4.82, 1.85, r"$h\nu$", fontsize=8.8, va="center", ha="right")
    ax1.text(5.45, 2.28, r"声子 $\hbar\mathbf{q}$", fontsize=8.4, ha="center", va="top")
    ax1.text(5.45, 4.32, "间接带隙（如 Si）", fontsize=9.2, ha="center")
    ax1.text(5.95, 3.45, "导带", fontsize=8.4, ha="center", color="#333333")
    ax1.text(4.95, 0.58, "价带", fontsize=8.4, ha="center", color="#333333")

    # Energy axis on far left
    ax1.annotate("", xy=(0.25, 4.25), xytext=(0.25, 0.15),
                 arrowprops=dict(arrowstyle="-|>", lw=1.0, color="#111111"))
    ax1.text(0.02, 4.18, r"$E$", fontsize=9.8, ha="center", va="center")
    # k labels
    ax1.text(1.6, -0.05, r"$k=0$", fontsize=8.8, ha="center")
    ax1.text(4.95, -0.05, r"$k=0$", fontsize=8.8, ha="center")
    ax1.text(5.95, -0.05, r"$k_0$", fontsize=8.8, ha="center")

    ax1.set_xlim(-0.15, 7.15)
    ax1.set_ylim(-0.25, 4.65)
    ax1.axis("off")
    ax1.set_title("直接带隙与间接带隙能带跃迁", fontsize=10.2, pad=6)

    # --- Right: ln(n0) vs 1/T Three Temperature Regimes for n-type Semiconductor ---
    x = np.linspace(0.85, 11.8, 450)
    N_D = math.exp(16.0)
    ln_ni = 23.0 - 4.4 * x
    ni = np.exp(ln_ni)
    # Sharper realistic donor freeze-out so the saturation plateau is visibly crisp and flat
    K = np.exp(24.0 - 1.12 * x)
    n_d = 0.5 * (-K + np.sqrt(K ** 2 + 4.0 * K * N_D))
    n_tot = 0.5 * (n_d + np.sqrt(n_d ** 2 + 4.0 * ni ** 2))
    ln_n = np.log(n_tot)

    x_b1, x_b2 = 2.0, 6.4
    ax2.axvspan(0.85, x_b1, color="#e8e8e8", zorder=0)
    ax2.axvspan(x_b1, x_b2, color="#f6f6f6", zorder=0)
    ax2.axvspan(x_b2, 11.8, color="#ededed", zorder=0)
    ax2.axvline(x_b1, color="#777777", lw=0.85, ls="--", zorder=1)
    ax2.axvline(x_b2, color="#777777", lw=0.85, ls="--", zorder=1)

    ax2.axhline(math.log(N_D), color="#888888", lw=0.85, ls=":", zorder=1)
    ax2.plot(x, ln_n, color="#111111", lw=2.0, zorder=4)

    ax2.text(1.42, 19.45, "高温\n本征区", fontsize=8.2, ha="center", va="top", color="#222222")
    ax2.text(4.20, 19.45, "杂质饱和电离区\n($n_0 \\approx N_D$)", fontsize=8.3, ha="center", va="top", color="#222222")
    ax2.text(9.10, 19.45, "低温弱电离区\n（冻结区）", fontsize=8.3, ha="center", va="top", color="#222222")

    ax2.annotate(r"斜率 $-\frac{E_g}{2k_B}$", xy=(1.32, 17.2), xytext=(2.55, 17.65),
                 fontsize=8.4, ha="left",
                 arrowprops=dict(arrowstyle="->", lw=0.8, color="#222222"))
    ax2.annotate(r"斜率 $-\frac{\Delta E_D}{2k_B}$", xy=(9.6, 14.35), xytext=(7.2, 13.0),
                 fontsize=8.4, ha="center",
                 arrowprops=dict(arrowstyle="->", lw=0.8, color="#222222"))

    ax2.set_xlim(0.7, 11.8)
    ax2.set_ylim(12.2, 19.9)
    ax2.set_xticks([])
    ax2.set_yticks([math.log(N_D)])
    ax2.set_yticklabels([r"$\ln N_D$"], fontsize=8.8)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    ax2.set_xlabel(r"温度倒数 $1/T$（左高温，右低温）", fontsize=9.8)
    ax2.set_ylabel(r"$\ln n_0$", fontsize=10, labelpad=4)
    ax2.set_title(r"$n$ 型半导体载流子浓度随温度的变化", fontsize=10.2, pad=8)

    plt.tight_layout(pad=0.9)
    fig.savefig(os.path.join(OUT_DIR, "ch06-semiconductor-stats.svg"), format="svg", bbox_inches="tight")
    if preview_dir:
        fig.savefig(os.path.join(preview_dir, "ch06-semiconductor-stats.png"), dpi=160, bbox_inches="tight")
    plt.close(fig)


def fig2_pn_mis_bands(preview_dir=None):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.0, 4.0))

    # --- Left: Thermal Equilibrium PN Junction Band Diagram ---
    x = np.linspace(-3.0, 3.0, 400)
    xp, xn = -1.15, 1.15

    def bend(xv, x_l, x_r, height):
        out = np.zeros_like(xv)
        for i, xi in enumerate(xv):
            if xi <= x_l:
                out[i] = height
            elif xi <= 0.0:
                u = (xi - x_l) / (0.0 - x_l)
                out[i] = height * (1.0 - 0.5 * u * u)
            elif xi < x_r:
                u = (x_r - xi) / (x_r - 0.0)
                out[i] = height * (0.5 * u * u)
            else:
                out[i] = 0.0
        return out

    qVbi = 1.55
    Eg = 2.25
    b = bend(x, xp, xn, qVbi)
    Ec = 3.15 + b
    Ev = Ec - Eg
    Efi = 0.5 * (Ec + Ev)
    Ef = 2.80  # cleanly separated from Ec[-1] = 3.15 (gap 0.35) and Ev[0] = 2.45 (gap 0.35)!

    # Shaded depletion zone
    ax1.axvspan(xp, xn, color="#f0f0f0", zorder=0)
    ax1.axvline(xp, color="#888888", lw=0.8, ls=":", zorder=1)
    ax1.axvline(xn, color="#888888", lw=0.8, ls=":", zorder=1)
    ax1.axvline(0.0, color="#666666", lw=0.85, ls="--", zorder=1)

    ax1.plot(x, Ec, color="#111111", lw=1.9, zorder=3)
    ax1.plot(x, Ev, color="#111111", lw=1.9, zorder=3)
    ax1.plot(x, Efi, color="#666666", lw=1.05, ls="-.", zorder=2)
    ax1.plot([-3.0, 3.0], [Ef, Ef], color="#222222", lw=1.25, ls="--", zorder=4)

    # Right-side band edge labels (well separated, no line overlap)
    ax1.text(3.10, Ec[-1], r"$E_c$", fontsize=9.2, va="center", ha="left")
    ax1.text(3.10, Ef, r"$E_F$", fontsize=9.2, va="center", ha="left")
    ax1.text(3.10, Efi[-1], r"$E_{Fi}$", fontsize=8.8, va="center", ha="left", color="#555555")
    ax1.text(3.10, Ev[-1], r"$E_v$", fontsize=9.2, va="center", ha="left")

    # Built-in potential e V_bi arrow
    ax1.plot([xp, 2.20], [Ec[0], Ec[0]], color="#888888", lw=0.75, ls=":")
    ax1.annotate("", xy=(2.05, Ec[0]), xytext=(2.05, Ec[-1]),
                 arrowprops=dict(arrowstyle="<->", lw=1.0, color="#111111"), zorder=5)
    ax1.text(2.18, 0.5 * (Ec[0] + Ec[-1]), r"$e V_{bi}$", fontsize=9.2, va="center", ha="left")

    # Space charge signs & built-in field arrow cleanly BELOW lowest band edge (Ev[-1] = 0.90)
    for sx in [-0.80, -0.35]:
        ax1.text(sx, 0.62, "−", fontsize=10, ha="center", va="center", fontweight="bold", color="#333333")
    for sx in [0.35, 0.80]:
        ax1.text(sx, 0.62, "+", fontsize=10, ha="center", va="center", fontweight="bold", color="#333333")

    ax1.annotate("", xy=(-0.68, 0.28), xytext=(0.68, 0.28),
                 arrowprops=dict(arrowstyle="-|>", lw=1.2, color="#111111"))
    ax1.text(0.0, 0.00, r"内建电场 $\mathcal{E}_{bi}$", fontsize=8.4, ha="center", color="#222222")

    # Region labels
    ax1.text(-2.1, 5.05, "P 区", fontsize=9.4, ha="center")
    ax1.text(0.0, 5.05, "空间电荷区", fontsize=8.8, ha="center", color="#444444")
    ax1.text(2.1, 5.05, "N 区", fontsize=9.4, ha="center")
    ax1.text(xp, -0.35, r"$-x_p$", fontsize=8.8, ha="center")
    ax1.text(xn, -0.35, r"$x_n$", fontsize=8.8, ha="center")

    ax1.set_xlim(-3.15, 3.65)
    ax1.set_ylim(-0.55, 5.38)
    ax1.axis("off")
    ax1.set_title("热平衡 PN 结能带图", fontsize=10.2, pad=6)

    # --- Right: p-type MIS Structure at Strong Inversion (V_G > V_T) ---
    Ev_b, Ef_s, Efi_b, Ec_b = 1.65, 2.00, 2.70, 3.75  # e*phi_F = 0.70, Eg = 2.10
    psi_s = 1.40  # 2 * e*phi_F
    W_dep = 2.35  # depletion width from x=2.3 to x=4.65

    # Metal occupied states
    Ef_m = 0.85
    ax2.add_patch(Rectangle((0.0, 0.0), 1.3, Ef_m, facecolor="#dedede", edgecolor="none", zorder=1))
    ax2.plot([0.0, 1.3], [Ef_m, Ef_m], color="#111111", lw=1.6, zorder=3)
    ax2.text(0.12, Ef_m + 0.16, r"$E_{FM}$", fontsize=8.8, ha="left")
    ax2.text(0.65, 4.82, "金属", fontsize=8.8, ha="center")

    # Sloped oxide barrier cleanly below title labels
    ox_top_L, ox_top_R = 3.92, 4.42
    ax2.fill_between([1.3, 2.3], [0.0, 0.0], [ox_top_L, ox_top_R], color="#f5f5f5", zorder=0)
    ax2.plot([1.3, 1.3], [0.0, ox_top_L], color="#111111", lw=1.4, zorder=3)
    ax2.plot([2.3, 2.3], [0.0, ox_top_R], color="#111111", lw=1.4, zorder=3)
    ax2.plot([1.3, 2.3], [ox_top_L, ox_top_R], color="#111111", lw=1.6, zorder=3)
    ax2.text(1.8, 4.82, "绝缘层", fontsize=8.6, ha="center")

    # p-Si bands
    xs = np.linspace(2.3, 6.2, 260)
    u = np.clip((2.3 + W_dep - xs) / W_dep, 0.0, 1.0)
    bend_mis = psi_s * (u ** 2)
    Ec_m = Ec_b - bend_mis
    Efi_m = Efi_b - bend_mis
    Ev_m = Ev_b - bend_mis

    ax2.plot(xs, Ec_m, color="#111111", lw=1.9, zorder=3)
    ax2.plot(xs, Efi_m, color="#666666", lw=1.05, ls="-.", zorder=2)
    ax2.plot(xs, Ev_m, color="#111111", lw=1.9, zorder=3)
    ax2.plot([2.3, 6.2], [Ef_s, Ef_s], color="#222222", lw=1.25, ls="--", zorder=4)

    # Inversion electrons cleanly inside triangular pocket above Ec_m
    for ex, ey in [(2.44, 2.86), (2.44, 3.16), (2.70, 3.12)]:
        ax2.text(ex, ey, "−", fontsize=9.2, ha="center", va="center", fontweight="bold", color="#111111")
    ax2.annotate("反型层电子", xy=(2.60, 3.22), xytext=(3.18, 4.30),
                 fontsize=8.2, ha="left",
                 arrowprops=dict(arrowstyle="->", lw=0.8, color="#222222"))

    # Bulk e*phi_F arrow
    ax2.annotate("", xy=(5.65, Efi_b), xytext=(5.65, Ef_s),
                 arrowprops=dict(arrowstyle="<->", lw=0.9, color="#333333"))
    ax2.text(5.78, 0.5 * (Efi_b + Ef_s), r"$e\phi_F$", fontsize=8.4, va="center", ha="left")

    # Surface band bending 2 e*phi_F arrow (exact vertical span between dotted Efi_b and dotted Efi_m[0])
    ax2.plot([2.3, 4.65], [Efi_b, Efi_b], color="#888888", lw=0.75, ls=":")
    ax2.plot([2.3, 3.15], [Efi_m[0], Efi_m[0]], color="#888888", lw=0.75, ls=":")
    ax2.annotate("", xy=(2.95, Efi_b), xytext=(2.95, Efi_m[0]),
                 arrowprops=dict(arrowstyle="<->", lw=0.95, color="#111111"))
    ax2.text(3.10, 1.66, r"$2e\phi_F$", fontsize=8.4, va="center", ha="left",
             bbox=dict(facecolor="white", edgecolor="none", pad=0.8))

    # Right labels
    ax2.text(6.28, Ec_b, r"$E_c$", fontsize=9.0, va="center", ha="left")
    ax2.text(6.28, Efi_b, r"$E_{Fi}$", fontsize=8.6, va="center", ha="left", color="#555555")
    ax2.text(6.28, Ef_s, r"$E_{FS}$", fontsize=9.0, va="center", ha="left")
    ax2.text(6.28, Ev_b, r"$E_v$", fontsize=9.0, va="center", ha="left")
    ax2.text(4.35, 4.82, r"$p$ 型半导体", fontsize=8.8, ha="center")

    # Gate voltage e V_G arrow cleanly placed to the right of E_FM label
    ax2.plot([0.55, 1.3], [Ef_s, Ef_s], color="#888888", lw=0.75, ls=":")
    ax2.annotate("", xy=(0.95, Ef_s), xytext=(0.95, Ef_m),
                 arrowprops=dict(arrowstyle="<->", lw=0.95, color="#333333"))
    ax2.text(0.84, 0.5 * (Ef_s + Ef_m) + 0.05, r"$eV_G$", fontsize=8.6, va="center", ha="right")

    ax2.set_xlim(-0.15, 6.95)
    ax2.set_ylim(-0.20, 5.20)
    ax2.axis("off")
    ax2.set_title(r"$p$ 型 MIS 结构强反型能带图（$V_G > V_T$）", fontsize=10.2, pad=6)

    plt.tight_layout(pad=0.85)
    fig.savefig(os.path.join(OUT_DIR, "ch06-pn-mis-bands.svg"), format="svg", bbox_inches="tight")
    if preview_dir:
        fig.savefig(os.path.join(preview_dir, "ch06-pn-mis-bands.png"), dpi=160, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    import sys
    pdir = sys.argv[1] if len(sys.argv) > 1 else None
    if pdir:
        os.makedirs(pdir, exist_ok=True)
    fig1_semiconductor_stats(pdir)
    fig2_pn_mis_bands(pdir)
    print("Generated 2 SVG figures for Chapter 6 in", OUT_DIR)
