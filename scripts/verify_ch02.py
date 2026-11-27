"""Numerical and symbolic verification for Chapter 2 (Crystal Bonding)."""
import math

e_charge = 1.602176634e-19
eps0 = 8.8541878128e-12
k_e = 1 / (4 * math.pi * eps0)

print("=== CH02-KP2-04: 1D Madelung constant ===")
alpha_1d = 2 * math.log(2)
n_ex = 9
ratio_bind = 1 - 1 / n_ex
print(f"alpha_1D = 2 ln 2 = {alpha_1d:.6f}")
print(f"Binding / Madelung (n=9) = {ratio_bind:.6f} ({ratio_bind*100:.2f}%)")

print("\n=== CH02-KP2-05: NaCl Born-Lande & Born-Haber ===")
R0_nacl = 2.82e-10  # m
alpha_nacl = 1.7476
K_nacl = 2.40e10  # N/m^2 = Pa
# For NaCl: V/N = 2 R^3 (conventional cell a=2R0 has 4 ion pairs -> a^3/4 = 8 R0^3 / 4 = 2 R0^3)
# U(r)/N = -alpha*k_e*e^2 / r + B / r^n
# dU/dr = 0 => B = alpha*k_e*e^2 * R0^(n-1) / n
# d^2(U/N)/dr^2|_{R0} = -2 alpha k_e e^2 / R0^3 + n(n+1) B / R0^(n+2)
#                     = (n - 1) alpha k_e e^2 / R0^3
# K = R0^2 / (9 V0) * d^2U/dr^2 = R0^2 / (9 * 2 N R0^3) * N (n-1) alpha k_e e^2 / R0^3
#   = (n - 1) alpha k_e e^2 / (18 R0^4) = (n - 1) alpha e^2 / (72 pi eps0 R0^4)
n_nacl = 1 + 18 * K_nacl * (R0_nacl ** 4) / (alpha_nacl * k_e * e_charge ** 2)
u_mad_eV = alpha_nacl * k_e * e_charge / R0_nacl  # in eV (since divided by e)
w_ion_eV = u_mad_eV * (1 - 1 / n_nacl)
# Also check using rounded n = 8.43 or exact
I_Na = 5.14
EA_Cl = 3.61
w_atom_eV = w_ion_eV - I_Na + EA_Cl
print(f"n (NaCl) = {n_nacl:.4f}")
print(f"Madelung energy per pair = {u_mad_eV:.4f} eV")
print(f"Ionic binding energy W_ion = {w_ion_eV:.4f} eV")
print(f"Atomic binding energy W_atom = {w_atom_eV:.4f} eV")

# Check numerical derivative for K_nacl
B_nacl = alpha_nacl * k_e * e_charge ** 2 * (R0_nacl ** (n_nacl - 1)) / n_nacl
def u_nacl(r):
    return -alpha_nacl * k_e * e_charge ** 2 / r + B_nacl / (r ** n_nacl)
dr = 1e-15
d2u = (u_nacl(R0_nacl + dr) - 2 * u_nacl(R0_nacl) + u_nacl(R0_nacl - dr)) / (dr ** 2)
K_num = R0_nacl ** 2 / (9 * 2 * R0_nacl ** 3) * d2u
print(f"Numerical K check: {K_num:.4e} vs {K_nacl:.4e} Pa")

print("\n=== CH02-KP2-06: Born-Mayer exponential repulsion ===")
# U(r)/N = -alpha k_e q^2 / r + z lambda exp(-r/rho)
# dU/dr = 0 => z lambda / rho * exp(-R0/rho) = alpha k_e q^2 / R0^2
# d2U/dr2|_{R0} = -2 alpha k_e q^2 / R0^3 + (1/rho) * (alpha k_e q^2 / R0^2)
#               = alpha k_e q^2 / R0^3 * (R0/rho - 2)
# V0/N = c R0^3 => K = R0^2 / (9 c R0^3) * d2(U/N)/dr2 = alpha k_e q^2 / (9 c R0^4) * (R0/rho - 2)
#                    = alpha q^2 / (36 pi eps0 c R0^4) * (R0/rho - 2)
rho_test = 0.32e-10
c_test = 2.0
z_lam = (alpha_nacl * k_e * e_charge ** 2 / R0_nacl ** 2) * rho_test * math.exp(R0_nacl / rho_test)
def u_bm(r):
    return -alpha_nacl * k_e * e_charge ** 2 / r + z_lam * math.exp(-r / rho_test)
d2u_bm = (u_bm(R0_nacl + dr) - 2 * u_bm(R0_nacl) + u_bm(R0_nacl - dr)) / (dr ** 2)
K_bm_num = R0_nacl ** 2 / (9 * c_test * R0_nacl ** 3) * d2u_bm
K_bm_ana = alpha_nacl * k_e * e_charge ** 2 / (9 * c_test * R0_nacl ** 4) * (R0_nacl / rho_test - 2)
assert math.isclose(K_bm_num, K_bm_ana, rel_tol=1e-5)
print(f"Born-Mayer K formula verified: {K_bm_ana:.4e} Pa == {K_bm_num:.4e} Pa")

print("\n=== CH02-KP3-02: Inflection point r_m / r_0 for 6-12 potential ===")
rm_over_r0 = (13 / 7) ** (1 / 6)
print(f"r_m / r_0 (6-12) = {rm_over_r0:.4f}")

print("\n=== CH02-KP3-04: Argon FCC Lennard-Jones ===")
A6 = 14.45
A12 = 12.13
eps_ar = 1.67e-21  # J
sig_ar = 3.40e-10  # m
# U(R)/N = 2 eps [ A12 (sig/R)^12 - A6 (sig/R)^6 ]
# dU/dR = 0 => 2 eps [ -12 A12 sig^12 / R0^13 + 6 A6 sig^6 / R0^7 ] = 0
#           => (R0/sig)^6 = 2 A12 / A6
R0_over_sig = (2 * A12 / A6) ** (1 / 6)
R0_ar = R0_over_sig * sig_ar
w_over_eps = 0.5 * (A6 ** 2) / A12
w_ar_J = w_over_eps * eps_ar
w_ar_eV = w_ar_J / e_charge

# Volume per atom in FCC: a = sqrt(2) R, V0/N = a^3/4 = (2*sqrt(2) R^3)/4 = R^3 / sqrt(2)
# d^2(U/N)/dR^2|_{R0} = 2 eps [ 156 A12 sig^12 / R0^14 - 42 A6 sig^6 / R0^8 ]
# Since (sig/R0)^6 = A6 / (2 A12), (sig/R0)^12 = A6^2 / (4 A12^2):
#   156 A12 * A6^2 / (4 A12^2) - 42 A6 * A6 / (2 A12) = (39 - 21) A6^2 / A12 = 18 A6^2 / A12
# So d^2(U/N)/dR^2|_{R0} = 36 eps (A6^2 / A12) / R0^2
# And K = R0^2 / (9 V0/N) * d^2(U/N)/dR^2 = R0^2 / (9 R0^3 / sqrt(2)) * 36 eps (A6^2 / A12) / R0^2
#       = 4 sqrt(2) eps (A6^2 / A12) / R0^3
# Wait! Let's verify numerically!
def u_lj_fcc(R):
    return 2 * eps_ar * (A12 * (sig_ar / R) ** 12 - A6 * (sig_ar / R) ** 6)
dR = 1e-15
d2u_lj = (u_lj_fcc(R0_ar + dR) - 2 * u_lj_fcc(R0_ar) + u_lj_fcc(R0_ar - dR)) / (dR ** 2)
K_lj_num = (R0_ar ** 2) / (9 * (R0_ar ** 3 / math.sqrt(2))) * d2u_lj
K_lj_ana = 4 * math.sqrt(2) * eps_ar * (A6 ** 2 / A12) / (R0_ar ** 3)
K_lj_alt = 4 * math.sqrt(2) * eps_ar * (A6 ** 2.5) / ((2 ** 0.5) * (A12 ** 1.5) * sig_ar ** 3)
assert math.isclose(K_lj_num, K_lj_ana, rel_tol=1e-5)
assert math.isclose(K_lj_num, K_lj_alt, rel_tol=1e-5)
print(f"R0/sigma = {R0_over_sig:.4f}, R0(Ar) = {R0_ar*1e10:.4f} A")
print(f"w/eps = {w_over_eps:.4f}, w(Ar) = {w_ar_eV:.4f} eV ({w_ar_eV*1000:.2f} meV)")
print(f"K(Ar) = {K_lj_ana/1e9:.4f} GPa (num check: {K_lj_num/1e9:.4f} GPa)")

print("\n=== CH02-KP3-05: 1D Lennard-Jones chain (NN vs all neighbors) ===")
# NN only: each atom has 2 nearest neighbors -> A6_nn = 2, A12_nn = 2
# All neighbors: A6_all = 2 * zeta(6), A12_all = 2 * zeta(12)
zeta6 = math.pi ** 6 / 945
zeta12 = sum(1 / (m ** 12) for m in range(1, 1000))
a0_nn = (2 * 2 / 2) ** (1 / 6)  # 2^(1/6)
w_nn = 0.5 * (2 ** 2) / 2       # 1.0 eps
a0_all = (2 * (2 * zeta12) / (2 * zeta6)) ** (1 / 6)
w_all = 0.5 * ((2 * zeta6) ** 2) / (2 * zeta12)
print(f"zeta(6) = {zeta6:.6f}, zeta(12) = {zeta12:.6f}")
print(f"NN only: a0/sigma = {a0_nn:.5f}, w/eps = {w_nn:.5f}")
print(f"All    : a0/sigma = {a0_all:.5f}, w/eps = {w_all:.5f}")
print(f"Relative diffs: a0 {(a0_all-a0_nn)/a0_nn*100:.2f}%, w {(w_all-w_nn)/w_nn*100:.2f}%")

print("\n=== CH02-KP3-06: NaCl vs CsCl stability ===")
a1, z1 = 1.7476, 6  # NaCl
a2, z2 = 1.7627, 8  # CsCl
# U(r)/N = -alpha k_e e^2 / r + z B / r^n
# Equilibrium: R0^(n-1) = n z B / (alpha k_e e^2) => R0 proportional to (z / alpha)^(1/(n-1))
# W/N = (alpha k_e e^2 / R0) * (1 - 1/n) proportional to alpha * (alpha/z)^(1/(n-1)) = alpha^(n/(n-1)) * z^(-1/(n-1))
# Ratio W_CsCl / W_NaCl = (a2/a1)^(n/(n-1)) * (z1/z2)^(1/(n-1))
# Critical n_c where W_CsCl = W_NaCl: (a2/a1)^n = z2/z1 => n_c = ln(z2/z1) / ln(a2/a1)
n_c = math.log(z2 / z1) / math.log(a2 / a1)
ratio_n9 = ((a2 / a1) ** (9 / 8)) * ((z1 / z2) ** (1 / 8))
R0_ratio_n9 = ((z2 / z1) * (a1 / a2)) ** (1 / 8)
print(f"Critical n_c = {n_c:.2f}")
print(f"At n=9: R0(CsCl)/R0(NaCl) = {R0_ratio_n9:.4f}, W(CsCl)/W(NaCl) = {ratio_n9:.4f}")
