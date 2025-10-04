# Kirchhoff's Laws

Kirchhoff's Laws are fundamental principles used to analyze **electrical circuits**.

## 1. Kirchhoff's Current Law

Kirchhoff's Current Law (also called Kirchhoff's first law or Kirchhoff's junction rule) states that the **total current entering a node is equal to the total current leaving the node**. Mathematically:

$$
\sum_{k=1}^{n} I_k = 0
$$

Where:

- $I_k$ are the currents flowing **toward or away from a node**.
- Currents entering the node are considered positive, and currents leaving are negative (or vice versa, as long as you are consistent).

This law can be seen as analogous to a [mass balance](/docs/mass-balance.md) in fluid systems.
However, since wires cannot store significant charge, the accumulation at the node is effectively zero.

## 2. Kirchhoff's Voltage Law

Kirchhoff's Voltage Law (also called Kirchhoff's second law or Kirchhoff's loop rule) states that the **sum of voltages around any closed loop in a circuit is zero**. Mathematically:

$$
\sum_{k=1}^{n} V_k = 0
$$

Where:

- $V_k$ are the voltages across each component in the loop.
