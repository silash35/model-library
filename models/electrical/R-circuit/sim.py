from typing import Final

# --- Model Constants ---
R: Final[float] = 10.0
"""Resistance [Ω]"""

# --- Model Input ---
V = 5
"""Applied voltage [V]"""

# --- Model Output ---
I = V / R  # Algebraic solution
"""Current [A]"""

# --- Print result ---
print("Voltage [V] | Current [A]")
print(f"{V:.2f}        | {I:.2f}")
