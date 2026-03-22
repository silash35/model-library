import os
from typing import Final

import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import zero_Celsius
from scipy.integrate import solve_ivp

# --- Model Constants ---
rho: Final = 1000.0
"""Fluid density [kg/m³]"""

Cp: Final = 4.2
"""Heat capacity [kJ/kg·K]"""

m: Final = 0.00279
"""Molality [kmol/kg]"""

R: Final = 8.314
"""Universal gas constant [kJ/kmol·K]"""

k1: Final = 2.77e3 * 3600
"""Pre-exponential factor for reaction A -> B [1/h]"""

k2: Final = 2.5e3 * 3600
"""Pre-exponential factor for reaction B -> C [1/h]"""

E1: Final = 5.0e4
"""Activation energy for reaction A -> B [kJ/kmol]"""

E2: Final = 6.0e4
"""Activation energy for reaction B -> C [kJ/kmol]"""

dH1: Final = -6.0e4
"""Heat of reaction A -> B [kJ/kmol]"""

dH2: Final = -7.0e4
"""Heat of reaction B -> C [kJ/kmol]"""

alphaA: Final = 5.0
"""Relative volatility of component A [-]"""

alphaB: Final = 1.0
"""Relative volatility of component B [-]"""

alphaC: Final = 0.5
"""Relative volatility of component C [-]"""

eps: Final = 0.02
"""Purge ratio (FP = eps * FR) [-]"""

xA0 = 1.0
"""Feed mole fraction of component A [-]"""

V1 = 1.0
"""Volume of reactor 1 [m³]"""

V2 = 0.5
"""Volume of reactor 2 [m³]"""

V3 = 1.0
"""Volume of separator [m³]"""


# --- System Dynamics ---
def model(t: float, y: np.ndarray, u: dict):
    """
    Differential equations for reactor-separator system.

    Parameters:
    - t: time [s]
    - y: state vector
    - u: input vector
    """

    # States
    T1 = y[0]  # Temperature of reactor 1 [K]
    T2 = y[1]  # Temperature of reactor 2 [K]
    T3 = y[2]  # Temperature of separator [K]

    xA1 = y[3]  # Mole fraction of A in reactor 1 [-]
    xB1 = y[4]  # Mole fraction of B in reactor 1 [-]

    xA2 = y[5]  # Mole fraction of A in reactor 2 [-]
    xB2 = y[6]  # Mole fraction of B in reactor 2 [-]

    xA3 = y[7]  # Mole fraction of A in separator [-]
    xB3 = y[8]  # Mole fraction of B in separator [-]

    # Inputs
    Ff1 = u[0]  # Feed flow rate to reactor 1 [m³/h]
    Ff2 = u[1]  # Feed flow rate to reactor 2 [m³/h]
    FR = u[2]  # Recycle flow rate [m³/h]

    Q1 = u[3]  # Heat input to reactor 1 [kJ/h]
    Q2 = u[4]  # Heat input to reactor 2 [kJ/h]
    Q3 = u[5]  # Heat input to separator [kJ/h]

    T0 = u[6](t)  # Feed temperature [K]

    # Flow rate to keep volumes constant
    F1 = Ff1 + FR
    F2 = Ff2 + F1

    # Component C
    xC3 = 1 - xA3 - xB3

    # Purge
    FP = eps * FR

    # Arrhenius kinetics
    k11 = k1 * np.exp(-E1 / (R * T1))
    k21 = k2 * np.exp(-E2 / (R * T1))

    k12 = k1 * np.exp(-E1 / (R * T2))
    k22 = k2 * np.exp(-E2 / (R * T2))

    # Recycle composition (equilibrium)
    denom = alphaA * xA3 + alphaB * xB3 + alphaC * xC3
    xAR = alphaA * xA3 / denom
    xBR = alphaB * xB3 / denom

    # --- Balances ---
    # Temperature
    dT1dt = (
        (Ff1 / V1) * (T0 - T1)
        + (FR / V1) * (T3 - T1)
        + Q1 / (rho * Cp * V1)
        - (m / Cp) * (k11 * xA1 * dH1 + k21 * xB1 * dH2)
    )

    dT2dt = (
        (Ff2 / V2) * (T0 - T2)
        + (F1 / V2) * (T1 - T2)
        + Q2 / (rho * Cp * V2)
        - (m / Cp) * (k12 * xA2 * dH1 + k22 * xB2 * dH2)
    )

    dT3dt = (F2 / V3) * (T2 - T3) + Q3 / (rho * Cp * V3)

    # Compositions
    dxA1dt = (Ff1 / V1) * (xA0 - xA1) + (FR / V1) * (xAR - xA1) - k11 * xA1
    dxB1dt = (FR / V1) * (xBR - xB1) - (Ff1 / V1) * xB1 + k11 * xA1 - k21 * xB1

    dxA2dt = (Ff2 / V2) * (xA0 - xA2) + (F1 / V2) * (xA1 - xA2) - k12 * xA2
    dxB2dt = (F1 / V2) * (xB1 - xB2) - (Ff2 / V2) * xB2 + k12 * xA2 - k22 * xB2

    dxA3dt = (F2 / V3) * (xA2 - xA3) - ((FP + FR) / V3) * (xAR - xA3)
    dxB3dt = (F2 / V3) * (xB2 - xB3) - ((FP + FR) / V3) * (xBR - xB3)

    return [
        dT1dt,
        dT2dt,
        dT3dt,
        dxA1dt,
        dxB1dt,
        dxA2dt,
        dxB2dt,
        dxA3dt,
        dxB3dt,
    ]


# --- Model Inputs ---
Ff1 = 5.04
"""Feed flow rate to reactor 1 [m³/h]"""

Ff2 = 5.04
"""Feed flow rate to reactor 2 [m³/h]"""

FR = 17.0
"""Recycle flow rate [m³/h]"""

Q1 = 715.3e3
"""Heat input to reactor 1 [kJ/h]"""

Q2 = 579.8e3
"""Heat input to reactor 2 [kJ/h]"""

Q3 = 568.7e3
"""Heat input to separator [kJ/h]"""


def T0_func(t: float) -> float:
    """Feed temperature [K]"""
    if t < 0.2:
        return 359.1
    else:
        return 370.0


u = [Ff1, Ff2, FR, Q1, Q2, Q3, T0_func]
"""Inputs vector"""

# --- Initial Conditions ---
T0 = [432.4, 427.1, 432.1]  # T1, T2, T3
x10 = [0.536, 0.448]  # xA1, xB1
x20 = [0.545, 0.438]  # xA2, xB2
x30 = [0.298, 0.670]  # xA3, xB3
y0 = T0 + x10 + x20 + x30

# --- Simulation ---
t = np.linspace(0, 2.5, 1500)  # Simulation time [h]
sol = solve_ivp(model, [t[0], t[-1]], y0, t_eval=t, args=(u,), rtol=1e-8, atol=1e-10)

# --- Model Outputs ---
T1, T2, T3 = sol.y[0:3]
xA1, xB1 = sol.y[3:5]
xA2, xB2 = sol.y[5:7]
xA3, xB3 = sol.y[7:9]

# --- Plot results ---
fig, axs = plt.subplots(2, 3, figsize=(10, 6), sharex=True, constrained_layout=True)
fig.suptitle("Simple Reactor-Separator System")

# Reactor 1
axs[0, 0].set_title("Reactor 1")
axs[0, 0].plot(sol.t, T1 - zero_Celsius)
axs[0, 0].set_ylabel("Temperature / °C")

xC1 = 1 - xA1 - xB1
axs[1, 0].plot(sol.t, xA1, label="$x_{A1}$")
axs[1, 0].plot(sol.t, xB1, label="$x_{B1}$")
axs[1, 0].plot(sol.t, xC1, label="$x_{C1}$")
axs[1, 0].set_ylabel("Composition")
axs[1, 0].set_xlabel("Time / h")

# Reactor 2
axs[0, 1].set_title("Reactor 2")
axs[0, 1].plot(sol.t, T2 - zero_Celsius)

xC2 = 1 - xA2 - xB2
axs[1, 1].plot(sol.t, xA2, label="$x_{A2}$")
axs[1, 1].plot(sol.t, xB2, label="$x_{B2}$")
axs[1, 1].plot(sol.t, xC2, label="$x_{C2}$")
axs[1, 1].set_xlabel("Time / h")

# Separator 3
axs[0, 2].set_title("Separator")
axs[0, 2].plot(sol.t, T3 - zero_Celsius)

xC3 = 1 - xA3 - xB3
axs[1, 2].plot(sol.t, xA3, label="$x_{A3}$")
axs[1, 2].plot(sol.t, xB3, label="$x_{B3}$")
axs[1, 2].plot(sol.t, xC3, label="$x_{C3}$")
axs[1, 2].set_xlabel("Time / h")

for ax in axs[1, :]:
    ax.legend()

for ax in axs.flat:
    ax.grid(True)

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "simulations"), exist_ok=True)
save_path = os.path.join(script_dir, "simulations", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
