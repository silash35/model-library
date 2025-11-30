import os
from typing import Final

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

# --- Model Constants ---
m1: Final = 5.0
"""Mass 1 [kg]"""

m2: Final = 2.0
"""Mass 2 [kg]"""

c: Final = 1.0
"""Damping coefficient [N·s/m]"""

k: Final = 8.0
"""Spring stiffness [N/m]"""


# --- System Dynamics ---
def model(t: float, y: np.ndarray, u: float):
    """
    Differential equations for the two-mass–spring–damper system.

    Parameters:
    - t: time [s]
    - y: state vector
    - u: external applied force [N]
    """
    x1 = y[0]  # Position of mass 1 [m]
    v1 = y[1]  # Velocity of mass 1 [m/s]
    x2 = y[2]  # Position of mass 2 [m]
    v2 = y[3]  # Velocity of mass 2 [m/s]

    # Relative position and velocity
    dx = x2 - x1
    dv = v2 - v1

    # Derivatives
    dx1dt = v1
    dv1dt = (c * dv + k * dx) / m1
    dx2dt = v2
    dv2dt = (u - c * dv - k * dx) / m2
    return [dx1dt, dv1dt, dx2dt, dv2dt]


# --- Model Input ---
u = 2.0
"""External applied force [N]"""

# --- Initial Conditions ---
x1_0 = 0.0  # Initial position of mass 1 [m]
v1_0 = 0.0  # Initial velocity of mass 1 [m/s]
x2_0 = 0.0  # Initial position of mass 2 [m]
v2_0 = 0.0  # Initial velocity of mass 2 [m/s]
y0 = [x1_0, v1_0, x2_0, v2_0]

# --- Simulation ---
t = np.linspace(0, 8, 10000)  # Simulation time [s]
sol = solve_ivp(model, [t[0], t[-1]], y0, t_eval=t, args=(u,))

# --- Model Outputs ---
x1 = sol.y[0]
"""Mass 1 position [m]"""

v1 = sol.y[1]
"""Mass 1 velocity [m/s]"""

x2 = sol.y[2]
"""Mass 2 position [m]"""

v2 = sol.y[3]
"""Mass 2 velocity [m/s]"""

# --- Plot results ---
fig, axs = plt.subplots(2, 1, figsize=(8, 6), sharex=True, constrained_layout=True)
fig.suptitle("Two-Mass–Spring–Damper System")

# Positions
axs[0].plot(sol.t, x1, label="$x_1(t)$")
axs[0].plot(sol.t, x2, label="$x_2(t)$")
axs[0].set_ylabel("Position / m")
axs[0].grid(True)
axs[0].legend()

# Velocities
axs[1].plot(sol.t, v1, label="$v_1(t)$")
axs[1].plot(sol.t, v2, label="$v_2(t)$")
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
