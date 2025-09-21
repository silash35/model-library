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


# --- Tank dynamics ---
def tank_model(t: float, h: float, Q_in: float, Q_out: float):
    """
    Differential equation for the tank level.

    Parameters:
    - h: liquid level [m]
    - t: time [s]
    - Q_in: inlet flow [m^3/s]
    - Q_out: outlet flow [m^3/s]
    """
    dhdt = (Q_in - Q_out) / A

    # Ensure the level stays within physical limits of the cubic tank
    if h <= 0 and dhdt < 0:
        # Tank is empty and the level would decrease
        dhdt = 0
    elif h >= L and dhdt > 0:
        # Tank is full and the level would increase
        dhdt = 0

    return dhdt


# --- Model Parameters ---
Q_in = 0.3  # Inlet flow rate [m^3/s]
Q_out = 0.7  # Outlet flow rate [m^3/s]

# --- Simulation ---
h0 = 2  # Initial liquid level [m]
t = np.linspace(0, 100, 1000)  # Simulation time [s]
sol = solve_ivp(tank_model, [t[0], t[-1]], [h0], t_eval=t, args=(Q_in, Q_out))

# --- Plot results ---
plt.axhline(L, color="tab:red", linestyle="--", label="Tank Limits")
plt.plot(sol.t, sol.y[0], label="$h(t)$")
plt.axhline(0, color="tab:red", linestyle="--")

plt.xlabel("Time / s")
plt.ylabel("Level / m")
plt.title("Cubic Tank with Pumped Inlet and Outlet")
plt.grid(True)
plt.legend()

script_dir = os.path.dirname(os.path.abspath(__file__))
save_path = os.path.join(script_dir, "simulations", "scipy.png")
plt.savefig(save_path)
