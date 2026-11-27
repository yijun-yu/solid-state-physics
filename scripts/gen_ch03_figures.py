"""Generate clean monochrome academic SVG diagrams for Chapter 3 (Lattice Vibrations)."""
import os
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

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


def fig1_dispersion_chains():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.8, 3.8))

    # --- Left: 1D Monatomic chain ---
    qa = np.linspace(-1.25 * math.pi, 1.25 * math.pi, 500)
    w_mono = 2.0 * np.abs(np.sin(qa / 2.0))
    qa_bz = np.linspace(-math.pi, math.pi, 400)
    w_mono_bz = 2.0 * np.abs(np.sin(qa_bz / 2.0))

    # Shaded 1st BZ
    ax1.axvspan(-math.pi, math.pi, color="#f2f2f2", zorder=0)
    ax1.axvline(-math.pi, color="#666666", lw=0.9, ls="--", zorder=1)
    ax1.axvline(math.pi, color="#666666", lw=0.9, ls="--", zorder=1)
    ax1.axvline(0, color="#666666", lw=0.8, zorder=1)

    # Periodic continuation dashed outside 1st BZ
    ax1.plot(qa, w_mono, color="#888888", lw=1.0, ls=":", zorder=2)
    ax1.plot(qa_bz, w_mono_bz, color="#111111", lw=1.9, zorder=3)

    # Long-wavelength linear tangent omega = v_s q
    q_lin = np.linspace(0, 1.65, 100)
    ax1.plot(q_lin, q_lin, color="#444444", lw=1.0, ls="--", zorder=2)
    ax1.text(1.42, 1.05, r"$\omega = v_s q$", fontsize=9.2, color="#333333")

    # Max frequency line
    ax1.axhline(2.0, color="#888888", lw=0.8, ls=":")
    ax1.scatter([math.pi, -math.pi], [2.0, 2.0], s=26, color="#111111", zorder=5)
    ax1.text(0.12, 2.10, r"$\omega_m = 2\sqrt{\beta/m}$", fontsize=9.2, ha="left")
    ax1.text(-1.65, 2.18, "1st BZ", fontsize=8.8, ha="center", color="#555555")

    ax1.set_xlim(-1.25 * math.pi, 1.25 * math.pi)
    ax1.set_ylim(0, 2.48)
    ax1.set_xticks([-math.pi, 0, math.pi])
    ax1.set_xticklabels([r"$-\frac{\pi}{a}$", r"$0$", r"$\frac{\pi}{a}$"], fontsize=10)
    ax1.set_yticks([])
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    ax1.set_xlabel(r"波矢 $q$", fontsize=10)
    ax1.set_ylabel(r"角频率 $\omega$", fontsize=10)
    ax1.set_title("一维单原子链色散关系", fontsize=10.5, pad=8)

    # --- Right: 1D Diatomic chain (M = 2.5 m, beta = 1, m = 1) ---
    m_val, M_val = 1.0, 2.5
    qa2 = np.linspace(-math.pi / 2, math.pi / 2, 400)  # qa where lattice period is 2a
    s = (1 / m_val + 1 / M_val)
    disc = np.sqrt(np.maximum(0.0, s ** 2 - 4 * (np.sin(qa2) ** 2) / (m_val * M_val)))
    w_opt = np.sqrt(s + disc)
    w_ac = np.sqrt(s - disc)

    w_opt_0 = math.sqrt(2 * s)
    w_opt_b = math.sqrt(2 / m_val)
    w_ac_b = math.sqrt(2 / M_val)

    ax2.axvspan(-math.pi / 2, math.pi / 2, color="#f2f2f2", zorder=0)
    ax2.fill_between([-math.pi / 2, math.pi / 2], w_ac_b, w_opt_b, color="#e4e4e4", zorder=1)
    ax2.axvline(-math.pi / 2, color="#666666", lw=0.9, ls="--", zorder=2)
    ax2.axvline(math.pi / 2, color="#666666", lw=0.9, ls="--", zorder=2)
    ax2.axvline(0, color="#666666", lw=0.8, zorder=2)

    ax2.plot(qa2, w_opt, color="#111111", lw=1.9, zorder=4)
    ax2.plot(qa2, w_ac, color="#111111", lw=1.9, zorder=4)

    # Key points
    ax2.scatter([0, math.pi / 2, math.pi / 2], [w_opt_0, w_opt_b, w_ac_b], s=26, color="#111111", zorder=5)
    ax2.text(0.08, w_opt_0 + 0.08, r"$\sqrt{2\beta(\frac{1}{m}+\frac{1}{M})}$", fontsize=8.8, ha="left")
    ax2.text(math.pi / 2 + 0.06, w_opt_b, r"$\sqrt{\frac{2\beta}{m}}$", fontsize=9.0, va="center", ha="left")
    ax2.text(math.pi / 2 + 0.06, w_ac_b, r"$\sqrt{\frac{2\beta}{M}}$", fontsize=9.0, va="center", ha="left")

    ax2.text(-0.92, w_opt_0 + 0.02, "光学支", fontsize=9.2, ha="center")
    ax2.text(-1.05, 0.25, "声学支", fontsize=9.2, ha="center")
    ax2.text(0.0, 0.5 * (w_opt_b + w_ac_b), "频率禁带", fontsize=9.0, ha="center", va="center", color="#333333")

    ax2.set_xlim(-0.72 * math.pi, 0.78 * math.pi)
    ax2.set_ylim(0, w_opt_0 + 0.42)
    ax2.set_xticks([-math.pi / 2, 0, math.pi / 2])
    ax2.set_xticklabels([r"$-\frac{\pi}{2a}$", r"$0$", r"$\frac{\pi}{2a}$"], fontsize=10)
    ax2.set_yticks([])
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    ax2.set_xlabel(r"波矢 $q$", fontsize=10)
    ax2.set_ylabel(r"角频率 $\omega$", fontsize=10)
    ax2.set_title(r"一维双原子链色散关系（$M > m$）", fontsize=10.5, pad=8)

    plt.tight_layout(pad=0.8)
    fig.savefig(os.path.join(OUT_DIR, "ch03-dispersion-chains.svg"), format="svg", bbox_inches="tight")
    plt.close(fig)


def debye_cv_ratio(t_ratio):
    """Return C_V / (3 N k_B) for Debye model at t_ratio = T / Theta_D."""
    res = np.zeros_like(t_ratio)
    for i, t in enumerate(t_ratio):
        if t < 1e-4:
            res[i] = 0.0
            continue
        x_max = 1.0 / t
        xs = np.linspace(1e-6, min(x_max, 60.0), 4000)
        integrand = (xs ** 4) * np.exp(xs) / ((np.exp(xs) - 1.0) ** 2)
        res[i] = 3.0 * (t ** 3) * np.trapezoid(integrand, xs)
    return res


def einstein_cv_ratio(t_ratio):
    """Return C_V / (3 N k_B) for Einstein model at t_ratio = T / Theta_E (scaled Theta_E = 0.75 Theta_D for visual match at mid-T)."""
    res = np.zeros_like(t_ratio)
    for i, t in enumerate(t_ratio):
        x = 1.0 / t
        if x > 60.0:
            res[i] = 0.0
        else:
            ex = math.exp(x)
            res[i] = (x ** 2) * ex / ((ex - 1.0) ** 2)
    return res


def fig2_heat_capacity():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.8, 3.7))

    # --- Left: Dulong-Petit vs Debye vs Einstein ---
    t = np.linspace(0.015, 1.6, 220)
    cv_deb = debye_cv_ratio(t)
    # Use same T/Theta_D horizontal axis; standard comparison uses Theta_E = Theta_D (or 0.75 Theta_D)
    # Using T/Theta with Theta_E = Theta_D shows clearly why Einstein drops faster at low T
    cv_ein = einstein_cv_ratio(t)
    # Low-T Debye T^3 reference curve up to t=0.28
    t_low = np.linspace(0.0, 0.29, 80)
    cv_t3 = (4 * math.pi ** 4 / 5.0) * (t_low ** 3)

    ax1.axhline(1.0, color="#666666", lw=1.0, ls=":", label=r"杜隆-珀蒂定律 ($3Nk_B$)")
    ax1.plot(t, cv_deb, color="#111111", lw=1.9, label=r"德拜模型 ($T/\Theta_D$)")
    ax1.plot(t, cv_ein, color="#555555", lw=1.35, ls="--", label=r"爱因斯坦模型 ($T/\Theta_E$)")
    ax1.plot(t_low, cv_t3, color="#222222", lw=1.0, ls="-.", label=r"低温 $T^3$ 近似")

    ax1.set_xlim(0, 1.6)
    ax1.set_ylim(0, 1.15)
    ax1.set_xticks([0, 0.2, 0.5, 1.0, 1.5])
    ax1.set_yticks([0, 0.5, 1.0])
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)
    ax1.set_xlabel(r"无量纲温度 $T/\Theta$", fontsize=10)
    ax1.set_ylabel(r"相对热容 $C_V / (3Nk_B)$", fontsize=10)
    ax1.legend(loc="lower right", frameon=False, fontsize=8.5)
    ax1.set_title("晶格热容模型对比", fontsize=10.5, pad=8)

    # --- Right: Phonon DOS g(omega) Debye vs Einstein vs real schematic ---
    w = np.linspace(0, 1.0, 300)
    g_deb = 3.0 * (w ** 2)  # normalized so integral from 0 to 1 is 1 (represents 3N)

    # Schematic realistic acoustic DOS (van Hove peaks) with same area = 1
    w_real = np.linspace(0, 1.15, 400)
    g_raw = (2.6 * w_real ** 2) * np.exp(-((w_real - 0.62) / 0.24) ** 2) \
            + 1.5 * np.exp(-((w_real - 0.52) / 0.07) ** 2) * (w_real < 0.7) \
            + 1.1 * np.exp(-((w_real - 0.92) / 0.08) ** 2) * (w_real < 1.08)
    # Ensure exact quadratic onset at small w and zero at w > 1.08
    g_raw = np.where(w_real < 1.08, g_raw, 0.0)
    g_real = g_raw / np.trapezoid(g_raw, w_real)

    ax2.fill_between(w, 0, g_deb, color="#ececec", zorder=1)
    ax2.plot(w, g_deb, color="#111111", lw=1.8, label=r"德拜态密度 $g(\omega) \propto \omega^2$", zorder=3)
    ax2.plot([1.0, 1.0], [0, 3.0], color="#111111", lw=1.5, ls="-", zorder=3)
    ax2.plot(w_real, g_real, color="#555555", lw=1.2, ls="--", label="真实晶体声学支示意", zorder=2)

    # Einstein delta spike at w_E = 0.75
    ax2.annotate("", xy=(0.75, 2.75), xytext=(0.75, 0.0),
                 arrowprops=dict(arrowstyle="-|>", lw=1.4, color="#333333"))
    ax2.text(0.75, 2.86, r"爱因斯坦 $\delta(\omega-\omega_E)$", fontsize=8.6, ha="center")

    ax2.text(0.60, 0.38, r"面积 $= 3N$", fontsize=9.0, ha="center")
    ax2.set_xlim(0, 1.25)
    ax2.set_ylim(0, 3.45)
    ax2.set_xticks([0, 0.75, 1.0])
    ax2.set_xticklabels([r"$0$", r"$\omega_E$", r"$\omega_D$"], fontsize=10)
    ax2.set_yticks([])
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)
    ax2.set_xlabel(r"角频率 $\omega$", fontsize=10)
    ax2.set_ylabel(r"模式态密度 $g(\omega)$", fontsize=10)
    ax2.legend(loc="upper left", frameon=False, fontsize=8.4)
    ax2.set_title("三维声子态密度模型对比", fontsize=10.5, pad=8)

    plt.tight_layout(pad=0.8)
    fig.savefig(os.path.join(OUT_DIR, "ch03-heat-capacity.svg"), format="svg", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    fig1_dispersion_chains()
    fig2_heat_capacity()
    print("Generated 2 SVG figures for Chapter 3 in", OUT_DIR)
