import os
from typing import Final

import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import g as gravity
from scipy.integrate import solve_ivp

# --- Define Models ---
g: Final[float] = gravity  # Gravitational acceleration [m/s²]

L: Final[float] = 1.0  # Pendulum length [m]


def diff_equations(t: float, y: np.ndarray):
    theta = y[0]  # Angle for nonlinear pendulum [rad]
    omega = y[1]  # Angular velocity for nonlinear pendulum [rad/s]

    linear_theta = y[2]  # Angle for linear pendulum [rad]
    linear_omega = y[3]  # Angular velocity for linear pendulum [rad/s]

    # Nonlinear model
    dtheta_dt = omega
    domega_dt = -(g / L) * np.sin(theta)

    # Linear model
    dlinear_theta_dt = linear_omega
    dlinear_omega_dt = -(g / L) * linear_theta
    return [dtheta_dt, domega_dt, dlinear_theta_dt, dlinear_omega_dt]


# --- Make simulations ---
t = np.linspace(0, 10, 1000)  # Simulation time [s]
test_angles = np.deg2rad(np.array([15, 30, 60]))
solutions = np.zeros((test_angles.size, 2, t.size))

for i in range(test_angles.size):
    y0 = [test_angles[i], 0.0, test_angles[i], 0.0]
    sol = solve_ivp(diff_equations, [t[0], t[-1]], y0, t_eval=t)
    solutions[i, 0] = sol.y[0]
    solutions[i, 1] = sol.y[2]


# --- Plot results ---
# Convert angle to degrees
solutions = np.rad2deg(solutions)

fig, axs = plt.subplots(
    test_angles.size, 1, figsize=(8, 6), sharex=True, constrained_layout=True
)
fig.suptitle("Linear vs Nonlinear Pendulum")

for i in range(test_angles.size):
    axs[i].set_title(f"Initial Angle = {np.rad2deg(test_angles[i]):.0f}°")
    axs[i].plot(t, solutions[i, 0], label="Nonlinear")
    axs[i].plot(t, solutions[i, 1], label="Linear")
    axs[i].set_ylabel("$\\theta(t)$ / deg")
    axs[i].grid(True)
    axs[i].legend(loc="upper right")
axs[-1].set_xlabel("Time / s")

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "results"), exist_ok=True)
save_path = os.path.join(script_dir, "results", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
