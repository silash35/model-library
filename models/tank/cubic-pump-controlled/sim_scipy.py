import os
from typing import Final

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

# --- Model Constants ---
L: Final[float] = 4
"""Tank side length [m]"""

A: Final[float] = L**2
"""Cross-sectional area [m^2]"""


# --- Tank Dynamics ---
def tank_model(t: float, h: float, Q_in: float, Q_out: float):
    """
    Differential equation for the tank level.

    Parameters:
    - t: time [s]
    - h: liquid level [m]
    - Q_in: inlet flow [m^3/s]
    - Q_out: outlet flow [m^3/s]
    """
    dhdt = (Q_in - Q_out) / A
    return dhdt


# --- Model Inputs ---
Q_in = 0.3
"""Inlet flow rate [m^3/s]"""

Q_out = 0.5
"""Outlet flow rate [m^3/s]"""

# --- Simulation ---
h0 = 2  # Initial level [m]
t = np.linspace(0, 100, 1000)  # Simulation time [s]
sol = solve_ivp(tank_model, [t[0], t[-1]], [h0], t_eval=t, args=(Q_in, Q_out))

# --- Model Output ---
h = sol.y[0]
"""Liquid level [m]"""

# --- Plot results ---
plt.axhline(L, color="tab:red", linestyle="--", label="Tank Limits")
plt.plot(sol.t, h, label="$h(t)$")
plt.axhline(0, color="tab:red", linestyle="--")

plt.xlabel("Time / s")
plt.ylabel("Level / m")
plt.title("Cubic Tank with Pumped Inlet and Outlet")
plt.grid(True)
plt.legend()

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "simulations"), exist_ok=True)
save_path = os.path.join(script_dir, "simulations", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
