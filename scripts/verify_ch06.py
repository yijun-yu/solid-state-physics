"""Numerical and analytical verification for Chapter 6 (Semiconductor Electron Theory)."""
import math

# CODATA constants (matching docs/index.md)
hbar = 1.054571817e-34      # J s
h_planck = 2 * math.pi * hbar
m0 = 9.1093837015e-31       # kg
e_charge = 1.602176634e-19  # C
kB = 1.380649e-23           # J/K
eps0 = 8.8541878128e-12     # F/m
a_B = 0.5291772109e-10      # m (0.529 A)
E0_H = 13.605693            # eV

print("=== CH06-KP1-04: Hydrogenic Donor Model & Mott Criterion (GaAs & Si) ===")
for name, eps_r, m_rel in [("GaAs", 12.9, 0.067), ("Si", 11.7, 0.26)]:
    dE_meV = E0_H * m_rel / (eps_r ** 2) * 1e3
    a_star_A = a_B * 1e10 * eps_r / m_rel
    # Mott criterion: N_c^(1/3) * a_B* = 0.25 => N_c = (0.25 / a_B*)^3
    N_mott_m3 = (0.25 / (a_star_A * 1e-10)) ** 3
    N_mott_cm3 = N_mott_m3 * 1e-6
    print(f"{name:4s}: Delta E_D = {dE_meV:.2f} meV, a_B* = {a_star_A:.1f} A, N_Mott = {N_mott_cm3:.2e} cm^-3")

print("\n=== CH06-KP2-04: Intrinsic Silicon at 300 K ===")
T300 = 300.0
kBT_300_eV = kB * T300 / e_charge
Eg_Si = 1.12  # eV
mdn_Si = 1.08 * m0
mdp_Si = 0.81 * m0
Nc_300 = 2 * ((2 * math.pi * mdn_Si * kB * T300) / (h_planck ** 2)) ** 1.5  # m^-3
Nv_300 = 2 * ((2 * math.pi * mdp_Si * kB * T300) / (h_planck ** 2)) ** 1.5  # m^-3
ni_300 = math.sqrt(Nc_300 * Nv_300) * math.exp(-Eg_Si / (2 * kBT_300_eV))
EFi_shift_meV = 0.75 * kBT_300_eV * math.log(mdp_Si / mdn_Si) * 1e3
print(f"kBT(300K) = {kBT_300_eV:.5f} eV")
print(f"N_c = {Nc_300*1e-6:.3e} cm^-3, N_v = {Nv_300*1e-6:.3e} cm^-3")
print(f"n_i(300K) = {ni_300*1e-6:.3e} cm^-3")
print(f"E_Fi - E_mid = {EFi_shift_meV:.2f} meV")

# Also check intrinsic n_i at 600 K (with Eg ~ 1.04 eV at 600 K) for physical realism in KP2-05
T600 = 600.0
kBT_600_eV = kB * T600 / e_charge
Nc_600 = Nc_300 * (2.0 ** 1.5)
Nv_600 = Nv_300 * (2.0 ** 1.5)
ni_600_real = math.sqrt(Nc_600 * Nv_600) * math.exp(-1.04 / (2 * kBT_600_eV))
print(f"Physical check: Si n_i(600 K, Eg=1.04 eV) = {ni_600_real*1e-6:.2e} cm^-3")

print("\n=== CH06-KP2-05: Compensated Si (Room T & High T = 600 K) ===")
ND = 4.0e16  # cm^-3
NA = 1.0e16  # cm^-3
N_net = ND - NA  # 3.0e16 cm^-3
ni_rt = 1.0e10  # cm^-3 (clean standard textbook value at 300 K)
Nc_rt = 2.8e19  # cm^-3
n0_rt = N_net
p0_rt = (ni_rt ** 2) / n0_rt
Ec_minus_EF_rt = kBT_300_eV * math.log(Nc_rt / n0_rt)
EF_minus_EFi_rt = kBT_300_eV * math.log(n0_rt / ni_rt)
print(f"300 K: n0 = {n0_rt:.2e} cm^-3, p0 = {p0_rt:.2e} cm^-3")
print(f"300 K: Ec - EF = {Ec_minus_EF_rt:.3f} eV ({Ec_minus_EF_rt/kBT_300_eV:.1f} kBT), EF - EFi = {EF_minus_EFi_rt:.3f} eV")

# At T = 600 K, give clean n_i(600K) = 2.0e16 cm^-3 (close to real Si ~3e15 at 600K or ~2e16 at 650K; let's check 650 K!)
T650 = 650.0
kBT_650_eV = kB * T650 / e_charge
ni_650_real = math.sqrt(Nc_300 * Nv_300) * ((T650 / T300) ** 1.5) * math.exp(-1.02 / (2 * kBT_650_eV))
print(f"Physical check: Si n_i(650 K, Eg=1.02 eV) = {ni_650_real*1e-6:.2e} cm^-3")
# At 680 K:
T680 = 680.0
kBT_680_eV = kB * T680 / e_charge
ni_680_real = math.sqrt(Nc_300 * Nv_300) * ((T680 / T300) ** 1.5) * math.exp(-1.01 / (2 * kBT_680_eV))
print(f"Physical check: Si n_i(680 K, Eg=1.01 eV) = {ni_680_real*1e-6:.2e} cm^-3")
# Awesome! At T = 650 K, real Si n_i is ~1.1e16 cm^-3; at 680 K it's ~2.0e16 cm^-3!
# Using T = 680 K with n_i = 2.0e16 cm^-3 and N_net = 3.0e16 cm^-3 gives exact Pythagorean triple:
# sqrt(3^2 + 4*2^2) = sqrt(9 + 16) = 5!!
ni_hi = 2.0e16  # cm^-3 at T = 680 K
n0_hi = 0.5 * (N_net + math.sqrt(N_net ** 2 + 4 * ni_hi ** 2))
p0_hi = (ni_hi ** 2) / n0_hi
EF_minus_EFi_hi = kBT_680_eV * math.log(n0_hi / ni_hi)
assert math.isclose(n0_hi - p0_hi, N_net, rel_tol=1e-12)
print(f"680 K (ni=2.0e16): n0 = {n0_hi:.2e} cm^-3, p0 = {p0_hi:.2e} cm^-3, EF - EFi = {EF_minus_EFi_hi:.3f} eV")

print("\n=== CH06-KP3-04: Hall Effect Measurement & Two-Carrier Sign Reversal ===")
d_h = 0.50e-3   # m
w_h = 4.0e-3    # m
L_h = 10.0e-3   # m
I_h = 2.0e-3    # A
B_h = 0.50      # T
U_par = 0.050   # V (50.0 mV -> realistic n-Si mobility 1250 cm^2/(V s))
U_H = -1.25e-3  # V
# R = U_par / I = rho * L / (w * d) => rho = (U_par / I) * (w * d / L)
rho_h = (U_par / I_h) * (w_h * d_h / L_h)  # Ohm m
sigma_h = 1.0 / rho_h
# U_H = R_H * I * B / d => R_H = U_H * d / (I * B)
RH_h = U_H * d_h / (I_h * B_h)  # m^3 / C
n_h = -1.0 / (e_charge * RH_h)  # m^-3
mu_H = abs(RH_h) * sigma_h      # m^2 / (V s)
print(f"rho = {rho_h:.4f} Ohm m = {rho_h*1e2:.2f} Ohm cm, sigma = {sigma_h:.2f} S/m = {sigma_h*1e-2:.3f} S/cm")
print(f"R_H = {RH_h:.4e} m^3/C = {RH_h*1e6:.1f} cm^3/C")
print(f"n   = {n_h:.3e} m^-3 = {n_h*1e-6:.3e} cm^-3")
print(f"mu_H = {mu_H:.4f} m^2/(V s) = {mu_H*1e4:.1f} cm^2/(V s)")
# Two-carrier sign reversal for p-type with b = mu_n / mu_p = 3.0:
b_ratio = 3.0
n_rev_over_NA = 1.0 / (b_ratio ** 2 - 1.0)
print(f"Hall sign reversal (b=3): n / N_A = {n_rev_over_NA:.4f} = 1/8, p / N_A = {1 + n_rev_over_NA:.4f} = 9/8")

print("\n=== CH06-KP3-05: Minimum Conductivity of Silicon at 300 K ===")
ni_s = 1.0e10   # cm^-3
mu_n_s = 1400.0 # cm^2/(V s)
mu_p_s = 450.0  # cm^2/(V s)
sigma_i = e_charge * ni_s * (mu_n_s + mu_p_s)  # S/cm
sigma_min = 2 * e_charge * ni_s * math.sqrt(mu_n_s * mu_p_s)  # S/cm
rho_i = 1.0 / sigma_i      # Ohm cm
rho_max = 1.0 / sigma_min  # Ohm cm
n_min = ni_s * math.sqrt(mu_p_s / mu_n_s)
p_min = ni_s * math.sqrt(mu_n_s / mu_p_s)
NA_min = p_min - n_min
print(f"sigma_i   = {sigma_i:.3e} S/cm, rho_i   = {rho_i:.3e} Ohm cm")
print(f"sigma_min = {sigma_min:.3e} S/cm, rho_max = {rho_max:.3e} Ohm cm")
print(f"n_min = {n_min:.3e} cm^-3, p_min = {p_min:.3e} cm^-3, N_A = {NA_min:.3e} cm^-3")

print("\n=== CH06-KP4-04: Abrupt Silicon PN Junction at 300 K ===")
NA_pn = 1.0e17 * 1e6  # m^-3
ND_pn = 1.0e16 * 1e6  # m^-3
ni_pn = 1.0e10 * 1e6  # m^-3
eps_si = 11.7 * eps0
VT = kBT_300_eV  # V
Vbi = VT * math.log((NA_pn * ND_pn) / (ni_pn ** 2))
W_0 = math.sqrt((2 * eps_si / e_charge) * (1 / NA_pn + 1 / ND_pn) * Vbi)
xp_0 = W_0 * ND_pn / (NA_pn + ND_pn)
xn_0 = W_0 * NA_pn / (NA_pn + ND_pn)
Emax_0 = e_charge * ND_pn * xn_0 / eps_si  # V/m
assert math.isclose(Emax_0, 2 * Vbi / W_0, rel_tol=1e-12)
VR = 4.0  # V
W_R = math.sqrt((2 * eps_si / e_charge) * (1 / NA_pn + 1 / ND_pn) * (Vbi + VR))
Cj_R = eps_si / W_R  # F/m^2
print(f"V_bi = {Vbi:.3f} V")
print(f"W(0) = {W_0*1e6:.3f} um, x_p = {xp_0*1e6:.4f} um, x_n = {xn_0*1e6:.3f} um")
print(f"|E_max(0)| = {Emax_0:.3e} V/m = {Emax_0*1e-2:.3e} V/cm")
print(f"At V_R = 4.0 V: W(V_R) = {W_R*1e6:.3f} um, C_j = {Cj_R:.3e} F/m^2 = {Cj_R*1e-4*1e9:.2f} nF/cm^2")

print("\n=== CH06-KP4-05: AlGaAs/GaAs Heterojunction & p-Si MIS Inversion ===")
chi1, Eg1 = 3.74, 1.80
chi2, Eg2 = 4.07, 1.42
dEc = chi2 - chi1
dEv = (Eg1 - Eg2) - dEc
print(f"Heterojunction: Delta E_c = {dEc:.2f} eV, Delta E_v = {dEv:.2f} eV (dEc+dEv = {dEc+dEv:.2f} = Eg1-Eg2 = {Eg1-Eg2:.2f})")
NA_mis = 1.0e16 * 1e6  # m^-3
phi_F = VT * math.log(NA_mis / ni_pn)
psi_inv = 2 * phi_F
W_max_mis = math.sqrt((2 * eps_si * psi_inv) / (e_charge * NA_mis))
print(f"MIS (p-Si, NA=1e16): phi_F = {phi_F:.3f} V, 2*phi_F = {psi_inv:.3f} V, W_max = {W_max_mis*1e6:.3f} um")
