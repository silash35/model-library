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


# --- System Dynamics ---
def model(t: float, q: float, epsilon: float):
    """
    Differential equation for the circuit in terms of capacitor charge.

    Parameters:
    - t: time [s]
    - q: charge on the capacitor [C]
    - epsilon: applied voltage [V]
    """
    dqdt = -q / (R * C) + epsilon / R
    return dqdt


# --- Model Input ---
epsilon = 5.0
"""Applied voltage [V]"""

# --- Simulation ---
q0 = 0.0  # Initial charge [C]
t = np.linspace(0, 3, 1000)  # Simulation time [s]
sol = solve_ivp(model, [t[0], t[-1]], [q0], t_eval=t, args=(epsilon,))

# --- Model Output ---
q = sol.y[0]
"""Capacitor charge [C]"""

# --- Plot results ---
plt.plot(sol.t, q, label="$q(t)$")

plt.xlabel("Time / s")
plt.ylabel("Charge / C")
plt.title("Series RC Circuit")
plt.grid(True)
plt.legend()

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "simulations"), exist_ok=True)
save_path = os.path.join(script_dir, "simulations", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
