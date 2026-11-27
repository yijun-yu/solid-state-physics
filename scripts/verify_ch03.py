"""Numerical and analytical verification for Chapter 3 (Lattice Vibrations)."""
import math
import numpy as np

hbar = 1.054571817e-34   # J s
kB = 1.380649e-23        # J/K
e_charge = 1.602176634e-19
c_light = 2.99792458e8   # m/s
N_A = 6.02214076e23
R_gas = N_A * kB

print("=== CH03-KP1-05: 1D chain with 1st (beta1) & 2nd (beta2) NN ===")
# w^2(q) = (4/m) [ beta1 sin^2(qa/2) + beta2 sin^2(qa) ]
# Let u = sin^2(qa/2) in [0, 1]. Then sin^2(qa) = 4 u (1 - u).
# f(u) = beta1 * u + 4 * beta2 * u * (1 - u) = (beta1 + 4 beta2) u - 4 beta2 u^2
# f'(u) = beta1 + 4 beta2 - 8 beta2 u = 0 => u* = (beta1 + 4 beta2) / (8 beta2) = 1/2 + beta1/(8 beta2)
# u* < 1 (interior max) iff beta1 / (8 beta2) < 1/2 => beta2 / beta1 > 1/4!
for ratio in [0.1, 0.25, 0.5]:
    qs = np.linspace(0, math.pi, 10001)
    w2 = 4 * (np.sin(qs / 2) ** 2 + ratio * np.sin(qs) ** 2)
    q_max = qs[np.argmax(w2)]
    print(f"beta2/beta1={ratio:.2f}: argmax(q*a/pi) = {q_max/math.pi:.4f}, w^2_max/(beta1/m) = {w2.max():.4f}")

print("\n=== CH03-KP3-05: NaCl optical phonons & LST relation ===")
eps_0 = 5.62
eps_inf = 2.25
lam_T = 61.0e-6  # m
w_T = 2 * math.pi * c_light / lam_T
E_T_meV = hbar * w_T / e_charge * 1e3
w_L = w_T * math.sqrt(eps_0 / eps_inf)
E_L_meV = hbar * w_L / e_charge * 1e3
T_room = 300.0
x_T = hbar * w_T / (kB * T_room)
n_bar_T = 1.0 / (math.exp(x_T) - 1.0)
print(f"omega_T = {w_T:.4e} rad/s, hbar*omega_T = {E_T_meV:.2f} meV")
print(f"omega_L = {w_L:.4e} rad/s, hbar*omega_L = {E_L_meV:.2f} meV (ratio={w_L/w_T:.4f})")
print(f"At 300 K: hbar*w_T/(kB*T) = {x_T:.4f}, n_bar = {n_bar_T:.3f}")

print("\n=== CH03-KP4-04: Debye integrals & T^3 prefactor ===")
# 12 * pi^4 / 5
pref_3d = 12 * (math.pi ** 4) / 5
print(f"12 pi^4 / 5 = {pref_3d:.4f}, 12 pi^4 / 5 * R = {pref_3d * R_gas:.2f} J/(mol K)")

print("\n=== CH03-KP4-05: Copper Debye temperature & 10 K molar heat capacity ===")
a_cu = 3.615e-10  # m
n_cu = 4 / (a_cu ** 3)  # fcc: 4 atoms per conventional cell
v_l = 4760.0  # m/s
v_t = 2325.0  # m/s
# 3 / v_bar^3 = 1/v_l^3 + 2/v_t^3
inv_v3 = (1 / v_l ** 3 + 2 / v_t ** 3) / 3
v_bar = inv_v3 ** (-1 / 3)
w_D = (6 * math.pi ** 2 * n_cu / inv_v3) ** (1 / 3)
Theta_D = hbar * w_D / kB
T_low = 10.0
C_Vm_10K = pref_3d * R_gas * ((T_low / Theta_D) ** 3)
print(f"n_Cu = {n_cu:.4e} m^-3")
print(f"v_bar = {v_bar:.2f} m/s")
print(f"omega_D = {w_D:.4e} rad/s")
print(f"Theta_D = {Theta_D:.2f} K")
print(f"C_Vm(10 K) = {C_Vm_10K:.5f} J/(mol K) = {C_Vm_10K*1e3:.2f} mJ/(mol K)")

print("\n=== CH03-KP4-06: 2D Debye model ===")
# 2 polarizations in 2D: number of modes in dq is 2 * (S/(2pi)^2) * 2pi q dq = (S/pi) q dq
# Since omega = v_s q => g(omega) = (S / (pi v_s^2)) omega
# Integral_0^{w_D} g(w) dw = 2N => S w_D^2 / (2 pi v_s^2) = 2N => w_D = v_s * sqrt(4 pi N / S)
# g(omega) = 4N omega / w_D^2
# U(T) = int_0^{w_D} (4N / w_D^2) hbar w^2 / (exp(hbar w / kB T) - 1) dw
# Let x = hbar w / kB T: U(T) = 4N kB T (T / Theta_D)^2 int_0^{Theta_D/T} x^2 / (e^x - 1) dx
# Low T: int_0^inf x^2 / (e^x - 1) dx = 2 zeta(3) = 2.4041138
# U(T) = 8 zeta(3) N kB T^3 / Theta_D^2
# C_V = dU/dT = 24 zeta(3) N kB (T / Theta_D)^2
zeta3 = sum(1 / (k ** 3) for k in range(1, 50000))
# Check integral numerically
xs = np.linspace(1e-5, 50, 200000)
int_x2 = np.trapezoid((xs ** 2) / (np.exp(xs) - 1), xs)
assert math.isclose(int_x2, 2 * zeta3, rel_tol=1e-4)
print(f"2*zeta(3) = {2*zeta3:.5f} (num integral = {int_x2:.5f})")
print(f"2D C_V prefactor 24*zeta(3) = {24*zeta3:.3f}")

print("\n=== CH03-KP5-04: Anharmonic thermal expansion <x> ===")
# V(x) = c x^2 - g x^3 - f x^4
# Numerator: int x * (1 + g x^3/kBT + f x^4/kBT) exp(-c x^2/kBT) dx
#          = (g/kBT) int x^4 exp(-beta c x^2) dx  (odd terms x and x^5 vanish)
# Denominator (lowest order): int exp(-beta c x^2) dx
# Recall <x^4>_0 = 3 / (4 (beta c)^2) = 3 (kBT)^2 / (4 c^2)
# So <x> = (g/kBT) * 3 (kBT)^2 / (4 c^2) = 3 g kBT / (4 c^2)!
c_val, g_val, f_val, kBT_val = 10.0, 0.05, 0.01, 0.1
xgrid = np.linspace(-2.0, 2.0, 40001)
w_lin = (1 + (g_val * xgrid ** 3 + f_val * xgrid ** 4) / kBT_val) * np.exp(-c_val * xgrid ** 2 / kBT_val)
x_mean_num = np.trapezoid(xgrid * w_lin, xgrid) / np.trapezoid(np.exp(-c_val * xgrid ** 2 / kBT_val), xgrid)
x_mean_ana = 3 * g_val * kBT_val / (4 * c_val ** 2)
assert math.isclose(x_mean_num, x_mean_ana, rel_tol=1e-4)
print(f"Anharmonic <x> verified: ana={x_mean_ana:.6e}, num={x_mean_num:.6e}")
