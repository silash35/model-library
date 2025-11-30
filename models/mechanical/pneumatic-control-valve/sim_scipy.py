import os
from collections.abc import Callable
from typing import Final

import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import psi
from scipy.integrate import solve_ivp

# --- Model Constants ---
m: Final[float] = 0.5
"""Equivalent moving mass [kg]"""

b: Final[float] = 200.0
"""Viscous friction coefficient [N·s/m]"""

k: Final[float] = 8000.0
"""Spring stiffness [N/m]"""

A: Final[float] = np.pi * (6 / 100) ** 2
"""Effective diaphragm area where the pressure acts [m²]"""

x_min: Final[float] = 2.92 / 100
"""Fully open position [m]"""

x_max: Final[float] = 14.62 / 100
"""Fully closed position [m]"""


# --- System Dynamics ---
def model(t: float, y: np.ndarray, P_func: Callable[[float], float]):
    """
    Differential equation for the pneumatic control valve.

    Parameters:
    - t: time [s]
    - y: state vector
    - P_func: function returning the pneumatic pressure [Pa]
    """
    x = y[0]  # Displacement [m]
    v = y[1]  # Velocity [m/s]
    P = P_func(t)  # Pressure input [Pa]

    # Derivatives
    dxdt = v
    dvdt = (A * P - b * v - k * x) / m

    return [dxdt, dvdt]


# --- Model Input ---
def P_input(t: float) -> float:
    """Example pneumatic control signal [Pa]

    Follows the Standard industrial signal:
    - 3 psi: valve fully open
    - 15 psi: valve fully closed
    """
    if t < 0.5:
        return 3 * psi
    else:
        return 15 * psi


# --- Initial Conditions ---
x0 = x_min  # Initial displacement [m]
v0 = 0.0  # Initial velocity [m/s]
y0 = [x0, v0]

# --- Simulation ---
t = np.linspace(0, 1, 1000)  # Simulation time [s]
sol = solve_ivp(model, [t[0], t[-1]], y0, t_eval=t, args=(P_input,))

# --- Model Outputs ---
x = sol.y[0]
"""Valve stem displacement [m]"""

v = sol.y[1]
"""Valve stem velocity [m/s]"""

# --- Plot results ---
fig, axs = plt.subplots(2, 1, figsize=(8, 6), sharex=True, constrained_layout=True)
fig.suptitle("Pneumatic Control Valve")

# Pressure input
P = np.array([P_input(t) for t in sol.t]) / psi
axs[0].plot(sol.t, P, label="$P(t)$", color="tab:orange")
axs[0].set_ylabel("Pressure / psi")
axs[0].grid(True)
axs[0].legend()

# Displacement
axs[1].axhline(x_min * 100, color="tab:red", linestyle="--", label="Valve Limits")
axs[1].plot(sol.t, x * 100, label="$x(t)$")
axs[1].axhline(x_max * 100, color="tab:red", linestyle="--")

axs[1].set_ylabel("Displacement / cm")
axs[1].grid(True)
axs[1].legend()

axs[-1].set_xlabel("Time / s")

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "simulations"), exist_ok=True)
save_path = os.path.join(script_dir, "simulations", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
