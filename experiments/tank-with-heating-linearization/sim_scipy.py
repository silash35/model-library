import os
from typing import Callable, Final, List

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from scipy.constants import zero_Celsius
from scipy.integrate import solve_ivp

# --- Model Constants ---
rho: Final = 1000.0  # Liquid density (water) [kg/m^3]
cp: Final = 4180.0  # Specific heat capacity (water) [J/(kg·K)]
rho_j: Final = 958.0  # Condensate density (liquid water at 100°C) [kg/m^3]
lambda_j: Final = 2.256e6  # Latent heat of condensation of water [J/kg]
A_c: Final = np.pi * (1.5**2)  # Tank cross-sectional area [m^2]
k: Final = 0.12  # Outlet discharge parameter [m^2.5/s]

# --- Symbolic Model ---
t_sym = sp.symbols("t")  # Time [s]

# System states
L_sym = sp.symbols("L")  # liquid level [m]
T_sym = sp.symbols("T")  # liquid temperature [K]
states = sp.Matrix([L_sym, T_sym])  # x

# System inputs
q_in_sym = sp.symbols("q_in")  # Inlet volumetric flow rate [m^3/s]
q_j_sym = sp.symbols("q_j")  # Jacket flow rate [kg/s]
T_in_sym = sp.symbols("T_in")  # Temperature of the inlet liquid [K]
inputs = sp.Matrix([q_in_sym, q_j_sym, T_in_sym])  # u

# Symbolic Differential equations
f = sp.Matrix(
    [
        (q_in_sym - k * (L_sym**0.5)) / A_c,
        (rho * q_in_sym * cp * (T_in_sym - T_sym) + rho_j * q_j_sym * lambda_j)
        / (rho * A_c * L_sym * cp),
    ]
)

# Numpy version for fast evaluation
f_func = sp.lambdify((L_sym, T_sym, q_in_sym, q_j_sym, T_in_sym), f, "numpy")


# --- Model Inputs ---
def q_in(t):
    """Inlet flow rate [m^3/s]"""
    if t > 2000:
        return 0.6
    elif t > 1000:
        return 0.5
    elif t > 100:
        return 0.22
    else:
        return 0.4


def q_j(t):
    """jacket condensate flow [m^3/s]"""
    if t > 1500:
        return 0.035
    elif t > 1000:
        return 0.002
    else:
        return 0.015


def T_in(t):
    """inlet temperature [K]"""
    if t > 2500:
        Tin = 40
    elif t > 2000:
        Tin = 20
    else:
        Tin = 30

    return Tin + zero_Celsius


u_funcs = [q_in, q_j, T_in]

# --- Linearization ---
# Linearization point (steady-state values)
L0 = 11.111111111111086
T0 = 322.5391866028708

x0 = np.array([L0, T0])  # States: [level, temperature]
u0 = np.array([q_in(0), q_j(0), T_in(0)])  # Inputs: [q_in, q_j, T_in]

subs_state = {
    L_sym: x0[0],
    T_sym: x0[1],
    q_in_sym: u0[0],
    q_j_sym: u0[1],
    T_in_sym: u0[2],
}

# Compute the Jacobians at the linearization point
A = np.array(f.jacobian(states).subs(subs_state))
B = np.array(f.jacobian(inputs).subs(subs_state))


# --- Differential Equations for Simulation ---
def nonlinear_diff_eq(t: float, x: np.ndarray, u_funcs: List[Callable[[float], float]]):
    L, T = x
    q_in, q_j, T_in = u_funcs

    dxdt = f_func(L, T, q_in(t), q_j(t), T_in(t))
    return dxdt.flatten()


def linear_diff_eq(
    t: float, x_bar: np.ndarray, u_funcs: List[Callable[[float], float]]
):
    u = np.array([u_func(t) for u_func in u_funcs])
    u_bar = u - u0  # Calc input deviations

    dx_bar_dt = A @ x_bar + B @ u_bar
    return dx_bar_dt


# --- Simulation ---
t = np.linspace(0, 3500, 1000)  # Simulation time [s]

# Nonlinear simulation
sol = solve_ivp(
    nonlinear_diff_eq, [t[0], t[-1]], x0, t_eval=t, args=(u_funcs,), method="LSODA"
)
L, T = sol.y

# Linear Simulation
sol_linear = solve_ivp(linear_diff_eq, [t[0], t[-1]], [0, 0], t_eval=t, args=(u_funcs,))
# The linearized simulation returns the deviations from the linearization point
L_bar, T_bar = sol_linear.y

# To get the absolute states, add the linearization point (x0) back
L_linear = L_bar + L0
T_linear = T_bar + T0

# --- Plot results ---
t_min = sol.t / 60  # convert seconds to minutes

# Get input values for plot
q_in_values = np.array([q_in(t) for t in sol.t])
q_j_values = np.array([q_j(t) for t in sol.t])
T_in_values = np.array([T_in(t) for t in sol.t])


fig, axs = plt.subplots(5, 1, figsize=(8, 10), constrained_layout=True, sharex=True)
fig.suptitle("Heated Tank")

# Plot inputs
axs[0].plot(t_min, q_in_values)
axs[0].set_ylabel("Inlet flow rate / m$^3\\cdot$s$^{-1}$")

axs[1].plot(t_min, q_j_values)
axs[1].set_ylabel("Jacket flow rate / m$^3\\cdot$s$^{-1}$")

axs[2].plot(t_min, T_in_values - zero_Celsius)
axs[2].set_ylabel("Inlet temperature / °C")

# Plot states
axs[3].plot(t_min, L, label="$L(t)$")
axs[3].plot(t_min, L_linear, label="$L(t)$ linear")
axs[3].axhline(0, color="tab:red", linestyle="--", label="Tank Limit")
axs[3].set_ylabel("Level / m")
axs[3].legend()

axs[4].plot(t_min, T - zero_Celsius, label="$T(t)$")
axs[4].plot(t_min, T_linear - zero_Celsius, label="$T(t)$ linear")
axs[4].set_ylabel("Temperature / °C")
axs[4].legend()

for ax in axs:
    ax.grid(True)
axs[-1].set_xlabel("Time / min")

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "results"), exist_ok=True)
save_path = os.path.join(script_dir, "results", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
