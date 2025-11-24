import os
from typing import Final

import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import g as gravity
from scipy.integrate import solve_ivp

# --- Model Constants ---
rho: Final[float] = 1000.0
"""Density of water [kg/m³]"""

g: Final[float] = gravity
"""Gravitational acceleration [m/s²]"""

gamma: Final[float] = rho * g
"""Specific weight [N/m³]"""

L: Final[float] = 4
"""Tank side length [m]"""

A: Final[float] = L**2
"""Cross-sectional area [m²]"""

D_p: Final[float] = 0.20
"""Pipe diameter [m]"""

A_p: Final[float] = np.pi * (D_p / 2) ** 2
"""Pipe cross-sectional area [m²]"""

L_p: Final[float] = 1.0
"""Pipe length [m]"""

m_p: Final[float] = rho * A_p * L_p
"""Mass of fluid inside the pipe [kg]"""

k_f: Final[float] = 1.0
"""Friction coefficient [kg/m]"""


# --- System Dynamics ---
def model(t: float, y: np.ndarray, Q_in: float):
    """
    Differential equations for the tank pipe system.

    Parameters:
    - t: time [s]
    - y: state vector
    - Q_in: inlet flow [m^3/s]
    """

    h = y[0]  # Liquid level [m]
    v_p = y[1]  # Outlet pipe velocity [m/s]

    dhdt = (Q_in - A_p * v_p) / A
    dvdt = (gamma * A_p * h - k_f * v_p**2) / m_p

    return [dhdt, dvdt]


# --- Model Input ---
Q_in = 1.0
"""Inlet flow rate [m^3/s]"""

# --- Initial Conditions ---
h0 = 0.1  # Initial level [m]
v0 = 0.0  # Initial velocity [m/s]
y0 = [h0, v0]

# --- Simulation ---
t = np.linspace(0, 600, 1000)  # Simulation time [s]
sol = solve_ivp(model, [t[0], t[-1]], y0, t_eval=t, args=(Q_in,))

# --- Model Outputs ---
h = sol.y[0]
"""Liquid level [m]"""

v_p = sol.y[1]
"""Outlet pipe velocity [m/s]"""

# --- Plot results ---
t_min = t / 60  # Convert time to minutes

fig, axs = plt.subplots(2, 1, figsize=(8, 5), constrained_layout=True)
fig.suptitle("Cubic Tank with Pumped Inlet and Gravity-Driven Outlet")

# Plot Liquid level
axs[0].axhline(L, color="tab:red", linestyle="--", label="Tank Limits")
axs[0].plot(t_min, h, label="$h(t)$")
axs[0].axhline(0, color="tab:red", linestyle="--")
axs[0].set_xlabel("Time / min")
axs[0].set_ylabel("Level / m")
axs[0].grid(True)
axs[0].legend()

# Plot angular velocity
axs[1].plot(t_min, v_p, label="$v_p(t)$", color="tab:orange")
axs[1].set_xlabel("Time / min")
axs[1].set_ylabel("Velocity / m$\\cdot$s$^{-1}$")
axs[1].grid(True)
axs[1].legend()

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "simulations"), exist_ok=True)
save_path = os.path.join(script_dir, "simulations", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
