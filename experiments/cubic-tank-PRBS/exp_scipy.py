import os
from collections.abc import Callable
from typing import Final

import matplotlib.pyplot as plt
import numpy as np
from scipy.constants import g
from scipy.integrate import solve_ivp

# --- Define Model ---
rho: Final = 1000.0  # Density of water [kg/m³]

gamma: Final = rho * g  # Specific weight [N/m³]

L: Final = 4  # Tank side length [m]

A: Final = L**2  # Cross-sectional area [m²]

D_p: Final = 0.20  # Pipe diameter [m]

A_p: Final = np.pi * (D_p / 2) ** 2  # Pipe cross-sectional area [m²]

k_f: Final = 1.0  # Friction coefficient [kg/m]

alpha = A_p * np.sqrt(gamma * A_p / k_f)  # Outlet discharge parameter [m^{2.5}/s]


def diff_equation(t: float, h: float, Q_in: Callable[[float], float]):
    dhdt = (Q_in(t) - alpha * np.sqrt(h)) / A
    return dhdt


# --- Model Input (PRBS) ---
Q_low = 0.3  # Low flow [m³/s]
Q_high = 1.0  # High flow [m³/s]
T_switch = 20.0  # Switching period [s]
t_end = 600.0  # End time [s]

t_prbs = np.arange(0, t_end + T_switch, T_switch)


# Random number generator with fixed seed
# Ensures the PRBS is reproducible
rng = np.random.default_rng(seed=42)

# Generate the PRBS sequence
prbs_signal = rng.choice([Q_low, Q_high], size=len(t_prbs))


def Q_in(t: float) -> float:
    """Inlet flow rate [m^3/s]"""
    idx = int(np.floor(t / T_switch))
    idx = min(idx, len(prbs_signal) - 1)
    return prbs_signal[idx]


# --- Simulation ---
h0 = 0.2  # Initial level [m]
t = np.linspace(0, t_end, 1000)  # Simulation time [s]
sol = solve_ivp(
    diff_equation, [t[0], t[-1]], [h0], t_eval=t, args=(Q_in,), method="LSODA"
)

h = sol.y[0]  # Liquid level [m]

# --- Plot results ---
fig, axs = plt.subplots(2, 1, figsize=(9, 5), sharex=True, constrained_layout=True)
fig.suptitle("Cubic Tank (PRBS input)")

axs[0].plot(sol.t, [Q_in(t) for t in sol.t], color="tab:orange")
axs[0].set_ylabel("Inlet flow rate / m$^3\\cdot$s$^{-1}$")
axs[0].grid(True)

axs[1].axhline(L, color="tab:red", linestyle="--", label="Tank Limits")
axs[1].plot(sol.t, h, label="$h(t)$")
axs[1].axhline(0, color="tab:red", linestyle="--")
axs[1].set_ylabel("Level / m")
axs[1].legend()
axs[1].grid(True)


axs[-1].set_xlabel("Time / s")

# Save plot to file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "results"), exist_ok=True)
save_path = os.path.join(script_dir, "results", "scipy.png")
plt.savefig(save_path)
print(f"Plot saved to {save_path}")
