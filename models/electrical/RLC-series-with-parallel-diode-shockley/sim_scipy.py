import os
from typing import Final

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

# --- Model Constants ---
R: Final[float] = 100.0
"""Resistance [Ω]"""

L: Final[float] = 100 * 1e-3
"""Inductance [H]"""

C: Final[float] = 5000e-6
"""Capacitance [F]"""

i_S: Final[float] = 1e-12
"""Diode reverse saturation current [A]"""

n: Final[float] = 1.5
"""Diode ideality factor"""

V_T: Final[float] = 26e-3
"""Thermal voltage [V]"""


# --- Shockley diode model ---
def shockley_model(Vd: float) -> float:
    """Shockley diode equation"""
    return i_S * (np.exp(Vd / (n * V_T)) - 1)


# --- Circuit Dynamics ---
def circuit_model(t: float, y: np.ndarray, epsilon: float):
    """
    Differential equations for the series RLC circuit with a parallel diode.

    Parameters:
    - t: time [s]
    - y: state vector
    - epsilon: applied voltage [V]
    """
    Vc = y[0]  # Capacitor voltage [V]
    I = y[1]  # Circuit current [A]

    Id = shockley_model(Vc)

    dVc_dt = (I - Id) / C
    dI_dt = (epsilon - R * I - Vc) / L

    return [dVc_dt, dI_dt]


# --- Model Input ---
epsilon = 5.0
"""Applied voltage [V]"""

# --- Initial Conditions ---
Vc0 = 0.0  # Initial capacitor voltage [V]
I0 = 0.0  # Initial current [A]
y0 = [Vc0, I0]

# --- Simulation ---
t = np.linspace(0, 0.2, 2000)  # Simulation time [s]
sol = solve_ivp(circuit_model, [t[0], t[-1]], y0, t_eval=t, args=(epsilon,))

# --- Model Outputs ---
Vc = sol.y[0]
"""Capacitor voltage [V]"""

I = sol.y[1]
"""Circuit current [A]"""

# Calculate the other currents
Id = shockley_model(Vc)
"""Diode current [A]"""

Ic = I - Id
"""Capacitor current [A]"""

# --- Plot results ---
fig, axs = plt.subplots(2, 1, figsize=(8, 5), constrained_layout=True)
fig.suptitle("Series RLC Circuit with Parallel Diode")

axs[0].plot(sol.t, Vc, label="$V_C(t)$")
axs[0].set_ylabel("Voltage [V]")
axs[0].grid(True)
axs[0].legend()

axs[1].plot(sol.t, I, label="$I(t)$")
axs[1].plot(sol.t, Id, label="$I_D(t)$")
axs[1].plot(sol.t, Ic, label="$I_C(t)$")
axs[1].set_ylabel("Current [A]")
axs[1].grid(True)
axs[1].legend()

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "simulations"), exist_ok=True)
save_path = os.path.join(script_dir, "simulations", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
