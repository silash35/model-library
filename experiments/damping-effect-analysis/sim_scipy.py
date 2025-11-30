import os
from typing import Final

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

# --- Define Model ---
m: Final = 1.0  # Mass [kg]

k: Final = 20.0  # Spring stiffness [N/m]


def diff_equations(t: float, y: np.ndarray, F_ext: float, c: float):
    x = y[0]  # Displacement [m]
    v = y[1]  # Velocity [m/s]

    dxdt = v
    dvdt = (F_ext - c * v - k * x) / m
    return [dxdt, dvdt]


# --- Make simulations ---
F_ext = 10.0  # External applied force [N]

# Define damping ratios and corresponding damping coefficients
zeta_values = np.array([0, 0.2, 1, 1.8])
damping_coeffs = zeta_values * 2 * np.sqrt(k * m)

# Simulation time [s]
t = np.linspace(0, 10, 1000)

# Pre-allocate displacement array
displacements = np.zeros((zeta_values.size, t.size))

# Initial conditions: [displacement, velocity]
y0 = [0.0, 0.0]

for i in range(zeta_values.size):
    sol = solve_ivp(
        diff_equations, [t[0], t[-1]], y0, t_eval=t, args=(F_ext, damping_coeffs[i])
    )
    displacements[i] = sol.y[0]


# --- Plot results ---
for i in range(zeta_values.size):
    plt.plot(t, displacements[i], label=f"$\\zeta$ = {zeta_values[i]}")

plt.xlabel("Time / s")
plt.ylabel("Displacement / m")
plt.title("Mass–Spring–Damper System Responses")
plt.grid(True)
plt.legend()

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "results"), exist_ok=True)
save_path = os.path.join(script_dir, "results", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
