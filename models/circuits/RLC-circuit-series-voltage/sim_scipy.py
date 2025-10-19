import os
from typing import Final

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

# --- Model Constants ---
R: Final[float] = 10.0
"""Resistance [Ω]"""

L: Final[float] = 2
"""Inductance [H]"""

C: Final[float] = 5000e-6
"""Capacitance [F]"""


# --- Circuit Dynamics ---
def circuit_model(t: float, y: np.ndarray, epsilon: float):
    """
    Differential equation for the circuit in terms of capacitor voltage.

    Parameters:
    - t: time [s]
    - y: state vector
    - epsilon: applied voltage [V]
    """
    Vc = y[0]  # Capacitor voltage [V]
    Vc_dot = y[1]  # Time derivative of capacitor voltage [V/s]

    dVc_dt = Vc_dot
    d2Vc_dt2 = (epsilon / (L * C)) - (R / L) * Vc_dot - (Vc / (L * C))
    return [dVc_dt, d2Vc_dt2]


# --- Model Inputs ---
epsilon = 5.0
"""Applied voltage [V]"""

# --- Initial Conditions ---
Vc = 0.0  # Initial capacitor voltage [V]
Vc_dot = 0.0  # Initial time derivative of capacitor voltage [V/s]
y0 = [Vc, Vc_dot]

# --- Simulation ---
t = np.linspace(0, 3, 1000)  # Simulation time [s]
sol = solve_ivp(circuit_model, [t[0], t[-1]], y0, t_eval=t, args=(epsilon,))

# --- Model Outputs ---
Vc = sol.y[0]
"""Capacitor voltage [V]"""

Vc_dot = sol.y[1]
""" Derivative of capacitor voltage [V/s]"""

# --- Plot results ---
plt.plot(sol.t, Vc, label="$V_C(t)$")
plt.xlabel("Time / s")
plt.ylabel("Voltage / V")
plt.title("Series RLC Circuit")
plt.grid(True)
plt.legend()

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "simulations"), exist_ok=True)
save_path = os.path.join(script_dir, "simulations", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
