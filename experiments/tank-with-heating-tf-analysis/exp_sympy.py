from typing import Final

import sympy as sp

# --- Linear Model ---
# A and B matrices (from Heated Tank System Linearization Experiment)
A: Final = sp.Matrix(
    [[-0.00254647908947033, 0], [0.125202737391988, -0.00509295817894066]]
)
B: Final = sp.Matrix(
    [
        [0.141471060526129, 0, 0],
        [-3.72472460767435, 6.58322109947318, 0.00509295817894066],
    ]
)

# --- Transfer Matrix ---
s = sp.symbols("s")
I = sp.eye(A.rows)
G = (s * I - A).inv() * B

# Simplify the transfer matrix
G = sp.simplify(G)  # Simplify the transfer matrix

# --- Analysing Matrix ---
print("--- Analysing each transfer function in the matrix: ---\n")
for i in range(G.rows):
    for j in range(G.cols):
        Gij = G[i, j]
        print(f"- G[{i},{j}] = {Gij}")

        if Gij == 0:
            print(f"  Skipping G[{i},{j}] as it is zero.\n")
            continue

        # Get numerator and denominator
        num, den = sp.fraction(Gij)

        # Compute the poles by finding the numerical roots of the denominator.
        den_poly = sp.Poly(den, s)
        poles = den_poly.nroots()
        print(f"  Poles: {poles}\n")
