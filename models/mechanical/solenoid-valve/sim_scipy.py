import os
from typing import Callable, Final

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

# --- Model Constants ---
m: Final[float] = 0.02
"""Equivalent moving mass [kg]"""

c: Final[float] = 50.0
"""Viscous damping coefficient [N·s/m]"""

k: Final[float] = 500.0
"""Spring stiffness [N/m]"""

R: Final[float] = 2.0
"""Coil electrical resistance [Ω]"""

A: Final[float] = (2.5 / 100) ** 2 * np.pi
"""Effective area where the fluid pressure acts [m²]"""

L0: Final[float] = 0.005
"""Inductance model constant [H]"""

L1: Final[float] = 0.0005
"""Inductance model constant [H·m]"""

g0: Final[float] = 4.0 / 100
"""Inductance model constant [m]"""

x_min: Final[float] = 0 / 100
"""Fully closed position [m]"""

x_max: Final[float] = 3.0 / 100
"""Fully open position [m]"""


# --- Algebraic Functions ---
def L(x: float) -> float:
    """Inductance as a function of displacement [H]"""
    return L0 + L1 / (g0 - x)


def dLdx(x: float) -> float:
    """Derivative of inductance with respect to displacement [H/m]"""
    return L1 / (g0 - x) ** 2


def alpha(x: float) -> float:
    """Opening factor (0 = closed, 1 = fully open)"""
    return x / x_max


def F_fluid(x: float, dP: float) -> float:
    """Fluid force [N]"""
    return dP * A * alpha(x)


def F_magnetic(i: float, x: float) -> float:
    """Magnetic force [N]"""
    return 0.5 * dLdx(x) * i**2


# --- System Dynamics ---
def model(
    t: float,
    y: np.ndarray,
    u_func: Callable[[float], float],
    dP_func: Callable[[float], float],
):
    """
    Differential equation for the pneumatic control valve.

    Parameters:
    - t: time [s]
    - y: state vector
    - u_func: function returning the applied coil voltage [V]
    - P_func: function returning the pressure differential [Pa]
    """
    x = y[0]  # Displacement [m]
    v = y[1]  # Velocity [m/s]
    i = y[2]  # Coil current [A]

    u = u_func(t)  # Applied coil voltage [V]
    dP = dP_func(t)  # Pressure differential [Pa]

    # Enforce position limits
    x = np.clip(x, x_min, x_max)

    # Derivatives
    dxdt = v
    dvdt = (F_magnetic(i, x) - c * v - k * x - F_fluid(x, dP)) / m
    di_dt = (u - R * i - i * dLdx(x) * v) / L(x)

    return [dxdt, dvdt, di_dt]


# --- Model Input ---
def u_input(t: float) -> float:
    """Example voltage input [V]"""
    if t < 0.2:
        return 0.0
    elif t < 0.6:
        return 12.0

    return 24.0


def dP_input(t: float) -> float:
    """Example pressure differential [Pa]"""
    return 20000.0


# --- Initial Conditions ---
x0 = x_min  # Initial displacement [m]
v0 = 0.0  # Initial velocity [m/s]
i0 = 0.0  # Initial current [A]
y0 = [x0, v0, i0]

# --- Simulation ---
t = np.linspace(0, 1, 1000)  # Simulation time [s]
sol = solve_ivp(model, [t[0], t[-1]], y0, t_eval=t, args=(u_input, dP_input))

# --- Model Outputs ---
x = sol.y[0]
"""Valve plunger displacement [m]"""

v = sol.y[1]
"""Valve plunger velocity [m/s]"""

i = sol.y[2]
"""Coil current [A]"""

# Enforce position limits on output
x = np.clip(x, x_min, x_max)

# --- Plot results ---
fig, axs = plt.subplots(3, 1, figsize=(8, 8), sharex=True, layout="tight")
fig.suptitle("Solenoid Valve")

# Voltage input
u = np.array([u_input(t) for t in sol.t])
axs[0].plot(sol.t, u, label="$u(t)$")
axs[0].set_ylabel("Coil Voltage / V")

# Displacement
axs[1].axhline(x_min * 100, color="tab:red", linestyle="--", label="Valve Limits")
axs[1].plot(sol.t, x * 100, label="$x(t)$")
axs[1].axhline(x_max * 100, color="tab:red", linestyle="--")
axs[1].set_ylabel("Displacement / cm")

# Current
axs[2].plot(sol.t, i, label="$i(t)$")
axs[2].set_ylabel("Coil Current / A")

for ax in axs:
    ax.grid(True)
    ax.legend()
axs[-1].set_xlabel("Time / s")

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "simulations"), exist_ok=True)
save_path = os.path.join(script_dir, "simulations", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
