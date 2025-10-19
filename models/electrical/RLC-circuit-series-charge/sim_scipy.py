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
    Differential equation for the circuit in terms of capacitor charge.

    Parameters:
    - t: time [s]
    - y: state vector
    - epsilon: applied voltage [V]
    """
    q = y[0]  # Charge on the capacitor [C]
    I = y[1]  # Current through the circuit [A]

    dqdt = I
    dIdt = (epsilon - R * I - q / C) / L
    return [dqdt, dIdt]


# --- Model Inputs ---
epsilon = 5.0
"""Applied voltage [V]"""

# --- Initial Conditions ---
q0 = 0.0  # Initial charge [C]
I0 = 0.0  # Initial current [A]
y0 = [q0, I0]

# --- Simulation ---
t = np.linspace(0, 3, 1000)  # Simulation time [s]
sol = solve_ivp(circuit_model, [t[0], t[-1]], y0, t_eval=t, args=(epsilon,))

# --- Model Outputs ---
q = sol.y[0]
"""Capacitor charge [C]"""

I = sol.y[1]
"""Circuit current [A]"""

# --- Plot results ---
fig, axs = plt.subplots(2, 1, figsize=(8, 5), constrained_layout=True)
fig.suptitle("Series RLC Circuit")

# Plot capacitor charge
axs[0].plot(sol.t, q, label="$q(t)$")
axs[0].plot(sol.t, np.full_like(sol.t, C * epsilon), label="$q_{max}(t)$")
axs[0].set_xlabel("Time / s")
axs[0].set_ylabel("Charge / C")
axs[0].grid(True)
axs[0].legend()

# Plot circuit current
axs[1].plot(sol.t, I, label="$I(t)$")
axs[1].set_xlabel("Time / s")
axs[1].set_ylabel("Current / A")
axs[1].grid(True)
axs[1].legend()

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "simulations"), exist_ok=True)
save_path = os.path.join(script_dir, "simulations", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
