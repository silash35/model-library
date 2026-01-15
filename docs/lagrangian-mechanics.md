# Lagrangian Mechanics

**Lagrangian mechanics** is a reformulation of classical mechanics that provides a powerful and elegant framework for describing the motion of physical systems.

> [!NOTE]
> To see the Newtonian formulation, see [Newton's Laws of Motion](/docs/newton-laws.md).

The central quantity in Lagrangian mechanics is the **Lagrangian**, denoted by $L$, defined as:

$$
L = T - V
$$

Where:

- $L$: Lagrangian [J]
- $T$: total kinetic energy of the system [J]
- $V$: total potential energy of the system [J]

> [!NOTE]
> For more details on the definition of energy and its main types, see [Energy](/docs/energy.md).

Once $L$ is expressed in terms of the system’s generalized coordinates $q_i$, it becomes possible to determine how the system evolves in time. The relationship between these quantities is expressed through the **Lagrange’s Equation of Motion**, which provides one equation for each coordinate $q_i$:

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}_i}\right) - \frac{\partial L}{\partial q_i} = Q_i
$$

Where:

- $q_i$: generalized coordinate
- $\dot{q}_i$: generalized velocity
- $Q_i$: generalized external force corresponding to $q_i$

This differential equation governs the system’s dynamics, including the effects of external forces.
