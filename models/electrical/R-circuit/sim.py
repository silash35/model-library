import os
from typing import Final

# --- Setup save txt ---
script_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(script_dir, "simulations"), exist_ok=True)
save_txt = os.path.join(script_dir, "simulations", "python.txt")

# Clear the file (create empty if it doesn't exist)
open(save_txt, "w", encoding="utf-8").close()


def write_line(line: str):
    """Append a line of text to save_txt."""
    with open(save_txt, "a", encoding="utf-8") as f:
        f.write(line + "\n")


# --- Model Constant ---
R: Final = 10.0
"""Resistance [Ω]"""

# --- Model Input ---
V = 5
"""Applied voltage [V]"""

# --- Model Output ---
I = V / R  # Algebraic solution
"""Current [A]"""

# --- Save result to file ---
write_line("Voltage [V] | Current [A]")
write_line(f"{V:.2f}        | {I:.2f}")

print(f"Result saved to {save_txt}")
