import os
from typing import Final

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

# --- Model Constants ---
m: Final = 1.0
"""Mass [kg]"""

c: Final = 2.0
"""Damping coefficient [N·s/m]"""

k: Final = 20.0
"""Spring stiffness [N/m]"""


# --- System Dynamics ---
def model(t: float, y: np.ndarray, F_ext: float):
    """
    Differential equations for the mass–spring–damper system.

    Parameters:
    - t: time [s]
    - y: state vector
    - F_ext: external applied force [N]
    """
    x = y[0]  # Displacement [m]
    v = y[1]  # Velocity [m/s]

    dxdt = v
    dvdt = (F_ext - c * v - k * x) / m
    return [dxdt, dvdt]


# --- Model Input ---
F_ext = 10.0
"""External applied force [N]"""

# --- Initial Conditions ---
x0 = 0.0  # Initial displacement [m]
v0 = 0.0  # Initial velocity [m/s]
y0 = [x0, v0]

# --- Simulation ---
t = np.linspace(0, 10, 1000)  # Simulation time [s]
sol = solve_ivp(model, [t[0], t[-1]], y0, t_eval=t, args=(F_ext,))

# --- Model Outputs ---
x = sol.y[0]
"""Mass displacement [m]"""

v = sol.y[1]
"""Mass velocity [m/s]"""

# --- Plot results ---
fig, axs = plt.subplots(2, 1, figsize=(8, 5), sharex=True, constrained_layout=True)
fig.suptitle("Mass–Spring–Damper System")

# Plot displacement
axs[0].plot(sol.t, x, label="$x(t)$")
axs[0].set_ylabel("Displacement / m")
axs[0].grid(True)
axs[0].legend()

# Plot velocity
axs[1].plot(sol.t, v, label="$v(t)$", color="tab:orange")
axs[1].set_ylabel("Velocity / m$\\cdot$s$^{-1}$")
axs[1].grid(True)
axs[1].legend()

axs[-1].set_xlabel("Time / s")

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "simulations"), exist_ok=True)
save_path = os.path.join(script_dir, "simulations", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
