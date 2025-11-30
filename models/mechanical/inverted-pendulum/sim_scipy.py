import os
from typing import Final

import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import g as gravity
from scipy.integrate import solve_ivp

# --- Model Constants ---
m_c: Final = 1.0
"""Mass of the cart [kg]"""

m_p: Final = 0.2
"""Mass of the pendulum rod [kg]"""

L: Final = 0.5
"""Distance from pivot to rod center of mass [m]"""

J: Final = (1 / 12) * m_p * (2 * L) ** 2
"""Moment of inertia of the pendulum about its center of mass [kg·m²]"""

b: Final = 10.0
"""Viscous damping coefficient of the cart [N·s/m]"""

g: Final = gravity
"""Gravitational acceleration [m/s²]"""


# --- System Dynamics ---
def model(t: float, y: np.ndarray, F: float):
    """
    Differential equations for the inverted pendulum on a cart.

    Parameters:
    - t: time [s]
    - y: state vector
    """

    theta = y[0]  # Pendulum angle [rad]
    omega = y[1]  # Angular velocity [rad/s]
    # x = y[2]  # Cart position [m]
    v = y[3]  # Cart velocity [m/s]

    # A Matrix (system coefficients)
    A = np.array(
        [
            [1, 0, 0, 0],
            [0, m_p * L**2 + J, 0, m_p * L * np.cos(theta)],
            [0, 0, 1, 0],
            [0, m_p * L * np.cos(theta), 0, m_c + m_p],
        ]
    )

    # b vector (right-hand side)
    b_rhs = np.array(
        [
            omega,
            m_p * g * L * np.sin(theta),
            v,
            F - b * v + m_p * L * omega**2 * np.sin(theta),
        ]
    )

    # Solve the linear system A * [dtheta_dt, domega_dt, dx_dt, dv_dt]^T = b
    dydt = np.linalg.solve(A, b_rhs)
    return dydt


# --- Model Input ---
F: Final = 0.0
"""External force applied to the cart [N]"""

# --- Initial Conditions ---
theta0 = np.deg2rad(10.0)  # Pendulum initial angle [rad]
omega0 = 0.0  # Pendulum initial angular velocity [rad/s]
x0 = 0.0  # Cart initial position [m]
v0 = 0.0  # Cart initial velocity [m/s]
y0 = [theta0, omega0, x0, v0]

# --- Simulation ---
t = np.linspace(0, 10, 1000)  # Simulation time [s]
sol = solve_ivp(model, [t[0], t[-1]], y0, t_eval=t, args=(F,))

# --- Model Outputs ---

theta = sol.y[0]
"""Pendulum angle [rad]"""

omega = sol.y[1]
"""Angular velocity [rad/s]"""

x = sol.y[2]
"""Cart position [m]"""

v = sol.y[3]
"""Cart velocity [m/s]"""

# --- Convert angle to degrees for better interpretability ---
theta_deg = np.rad2deg(theta)
omega_deg = np.rad2deg(omega)

# --- Plot results ---
fig, axs = plt.subplots(2, 2, figsize=(10, 6), constrained_layout=True)
fig.suptitle("Inverted Pendulum on a Cart")

# Pendulum angle
axs[0, 0].plot(sol.t, theta_deg, label="$\\theta(t)$", color="tab:blue")
axs[0, 0].set_ylabel("Angle / deg")

# Pendulum angular velocity
axs[0, 1].plot(sol.t, omega_deg, label="$\\omega(t)$", color="tab:orange")
axs[0, 1].set_ylabel("Angular velocity / deg$\\cdot$s$^{-1}$")

# Cart position
axs[1, 0].plot(sol.t, x, label="$x(t)$", color="tab:green")
axs[1, 0].set_ylabel("Position / m")

# Cart velocity
axs[1, 1].plot(sol.t, v, label="$v(t)$", color="tab:red")
axs[1, 1].set_ylabel("Velocity / m/s")

# Enable grid, legend, and set x-label for all subplots
for ax in axs.flat:
    ax.set_xlabel("Time / s")
    ax.grid(True)
    ax.legend()

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "simulations"), exist_ok=True)
save_path = os.path.join(script_dir, "simulations", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
