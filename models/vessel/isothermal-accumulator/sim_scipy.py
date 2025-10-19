import os
from typing import Final

import matplotlib.pyplot as plt
import numpy as np
from scipy import constants as C
from scipy.integrate import solve_ivp

# --- Model Constants ---
V: Final[float] = 1
"""Vessel volume [m^3]"""

R: Final[float] = C.R
"""Universal gas constant [J/(mol*K)]"""

MM: Final[float] = 0.0289647
"""Molar mass of gas (air) [kg/mol]"""

T: Final[float] = 293
"""Gas temperature [K]"""

k1: Final[float] = 0.01
"""Inlet flow coefficient [kg/(s*Pa^0.5)]"""

k2: Final[float] = 0.015
"""Outlet flow coefficient [kg/(s*Pa^0.5)]"""


# --- Vessel Dynamics ---
def vessel_model(t: float, P: float, P1: float, P2: float):
    """
    Differential equation for the vessel pressure.

    Parameters:
    - t: time [s]
    - P: pressure inside the vessel [m]
    - P1: inlet pressure [Pa]
    - P2: outlet pressure [Pa]
    """
    dPdt = (R * T / (V * MM)) * (k1 * np.sqrt(P1 - P) - k2 * np.sqrt(P - P2))
    return dPdt


# --- Model Inputs ---
P1 = C.atm * 2
"""Inlet pressure [Pa]"""

P2 = C.atm
"""Outlet pressure [Pa]"""

# --- Simulation ---
P0 = C.atm * 1.5  # Initial pressure [Pa]
t = np.linspace(0, 3, 1000)  # Simulation time [s]
sol = solve_ivp(vessel_model, [t[0], t[-1]], [P0], t_eval=t, args=(P1, P2))

# --- Model Outputs ---
P = sol.y[0]
"""Pressure inside the vessel [Pa]"""

# --- Plot results ---
# Convert pressure from Pa to bar for easier visualization
plt.plot(sol.t, P1 * 1e-5 * np.ones_like(sol.t), label="$P_1(t)$")
plt.plot(sol.t, P * 1e-5, label="$P(t)$")
plt.plot(sol.t, P2 * 1e-5 * np.ones_like(sol.t), label="$P_2(t)$")

plt.xlabel("Time / s")
plt.ylabel("Pressure / Bar")
plt.title("Pressurized Isothermal Gas Vessel")
plt.grid(True)
plt.legend()

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "simulations"), exist_ok=True)
save_path = os.path.join(script_dir, "simulations", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
