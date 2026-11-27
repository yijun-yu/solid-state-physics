"""Numerical and symbolic verification for Chapter 1 (Crystal Structure)."""
import math
import numpy as np

print("=== CH01-KP1-05: Diamond packing & Silicon ===")
pf_diamond = math.sqrt(3) * math.pi / 16
a_si = 5.43  # Angstrom
d_nn_si = math.sqrt(3) / 4 * a_si
n_si_cm3 = 8 / ((a_si * 1e-8) ** 3)
print(f"Diamond packing factor: {pf_diamond:.6f} ({pf_diamond*100:.2f}%)")
print(f"Si nearest-neighbor distance: {d_nn_si:.4f} A")
print(f"Si atomic density: {n_si_cm3:.4e} cm^-3")

print("\n=== CH01-KP1-06: HCP ideal c/a and packing ===")
c_over_a = math.sqrt(8 / 3)
pf_hcp = math.sqrt(2) * math.pi / 6
print(f"Ideal c/a: {c_over_a:.4f}")
print(f"HCP/FCC packing factor: {pf_hcp:.6f} ({pf_hcp*100:.2f}%)")

print("\n=== CH01-KP2-04: FCC planar density & spacing ===")
# For FCC conventional cell (side a):
# (100): 2 atoms / a^2, d_200 = a/2 (effective spacing between adjacent atomic planes)
# (110): 2 atoms / (sqrt(2) a^2) = sqrt(2)/a^2, d_220 = a/(2*sqrt(2)) = sqrt(2)a/4
# (111): 2 atoms / (sqrt(3)/2 * a^2) = 4/(sqrt(3) a^2) = 2.3094/a^2, d_111 = a/sqrt(3)
print(f"rho_100 * a^2 = {2.0:.4f}, d_eff/a = {0.5:.4f}")
print(f"rho_110 * a^2 = {math.sqrt(2):.4f}, d_eff/a = {1/(2*math.sqrt(2)):.4f}")
print(f"rho_111 * a^2 = {4/math.sqrt(3):.4f}, d_eff/a = {1/math.sqrt(3):.4f}")

print("\n=== CH01-KP2-05: Angle between (111) and (110), zone axis ===")
n1 = np.array([1, 1, 1])
n2 = np.array([1, 1, 0])
cos_theta = np.dot(n1, n2) / (np.linalg.norm(n1) * np.linalg.norm(n2))
theta_deg = math.degrees(math.acos(cos_theta))
zone = np.cross(n1, n2)
print(f"cos(theta) = {cos_theta:.6f} (sqrt(2/3)={math.sqrt(2/3):.6f}), theta = {theta_deg:.2f} deg")
print(f"Zone axis [111] x [110] = {zone} (or [-1, 1, 0])")

print("\n=== CH01-KP4-04: BCC primitive -> FCC reciprocal ===")
a = 1.0
a1 = (a / 2) * np.array([-1, 1, 1])
a2 = (a / 2) * np.array([1, -1, 1])
a3 = (a / 2) * np.array([1, 1, -1])
omega = abs(np.dot(a1, np.cross(a2, a3)))
b1 = 2 * math.pi * np.cross(a2, a3) / np.dot(a1, np.cross(a2, a3))
b2 = 2 * math.pi * np.cross(a3, a1) / np.dot(a1, np.cross(a2, a3))
b3 = 2 * math.pi * np.cross(a1, a2) / np.dot(a1, np.cross(a2, a3))
omega_star = abs(np.dot(b1, np.cross(b2, b3)))
print(f"Omega = {omega:.4f} a^3 (expected 0.5)")
print(f"b1 / (2pi/a) = {b1 / (2*math.pi/a)}")
print(f"b2 / (2pi/a) = {b2 / (2*math.pi/a)}")
print(f"b3 / (2pi/a) = {b3 / (2*math.pi/a)}")
print(f"Omega* / (pi^3/a^3) = {omega_star / (math.pi**3):.4f} (expected 16)")
# Verify a_i . b_j = 2pi delta_ij
A = np.vstack([a1, a2, a3])
B = np.vstack([b1, b2, b3])
assert np.allclose(A @ B.T, 2 * math.pi * np.eye(3))
print("Orthogonality a_i . b_j = 2pi delta_ij verified.")

print("\n=== CH01-KP5-04: Structure factor verification ===")
fcc_basis = [(0, 0, 0), (0.5, 0.5, 0), (0.5, 0, 0.5), (0, 0.5, 0.5)]
diamond_basis = fcc_basis + [(x + 0.25, y + 0.25, z + 0.25) for x, y, z in fcc_basis]
for hkl in [(1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 0, 0), (2, 2, 0), (3, 1, 1), (2, 2, 2), (4, 0, 0)]:
    h, k, l = hkl
    s_fcc = sum(np.exp(-1j * 2 * math.pi * (h*x + k*y + l*z)) for x, y, z in fcc_basis)
    s_dia = sum(np.exp(-1j * 2 * math.pi * (h*x + k*y + l*z)) for x, y, z in diamond_basis)
    print(f"({h}{k}{l}): |S_fcc|={abs(s_fcc):.2f}, |S_dia|={abs(s_dia):.2f}")

print("\n=== CH01-KP5-05: Copper (FCC) powder XRD indexing ===")
lam = 1.5418  # Cu K_alpha in Angstrom
a_cu = 3.615  # Angstrom
hkls = [(1, 1, 1), (2, 0, 0), (2, 2, 0), (3, 1, 1)]
sin2_vals = []
for h, k, l in hkls:
    N = h*h + k*k + l*l
    d = a_cu / math.sqrt(N)
    sin_th = lam / (2 * d)
    th = math.degrees(math.asin(sin_th))
    two_th = 2 * th
    sin2_vals.append(sin_th ** 2)
    print(f"({h}{k}{l}) N={N:2d}: d={d:.4f} A, 2theta={two_th:.2f} deg, sin^2(theta)={sin_th**2:.4f}")

# Check reconstructed a from rounded 2theta values (2 decimals)
two_thetas_given = [43.35, 50.49, 74.19, 90.03]
ratios = []
a_est = []
for t2, (h, k, l) in zip(two_thetas_given, hkls):
    s2 = math.sin(math.radians(t2 / 2)) ** 2
    ratios.append(s2 / (math.sin(math.radians(two_thetas_given[0] / 2)) ** 2))
    N = h*h + k*k + l*l
    a_val = lam * math.sqrt(N) / (2 * math.sin(math.radians(t2 / 2)))
    a_est.append(a_val)
print("Given 2theta:", two_thetas_given)
print("sin^2 ratios (norm to first):", [round(r, 4) for r in ratios])
print("sin^2 ratios * 3:", [round(r * 3, 3) for r in ratios])
print("Estimated a from each line:", [round(x, 4) for x in a_est], "mean:", round(np.mean(a_est), 4))
print("Cu nearest neighbor d_nn:", round(a_cu / math.sqrt(2), 4))
