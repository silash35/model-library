import os
from typing import Final

import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import g as gravity
from scipy.integrate import solve_ivp

# --- Model Constants ---
m: Final[float] = 1.0
"""Mass of the rod [kg]"""

L: Final[float] = 0.5
"""Distance from pivot to center of mass [m] (rod length = 2*L)"""

J: Final[float] = (1 / 3) * m * (L * 2) ** 2
"""Moment of inertia of the rod about the pivot [kg·m²]"""

k: Final[float] = 0.3
"""Viscous damping coefficient [N·m·s/rad]"""

g: Final[float] = gravity
"""Gravitational acceleration [m/s²]"""


# --- System Dynamics ---
def model(t: float, y: np.ndarray):
    """
    Differential equations for the physical pendulum (rigid rod with distributed mass).

    Parameters:
    - t: time [s]
    - y: state vector
    """

    theta = y[0]  # Angle [rad]
    omega = y[1]  # Angular velocity [rad/s]

    dtheta_dt = omega
    domega_dt = -(k / J) * omega - (3 * g / (4 * L)) * np.sin(theta)
    return [dtheta_dt, domega_dt]


# --- Initial Conditions ---
theta0 = np.deg2rad(30.0)  # Initial angle [rad]
omega0 = 0.0  # Initial angular velocity [rad/s]
y0 = [theta0, omega0]

# --- Simulation ---
t = np.linspace(0, 10, 1000)  # Simulation time [s]
sol = solve_ivp(model, [t[0], t[-1]], y0, t_eval=t)

# --- Model Outputs ---
theta = sol.y[0]
"""Pendulum angle [rad]"""

omega = sol.y[1]
"""Angular velocity [rad/s]"""

# --- Convert angle to degrees for better interpretability ---
theta_deg = np.rad2deg(theta)
omega_deg = np.rad2deg(omega)

# --- Plot results ---
fig, axs = plt.subplots(2, 1, figsize=(8, 5), constrained_layout=True)
fig.suptitle("Physical Pendulum")

# Plot angle
axs[0].plot(sol.t, theta_deg, label="$\\theta(t)$")
axs[0].set_xlabel("Time / s")
axs[0].set_ylabel("Angle / deg")
axs[0].grid(True)
axs[0].legend()

# Plot angular velocity
axs[1].plot(sol.t, omega_deg, label="$\\omega(t)$", color="tab:orange")
axs[1].set_xlabel("Time / s")
axs[1].set_ylabel("Angular velocity / deg$\\cdot$s$^{-1}$")
axs[1].grid(True)
axs[1].legend()

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "simulations"), exist_ok=True)
save_path = os.path.join(script_dir, "simulations", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
