import os
from typing import Callable, Final

import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import psi
from scipy.integrate import solve_ivp

# --- Model Constants ---
m: Final[float] = 0.5
"""Equivalent moving mass [kg]"""

b: Final[float] = 50.0
"""Viscous friction coefficient [N·s/m]"""

k: Final[float] = 8000.0
"""Spring stiffness [N/m]"""

A: Final[float] = np.pi * (6 / 100) ** 2
"""Effective diaphragm area where the pressure acts [m²]"""


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
    if t < 1.0:
        return 3 * psi
    else:
        return 15 * psi


# --- Initial Conditions ---
x0 = 0.0292  # Initial displacement [m]
v0 = 0.0  # Initial velocity [m/s]
y0 = [x0, v0]

# --- Simulation ---
t = np.linspace(0, 2, 5000)  # Simulation time [s]
sol = solve_ivp(model, [t[0], t[-1]], y0, t_eval=t, args=(P_input,))

# --- Model Outputs ---
x = sol.y[0]
"""Valve stem displacement [m]"""

v = sol.y[1]
"""Valve stem velocity [m/s]"""

# --- Plot results ---
fig, axs = plt.subplots(2, 1, figsize=(8, 6), constrained_layout=True)
fig.suptitle("Pneumatic Control Valve")

# Displacement
axs[0].plot(sol.t, x * 100, label="$x(t)$")
axs[0].set_xlabel("Time / s")
axs[0].set_ylabel("Displacement / cm")
axs[0].grid(True)
axs[0].legend()

# Velocity
axs[1].plot(sol.t, v, label="$v(t)$", color="tab:orange")
axs[1].set_xlabel("Time / s")
axs[1].set_ylabel("Velocity / m$\\cdot$s$^{-1}$")
axs[1].grid(True)
axs[1].legend()

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "simulations"), exist_ok=True)
save_path = os.path.join(script_dir, "simulations", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
