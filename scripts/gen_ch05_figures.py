"""Generate clean monochrome academic SVG diagrams for Chapter 5 (Band Theory)."""
import os
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
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


def fig1_band_diagrams(preview_dir=None):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.0, 4.0))

    # --- Left: 1D Nearly Free Electron (Extended + Reduced BZ) ---
    # Exact plane-wave Hamiltonian in units where hbar^2/(2m) = 1, a = 1 (so pi/a = pi)
    # Use scaled k in units of pi/a, so k_s in [-2, 2], E0 = k_s^2
    # V1 = 0.22 (gap 0.44 at |k_s|=1), V2 = 0.14 (gap 0.28 at |k_s|=2)
    V1, V2 = 0.22, 0.13
    G_list = np.array([-4, -2, 0, 2, 4], dtype=float)  # reciprocal vectors in units of pi/a

    def solve_bands(k_arr):
        nb = len(G_list)
        out = np.zeros((len(k_arr), nb))
        for idx, kv in enumerate(k_arr):
            H = np.diag((kv + G_list) ** 2)
            for i in range(nb):
                for j in range(nb):
                    d = abs(G_list[i] - G_list[j])
                    if abs(d - 2.0) < 1e-6:
                        H[i, j] = -V1
                    elif abs(d - 4.0) < 1e-6:
                        H[i, j] = -V2
            out[idx] = np.linalg.eigvalsh(H)
        return out

    ks_1 = np.linspace(-1.0, 1.0, 240)
    ks_2R = np.linspace(1.0, 2.0, 160)
    ks_2L = np.linspace(-2.0, -1.0, 160)
    ks_full = np.linspace(-2.15, 2.15, 400)

    E_1 = solve_bands(ks_1)
    E_2R = solve_bands(ks_2R)
    E_2L = solve_bands(ks_2L)

    # Shaded 1st BZ
    ax1.axvspan(-1.0, 1.0, color="#f2f2f2", zorder=0)
    for xb in [-2.0, -1.0, 1.0, 2.0]:
        ax1.axvline(xb, color="#777777", lw=0.85, ls="--", zorder=1)
    ax1.axvline(0.0, color="#999999", lw=0.7, zorder=1)

    # Free-electron parabola
    ax1.plot(ks_full, ks_full ** 2, color="#888888", lw=1.0, ls=":", label="自由电子抛物线", zorder=2)

    # Extended zone: 1st band in [-1, 1], 2nd band in [-2,-1] & [1,2]
    ax1.plot(ks_1, E_1[:, 0], color="#111111", lw=1.9, label="扩展区能带", zorder=4)
    ax1.plot(ks_2R, E_2R[:, 1], color="#111111", lw=1.9, zorder=4)
    ax1.plot(ks_2L, E_2L[:, 1], color="#111111", lw=1.9, zorder=4)

    # Reduced zone folded 2nd band inside 1st BZ [-1, 1]
    ax1.plot(ks_1, E_1[:, 1], color="#444444", lw=1.45, ls="-.", label="简约区折合（第 2 带）", zorder=3)

    # Gap annotation at k = +1
    e_bot = E_1[-1, 0]
    e_top = E_1[-1, 1]
    ax1.annotate("", xy=(1.0, e_top), xytext=(1.0, e_bot),
                 arrowprops=dict(arrowstyle="<->", lw=1.05, color="#111111"), zorder=6)
    ax1.text(1.10, 0.5 * (e_bot + e_top), r"$2|V_1|$", fontsize=9.2, va="center", ha="left", color="#111111")

    ax1.text(0.0, 0.28, "1st BZ", fontsize=8.5, ha="center", color="#555555")
    ax1.set_xlim(-2.2, 2.2)
    ax1.set_ylim(-0.15, 5.25)
    ax1.set_xticks([-2.0, -1.0, 0.0, 1.0, 2.0])
    ax1.set_xticklabels([r"$-\frac{2\pi}{a}$", r"$-\frac{\pi}{a}$", r"$0$", r"$\frac{\pi}{a}$", r"$\frac{2\pi}{a}$"], fontsize=9.5)
    ax1.set_yticks([])
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    ax1.set_xlabel(r"波矢 $k$", fontsize=10)
    ax1.set_ylabel(r"能量 $E$", fontsize=10)
    ax1.legend(loc="upper center", frameon=True, facecolor="white", edgecolor="none", framealpha=0.85, fontsize=8.0)
    ax1.set_title("一维近自由电子能带（扩展与简约图示）", fontsize=10.2, pad=8)

    # --- Right: 2D Square Lattice Tight-Binding Constant-Energy Contours ---
    k_grid = np.linspace(-math.pi, math.pi, 320)
    KX, KY = np.meshgrid(k_grid, k_grid)
    # Dimensionless energy eps = -(cos kx + cos ky) in [-2, 2]
    EPS = -(np.cos(KX) + np.cos(KY))

    # Shade half-filled Fermi sea (EPS <= 0)
    ax2.contourf(KX, KY, EPS, levels=[-2.1, 0.0], colors=["#e8e8e8"], zorder=0)

    # Electron-like contours (< 0)
    cs_e = ax2.contour(KX, KY, EPS, levels=[-1.6, -1.0, -0.45], colors="#444444", linewidths=1.05, linestyles="-", zorder=2)
    # Half-filled diamond contour (EPS = 0)
    ax2.contour(KX, KY, EPS, levels=[0.0], colors="#111111", linewidths=1.9, linestyles="-", zorder=3)
    # Hole-like contours (> 0)
    ax2.contour(KX, KY, EPS, levels=[0.45, 1.0, 1.6], colors="#666666", linewidths=1.05, linestyles="--", zorder=2)

    # BZ boundary square
    ax2.plot([-math.pi, math.pi, math.pi, -math.pi, -math.pi],
             [-math.pi, -math.pi, math.pi, math.pi, -math.pi], color="#111111", lw=1.4, zorder=4)
    # Axes through origin
    ax2.axhline(0, color="#888888", lw=0.7, ls=":", zorder=1)
    ax2.axvline(0, color="#888888", lw=0.7, ls=":", zorder=1)

    # High-symmetry points Gamma, X, M
    pts = [(0.0, 0.0), (math.pi, 0.0), (math.pi, math.pi)]
    ax2.scatter([p[0] for p in pts], [p[1] for p in pts], s=26, color="#111111", zorder=5)
    ax2.text(0.18, -0.34, r"$\Gamma$", fontsize=9.8, ha="left", va="top")
    ax2.text(math.pi + 0.16, 0.0, r"$X$", fontsize=9.8, ha="left", va="center")
    ax2.text(math.pi + 0.14, math.pi + 0.10, r"$M$", fontsize=9.8, ha="left", va="bottom")

    # Contour annotations
    ax2.annotate(r"半满费米线 ($E = E_c$)", xy=(-1.55, 1.59), xytext=(-3.05, 2.45),
                 fontsize=8.2, ha="left",
                 bbox=dict(facecolor="white", edgecolor="none", pad=1.2, alpha=0.88),
                 arrowprops=dict(arrowstyle="->", lw=0.8, color="#222222"))
    ax2.text(0.0, -2.55, "实线：电子型    虚线：空穴型", fontsize=8.0, ha="center",
             bbox=dict(facecolor="white", edgecolor="none", pad=1.2, alpha=0.85), color="#333333")

    ax2.set_xlim(-3.55, 3.85)
    ax2.set_ylim(-3.55, 3.65)
    ax2.set_aspect("equal")
    ax2.set_xticks([-math.pi, 0, math.pi])
    ax2.set_xticklabels([r"$-\frac{\pi}{a}$", r"$0$", r"$\frac{\pi}{a}$"], fontsize=9.5)
    ax2.set_yticks([-math.pi, 0, math.pi])
    ax2.set_yticklabels([r"$-\frac{\pi}{a}$", r"$0$", r"$\frac{\pi}{a}$"], fontsize=9.5)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    ax2.set_xlabel(r"$k_x$", fontsize=10)
    ax2.set_ylabel(r"$k_y$", fontsize=10)
    ax2.set_title(r"二维正方晶格紧束缚等能线（1st BZ）", fontsize=10.2, pad=8)

    plt.tight_layout(pad=0.9)
    fig.savefig(os.path.join(OUT_DIR, "ch05-band-diagrams.svg"), format="svg", bbox_inches="tight")
    if preview_dir:
        fig.savefig(os.path.join(preview_dir, "ch05-band-diagrams.png"), dpi=160, bbox_inches="tight")
    plt.close(fig)


def fig2_effective_mass_and_classification(preview_dir=None):
    fig = plt.figure(figsize=(9.2, 4.4))
    gs = GridSpec(3, 2, width_ratios=[1.08, 1.0], hspace=0.22, wspace=0.22, figure=fig)

    # --- Left column: 3 stacked synced plots E(k), v(k), 1/m*(k) ---
    ax_e = fig.add_subplot(gs[0, 0])
    ax_v = fig.add_subplot(gs[1, 0], sharex=ax_e)
    ax_m = fig.add_subplot(gs[2, 0], sharex=ax_e)

    k = np.linspace(-math.pi, math.pi, 400)
    E_k = -np.cos(k)
    v_k = np.sin(k)
    inv_m = np.cos(k)

    # Shaded m* > 0 vs m* < 0 zones on bottom panel
    ax_m.axvspan(-math.pi / 2, math.pi / 2, color="#f0f0f0", zorder=0)
    ax_m.axvspan(-math.pi, -math.pi / 2, color="#dfdfdf", zorder=0)
    ax_m.axvspan(math.pi / 2, math.pi, color="#dfdfdf", zorder=0)

    for ax in (ax_e, ax_v, ax_m):
        for xline in (-math.pi / 2, 0.0, math.pi / 2):
            ax.axvline(xline, color="#777777", lw=0.75, ls=":", zorder=1)
        ax.axhline(0.0, color="#888888", lw=0.7, ls="-", zorder=1)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.set_yticks([])

    ax_e.plot(k, E_k, color="#111111", lw=1.8, zorder=3)
    ax_e.scatter([-math.pi / 2, math.pi / 2], [0.0, 0.0], s=20, color="#111111", zorder=4)
    ax_e.set_ylabel(r"$E(k)$", fontsize=9.8)
    ax_e.set_ylim(-1.25, 1.25)
    ax_e.set_title("一维紧束缚能带：色散、群速度与倒有效质量", fontsize=10.0, pad=7)

    ax_v.plot(k, v_k, color="#111111", lw=1.8, zorder=3)
    ax_v.scatter([-math.pi / 2, math.pi / 2], [-1.0, 1.0], s=20, color="#111111", zorder=4)
    ax_v.text(math.pi / 2 + 0.16, 0.45, r"$v_{\max}$", fontsize=8.6, ha="left")
    ax_v.set_ylabel(r"$v(k)$", fontsize=9.8)
    ax_v.set_ylim(-1.28, 1.28)

    ax_m.plot(k, inv_m, color="#111111", lw=1.8, zorder=3)
    ax_m.scatter([-math.pi / 2, math.pi / 2], [0.0, 0.0], s=20, color="#111111", zorder=4)
    ax_m.text(0.0, 0.35, r"$m^* > 0$", fontsize=8.8, ha="center", color="#111111")
    ax_m.text(-0.77 * math.pi, -0.38, r"$m^* < 0$", fontsize=8.4, ha="center", color="#222222")
    ax_m.text(0.77 * math.pi, -0.38, r"$m^* < 0$", fontsize=8.4, ha="center", color="#222222")
    ax_m.set_ylabel(r"$1/m^*(k)$", fontsize=9.8)
    ax_m.set_ylim(-1.28, 1.28)
    ax_m.set_xlim(-math.pi, math.pi)
    ax_m.set_xticks([-math.pi, -math.pi / 2, 0.0, math.pi / 2, math.pi])
    ax_m.set_xticklabels([r"$-\frac{\pi}{a}$", r"$-\frac{\pi}{2a}$", r"$0$", r"$\frac{\pi}{2a}$", r"$\frac{\pi}{a}$"], fontsize=9.2)
    ax_m.set_xlabel(r"波矢 $k$", fontsize=10)

    plt.setp(ax_e.get_xticklabels(), visible=False)
    plt.setp(ax_v.get_xticklabels(), visible=False)

    # --- Right column: Conductor (monovalent & divalent overlap), Semiconductor, Insulator ---
    ax_c = fig.add_subplot(gs[:, 1])

    def draw_band(x0, y0, w, h, filled_frac=0.0, hatch=None, fill_color="#cccccc"):
        # Empty outer box
        ax_c.add_patch(Rectangle((x0, y0), w, h, facecolor="white", edgecolor="#111111", lw=1.2, zorder=2))
        if filled_frac > 0:
            ax_c.add_patch(Rectangle((x0, y0), w, h * filled_frac, facecolor=fill_color,
                                     edgecolor="#111111", lw=0.8, hatch=hatch, zorder=3))

    bw = 1.25
    # 1. Monovalent metal (half-filled band)
    x1 = 0.55
    draw_band(x1, 0.4, bw, 1.3, filled_frac=1.0, fill_color="#d8d8d8")
    draw_band(x1, 2.35, bw, 2.1, filled_frac=0.5, fill_color="#d8d8d8")
    ax_c.plot([x1 - 0.18, x1 + bw + 0.18], [3.4, 3.4], color="#111111", lw=1.1, ls="--", zorder=5)
    ax_c.text(x1 + bw / 2, -0.05, "一价金属\n(半满带)", fontsize=8.4, ha="center", va="top")

    # 2. Divalent metal (overlapping bands)
    x2 = 2.45
    draw_band(x2, 0.4, bw, 1.3, filled_frac=1.0, fill_color="#d8d8d8")
    # Overlapping two bands drawn slightly offset horizontally for crystal clarity
    draw_band(x2, 2.20, bw * 0.62, 1.75, filled_frac=0.72, fill_color="#d8d8d8")
    draw_band(x2 + bw * 0.38, 3.10, bw * 0.62, 1.65, filled_frac=0.22, fill_color="#bcbcbc")
    ax_c.plot([x2 - 0.18, x2 + bw + 0.18], [3.46, 3.46], color="#111111", lw=1.1, ls="--", zorder=5)
    ax_c.text(x2 + bw / 2, -0.05, "二价金属\n(能带交叠)", fontsize=8.4, ha="center", va="top")

    # 3. Semiconductor (narrow Eg)
    x3 = 4.35
    draw_band(x3, 0.4, bw, 2.0, filled_frac=1.0, fill_color="#d8d8d8")
    draw_band(x3, 3.35, bw, 1.55, filled_frac=0.0)
    ax_c.plot([x3 - 0.18, x3 + bw + 0.18], [2.875, 2.875], color="#555555", lw=1.0, ls="--", zorder=5)
    ax_c.annotate("", xy=(x3 + bw * 0.36, 3.35), xytext=(x3 + bw * 0.36, 2.4),
                  arrowprops=dict(arrowstyle="<->", lw=0.95, color="#111111"), zorder=6)
    ax_c.text(x3 + bw * 0.56, 2.88, r"$E_g$", fontsize=8.8, va="center", ha="left",
              bbox=dict(facecolor="white", edgecolor="none", pad=1.0), zorder=7)
    ax_c.text(x3 + bw / 2, -0.05, "半导体\n(窄禁带)", fontsize=8.4, ha="center", va="top")

    # 4. Insulator (wide Eg)
    x4 = 6.25
    draw_band(x4, 0.4, bw, 1.45, filled_frac=1.0, fill_color="#d8d8d8")
    draw_band(x4, 4.05, bw, 1.25, filled_frac=0.0)
    ax_c.plot([x4 - 0.18, x4 + bw + 0.18], [2.95, 2.95], color="#555555", lw=1.0, ls="--", zorder=5)
    ax_c.annotate("", xy=(x4 + bw * 0.36, 4.05), xytext=(x4 + bw * 0.36, 1.85),
                  arrowprops=dict(arrowstyle="<->", lw=0.95, color="#111111"), zorder=6)
    ax_c.text(x4 + bw * 0.56, 3.38, r"$E_g$", fontsize=8.8, va="center", ha="left", zorder=7)
    ax_c.text(x4 + bw / 2, -0.05, "绝缘体\n(宽禁带)", fontsize=8.4, ha="center", va="top")

    # Legend indicators at top of right panel
    ax_c.add_patch(Rectangle((0.6, 5.55), 0.42, 0.28, facecolor="#d8d8d8", edgecolor="#111111", lw=0.9))
    ax_c.text(1.15, 5.69, "电子占据态", fontsize=8.2, va="center")
    ax_c.add_patch(Rectangle((3.1, 5.55), 0.42, 0.28, facecolor="white", edgecolor="#111111", lw=0.9))
    ax_c.text(3.65, 5.69, "空态", fontsize=8.2, va="center")
    ax_c.plot([5.15, 5.70], [5.69, 5.69], color="#111111", lw=1.1, ls="--")
    ax_c.text(5.82, 5.69, r"$E_F$", fontsize=8.8, va="center")

    # Energy arrow on left
    ax_c.annotate("", xy=(0.15, 5.45), xytext=(0.15, 0.30),
                  arrowprops=dict(arrowstyle="-|>", lw=1.0, color="#111111"))
    ax_c.text(-0.08, 5.35, r"$E$", fontsize=9.8, ha="center", va="center")

    ax_c.set_xlim(-0.25, 7.85)
    ax_c.set_ylim(-0.75, 6.05)
    ax_c.axis("off")
    ax_c.set_title("能带填充与固体导电类型判别", fontsize=10.0, pad=7)

    fig.savefig(os.path.join(OUT_DIR, "ch05-tight-binding-effective-mass.svg"), format="svg", bbox_inches="tight")
    if preview_dir:
        fig.savefig(os.path.join(preview_dir, "ch05-tight-binding-effective-mass.png"), dpi=160, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    import sys
    pdir = sys.argv[1] if len(sys.argv) > 1 else None
    if pdir:
        os.makedirs(pdir, exist_ok=True)
    fig1_band_diagrams(pdir)
    fig2_effective_mass_and_classification(pdir)
    print("Generated 2 SVG figures for Chapter 5 in", OUT_DIR)
