import os
from typing import Final

import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import g as gravity
from scipy.integrate import solve_ivp

# --- Define Model and PID control ---
m_c: Final = 1.0  # Mass of the cart [kg]

m_p: Final = 0.2  # Mass of the pendulum rod [kg]

L: Final = 0.5  # Distance from pivot to rod center of mass [m]

J: Final = (
    (1 / 12) * m_p * (2 * L) ** 2
)  # Moment of inertia of the pendulum about its center of mass [kg·m²]

b: Final = 10.0  # Viscous damping coefficient of the cart [N·s/m]

g: Final = gravity  # Gravitational acceleration [m/s²]

Kp: Final = -500.0  # Proportional gain

Ki: Final = -300.0  # Integral gain

Kd: Final = -20.0  # Derivative gain


def PID_control(e: float | np.ndarray, de: float | np.ndarray, Ie: float | np.ndarray):
    """
    Compute the PID control action.

    Parameters:
    - e: Current error (setpoint - measured value).
    - de: Derivative of the error.
    - Ie: Integral of the error (accumulated error over time).
    Returns:
    - u: Control signal output (e.g., force or voltage).
    """

    u = Kp * e + Kd * de + Ki * Ie
    return u


def diff_equations(t: float, y: np.ndarray, SP: float):
    theta = y[0]  # Pendulum angle [rad]
    omega = y[1]  # Angular velocity [rad/s]
    # x = y[2]  # Cart position [m]
    v = y[3]  # Cart velocity [m/s]

    e = SP - theta  # Error
    Ie = y[4]  # Integral of error
    de = -omega  # Derivative of error

    # Force applied to the cart (calculated by the PID controller) [N]
    F = PID_control(e, de, Ie)

    # A Matrix (system coefficients)
    A = np.array(
        [
            [1, 0, 0, 0, 0],
            [0, m_p * L**2 + J, 0, m_p * L * np.cos(theta), 0],
            [0, 0, 1, 0, 0],
            [0, m_p * L * np.cos(theta), 0, m_c + m_p, 0],
            [0, 0, 0, 0, 1],
        ]
    )

    # b vector (right-hand side)
    b_rhs = np.array(
        [
            omega,
            m_p * g * L * np.sin(theta),
            v,
            F - b * v + m_p * L * omega**2 * np.sin(theta),
            e,
        ]
    )

    # Solve the linear system A * [dtheta/dt, domega/dt, dx/dt, dv/dt, dIe/dt]^T = b
    dydt = np.linalg.solve(A, b_rhs)
    return dydt


# --- Simulation ---
t = np.linspace(0, 1, 1000)  # Simulation time [s]
SP = 0.0  # Setpoint angle [rad]
y0 = [np.deg2rad(30.0), 0.0, 0.0, 0.0, 0.0]  # Initial conditions

sol = solve_ivp(diff_equations, [t[0], t[-1]], y0, t_eval=t, args=(SP,))
theta = sol.y[0]  # Pendulum angle [rad]
omega = sol.y[1]  # Angular velocity [rad/s]
Ie = sol.y[4]  # Integral of the error

# --- Prepare data for plotting ---
# Recalculate the PID control force at each time step for visualization
e = SP - theta  # Error
de = -omega  # Derivative error
F = PID_control(e, de, Ie)

# Convert theta to degrees
theta = np.rad2deg(theta)

# --- Plot results ---
fig, axs = plt.subplots(2, 1, figsize=(8, 5), constrained_layout=True, sharex=True)
fig.suptitle("Controlled Inverted Pendulum (PID)")

# Force
axs[0].plot(sol.t, F, color="tab:orange")
axs[0].set_ylabel("Applied Force $F(t)$ / N")
axs[0].grid(True)

# Pendulum angle
axs[1].plot(sol.t, theta, color="tab:blue")
axs[1].set_ylabel("Pendulum Angle $\\theta(t)$ / deg")
axs[1].grid(True)

axs[-1].set_xlabel("Time / s")

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "results"), exist_ok=True)
save_path = os.path.join(script_dir, "results", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
