"""Generate clean monochrome academic SVG diagrams for Chapter 1."""
import os
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, FancyArrowPatch

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


def project_3d(pt):
    """Simple isometric-like 3D projection: x right-down, y right-up, z up."""
    x, y, z = pt
    u = 0.88 * y - 0.50 * x
    v = 0.96 * z - 0.28 * x + 0.16 * y
    return np.array([u, v])


def draw_cube_edges(ax, lw=0.9, color="#888888"):
    corners = [(i, j, k) for i in (0, 1) for j in (0, 1) for k in (0, 1)]
    edges = []
    for c1 in corners:
        for c2 in corners:
            if sum(abs(a - b) for a, b in zip(c1, c2)) == 1 and c1 < c2:
                edges.append((c1, c2))
    # Back edges connected to (0,0,0) dashed
    for c1, c2 in edges:
        p1, p2 = project_3d(c1), project_3d(c2)
        is_back = (c1 == (0, 0, 0))
        ax.plot([p1[0], p2[0]], [p1[1], p2[1]],
                color=color, lw=lw, ls="--" if is_back else "-", zorder=1)


def draw_arrow_2d(ax, p0, p1, color="#111111", lw=1.8, zorder=5):
    arr = FancyArrowPatch(
        (p0[0], p0[1]), (p1[0], p1[1]),
        arrowstyle="-|>,head_length=6,head_width=3.5",
        color=color, lw=lw, zorder=zorder, shrinkA=0, shrinkB=2
    )
    ax.add_patch(arr)


def fig1_primitive_cells():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.4, 3.8))
    for ax in (ax1, ax2):
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_xlim(-0.78, 1.18)
        ax.set_ylim(-0.48, 1.32)

    # --- Left: BCC primitive vectors ---
    draw_cube_edges(ax1)
    # Corner lattice points
    for i in (0, 1):
        for j in (0, 1):
            for k in (0, 1):
                p = project_3d((i, j, k))
                ax1.scatter([p[0]], [p[1]], s=34, facecolors="#ffffff",
                            edgecolors="#111111", lw=1.1, zorder=4)
    # Body center
    pc = project_3d((0.5, 0.5, 0.5))
    ax1.scatter([pc[0]], [pc[1]], s=48, color="#111111", zorder=6)

    # Draw origin at (0,0,0) -> arrows to adjacent centers or from (0.5,0.5,0.5)
    # Using classic Huang Kun origin at (0,0,0) with body centers of neighbor cubes is messy;
    # cleaner: put origin at (0,0,0) for fcc, and for bcc put origin at (0,0,0) with 3 vectors:
    # Actually placing origin at (0,0,0) -> (1/2,1/2,1/2) plus (-1/2,1/2,1/2), (1/2,-1/2,1/2)
    # Even cleaner & textbook standard: origin at cube corner (1,0,0) or center (0.5,0.5,0.5)
    # Let's draw origin at (0,0,0) and highlight body center (0.5,0.5,0.5) plus 3 vectors from (0,0,0):
    # Wait: best textbook view (Kittel / Huang Kun):
    # Origin at (0,0,0) -> a1=(0.5,0.5,-0.5)? No, origin at (0,0,0) for BCC ->
    # Draw origin at (0.5, 0.5, 0.5) -> to (1,1,1)? No, standard vector signs are:
    # a1 = a/2(-x+y+z), a2 = a/2(x-y+z), a3 = a/2(x+y-z).
    # From corner (0.5,0.5,0.5) going to: (0,1,1), (1,0,1), (1,1,0) — ALL THREE ARE INSIDE THE SINGLE CUBE!!
    # Check: (0,1,1)-(0.5,0.5,0.5) = (-0.5, +0.5, +0.5) = a1 !!
    #        (1,0,1)-(0.5,0.5,0.5) = (+0.5, -0.5, +0.5) = a2 !!
    #        (1,1,0)-(0.5,0.5,0.5) = (+0.5, +0.5, -0.5) = a3 !!
    # THAT'S BRILLIANT! All 3 exact Huang Kun BCC primitive vectors lie cleanly inside one cube!
    targets_bcc = [
        ((0, 1, 1), r"$\mathbf{a}_1$", (0.06, -0.09)),
        ((1, 0, 1), r"$\mathbf{a}_2$", (-0.08, 0.08)),
        ((1, 1, 0), r"$\mathbf{a}_3$", (-0.15, -0.04)),
    ]
    for tgt, label, offset in targets_bcc:
        pt = project_3d(tgt)
        draw_arrow_2d(ax1, pc, pt)
        ax1.scatter([pt[0]], [pt[1]], s=42, color="#111111", zorder=6)
        mid = 0.58 * pt + 0.42 * pc
        ax1.text(mid[0] + offset[0], mid[1] + offset[1], label, fontsize=11)

    ax1.text(pc[0] - 0.10, pc[1] - 0.12, r"$O$", fontsize=10)
    # Coordinate triad hint
    p0 = project_3d((0, 0, 0))
    for vec, lab, off in [((1, 0, 0), r"$x$", (-0.09, -0.06)),
                          ((0, 1, 0), r"$y$", (0.07, 0.02)),
                          ((0, 0, 1), r"$z$", (-0.06, 0.07))]:
        pv = project_3d(vec)
        ax1.text(pv[0] + off[0], pv[1] + off[1], lab, fontsize=9.5, color="#555555")
    ax1.set_title("bcc 惯用胞与原胞基矢", fontsize=11, pad=6)

    # --- Right: FCC primitive vectors ---
    draw_cube_edges(ax2)
    for i in (0, 1):
        for j in (0, 1):
            for k in (0, 1):
                p = project_3d((i, j, k))
                ax2.scatter([p[0]], [p[1]], s=34, facecolors="#ffffff",
                            edgecolors="#111111", lw=1.1, zorder=4)
    # Face centers
    fcs = [(0.5, 0.5, 0), (0.5, 0, 0.5), (0, 0.5, 0.5),
           (0.5, 0.5, 1), (0.5, 1, 0.5), (1, 0.5, 0.5)]
    for fc in fcs:
        p = project_3d(fc)
        ax2.scatter([p[0]], [p[1]], s=28, facecolors="#dddddd",
                    edgecolors="#555555", lw=0.9, zorder=4)

    po = project_3d((0, 0, 0))
    ax2.scatter([po[0]], [po[1]], s=48, color="#111111", zorder=6)
    targets_fcc = [
        ((0, 0.5, 0.5), r"$\mathbf{a}_1$", (-0.14, 0.06)),
        ((0.5, 0, 0.5), r"$\mathbf{a}_2$", (-0.15, 0.03)),
        ((0.5, 0.5, 0), r"$\mathbf{a}_3$", (0.02, -0.14)),
    ]
    for tgt, label, offset in targets_fcc:
        pt = project_3d(tgt)
        draw_arrow_2d(ax2, po, pt)
        ax2.scatter([pt[0]], [pt[1]], s=42, color="#111111", zorder=6)
        mid = 0.60 * pt + 0.40 * po
        ax2.text(mid[0] + offset[0], mid[1] + offset[1], label, fontsize=11)

    ax2.text(po[0] - 0.14, po[1] - 0.10, r"$O$", fontsize=10)
    for vec, lab, off in [((1, 0, 0), r"$x$", (-0.09, -0.06)),
                          ((0, 1, 0), r"$y$", (0.07, 0.02)),
                          ((0, 0, 1), r"$z$", (-0.06, 0.07))]:
        pv = project_3d(vec)
        ax2.text(pv[0] + off[0], pv[1] + off[1], lab, fontsize=9.5, color="#555555")
    ax2.set_title("fcc 惯用胞与原胞基矢", fontsize=11, pad=6)

    plt.tight_layout(pad=0.6)
    fig.savefig(os.path.join(OUT_DIR, "ch01-primitive-cells.svg"), format="svg", bbox_inches="tight")
    plt.close(fig)


def fig2_brillouin_2d():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.4, 3.9))

    # --- Left: 2D Square Lattice 1st & 2nd BZ ---
    ax1.set_aspect("equal")
    ax1.set_xlim(-1.45, 1.45)
    ax1.set_ylim(-1.45, 1.45)
    ax1.axis("off")

    # Axes
    ax1.annotate("", xy=(1.38, 0), xytext=(-1.38, 0),
                 arrowprops=dict(arrowstyle="->", lw=0.8, color="#777777"))
    ax1.annotate("", xy=(0, 1.38), xytext=(0, -1.38),
                 arrowprops=dict(arrowstyle="->", lw=0.8, color="#777777"))
    ax1.text(1.32, -0.14, r"$k_x$", fontsize=10, color="#444444")
    ax1.text(0.06, 1.30, r"$k_y$", fontsize=10, color="#444444")

    # 2nd BZ (rotated square with vertices at (+-1, 0), (0, +-1) in units of 2pi/a?
    # Units: let b = 2pi/a = 1.0, so nearest G = (+-1, 0), (0, +-1);
    # 1st BZ is square [-0.5, 0.5]^2;
    # 2nd BZ outer diamond has vertices (+-1, 0), (0, +-1)!
    # Check area: 1st BZ area = 1*1 = 1; outer diamond area = 0.5*2*2 = 2 -> 2nd BZ area = 2 - 1 = 1! Exact!
    bz2_poly = Polygon([(1, 0), (0, 1), (-1, 0), (0, -1)],
                       closed=True, facecolor="#efefef", edgecolor="#222222", lw=1.1, ls="--", zorder=1)
    ax1.add_patch(bz2_poly)

    bz1_poly = Polygon([(-0.5, -0.5), (0.5, -0.5), (0.5, 0.5), (-0.5, 0.5)],
                       closed=True, facecolor="#d6d6d6", edgecolor="#111111", lw=1.6, zorder=2)
    ax1.add_patch(bz1_poly)

    # Reciprocal lattice points
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            ax1.scatter([i], [j], s=26, color="#111111", zorder=5)

    # High symmetry points Gamma, X, M
    ax1.scatter([0.5, 0.5], [0, 0.5], s=28, facecolors="#ffffff", edgecolors="#111111", lw=1.2, zorder=6)
    ax1.text(-0.14, -0.14, r"$\Gamma$", fontsize=10.5, zorder=7)
    ax1.text(0.55, -0.14, r"$X$", fontsize=10.5, zorder=7)
    ax1.text(0.54, 0.54, r"$M$", fontsize=10.5, zorder=7)
    ax1.text(0.5, -0.68, r"$\frac{\pi}{a}$", fontsize=9.5, ha="center", color="#333333")
    ax1.text(1.03, -0.16, r"$\frac{2\pi}{a}$", fontsize=9.5, color="#333333")
    ax1.text(-0.24, 0.24, "1st BZ", fontsize=9, ha="center", va="center", zorder=6)
    ax1.text(0.20, 0.66, "2nd", fontsize=8.5, ha="center", va="center", zorder=6)
    ax1.set_title("二维正方晶格第一、二布里渊区", fontsize=11, pad=6)

    # --- Right: 2D Hexagonal Lattice 1st BZ ---
    ax2.set_aspect("equal")
    ax2.set_xlim(-1.45, 1.45)
    ax2.set_ylim(-1.45, 1.45)
    ax2.axis("off")

    ax2.annotate("", xy=(1.38, 0), xytext=(-1.38, 0),
                 arrowprops=dict(arrowstyle="->", lw=0.8, color="#777777"))
    ax2.annotate("", xy=(0, 1.38), xytext=(0, -1.38),
                 arrowprops=dict(arrowstyle="->", lw=0.8, color="#777777"))
    ax2.text(1.32, -0.14, r"$k_x$", fontsize=10, color="#444444")
    ax2.text(0.06, 1.30, r"$k_y$", fontsize=10, color="#444444")

    # 6 nearest reciprocal lattice vectors at angles 30, 90, 150, 210, 270, 330 deg, length b = 1.0
    angles_G = [math.radians(30 + 60 * m) for m in range(6)]
    G_pts = [(math.cos(t), math.sin(t)) for t in angles_G]

    # 1st BZ hexagon vertices at angles 0, 60, ..., 300 deg, radius R = (b/2)/cos(30) = 1/sqrt(3)
    R_hex = 1.0 / math.sqrt(3)
    hex_verts = [(R_hex * math.cos(math.radians(60 * m)),
                  R_hex * math.sin(math.radians(60 * m))) for m in range(6)]
    bz1_hex = Polygon(hex_verts, closed=True, facecolor="#d6d6d6", edgecolor="#111111", lw=1.6, zorder=2)
    ax2.add_patch(bz1_hex)

    # Dashed bisector lines & G vectors
    for gx, gy in G_pts:
        ax2.scatter([gx], [gy], s=26, color="#111111", zorder=5)
        ax2.plot([0, gx], [0, gy], color="#999999", lw=0.75, ls=":", zorder=1)
    ax2.scatter([0], [0], s=26, color="#111111", zorder=5)

    # Highlight b1, b2
    draw_arrow_2d(ax2, np.array([0, 0]), np.array(G_pts[0]), lw=1.3, zorder=5)
    draw_arrow_2d(ax2, np.array([0, 0]), np.array(G_pts[1]), lw=1.3, zorder=5)
    ax2.text(G_pts[0][0] + 0.06, G_pts[0][1] + 0.02, r"$\mathbf{b}_1$", fontsize=10.5)
    ax2.text(G_pts[1][0] + 0.07, G_pts[1][1] - 0.02, r"$\mathbf{b}_2$", fontsize=10.5)

    # Gamma, K, M
    k_pt = hex_verts[0]
    m_pt = (0.5 * G_pts[0][0], 0.5 * G_pts[0][1])
    ax2.scatter([k_pt[0], m_pt[0]], [k_pt[1], m_pt[1]],
                s=28, facecolors="#ffffff", edgecolors="#111111", lw=1.2, zorder=6)
    ax2.text(-0.16, -0.14, r"$\Gamma$", fontsize=10.5, zorder=7)
    ax2.text(k_pt[0] + 0.06, k_pt[1] - 0.13, r"$K$", fontsize=10.5, zorder=7)
    ax2.text(m_pt[0] + 0.05, m_pt[1] - 0.12, r"$M$", fontsize=10.5, zorder=7)
    ax2.text(0.0, -0.25, "1st BZ", fontsize=9, ha="center", va="center", zorder=6)
    ax2.set_title("二维六角晶格第一布里渊区", fontsize=11, pad=6)

    plt.tight_layout(pad=0.6)
    fig.savefig(os.path.join(OUT_DIR, "ch01-brillouin-2d.svg"), format="svg", bbox_inches="tight")
    plt.close(fig)


def fig3_ewald_bragg():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.4, 3.6))

    # --- Left: Bragg diffraction geometry ---
    ax1.set_aspect("equal")
    ax1.set_xlim(-2.2, 2.2)
    ax1.set_ylim(-1.25, 1.45)
    ax1.axis("off")

    # Crystal planes
    for y in (0.0, -0.65):
        ax1.plot([-1.9, 1.9], [y, y], color="#888888", lw=0.9, ls="--", zorder=1)
        for x in np.linspace(-1.5, 1.5, 5):
            ax1.scatter([x], [y], s=26, color="#111111", zorder=4)

    # Spacing d marker
    ax1.annotate("", xy=(-1.78, 0.0), xytext=(-1.78, -0.65),
                 arrowprops=dict(arrowstyle="<->", lw=1.0, color="#333333"))
    ax1.text(-1.98, -0.36, r"$d$", fontsize=11)

    # Incident and reflected rays (theta = 32 deg)
    th = math.radians(32)
    L = 1.65
    # Ray 1 hitting (0, 0)
    p1_in = (-L * math.cos(th), L * math.sin(th))
    p1_out = (L * math.cos(th), L * math.sin(th))
    draw_arrow_2d(ax1, np.array(p1_in), np.array([0, 0]), lw=1.4)
    draw_arrow_2d(ax1, np.array([0, 0]), np.array(p1_out), lw=1.4)

    # Ray 2 hitting (0, -0.65)
    y2 = -0.65
    p2_in = (-L * math.cos(th), y2 + L * math.sin(th))
    p2_out = (L * math.cos(th), y2 + L * math.sin(th))
    draw_arrow_2d(ax1, np.array(p2_in), np.array([0, y2]), lw=1.4)
    draw_arrow_2d(ax1, np.array([0, y2]), np.array(p2_out), lw=1.4)

    # Perpendiculars from (0,0) onto ray 2 to show extra path 2 d sin(theta)
    d_val = 0.65
    # Foot on incoming ray 2: unit vector along incoming ray toward (0, y2) is (cos th, -sin th)
    # Vector from (0, y2) to (0, 0) is (0, d); projection along incoming direction (-cos th, sin th) is d sin th
    foot_in = np.array([-d_val * math.sin(th) * math.cos(th), y2 + d_val * math.sin(th) ** 2])
    foot_out = np.array([d_val * math.sin(th) * math.cos(th), y2 + d_val * math.sin(th) ** 2])
    ax1.plot([0, foot_in[0]], [0, foot_in[1]], color="#444444", lw=0.9, ls=":")
    ax1.plot([0, foot_out[0]], [0, foot_out[1]], color="#444444", lw=0.9, ls=":")
    # Highlight extra path segment
    ax1.plot([foot_in[0], 0, foot_out[0]], [foot_in[1], y2, foot_out[1]], color="#111111", lw=2.3, zorder=3)

    # Angle labels
    ax1.text(-0.68, 0.12, r"$\theta$", fontsize=10.5)
    ax1.text(0.56, 0.12, r"$\theta$", fontsize=10.5)
    ax1.text(0.0, -1.00, r"光程差 $= 2d\sin\theta = n\lambda$", fontsize=10, ha="center")
    ax1.set_title("实空间：布拉格反射几何", fontsize=11, pad=6)

    # --- Right: Ewald Sphere ---
    ax2.set_aspect("equal")
    ax2.set_xlim(-1.95, 1.95)
    ax2.set_ylim(-1.35, 1.35)
    ax2.axis("off")

    # Reciprocal lattice grid
    for gx in np.linspace(-1.4, 1.4, 5):
        for gy in np.linspace(-0.7, 0.7, 3):
            ax2.scatter([gx], [gy], s=18, color="#888888", zorder=2)

    # Origin O at (0.7, -0.7)? Better: O at (0.7, 0.0), center C at (-0.35, 0.0), radius R = 1.05
    # Choose G point on circle: say O = (0.7, -0.35), G_pt = (0.0, 0.7) -> check circle passing through O and G_pt!
    # Cleanest exact geometry: reciprocal grid spacing = 0.7
    # O = (0.7, 0.0), P = (0.0, 0.7) => midpoint (0.35, 0.35), perp bisector is y = x.
    # Choose sphere center C = (-0.2, -0.2): dist to O = sqrt(0.9^2 + 0.2^2) = sqrt(0.85) = 0.922
    # dist to P(0, 0.7) = sqrt(0.2^2 + 0.9^2) = sqrt(0.85) = 0.922! Exact!
    O = np.array([0.7, 0.0])
    P = np.array([0.0, 0.7])
    C = np.array([-0.2, -0.2])
    R = np.linalg.norm(O - C)

    circ = Circle((C[0], C[1]), R, facecolor="none", edgecolor="#333333", lw=1.2, ls="--", zorder=2)
    ax2.add_patch(circ)

    ax2.scatter([O[0], P[0]], [O[1], P[1]], s=38, color="#111111", zorder=6)
    ax2.scatter([C[0]], [C[1]], s=26, facecolors="#ffffff", edgecolors="#111111", lw=1.2, zorder=6)

    draw_arrow_2d(ax2, C, O, lw=1.6, zorder=5)
    draw_arrow_2d(ax2, C, P, lw=1.6, zorder=5)
    draw_arrow_2d(ax2, O, P, lw=1.8, color="#111111", zorder=6)

    ax2.text(O[0] + 0.08, O[1] - 0.14, r"$O$", fontsize=10.5)
    ax2.text(P[0] - 0.05, P[1] + 0.12, r"$\mathbf{G}$", fontsize=10.5)
    ax2.text(C[0] - 0.16, C[1] - 0.12, r"$C$", fontsize=10.5)
    ax2.text(0.26, -0.26, r"$\mathbf{k}$", fontsize=10.5)
    ax2.text(-0.28, 0.32, r"$\mathbf{k}'$", fontsize=10.5)
    ax2.text(0.56, 0.44, r"$\Delta\mathbf{k}=\mathbf{G}$", fontsize=10)
    ax2.text(0.0, -1.26, r"$|\mathbf{k}| = |\mathbf{k}'| = 2\pi/\lambda,\ \mathbf{k}' - \mathbf{k} = \mathbf{G}$",
             fontsize=10, ha="center")
    ax2.set_title("倒空间：厄瓦尔德球作图", fontsize=11, pad=6)

    plt.tight_layout(pad=0.6)
    fig.savefig(os.path.join(OUT_DIR, "ch01-ewald-bragg.svg"), format="svg", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    fig1_primitive_cells()
    fig2_brillouin_2d()
    fig3_ewald_bragg()
    print("Generated 3 SVG figures in", OUT_DIR)
