# --- Model Constants ---
R = 10.0
"""Resistance [Ω]"""

# --- Model Input ---
V = 5
"""Applied voltage [V]"""

# --- Model Output ---
I = V / R  # Algebraic solution  # noqa: E741
"""Current [A]"""

# --- Print result ---
print("Voltage [V] | Current [A]")
print(f"{V:.2f}        | {I:.2f}")
