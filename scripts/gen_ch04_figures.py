"""Generate clean monochrome academic SVG diagrams for Chapter 4 (Free Electron Theory)."""
import os
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

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


def fig1_fermi_dos(preview_dir=None):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.8, 3.8))

    # --- Left: 1D, 2D, 3D Free Electron DOS g(E) / g(E_F) ---
    e_all = np.linspace(0.0, 1.55, 500)
    e_occ = np.linspace(0.0, 1.0, 300)
    e_1d = np.linspace(0.15, 1.55, 400)

    g_3d = np.sqrt(e_all)
    g_3d_occ = np.sqrt(e_occ)
    g_2d = np.ones_like(e_all)
    g_1d = 1.0 / np.sqrt(e_1d)

    ax1.fill_between(e_occ, 0, g_3d_occ, color="#e8e8e8", zorder=1)
    ax1.plot(e_all, g_3d, color="#111111", lw=1.9, label=r"3D: $g(E)\propto E^{1/2}$", zorder=4)
    ax1.plot(e_all, g_2d, color="#444444", lw=1.4, ls="-.", label=r"2D: $g(E)=\mathrm{const}$", zorder=3)
    ax1.plot(e_1d, g_1d, color="#666666", lw=1.35, ls="--", label=r"1D: $g(E)\propto E^{-1/2}$", zorder=3)

    ax1.plot([1.0, 1.0], [0, 2.35], color="#555555", lw=0.9, ls=":", zorder=2)
    ax1.scatter([1.0], [1.0], s=26, color="#111111", zorder=5)
    ax1.text(0.55, 0.30, "3D 基态占据\n($T=0$)", fontsize=8.6, ha="center", va="center", color="#222222")

    ax1.set_xlim(0, 1.58)
    ax1.set_ylim(0, 2.55)
    ax1.set_xticks([0, 1.0])
    ax1.set_xticklabels([r"$0$", r"$E_F$"], fontsize=10)
    ax1.set_yticks([])
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    ax1.set_xlabel(r"能量 $E$", fontsize=10)
    ax1.set_ylabel(r"归一化态密度 $g(E)/g(E_F)$", fontsize=10)
    ax1.legend(loc="upper right", frameon=False, fontsize=8.4)
    ax1.set_title("1D/2D/3D 自由电子态密度", fontsize=10.5, pad=8)

    # --- Right: Fermi-Dirac distribution f(E) ---
    x = np.linspace(0.0, 1.85, 600)
    f_0 = np.where(x < 1.0, 1.0, 0.0)
    f_low = 1.0 / (np.exp(np.clip((x - 1.0) / 0.05, -200, 200)) + 1.0)
    f_high = 1.0 / (np.exp(np.clip((x - 1.0) / 0.16, -200, 200)) + 1.0)

    # Thermal excitation window around E = mu
    ax2.axvspan(0.84, 1.16, color="#efefef", zorder=0)
    ax2.plot([0, 1.0], [0.5, 0.5], color="#888888", lw=0.85, ls=":", zorder=1)
    ax2.plot([1.0, 1.0], [0, 1.0], color="#888888", lw=0.85, ls=":", zorder=1)

    # Plot T=0 step cleanly with vertical drop
    ax2.plot([0.0, 1.0, 1.0, 1.85], [1.0, 1.0, 0.0, 0.0], color="#111111", lw=1.9, label=r"$T = 0$", zorder=4)
    ax2.plot(x, f_low, color="#444444", lw=1.45, ls="--", label=r"$k_B T = 0.05\mu$", zorder=3)
    ax2.plot(x, f_high, color="#777777", lw=1.35, ls="-.", label=r"$k_B T = 0.16\mu$", zorder=3)
    ax2.scatter([1.0], [0.5], s=26, color="#111111", zorder=5)

    ax2.annotate(r"$f(\mu) = \frac{1}{2}$", xy=(1.0, 0.5), xytext=(1.22, 0.56),
                 fontsize=9.0, arrowprops=dict(arrowstyle="->", lw=0.8, color="#333333"))
    ax2.annotate("", xy=(0.84, 1.07), xytext=(1.16, 1.07),
                 arrowprops=dict(arrowstyle="<->", lw=0.95, color="#333333"))
    ax2.text(1.0, 1.115, r"$\sim 2k_B T$", fontsize=8.6, ha="center", color="#222222")

    ax2.set_xlim(0, 1.85)
    ax2.set_ylim(0, 1.24)
    ax2.set_xticks([0, 1.0])
    ax2.set_xticklabels([r"$0$", r"$\mu \approx E_F$"], fontsize=10)
    ax2.set_yticks([0, 0.5, 1.0])
    ax2.set_yticklabels(["0", "0.5", "1"], fontsize=9.5)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    ax2.set_xlabel(r"能量 $E$", fontsize=10)
    ax2.set_ylabel(r"占据几率 $f(E)$", fontsize=10)
    ax2.legend(loc="upper right", frameon=False, fontsize=8.4)
    ax2.set_title("费米-狄拉克分布函数", fontsize=10.5, pad=8)

    plt.tight_layout(pad=0.9)
    fig.savefig(os.path.join(OUT_DIR, "ch04-fermi-dos.svg"), format="svg", bbox_inches="tight")
    if preview_dir:
        fig.savefig(os.path.join(preview_dir, "ch04-fermi-dos.png"), dpi=160, bbox_inches="tight")
    plt.close(fig)


def fig2_contact_transport(preview_dir=None):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.8, 3.85))

    # --- Left: Contact potential energy diagram (Thermal equilibrium, W_A < W_B) ---
    y_ef = 2.6
    y_bot_a, y_vac_a = 0.65, 4.35
    y_bot_b, y_vac_b = 0.35, 5.45

    # Shaded occupied bands
    ax1.fill_between([0.3, 3.1], y_bot_a, y_ef, color="#e4e4e4", zorder=1)
    ax1.fill_between([5.1, 7.9], y_bot_b, y_ef, color="#e4e4e4", zorder=1)

    # Potential well walls & bottoms
    ax1.plot([0.3, 3.1, 3.1], [y_bot_a, y_bot_a, y_vac_a], color="#111111", lw=1.6, zorder=3)
    ax1.plot([0.3, 0.3], [y_bot_a, y_vac_a], color="#111111", lw=1.1, ls=":", zorder=3)
    ax1.plot([5.1, 5.1, 7.9], [y_vac_b, y_bot_b, y_bot_b], color="#111111", lw=1.6, zorder=3)
    ax1.plot([7.9, 7.9], [y_bot_b, y_vac_b], color="#111111", lw=1.1, ls=":", zorder=3)

    # Vacuum levels
    ax1.plot([0.3, 3.1], [y_vac_a, y_vac_a], color="#111111", lw=1.5, zorder=3)
    ax1.plot([5.1, 7.9], [y_vac_b, y_vac_b], color="#111111", lw=1.5, zorder=3)
    # Sloped vacuum level across interface gap
    ax1.plot([3.1, 5.1], [y_vac_a, y_vac_b], color="#111111", lw=1.5, zorder=3)
    # Horizontal dashed extension of E_vac,B leftward over Metal A edge for clean height measurement
    ax1.plot([2.45, 5.1], [y_vac_b, y_vac_b], color="#777777", lw=0.9, ls="--", zorder=2)

    # Aligned Fermi level
    ax1.plot([0.2, 8.0], [y_ef, y_ef], color="#333333", lw=1.15, ls="--", zorder=4)
    ax1.text(4.1, y_ef - 0.34, r"$E_{F,A} = E_{F,B}$", fontsize=8.8, ha="center", color="#222222")

    # Work function arrows W_A, W_B
    ax1.annotate("", xy=(1.55, y_vac_a), xytext=(1.55, y_ef),
                 arrowprops=dict(arrowstyle="<->", lw=1.0, color="#111111"))
    ax1.text(1.75, 0.5 * (y_ef + y_vac_a), r"$W_A$", fontsize=9.5, va="center")

    ax1.annotate("", xy=(6.5, y_vac_b), xytext=(6.5, y_ef),
                 arrowprops=dict(arrowstyle="<->", lw=1.0, color="#111111"))
    ax1.text(6.68, 0.5 * (y_ef + y_vac_b), r"$W_B$", fontsize=9.5, va="center")

    # Contact potential difference e Delta phi_AB = W_B - W_A (cleanly outside the sloped line)
    ax1.annotate("", xy=(2.75, y_vac_b), xytext=(2.75, y_vac_a),
                 arrowprops=dict(arrowstyle="<->", lw=1.05, color="#111111"))
    ax1.text(3.75, y_vac_b + 0.32, r"$e(\varphi_A - \varphi_B) = W_B - W_A$",
             fontsize=8.6, ha="center", color="#111111")

    # Surface charges & vacuum labels
    for yc in [3.15, 3.65]:
        ax1.text(3.26, yc, "+", fontsize=9.5, ha="center", va="center", color="#333333", fontweight="bold")
        ax1.text(4.94, yc, "−", fontsize=9.5, ha="center", va="center", color="#333333", fontweight="bold")

    ax1.text(1.35, y_vac_a + 0.25, r"$E_{\mathrm{vac},A}$", fontsize=8.8, ha="center", color="#333333")
    ax1.text(6.5, y_vac_b + 0.25, r"$E_{\mathrm{vac},B}$", fontsize=8.8, ha="center", color="#333333")
    ax1.text(1.7, 1.55, "金属 A\n(已占据)", fontsize=8.8, ha="center", va="center", color="#222222")
    ax1.text(6.5, 1.45, "金属 B\n(已占据)", fontsize=8.8, ha="center", va="center", color="#222222")

    # Energy axis arrow on far left
    ax1.annotate("", xy=(0.05, 5.95), xytext=(0.05, 0.15),
                 arrowprops=dict(arrowstyle="-|>", lw=1.0, color="#111111"))
    ax1.text(-0.18, 5.85, r"$E$", fontsize=10, ha="center", va="center")

    ax1.set_xlim(-0.45, 8.3)
    ax1.set_ylim(0.0, 6.25)
    ax1.axis("off")
    ax1.set_title(r"金属接触电势差（热平衡，$W_A < W_B$）", fontsize=10.5, pad=6)

    # --- Right: Shifted Fermi sphere under electric field E ---
    R = 1.0
    delta = 0.24  # exaggerated shift along -kx for E along +kx
    theta = np.linspace(0, 2 * math.pi, 400)

    # Intersection of circles (x^2 + y^2 = R^2) and ((x+delta)^2 + y^2 = R^2) is x_i = -delta/2
    x_i = -0.5 * delta
    y_i = math.sqrt(R ** 2 - x_i ** 2)
    # Angle on origin circle for intersection points
    ang0 = math.atan2(y_i, x_i)  # in (pi/2, pi)
    # Angle on shifted circle (center -delta, 0) for intersection points
    ang1 = math.atan2(y_i, x_i + delta)  # in (0, pi/2)

    # Left crescent (newly occupied): outer arc on shifted circle from ang1 to 2pi - ang1,
    # inner arc on origin circle from 2pi - ang0 down to ang0
    t_outer_L = np.linspace(ang1, 2 * math.pi - ang1, 200)
    t_inner_L = np.linspace(2 * math.pi - ang0, ang0, 200)
    xs_L = np.concatenate([-delta + R * np.cos(t_outer_L), R * np.cos(t_inner_L)])
    ys_L = np.concatenate([R * np.sin(t_outer_L), R * np.sin(t_inner_L)])
    ax2.add_patch(Polygon(np.column_stack([xs_L, ys_L]), closed=True,
                          facecolor="#cccccc", edgecolor="none", zorder=1))

    # Right crescent (vacated): outer arc on origin circle from -ang0 to +ang0,
    # inner arc on shifted circle from +ang1 down to -ang1
    t_outer_R = np.linspace(-ang0, ang0, 200)
    t_inner_R = np.linspace(ang1, -ang1, 200)
    xs_R = np.concatenate([R * np.cos(t_outer_R), -delta + R * np.cos(t_inner_R)])
    ys_R = np.concatenate([R * np.sin(t_outer_R), R * np.sin(t_inner_R)])
    ax2.add_patch(Polygon(np.column_stack([xs_R, ys_R]), closed=True,
                          facecolor="#f7f7f7", edgecolor="#999999", lw=0.4, hatch="////", zorder=1))

    # Circles
    ax2.plot(R * np.cos(theta), R * np.sin(theta), color="#666666", lw=1.25, ls="--", zorder=3)
    ax2.plot(-delta + R * np.cos(theta), R * np.sin(theta), color="#111111", lw=1.8, zorder=4)

    # Axes
    ax2.annotate("", xy=(1.42, 0), xytext=(-1.50, 0),
                 arrowprops=dict(arrowstyle="-|>", lw=0.9, color="#444444"), zorder=2)
    ax2.annotate("", xy=(0, 1.38), xytext=(0, -1.35),
                 arrowprops=dict(arrowstyle="-|>", lw=0.9, color="#444444"), zorder=2)
    ax2.text(1.44, -0.14, r"$k_x$", fontsize=10, ha="center")
    ax2.text(0.14, 1.34, r"$k_y$", fontsize=10, ha="center")

    # Radius k_F arrow
    ang_r = math.radians(52)
    ax2.annotate("", xy=(R * math.cos(ang_r), R * math.sin(ang_r)), xytext=(0, 0),
                 arrowprops=dict(arrowstyle="-|>", lw=1.0, color="#333333"), zorder=5)
    ax2.text(0.38, 0.56, r"$k_F$", fontsize=9.5, ha="center")

    # Shift vector Delta k
    ax2.annotate("", xy=(-delta, 0), xytext=(0, 0),
                 arrowprops=dict(arrowstyle="-|>", lw=1.6, color="#111111"), zorder=6)
    ax2.annotate(r"$\Delta \mathbf{k} = -\frac{e\tau}{\hbar}\mathbf{E}$",
                 xy=(-0.55 * delta, -0.05), xytext=(-0.48, -0.52),
                 fontsize=8.8, ha="center",
                 arrowprops=dict(arrowstyle="->", lw=0.8, color="#333333"))

    # Electric field E vector at top-right
    ax2.annotate("", xy=(1.36, 1.15), xytext=(0.76, 1.15),
                 arrowprops=dict(arrowstyle="-|>", lw=1.5, color="#111111"))
    ax2.text(1.06, 1.24, r"外电场 $\mathbf{E}$", fontsize=8.8, ha="center")

    # Crescent annotations
    ax2.annotate("新增占据态", xy=(-1.12, 0.25), xytext=(-1.52, 0.92),
                 fontsize=8.3, ha="left",
                 arrowprops=dict(arrowstyle="->", lw=0.75, color="#333333"))
    ax2.annotate("空出态", xy=(0.88, -0.28), xytext=(0.95, -0.98),
                 fontsize=8.3, ha="center",
                 arrowprops=dict(arrowstyle="->", lw=0.75, color="#333333"))

    ax2.set_xlim(-1.60, 1.56)
    ax2.set_ylim(-1.42, 1.48)
    ax2.set_aspect("equal")
    ax2.axis("off")
    ax2.set_title("外电场下费米球平移（索末菲模型）", fontsize=10.5, pad=6)

    plt.tight_layout(pad=0.8)
    fig.savefig(os.path.join(OUT_DIR, "ch04-contact-transport.svg"), format="svg", bbox_inches="tight")
    if preview_dir:
        fig.savefig(os.path.join(preview_dir, "ch04-contact-transport.png"), dpi=160, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    import sys
    pdir = sys.argv[1] if len(sys.argv) > 1 else None
    if pdir:
        os.makedirs(pdir, exist_ok=True)
    fig1_fermi_dos(pdir)
    fig2_contact_transport(pdir)
    print("Generated 2 SVG figures for Chapter 4 in", OUT_DIR)
