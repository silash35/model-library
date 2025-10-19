# Mechanical Systems

This section of the repository is dedicated to **mechanical system models**.

A mechanical system is a physical system composed of **mechanical components** connected together, through which forces and motions are transmitted.
For a detailed description of these components, see [Mechanical Components](/docs/mechanical-components.md).

## Mathematical Relations

In mechanical systems, motion can be described using linear and rotational quantities. These relationships start from the basic definitions of velocity and acceleration and form the foundation for analyzing dynamics.

- **Linear motion:**

  - Position: $x(t)$
  - Velocity: $v(t) = \frac{dx}{dt}$
  - Acceleration: $a(t) = \frac{dv}{dt} = \frac{d^2x}{dt^2}$

- **Rotational motion:**
  - Angular position: $\theta(t)$
  - Angular velocity: $\omega(t) = \frac{d\theta}{dt}$
  - Angular acceleration: $\alpha(t) = \frac{d\omega}{dt} = \frac{d^2\theta}{dt^2}$

## Assumptions

Unless explicitly stated otherwise, all models in this section consider the following assumptions:

- Mechanical elements behave ideally, exactly according to their constitutive relations.
- Unless explicitly stated otherwise, all friction is ignored. When considered, it follows ideal static or kinetic behavior.
- Mass is ideal, i.e., uniformly distributed, and applied forces are uniformly distributed, without deformations.
- The laws of [classical mechanics](/docs/newton-laws.md) are perfectly applied. Relativistic effects are ignored as they are negligible.
