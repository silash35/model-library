import os
from typing import Final

import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import zero_Celsius
from scipy.integrate import solve_ivp

# --- Model Constants ---
rho: Final = 1000.0
"""Liquid density (water) [kg/m^3]"""

cp: Final = 4180.0
"""Specific heat capacity (water) [J/(kg·K)]"""

rho_j: Final = 958.0
"""Condensate density (liquid water at 100°C) [kg/m^3]"""

lambda_j: Final = 2.256e6
"""Latent heat of condensation of water [J/kg]"""

A: Final = np.pi * (1.5**2)
"""Tank cross-sectional area [m^2]"""

k: Final = 0.12
"""Outlet discharge parameter [m^2.5/s]"""


# --- System Dynamics ---
def model(t: float, y: np.ndarray, q_in: float, q_j: float, T_in: float):
    """
    Differential equations for the tank system.

    Parameters:
    - t: time [s]
    - y: state vector
    - q_in: inlet flow [m^3/s]
    - q_j: jacket condensate flow [m^3/s]
    - T_in: inlet temperature [K]
    """
    L = y[0]  # Liquid level [m]
    T = y[1]  # Liquid temperature [K]

    dLdt = (q_in - k * np.sqrt(L)) / A

    heat_in = rho * q_in * cp * (T_in - T)
    heat_jacket = rho_j * q_j * lambda_j
    dTdt = (heat_in + heat_jacket) / (rho * A * L * cp)

    return [dLdt, dTdt]


# --- Model Inputs ---
q_in = 0.2
"""Inlet flow rate [m^3/s]"""

q_j: Final = 0.015
"""jacket condensate flow [m^3/s]"""

T_in: Final = zero_Celsius + 28.0
"""inlet temperature [K]"""

# --- Simulation ---
L0 = 0.5  # Initial level [m]
T0 = zero_Celsius + 28.0
y0 = [L0, T0]

t = np.linspace(0, 1000, 1000)  # Simulation time [s]
sol = solve_ivp(model, [t[0], t[-1]], y0, t_eval=t, args=(q_in, q_j, T_in))

# --- Model Output ---
L = sol.y[0]
"""Liquid level [m]"""

T = sol.y[1]
"""Liquid temperature [K]"""

# --- Plot results ---
t_min = sol.t / 60  # convert seconds to minutes

fig, axs = plt.subplots(2, 1, figsize=(8, 5), sharex=True, constrained_layout=True)
fig.suptitle("Heated Tank")

# Plot level
axs[0].plot(t_min, L, label="$L(t)$")
axs[0].axhline(0, color="tab:red", linestyle="--", label="Tank Limits")
axs[0].set_ylabel("Level / m")
axs[0].grid(True)
axs[0].legend()

# Plot temperature
axs[1].plot(t_min, T - zero_Celsius, label="$T(t)$", color="tab:orange")
axs[1].set_ylabel("Temperature / °C")
axs[1].grid(True)
axs[1].legend()

axs[-1].set_xlabel("Time / min")

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "simulations"), exist_ok=True)
save_path = os.path.join(script_dir, "simulations", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
