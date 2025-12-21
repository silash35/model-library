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

rho_c: Final = 958.0
"""Condensate density (liquid water at 100°C) [kg/m^3]"""

lambda_c: Final = 2.256e6
"""Latent heat of condensation of water [J/kg]"""


# --- System Dynamics ---
def model(t: float, y: np.ndarray, u: np.ndarray):
    """
    Differential equations for the tank system.

    Parameters:
    - t: time [s]
    - y: state vector
    - u: Input vector
    """
    # States
    V = y[0]  # Liquid volume [m^3]
    C_A = y[1]  # Concentration of species A [mol/m^3]
    C_B = y[2]  # Concentration of species B [mol/m^3]
    T = y[3]  # Liquid temperature [K]

    # Inputs
    q1 = u[0]  # Inlet 1 flow rate [m^3/s]
    q2 = u[1]  # Inlet 2 flow rate [m^3/s]
    q = u[2]  # Outlet flow rate [m^3/s]

    C_A1 = u[3]  # Species A concentration in inlet 1 [mol/m^3]
    C_A2 = u[4]  # Species A concentration in inlet 2 [mol/m^3]
    C_B1 = u[5]  # Species B concentration in inlet 1 [mol/m^3]
    C_B2 = u[6]  # Species B concentration in inlet 2 [mol/m^3]

    T1 = u[7]  # Temperature of inlet 1 [K]
    T2 = u[8]  # Temperature of inlet 2 [K]

    q_c = u[9]  # Condensate volumetric flow rate [m^3/s]

    dVdt = q1 + q2 - q
    dCAdt = ((C_A1 - C_A) * q1 + (C_A2 - C_A) * q2) / V
    dCBdt = ((C_B1 - C_B) * q1 + (C_B2 - C_B) * q2) / V

    heat_in = (
        rho * q1 * cp * (T1 - T) + rho * q2 * cp * (T2 - T) + rho_c * q_c * lambda_c
    )
    dTdt = heat_in / (rho * V * cp)

    return [dVdt, dCAdt, dCBdt, dTdt]


# --- Model Inputs ---
q1 = 0.10
"""Inlet 1 volumetric flow rate [m^3/s]"""

q2 = 0.08
"""Inlet 2 volumetric flow rate [m^3/s]"""

q = q1 + q2
"""Outlet volumetric flow rate [m^3/s]"""

C_A1 = 2.0
"""Species A concentration in inlet 1 [mol/m^3]"""

C_A2 = 1.5
"""Species A concentration in inlet 2 [mol/m^3]"""

C_B1 = 3.0
"""Species B concentration in inlet 1 [mol/m^3]"""

C_B2 = 2.5
"""Species B concentration in inlet 2 [mol/m^3]"""

T1 = zero_Celsius + 25.0
"""Temperature of inlet 1 [K]"""

T2 = zero_Celsius + 35.0
"""Temperature of inlet 2 [K]"""

q_c = 0.015
"""Flow rate of the condensate leaving the heating coil [m^3/s]"""

u = np.array([q1, q2, q, C_A1, C_A2, C_B1, C_B2, T1, T2, q_c])
"""Inputs vector"""

# --- Simulation ---
V0 = 2.0  # Initial Liquid volume [m^3]
C_A0 = 1.0  # Initial Concentration of species A [mol/m^3]
C_B0 = 1.0  # Initial Concentration of species B [mol/m^3]
T0 = zero_Celsius + 28.0  # Initial Liquid temperature [K]
y0 = [V0, C_A0, C_B0, T0]

t = np.linspace(0, 50, 1000)  # Simulation time [s]
sol = solve_ivp(model, [t[0], t[-1]], y0, t_eval=t, args=(u,))

# --- Model Output ---
V = sol.y[0]
"""Liquid volume [m^3]"""
C_A = sol.y[1]
"""Concentration of species A [mol/m^3]"""
C_B = sol.y[2]
"""Concentration of species B [mol/m^3]"""
T = sol.y[3]
"""Liquid temperature [K]"""

# --- Plot results ---
t_min = sol.t / 60  # convert seconds to minutes

fig, axs = plt.subplots(3, 1, figsize=(8, 8), sharex=True, constrained_layout=True)
fig.suptitle("Mixer with Heating")

# Plot level
axs[0].plot(t_min, V, label="$V(t)$")
axs[0].axhline(0, color="tab:red", linestyle="--", label="Tank Limit")
axs[0].set_ylabel("Liquid volume / m$^3$")
axs[0].legend()

# Plot Concentrations
axs[1].plot(t_min, np.full_like(t_min, C_A), label="$C_A(t)$")
axs[1].plot(t_min, np.full_like(t_min, C_B), label="$C_B(t)$")
axs[1].plot(t_min, np.full_like(t_min, C_A1), label="$C_{A,1}(t)$")
axs[1].plot(t_min, np.full_like(t_min, C_A2), label="$C_{A,2}(t)$")
axs[1].plot(t_min, np.full_like(t_min, C_B1), label="$C_{B,1}(t)$")
axs[1].plot(t_min, np.full_like(t_min, C_B2), label="$C_{B,2}(t)$")

axs[1].set_ylabel("Concentration / mol$\\cdot$m$^{-3}$")
axs[1].legend()

# Plot temperature
axs[2].plot(t_min, T - zero_Celsius, color="tab:orange")
axs[2].set_ylabel("Liquid Temperature / °C")

for ax in axs:
    ax.grid(True)

axs[-1].set_xlabel("Time / min")

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "simulations"), exist_ok=True)
save_path = os.path.join(script_dir, "simulations", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
