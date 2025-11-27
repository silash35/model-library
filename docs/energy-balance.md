# 🔥 Energy Balance

Many models in this repository rely on the **principle of energy conservation**.
This document explains the concept of **energy balance** and its general formulation.

## What is an Energy Balance?

An **energy balance** is a mathematical statement of the **first law of thermodynamics**, which states that **energy cannot be created or destroyed**, only transferred or transformed.

A general energy balance can be written as:

$$
\text{Accumulation of Energy} = \text{Energy In} - \text{Energy Out} \pm \text{Heat Transfer} \pm \text{Shaft Work}
$$

Where:

- **Accumulation of Energy**: Rate of change of total energy stored in the system
- **Energy In/Out**: Energy carried by mass entering or leaving the system
- **Heat Transfer ($\dot{Q}$)**: Heat added to ($+$) or removed from ($-$) the system
- **Shaft Work ($\dot{W}_s$)**: Mechanical work done on ($+$) or by ($-$) the system

## Differential Form

The full differential energy balance, including internal, kinetic, and potential energy, is:

$$
\frac{d\left(U + E_c + E_p\right)}{dt} = \sum_{i=1}^{n_u} \rho_i q_i \left(h_i + E_{c_i} + E_{p_i}\right) - \sum_{j=1}^{n_y} \rho_j q_j \left(h_j + E_{c_j} + E_{p_j}\right) \pm \dot{Q} \pm \dot{W}_s
$$

Where:

- $U$: Internal energy [J]
- $E_c$: Kinetic energy [J]
- $E_p$: Potential energy [J]
- $\rho_i q_i$: Mass flow rate of the $i$-th inlet stream [kg/s]
- $h_i$: Specific enthalpy of the $i$-th inlet stream [J/kg]
- $E_{c_i}$: Specific kinetic energy of the $i$-th inlet stream [J/kg]
- $E_{p_i}$: Specific potential energy of the $i$-th inlet stream [J/kg]
- $\rho_j q_j$: Mass flow rate of the $j$-th outlet stream [kg/s]
- $h_j$: Specific enthalpy of the $j$-th outlet stream [J/kg]
- $E_{c_j}$: Specific kinetic energy of the $j$-th outlet stream [J/kg]
- $E_{p_j}$: Specific potential energy of the $j$-th outlet stream [J/kg]
- $\dot{Q}$: Heat added to the system [J/s]
- $\dot{W}_s$: Shaft work [J/s]
