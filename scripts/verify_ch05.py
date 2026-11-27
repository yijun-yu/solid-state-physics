"""Numerical and analytical verification for Chapter 5 (Band Theory of Solids)."""
import math
import numpy as np

# CODATA constants (matching docs/index.md)
hbar = 1.054571817e-34    # J s
m0 = 9.1093837015e-31     # kg
e_charge = 1.602176634e-19  # C

print("=== CH05-KP2-04: 1D Nearly Free Electron at k = pi/a ===")
a_1d = 4.00e-10  # m
V0_eV = 0.50     # eV (V(x) = -2 V0 cos(2pi x / a), so |V_G| = V0)
V0_J = V0_eV * e_charge
E0_pi_J = (hbar ** 2) * ((math.pi / a_1d) ** 2) / (2 * m0)
E0_pi_eV = E0_pi_J / e_charge
Eg1_eV = 2 * V0_eV
m_upper_ratio = 1.0 / (1.0 + 2 * E0_pi_eV / V0_eV)
m_lower_ratio = 1.0 / (1.0 - 2 * E0_pi_eV / V0_eV)

# Numerical verification via finite-difference 2nd derivative of exact 2x2 eigenvalue
dq = 1e6  # m^-1 (optimal float64 step for 2nd difference, dq << pi/a ~ 7.85e9)
def eig_2x2(q, sign):
    G = 2 * math.pi / a_1d
    e1 = (hbar ** 2) * ((G / 2 + q) ** 2) / (2 * m0)
    e2 = (hbar ** 2) * ((-G / 2 + q) ** 2) / (2 * m0)
    return 0.5 * (e1 + e2) + sign * math.sqrt((0.5 * (e1 - e2)) ** 2 + V0_J ** 2)

d2E_upper = (eig_2x2(dq, +1) - 2 * eig_2x2(0, +1) + eig_2x2(-dq, +1)) / (dq ** 2)
d2E_lower = (eig_2x2(dq, -1) - 2 * eig_2x2(0, -1) + eig_2x2(-dq, -1)) / (dq ** 2)
m_upper_num = (hbar ** 2 / d2E_upper) / m0
m_lower_num = (hbar ** 2 / d2E_lower) / m0
assert math.isclose(m_upper_ratio, m_upper_num, rel_tol=1e-5)
assert math.isclose(m_lower_ratio, m_lower_num, rel_tol=1e-5)
print(f"E0(pi/a) = {E0_pi_eV:.3f} eV, Eg1 = {Eg1_eV:.2f} eV")
print(f"m*(2nd band bottom)/m0 = {m_upper_ratio:.4f} (num: {m_upper_num:.4f})")
print(f"m*(1st band top)/m0    = {m_lower_ratio:.4f} (num: {m_lower_num:.4f})")

print("\n=== CH05-KP2-05: 2D Square Lattice NFE (2 electrons/cell) ===")
# k_F / (pi/a) = 2 / sqrt(pi)
kF_over_kX = 2.0 / math.sqrt(math.pi)
kM_over_kX = math.sqrt(2.0)
print(f"k_F / (pi/a) = {kF_over_kX:.4f}, k_M / (pi/a) = {kM_over_kX:.4f}")
# Check 4x4 M-point coupling matrix eigenvalues when V_10 = V_01 = V
H_M = np.array([[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]], dtype=float)
eigs_M = np.linalg.eigvalsh(H_M)
print(f"M-point 4-wave eigenvalues (in units of V): {eigs_M}")

print("\n=== CH05-KP3-04: 3D Tight-Binding (sc, bcc, fcc) ===")
# Check global extrema of fcc factor F(kx,ky,kz) = cos(kx/2)cos(ky/2) + cos(ky/2)cos(kz/2) + cos(kz/2)cos(kx/2)
grid = np.linspace(-math.pi, math.pi, 101)
KX, KY, KZ = np.meshgrid(grid, grid, grid, indexing="ij")
F_bcc = np.cos(KX) * np.cos(KY) * np.cos(KZ)  # using u = k*a/2 in [-pi, pi]
F_fcc = np.cos(KX) * np.cos(KY) + np.cos(KY) * np.cos(KZ) + np.cos(KZ) * np.cos(KX)
# E_bcc = E0 - alpha - 8 J F_bcc => bandwidth = 8 J * (max - min)
W_bcc_J = 8.0 * (F_bcc.max() - F_bcc.min())
# E_fcc = E0 - alpha - 4 J F_fcc => bandwidth = 4 J * (max - min)
W_fcc_J = 4.0 * (F_fcc.max() - F_fcc.min())
print(f"BCC: F_bcc in [{F_bcc.min():.3f}, {F_bcc.max():.3f}] => W_bcc = {W_bcc_J:.2f} J")
print(f"FCC: F_fcc in [{F_fcc.min():.3f}, {F_fcc.max():.3f}] => W_fcc = {W_fcc_J:.2f} J")
# Check Gamma-point Taylor expansion:
# BCC: -8 J (1 - (kx^2+ky^2+kz^2) a^2 / 8) = -8J + J a^2 k^2 => d2E/dk^2 = 2 J a^2 => m* = hbar^2 / (2 J a^2)
# FCC: -4 J [3 - 2*(kx^2+ky^2+kz^2) a^2 / 8] = -12J + J a^2 k^2 ... WAIT A MINUTE!
# Let's check FCC Taylor expansion carefully!!
# cos(u)cos(v) ~ (1 - u^2/2)(1 - v^2/2) = 1 - (u^2 + v^2)/2
# Sum of 3 pairs: (1-(ux^2+uy^2)/2) + (1-(uy^2+uz^2)/2) + (1-(uz^2+ux^2)/2) = 3 - (ux^2 + uy^2 + uz^2)
# Here u_i = k_i a / 2, so u_i^2 = k_i^2 a^2 / 4!
# Therefore -4 J * F_fcc ~ -4 J * [3 - (kx^2 + ky^2 + kz^2) a^2 / 4] = -12 J + J a^2 (kx^2 + ky^2 + kz^2)!!
# SO d^2E / dk_x^2 = 2 J a^2 for BOTH BCC AND FCC!!
# THANK GOODNESS WE VERIFIED THIS IN PYTHON!!
du = 1e-4  # k*a
d2_sc = ((-2 * (math.cos(du) + 2)) - 2 * (-6) + (-2 * (math.cos(-du) + 2))) / (du ** 2)
d2_bcc = ((-8 * math.cos(du / 2)) - 2 * (-8) + (-8 * math.cos(-du / 2))) / (du ** 2)
d2_fcc = ((-4 * (2 * math.cos(du / 2) + 1)) - 2 * (-12) + (-4 * (2 * math.cos(-du / 2) + 1))) / (du ** 2)
print(f"d^2E / d(ka)^2 at Gamma (in units of J): sc={d2_sc:.4f}, bcc={d2_bcc:.4f}, fcc={d2_fcc:.4f}")
# ALL THREE (sc, bcc, fcc) give d^2E / dk^2 = 2 J a^2 => m* = hbar^2 / (2 J a^2)!!
# Wait: sc: -2J cos(ka) ~ -2J (1 - k^2 a^2 / 2) = -2J + J a^2 k^2 => d^2E/dk^2 = 2 J a^2!
# bcc: -8J cos(ka/2) ~ -8J (1 - k^2 a^2 / 8) = -8J + J a^2 k^2 => d^2E/dk^2 = 2 J a^2!
# fcc: -4J (2 cos(ka/2) + 1) ~ -4J (3 - k^2 a^2 / 4) = -12J + J a^2 k^2 => d^2E/dk^2 = 2 J a^2!
# What a remarkable and subtle result! Checking numerically prevented a classic slip!

print("\n=== CH05-KP4-04: 1D Bloch Oscillation ===")
a_bo = 4.00e-10   # m
J_bo_eV = 0.50    # eV (bandwidth W = 4J = 2.00 eV)
J_bo_J = J_bo_eV * e_charge
E_bo = 1.0e4      # V/m
w_B = e_charge * E_bo * a_bo / hbar
T_B = 2 * math.pi / w_B
x_max = 4 * J_bo_J / (e_charge * E_bo)  # full peak-to-peak excursion W / (e E); half-amplitude = 2J / (eE)
print(f"omega_B = {w_B:.3e} rad/s, T_B = {T_B:.3e} s")
print(f"Full excursion W/(eE) = {x_max*1e6:.2f} um, amplitude 2J/(eE) = {0.5*x_max*1e6:.2f} um")

print("\n=== CH05-KP4-06: Silicon Ellipsoidal Valley Effective Masses ===")
mt = 0.19
ml = 0.98
md_single = (ml * (mt ** 2)) ** (1.0 / 3.0)
mc_cond = 3.0 / (1.0 / ml + 2.0 / mt)
print(f"Single-valley DOS mass m_d*/m0 = {md_single:.3f}")
print(f"6-valley total DOS mass 6^(2/3)*m_d*/m0 = {(6**(2/3))*md_single:.3f}")
print(f"Conductivity effective mass m_c*/m0 = {mc_cond:.3f}")

print("\n=== CH05-KP5-04: Potassium dHvA & Cyclotron Resonance ===")
delta_invB = 5.46e-5  # T^-1
S_ext = 2 * math.pi * e_charge / (hbar * delta_invB)
kF_K = math.sqrt(S_ext / math.pi)
n_K = (kF_K ** 3) / (3 * math.pi ** 2)
nu_mw = 24.0e9  # Hz
B_c = 1.04      # T
w_c = 2 * math.pi * nu_mw
mc_K_ratio = (e_charge * B_c / w_c) / m0
print(f"S_ext = {S_ext:.3e} m^-2")
print(f"k_F   = {kF_K:.3e} m^-1 = {kF_K*1e-10:.3f} A^-1")
print(f"n_K   = {n_K:.3e} m^-3")
print(f"m_c*/m0 = {mc_K_ratio:.3f}")

print("\n=== CH05-KP5-05: ARPES Dispersion Extraction ===")
hv_eV = 21.22
W_eV = 4.50
Ekin_0 = 16.32  # eV at theta = 0 (band bottom)
Ekin_F = hv_eV - W_eV  # 16.72 eV at E = E_F
EB_0 = Ekin_F - Ekin_0  # 0.40 eV binding energy of band bottom
theta_F_deg = 10.0
theta_F = math.radians(theta_F_deg)
kF_arpes = math.sqrt(2 * m0 * (Ekin_F * e_charge)) / hbar * math.sin(theta_F)
# Parabolic band: E(k) - E(0) = hbar^2 k^2 / (2 m*) => at k = kF, EB_0 = hbar^2 kF^2 / (2 m*)
m_arpes_ratio = ((hbar ** 2) * (kF_arpes ** 2) / (2 * (EB_0 * e_charge))) / m0
print(f"E_kin(E_F) = {Ekin_F:.2f} eV, |E(0) - E_F| = {EB_0:.2f} eV")
print(f"k_F = {kF_arpes:.3e} m^-1 = {kF_arpes*1e-10:.3f} A^-1")
print(f"m*/m0 = {m_arpes_ratio:.3f}")
