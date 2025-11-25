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

k_f: Final[float] = 1.0
"""Friction coefficient [kg/m]"""

alpha = A_p * np.sqrt(gamma * A_p / k_f)
"""Outlet discharge parameter [m^{2.5}/s]"""


# --- System Dynamics ---
def model(t: float, h: float, Q_in: float):
    """
    Differential equation for the tank level.

    Parameters:
    - t: time [s]
    - h: liquid level [m]
    - Q_in: inlet flow [m^3/s]
    """

    dhdt = (Q_in - alpha * np.sqrt(h)) / A

    return dhdt


# --- Model Input ---
Q_in = 1.0
"""Inlet flow rate [m^3/s]"""

# --- Simulation ---
h0 = 0.1  # Initial level [m]
t = np.linspace(0, 600, 1000)  # Simulation time [s]
sol = solve_ivp(model, [t[0], t[-1]], [h0], t_eval=t, args=(Q_in,))

# --- Model Output ---
h = sol.y[0]
"""Liquid level [m]"""

# --- Plot results ---
plt.axhline(L, color="tab:red", linestyle="--", label="Tank Limits")
plt.plot(sol.t, h, label="$h(t)$")
plt.axhline(0, color="tab:red", linestyle="--")

plt.xlabel("Time / s")
plt.ylabel("Level / m")
plt.title("Cubic Tank")
plt.grid(True)
plt.legend()

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "simulations"), exist_ok=True)
save_path = os.path.join(script_dir, "simulations", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
