import os
from typing import Callable, Final, List

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from scipy.constants import zero_Celsius
from scipy.integrate import solve_ivp

# --- Model Constants ---
rho: Final[float] = 1000.0  # Liquid density (water) [kg/m^3]
cp: Final[float] = 4180.0  # Specific heat capacity (water) [J/(kg·K)]
rho_j: Final[float] = 958.0  # Condensate density (liquid water at 100°C) [kg/m^3]
lambda_j: Final[float] = 2.256e6  # Latent heat of condensation of water [J/kg]
A_c: Final[float] = np.pi * (1.5**2)  # Tank cross-sectional area [m^2]
k: Final[float] = 0.12  # Outlet discharge parameter [m^2.5/s]

# --- SymPy definitions ---
t_sym = sp.symbols("t")  # Time [s]

# System states
L_sym = sp.symbols("L")  # liquid level [m]
T_sym = sp.symbols("T")  # liquid temperature [K]
states = sp.Matrix([L_sym, T_sym])

# System inputs
q_in_sym = sp.symbols("q_in")  # Inlet volumetric flow rate [m^3/s]
q_j_sym = sp.symbols("q_j")  # Jacket flow rate [kg/s]
T_in_sym = sp.symbols("T_in")  # Temperature of the inlet liquid [K]
inputs = sp.Matrix([q_in_sym, q_j_sym, T_in_sym])

# Differential equations
f = sp.Matrix(
    [
        (q_in_sym - k * sp.sqrt(L_sym)) / A_c,  # type: ignore
        (rho * q_in_sym * cp * (T_in_sym - T_sym) + rho_j * q_j_sym * lambda_j)
        / (rho * A_c * L_sym * cp),
    ]
)


# --- Model Inputs ---
def q_in(t):
    """Inlet flow rate [m^3/s]"""
    if t > 2000:
        return 0.3
    elif t > 100:
        return 0.4
    return 0.2


def q_j(t):
    """jacket condensate flow [m^3/s]"""
    return 0.015 if t < 1000 else 0.014


def T_in(t):
    """inlet temperature [K]"""
    Tin = 28.0 if t < 2000 else 35.0
    return Tin + zero_Celsius


# --- Non Linear Simulation ---
def diff_equations(t: float, y: np.ndarray, u: List[Callable[[float], float]]):
    L, T = y
    q_in, q_j, T_in = u

    subs = {L_sym: L, T_sym: T, q_in_sym: q_in(t), q_j_sym: q_j(t), T_in_sym: T_in(t)}

    dfdt = f.subs(subs)
    return np.array(dfdt).flatten()


# --- Simulation ---

# Steady State Initial Conditions
L0 = 2.7777777777777777
T0 = zero_Celsius + 66.7374697102436
y0 = [L0, T0]

t = np.linspace(0, 5000, 1000)  # Simulation time [s]
sol = solve_ivp(diff_equations, [t[0], t[-1]], y0, t_eval=t, args=([q_in, q_j, T_in],))

# --- Model Outputs ---
L, T = sol.y

# --- Linear Simulation ---
subs_state = {
    L_sym: L0,
    T_sym: T0,
    q_in_sym: q_in(0),
    q_j_sym: q_j(0),
    T_in_sym: T_in(0),
}
A = np.array(f.jacobian(states).subs(subs_state))
B = np.array(f.jacobian(inputs).subs(subs_state))


def linear_diff_equations(
    t: float, x_bar: np.ndarray, u_func: List[Callable[[float], float]]
):
    q_in, q_j, T_in = u_func
    u = np.array([q_in(t), q_j(t), T_in(t)])
    u_bar = u - np.array([0.2, 0.015, 28.0 + zero_Celsius])

    x = A @ x_bar + B @ u_bar
    return x


sol_linear = solve_ivp(
    linear_diff_equations, [t[0], t[-1]], [0, 0], t_eval=t, args=([q_in, q_j, T_in],)
)
L_linear, T_linear = sol_linear.y
L_linear = L_linear + L0
T_linear = T_linear + T0


# --- Plot results ---
t_min = sol.t / 60  # convert seconds to minutes

fig, axs = plt.subplots(2, 1, figsize=(8, 5), constrained_layout=True)
fig.suptitle("Heated Tank")

# Plot level
axs[0].plot(t_min, L, label="$L(t)$")
axs[0].plot(t_min, L_linear, label="$L(t)$ linear")
axs[0].axhline(0, color="tab:red", linestyle="--", label="Tank Limits")
axs[0].set_xlabel("Time / min")
axs[0].set_ylabel("Level / m")
axs[0].grid(True)
axs[0].legend()

# Plot temperature
axs[1].plot(t_min, T - zero_Celsius, label="$T(t)$")
axs[1].plot(t_min, T_linear - zero_Celsius, label="$T(t)$ linear")
axs[1].set_xlabel("Time / min")
axs[1].set_ylabel("Temperature / °C")
axs[1].grid(True)
axs[1].legend()

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "results"), exist_ok=True)
save_path = os.path.join(script_dir, "results", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
