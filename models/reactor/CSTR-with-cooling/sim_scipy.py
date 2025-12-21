import os
from typing import Final

import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import gas_constant, zero_Celsius
from scipy.integrate import solve_ivp

# --- Model Constants ---
rho: Final = 1000.0
"""Reactor fluid density [kg/m^3]"""

cp: Final = 239.0
"""Reactor fluid heat capacity [J/(kg·K)]"""

rho_c: Final = 1000.0
"""Coolant density [kg/m^3]"""

cp_c: Final = 4180.0
"""Coolant heat capacity [J/(kg·K)]"""

k0: Final = 1.2e9
"""Pre-exponential factor [1/s]"""

R: Final = gas_constant
"""Universal gas constant [J/(mol·K)]"""

E: Final = 8.75e3 * R
"""Activation energy [J/mol]"""

delta_Hr: Final = -5.0e7
"""Reaction enthalpy [J/mol] (negative for exothermic)"""

U: Final = 915.6
"""Overall heat transfer coefficient [W/(m^2·K)]"""

A: Final = 2.7520
"""Heat transfer area [m^2]"""

V_c: Final = 0.55
"""Cooling jacket volume [m^3]"""


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
    V = y[0]  # Reactor volume [m^3]
    C_A = y[1]  # Concentration of A [mol/m^3]
    T = y[2]  # Reactor temperature [K]
    T_c = y[3]  # Coolant temperature [K]

    # Inputs
    q1 = u[0]  # Inlet flow rate [m^3/s]
    q = u[1]  # Outlet flow rate [m^3/s]
    C_A1 = u[2]  # Inlet concentration of A [mol/m^3]
    T1 = u[3]  # Inlet temperature [K]

    q_c = u[4]  # Coolant flow rate [m^3/s]
    T_c0 = u[5]  # Coolant inlet temperature [K]

    # Reaction rate (Arrhenius)
    Gamma = k0 * np.exp(-E / (R * T)) * C_A  # [mol/(m^3·s)]

    # --- Balances ---
    dVdt = q1 - q

    dCAdt = ((C_A1 - C_A) * q1 - Gamma * V) / V

    dTdt = (rho * q1 * cp * (T1 - T) + (-delta_Hr) * Gamma * V + U * A * (T_c - T)) / (
        rho * V * cp
    )

    dTcdt = (rho_c * q_c * cp_c * (T_c0 - T_c) - U * A * (T_c - T)) / (
        rho_c * V_c * cp_c
    )

    return [dVdt, dCAdt, dTdt, dTcdt]


# --- Model Inputs ---
q1 = 0.1
"""Inlet 1 volumetric flow rate [m^3/s]"""

q = q1
"""Outlet volumetric flow rate [m^3/s]"""

C_A1 = 1.0
"""Species A concentration in inlet 1 [mol/m^3]"""

T1 = zero_Celsius + 50.0
"""Temperature of inlet 1 [K]"""

q_c = 0.005
"""Coolant volumetric flow rate [m^3/s]"""

T_c0 = zero_Celsius + 20.0
"""Coolant inlet temperature [K]"""

u = np.array([q1, q, C_A1, T1, q_c, T_c0])
"""Inputs vector"""

# --- Initial Conditions ---
V0 = 1.5  # Initial liquid volume [m^3]
C_A0 = 0.9  # Initial concentration of A [mol/m^3]
T0 = zero_Celsius + 25.0  # Initial liquid temperature [K]
T_c_init = zero_Celsius + 20.0  # Initial coolant temperature [K]
y0 = [V0, C_A0, T0, T_c_init]

# --- Simulation ---
t = np.linspace(0, 60 * 20, 1000)  # Simulation time [s]
sol = solve_ivp(model, [t[0], t[-1]], y0, t_eval=t, args=(u,), method="LSODA")

# --- Model Output ---
V = sol.y[0]
"""Liquid volume [m^3]"""

C_A = sol.y[1]
"""Concentration of species A [mol/m^3]"""

T = sol.y[2]
"""Liquid temperature [K]"""

T_c = sol.y[3]
"""Coolant temperature [K]"""

# --- Plot results ---
t_min = sol.t / 60  # convert seconds to minutes

fig, axs = plt.subplots(3, 1, figsize=(8, 8), sharex=True, constrained_layout=True)
fig.suptitle("CSTR with Cooling Jacket")

axs[0].plot(t_min, V, label="$V(t)$")
axs[0].axhline(0, color="tab:red", linestyle="--", label="Tank Limit")
axs[0].set_ylabel("Liquid volume / m$^3$")

axs[1].plot(t_min, C_A, label="$C_A(t)$")
axs[1].plot(t_min, np.full_like(t_min, C_A1), label="$C_{A,1}(t)$")
axs[1].set_ylabel("Concentration / mol$\\cdot$m$^{-3}$")

axs[2].plot(t_min, T - zero_Celsius, color="tab:orange", label="$T(t)$")
axs[2].plot(t_min, T_c - zero_Celsius, color="tab:blue", label="$T_c(t)$")
axs[2].set_ylabel("Temperature / °C")

for ax in axs:
    ax.legend()
    ax.grid(True)

axs[-1].set_xlabel("Time / min")

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "simulations"), exist_ok=True)
save_path = os.path.join(script_dir, "simulations", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
