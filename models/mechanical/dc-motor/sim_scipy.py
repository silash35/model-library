import os
from typing import Final

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

# --- Model Constants ---
J: Final[float] = 0.03
"""Total moment of inertia [kg·m²]"""

b: Final[float] = 0.02
"""Viscous friction coefficient [N·m·s/rad]"""

K1: Final[float] = 0.01
"""Torque constant [N·m/A]"""

K2: Final[float] = 0.01
"""Back-emf constant [V·s/rad]"""

R: Final[float] = 10.0
"""Armature resistance [Ω]"""


# --- System Dynamics ---
def model(t: float, y: np.ndarray, epsilon: float):
    """
    Differential equations for the DC motor.

    Parameters:
    - t: time [s]
    - y: state vector
    - epsilon: applied voltage [V]
    """
    # theta = y[0]  # Angular position [rad]
    omega = y[1]  # Angular velocity [rad/s]

    dtheta_dt = omega
    domega_dt = ((K1 / R) * epsilon - (K1 * K2 / R + b) * omega) / J
    return [dtheta_dt, domega_dt]


# --- Model Input ---
epsilon = 24.0
"""Applied voltage [V]"""

# --- Initial Conditions ---
theta0 = 0.0  # Initial angular position [rad]
omega0 = 0.0  # Initial angular velocity [rad/s]
y0 = [theta0, omega0]

# --- Simulation ---
t = np.linspace(0, 10, 1000)  # Simulation time [s]
sol = solve_ivp(model, [t[0], t[-1]], y0, t_eval=t, args=(epsilon,))

# --- Model Outputs ---
theta = sol.y[0]
"""Rotor angular position [rad]"""

omega = sol.y[1]
"""Rotor angular velocity [rad/s]"""

# --- Convert angle to degrees for better interpretability ---
theta_deg = np.rad2deg(theta)
omega_deg = np.rad2deg(omega)

# --- Plot results ---
fig, axs = plt.subplots(2, 1, figsize=(8, 5), constrained_layout=True)
fig.suptitle("DC Motor Simulation")

# Angular position
axs[0].plot(sol.t, theta_deg, label="$\\theta(t)$")
axs[0].set_xlabel("Time / s")
axs[0].set_ylabel("Angle / deg")
axs[0].grid(True)
axs[0].legend()

# Angular velocity
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
