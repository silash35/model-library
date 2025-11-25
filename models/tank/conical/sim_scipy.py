import os
from typing import Final

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

# --- Model Constants ---
H: Final[float] = 4.0
"""Tank maximum height [m]"""

R: Final[float] = 1.5
"""Tank top radius [m]"""

k: Final[float] = 0.8
"""Outlet discharge parameter [m^2.5/s]"""


# --- System Dynamics ---
def model(t: float, h: float, q_in: float):
    """
    Differential equation for the tank level.

    Parameters:
    - t: time [s]
    - h: liquid level [m]
    - q_in: inlet flow [m^3/s]
    """

    dhdt = (H**2 / (np.pi * R**2)) * (q_in / (h**2) - k / np.sqrt(h**3))
    return dhdt


# --- Model Input ---
q_in = 1.5
"""Inlet flow rate [m^3/s]"""

# --- Simulation ---
h0 = 0.5  # Initial level [m]
t = np.linspace(0, 100, 1000)  # Simulation time [s]
sol = solve_ivp(model, [t[0], t[-1]], [h0], t_eval=t, args=(q_in,))

# --- Model Output ---
h = sol.y[0]
"""Liquid level [m]"""

# --- Plot results ---
plt.axhline(H, color="tab:red", linestyle="--", label="Tank Limits")
plt.plot(sol.t, h, label="$h(t)$")
plt.axhline(0, color="tab:red", linestyle="--")

plt.xlabel("Time / s")
plt.ylabel("Level / m")
plt.title("Conical Tank")
plt.grid(True)
plt.legend()

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "simulations"), exist_ok=True)
save_path = os.path.join(script_dir, "simulations", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
