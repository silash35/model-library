import os
from typing import Final

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

# --- Model Constants ---
R: Final[float] = 50.0
"""Resistance [Ω]"""

C: Final[float] = 5000e-6
"""Capacitance [F]"""


# --- Circuit Dynamics ---
def circuit_model(t: float, Vc: float, epsilon: float):
    """
    Differential equation for the circuit in terms of capacitor voltage.

    Parameters:
    - t: time [s]
    - Vc: voltage across the capacitor [V]
    - epsilon: applied voltage [V]
    """
    dVc_dt = (epsilon - Vc) / (R * C)
    return dVc_dt


# --- Model Inputs ---
epsilon = 5.0
"""Applied voltage [V]"""

# --- Simulation ---
Vc0 = 0.0  # Initial capacitor voltage [V]
t = np.linspace(0, 3, 1000)  # Simulation time [s]
sol = solve_ivp(circuit_model, [t[0], t[-1]], [Vc0], t_eval=t, args=(epsilon,))

# --- Model Outputs ---
Vc = sol.y[0]
"""Capacitor voltage [V]"""

# --- Plot results ---
plt.plot(sol.t, Vc, label="$V_C(t)$")

plt.xlabel("Time / s")
plt.ylabel("Voltage / V")
plt.title("Series RC Circuit")
plt.grid(True)
plt.legend()

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "simulations"), exist_ok=True)
save_path = os.path.join(script_dir, "simulations", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
