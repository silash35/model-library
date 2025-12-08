import os
from typing import Final

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

# --- Define Model ---
R: Final = 50.0  # Resistance [Ω]

C: Final = 5000e-6  # Capacitance [F]


def diff_equation(t: float, q: float, epsilon: float):
    dqdt = -q / (R * C) + epsilon / R
    return dqdt


# --- Simulation ---
epsilon = 5.0  # Applied voltage [V]
q0 = 0.0  # Initial charge [C]

# Numerical Solution
t = np.linspace(0, 3, 1000)  # Simulation time [s]
sol = solve_ivp(diff_equation, [t[0], t[-1]], [q0], t_eval=t, args=(epsilon,))
q_numeric = sol.y[0]


# Analytical Solution
def q_func(t: float | np.ndarray, epsilon: float):
    return epsilon * C * (1 - np.exp(-t / (R * C)))


q_analytic = q_func(t, epsilon)

# --- Error Analysis ---
# Skip the first point (t=0) because it is the initial condition q(0)=0
# This also avoids division by zero when computing the relative error
percent_error = 100 * np.abs(q_numeric[1:] - q_analytic[1:]) / np.abs(q_analytic[1:])
mean_error = np.mean(percent_error)  # Mean relative error in percent

# --- Plot results ---
plt.plot(t, q_analytic, label="Analytical $q(t)$", linestyle="dotted", linewidth=5)
plt.plot(t, q_numeric, label="Numerical $q(t)$")

plt.xlabel("Time / s")
plt.ylabel("Charge / C")
plt.title("Series RC Circuit")
plt.grid(True)
plt.legend()

error_text = f"Mean relative error: {mean_error:.3f}%"
plt.text(
    0.35,
    0.75,
    error_text,
    fontsize=12,
    transform=plt.gca().transAxes,
    bbox=dict(boxstyle="round,pad=0.5", facecolor="white", alpha=0.8),
)

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "results"), exist_ok=True)
save_path = os.path.join(script_dir, "results", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
