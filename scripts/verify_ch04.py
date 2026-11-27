"""Numerical and analytical verification for Chapter 4 (Free Electron Theory of Metals)."""
import math
import numpy as np

# CODATA physical constants (matching docs/index.md)
hbar = 1.054571817e-34    # J s
h_planck = 2 * math.pi * hbar
m0 = 9.1093837015e-31     # kg
e_charge = 1.602176634e-19  # C
kB = 1.380649e-23         # J/K
eps0 = 8.8541878128e-12   # F/m
N_A = 6.02214076e23       # mol^-1
R_gas = N_A * kB          # J/(mol K)

print("=== CH04-KP1-05: Copper (fcc, a = 3.61 A, Z = 1) ===")
a_cu = 3.61e-10  # m
n_cu = 4.0 / (a_cu ** 3)  # fcc: 4 atoms per conventional cell, Z=1
kF_cu = (3 * math.pi ** 2 * n_cu) ** (1.0 / 3.0)
EF_cu_J = (hbar ** 2) * (kF_cu ** 2) / (2 * m0)
EF_cu_eV = EF_cu_J / e_charge
TF_cu = EF_cu_J / kB
vF_cu = hbar * kF_cu / m0
P_cu = (2.0 / 5.0) * n_cu * EF_cu_J
B_cu = (2.0 / 3.0) * n_cu * EF_cu_J
print(f"n_Cu  = {n_cu:.4e} m^-3")
print(f"k_F   = {kF_cu:.4e} m^-1 = {kF_cu*1e-10:.3f} A^-1")
print(f"E_F   = {EF_cu_J:.4e} J = {EF_cu_eV:.3f} eV")
print(f"T_F   = {TF_cu:.4e} K")
print(f"v_F   = {vF_cu:.4e} m/s")
print(f"P     = {P_cu:.4e} Pa = {P_cu*1e-9:.2f} GPa")
print(f"B     = {B_cu:.4e} Pa = {B_cu*1e-9:.2f} GPa")

print("\n=== CH04-KP1-06: Al vs Na comparison & 2D electron gas (GaAs) ===")
a_al = 4.05e-10  # fcc, Z = 3
n_al = 4.0 * 3.0 / (a_al ** 3)
a_na = 4.29e-10  # bcc, Z = 1
n_na = 2.0 * 1.0 / (a_na ** 3)
ratio_n = n_al / n_na
ratio_EF = ratio_n ** (2.0 / 3.0)
EF_al_eV = (hbar ** 2 / (2 * m0)) * ((3 * math.pi ** 2 * n_al) ** (2.0 / 3.0)) / e_charge
EF_na_eV = (hbar ** 2 / (2 * m0)) * ((3 * math.pi ** 2 * n_na) ** (2.0 / 3.0)) / e_charge
print(f"n_Al  = {n_al:.4e} m^-3, E_F(Al) = {EF_al_eV:.2f} eV")
print(f"n_Na  = {n_na:.4e} m^-3, E_F(Na) = {EF_na_eV:.2f} eV")
print(f"n_Al / n_Na = {ratio_n:.3f}, E_F(Al) / E_F(Na) = {ratio_EF:.3f}")

# 2DEG in GaAs: n_2D = 5.0e15 m^-2, m* = 0.067 m0
n_2d = 5.0e15
m_star = 0.067 * m0
kF_2d = math.sqrt(2 * math.pi * n_2d)
EF_2d_J = (hbar ** 2) * (kF_2d ** 2) / (2 * m_star)
EF_2d_meV = EF_2d_J / e_charge * 1e3
g_2d_per_area = m_star / (math.pi * hbar ** 2)
assert math.isclose(g_2d_per_area * EF_2d_J, n_2d, rel_tol=1e-12)
print(f"2DEG: k_F = {kF_2d:.4e} m^-1, E_F = {EF_2d_meV:.2f} meV")

print("\n=== CH04-KP2-04: Sommerfeld expansion for Cu at 300 K ===")
EF_test_eV = EF_cu_eV
EF_test_J = EF_cu_J
T_room = 300.0
kBT_eV = kB * T_room / e_charge
rel_mu_shift = (math.pi ** 2 / 12.0) * ((kBT_eV / EF_test_eV) ** 2)
TF_test = EF_test_J / kB
CVe_m_300 = (math.pi ** 2 / 2.0) * R_gas * (T_room / TF_test)
CV_class = 1.5 * R_gas
print(f"kBT(300K) = {kBT_eV:.5f} eV, T/T_F = {T_room/TF_test:.5e}")
print(f"|mu(300K) - E_F|/E_F = {rel_mu_shift:.3e}")
print(f"C_Ve,m(300K) = {CVe_m_300:.4f} J/(mol K) vs 3/2 R = {CV_class:.2f}, ratio = {CVe_m_300/CV_class:.4e}")
print(f"3R = {3*R_gas:.2f} J/(mol K), C_Ve / 3R = {CVe_m_300/(3*R_gas):.4e}")

# Verify 1D/2D/3D chemical potential direction numerically
# N = int_0^inf g(E) f(E) dE; check sign of mu(T) - E_F for d=1,2,3
for dim, p in [("1D", -0.5), ("2D", 0.0), ("3D", 0.5)]:
    # E_F = 1.0, kBT = 0.05
    t_val = 0.05
    E_grid = np.linspace(1e-6, 3.0, 300000)
    # Exact N(T=0) = int_0^1 E^p dE = 1/(p+1)
    N0 = 1.0 / (p + 1.0)
    # Find mu by bisection
    lo, hi = 0.9, 1.1
    for _ in range(50):
        mid = 0.5 * (lo + hi)
        f_val = 1.0 / (np.exp(np.clip((E_grid - mid) / t_val, -500, 500)) + 1.0)
        N_mid = np.trapezoid((E_grid ** p) * f_val, E_grid)
        if N_mid > N0:
            hi = mid
        else:
            lo = mid
    mu_num = 0.5 * (lo + hi)
    mu_som = 1.0 - (math.pi ** 2 / 6.0) * (t_val ** 2) * p
    print(f"Dim {dim} (p={p:+.1f}): mu_num - E_F = {mu_num - 1.0:+.6e}, Sommerfeld = {mu_som - 1.0:+.6e}")

print("\n=== CH04-KP2-05: Low-T heat capacity analysis (C_V/T = gamma + A T^2) ===")
# Using realistic monovalent metal data (close to Na: gamma ~ 1.38 mJ/(mol K^2), Theta_D ~ 158 K)
gamma_val = 1.35e-3   # J/(mol K^2)
A_val = 4.64e-4       # J/(mol K^4)
T0 = math.sqrt(gamma_val / A_val)
# gamma = (pi^2 / 2) * R / T_F  => T_F = (pi^2 / 2) * R / gamma
TF_metal = (math.pi ** 2 / 2.0) * R_gas / gamma_val
EF_metal_eV = kB * TF_metal / e_charge
# A = (12 pi^4 / 5) * R / Theta_D^3 => Theta_D = ((12 pi^4 / 5) * R / A)^(1/3)
Theta_D_metal = ((12 * math.pi ** 4 / 5.0) * R_gas / A_val) ** (1.0 / 3.0)
for T_chk in [1.0, 10.0]:
    c_e = gamma_val * T_chk
    c_l = A_val * (T_chk ** 3)
    pct_e = c_e / (c_e + c_l) * 100.0
    print(f"T = {T_chk:4.1f} K: C_Ve = {c_e:.4e}, C_Vl = {c_l:.4e}, electron share = {pct_e:.2f}%")
print(f"T0 = {T0:.3f} K")
print(f"T_F = {TF_metal:.4e} K, E_F = {EF_metal_eV:.3f} eV")
print(f"Theta_D = {Theta_D_metal:.1f} K")

print("\n=== CH04-KP3-04: Richardson-Dushman thermionic emission (Tungsten W) ===")
A0 = 4 * math.pi * e_charge * m0 * (kB ** 2) / (h_planck ** 3)
A0_check = e_charge * m0 * (kB ** 2) / (2 * math.pi ** 2 * hbar ** 3)
assert math.isclose(A0, A0_check, rel_tol=1e-12)
print(f"Theoretical Richardson constant A0 = {A0:.4e} A/(m^2 K^2) = {A0*1e-4:.2f} A/(cm^2 K^2)")

# Check realistic tungsten data: W_true = 4.54 eV, A_eff = 6.0e5 A/(m^2 K^2) (experimental W ~ 60 A/(cm^2 K^2))
W_ref = 4.54 * e_charge
A_ref = 6.0e5
T1, T2 = 2000.0, 2500.0
j1_exact = A_ref * (T1 ** 2) * math.exp(-W_ref / (kB * T1))
j2_exact = A_ref * (T2 ** 2) * math.exp(-W_ref / (kB * T2))
print(f"Ref W (4.54 eV, A=6.0e5): j(2000K) = {j1_exact:.3f} A/m^2, j(2500K) = {j2_exact:.1f} A/m^2")

# Choose clean rounded problem inputs close to real tungsten:
# j1 = 8.65 A/m^2 at 2000 K, j2 = 2.66e3 A/m^2 at 2500 K -> let's test clean numbers:
j1_in, j2_in = 8.70, 2.65e3
# ln[(j2/T2^2) / (j1/T1^2)] = -(W/kB)*(1/T2 - 1/T1) = (W/kB)*(1/T1 - 1/T2)
lhs = math.log((j2_in / (T2 ** 2)) / (j1_in / (T1 ** 2)))
W_calc_eV = lhs * (kB / e_charge) / (1.0 / T1 - 1.0 / T2)
A_eff_calc = (j1_in / (T1 ** 2)) * math.exp(W_calc_eV * e_charge / (kB * T1))
print(f"Problem W inputs (j1={j1_in}, j2={j2_in}): W = {W_calc_eV:.3f} eV, A_eff = {A_eff_calc:.3e} A/(m^2 K^2)")

print("\n=== CH04-KP4-04: Copper conductivity, relaxation time, mean free path, drift velocity ===")
rho_cu = 1.72e-8   # Ohm m at 300 K
sigma_cu = 1.0 / rho_cu
n_cu_in = n_cu     # 8.502e28 m^-3 (consistent with CH04-KP1-05)
vF_cu_in = vF_cu   # 1.575e6 m/s
kF_cu_in = kF_cu   # 1.360e10 m^-1
tau_cu = m0 / (n_cu_in * (e_charge ** 2) * rho_cu)
l_cu = vF_cu_in * tau_cu
E_field = 1.0      # V/m
vd_cu = e_charge * tau_cu * E_field / m0
dk_cu = e_charge * tau_cu * E_field / hbar
print(f"sigma = {sigma_cu:.3e} S/m")
print(f"tau   = {tau_cu:.3e} s")
print(f"l     = {l_cu:.3e} m = {l_cu*1e9:.1f} nm = {l_cu/a_cu:.1f} a")
print(f"v_d   = {vd_cu:.3e} m/s (at E=1 V/m), mu_e = {vd_cu:.4e} m^2/(V s)")
print(f"|dk|  = {dk_cu:.3e} m^-1, |dk|/k_F = {dk_cu/kF_cu_in:.3e}")

print("\n=== CH04-KP4-05: Wiedemann-Franz law, Lorenz number & Matthiessen's rule ===")
L0 = (math.pi ** 2 / 3.0) * ((kB / e_charge) ** 2)
L_class = 1.5 * ((kB / e_charge) ** 2)
kappa_cu_300 = L0 * sigma_cu * T_room
rho_0_imp = 8.60e-10  # Ohm m at 4.2 K
rho_prime_300 = rho_cu + rho_0_imp
RRR = rho_prime_300 / rho_0_imp
kappa_4p2 = L0 * (1.0 / rho_0_imp) * 4.2
print(f"L_0 (quantum)   = {L0:.4e} W Ohm K^-2")
print(f"L_cl (Drude)    = {L_class:.4e} W Ohm K^-2 (ratio L0/L_cl = {L0/L_class:.3f})")
print(f"kappa_e(300 K)  = {kappa_cu_300:.1f} W/(m K)")
print(f"rho'(300 K)     = {rho_prime_300:.4e} Ohm m")
print(f"RRR             = {RRR:.1f}")
print(f"kappa_e(4.2 K)  = {kappa_4p2:.1f} W/(m K)")
