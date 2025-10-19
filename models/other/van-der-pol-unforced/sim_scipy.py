import os
from typing import Final

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

# --- Model Constants ---
mu: Final[float] = 1.0
"""Nonlinearity parameter"""


# --- Model Dynamics ---
def model(t: float, y: np.ndarray):
    """
    Van der Pol oscillator differential equation.

    Parameters:
    - t: time [s]
    - y: state vector
    """
    x = y[0]  # Position [m]
    v = y[1]  # Velocity [m/s]

    dxdt = v
    d2x_dt2 = mu * (1 - x**2) * v - x
    return [dxdt, d2x_dt2]


# --- Initial Conditions ---
x0 = 1  # Initial position [m]
v0 = 0  # Initial velocity [m/s]
y0 = [x0, v0]

# --- Simulation ---
t = np.linspace(0, 50, 1000)  # Simulation time [s]
sol = solve_ivp(model, [t[0], t[-1]], y0, t_eval=t)

# --- Model Outputs ---
x = sol.y[0]
"""Position [m]"""
v = sol.y[1]
"""Velocity [m/s]"""

# --- Plot results ---
plt.plot(x, v)

plt.xlabel("Position / m")
plt.ylabel("Velocity / m$\\cdot$s$^{-1}$")
plt.title("Phase Portrait of the Van der Pol Oscillator")
plt.grid(True)

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "simulations"), exist_ok=True)
save_path = os.path.join(script_dir, "simulations", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
