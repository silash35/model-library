# Simple Pendulum System

This section describes a simple **mechanical system** composed of a **point mass** suspended by a **massless, rigid rod** of length $L$ that swings under the influence of gravity.

The physical system is illustrated in the figure below:

<img src="diagram.svg" alt="Simple Pendulum System Diagram"/>

The dynamics of the system are described in terms of the angular displacement $\theta(t)$ from the vertical:

$$
\frac{d^2 \theta(t)}{dt^2} = -\frac{g}{L} \sin(\theta(t))
$$

Where:

- $\theta(t)$: angular displacement [rad]
- $L$: pendulum length [m]
- $g$: gravitational acceleration [m/s²]

> Note: This model contains one or more **second-order ODEs**.
> Most numerical solvers require the system to be expressed as first-order equations.
> For details on how to do this, see [Reducing Higher-Order ODEs](/docs/ode-reduction.md).

## Model Assumptions

This model builds on the general assumptions of **mechanical system models**.
For details on the general assumptions, see [Mechanical Systems](/models/mechanical/README.md).

In addition, for the simple pendulum system, we assume:

- The rod is **thin and rigid**, and its mass is negligible compared to the point mass.
- The point mass is treated as a **concentrated mass** at the end of the rod.
- The pivot point is fixed and frictionless.
- The motion occurs in a vertical plane under the influence of gravity only.
- Small rotational inertia of the rod is ignored.

## Model Classification

| Property                                 | Classification      |
| ---------------------------------------- | ------------------- |
| Static × Dynamic                         | **Dynamic**         |
| Linear × Nonlinear                       | **Nonlinear**       |
| SISO × SIMO × MISO × MIMO                | **Not applicable**  |
| Continuous-time × Discrete-time          | **Continuous-time** |
| Time-invariant × Time-variant            | **Time-invariant**  |
| Lumped-parameters × Distributed-elements | **Lumped**          |
| Deterministic × Stochastic               | **Deterministic**   |

## Model Derivation

We will derive the equation of motion using **Lagrangian mechanics**.
For an introduction to this method, see [Lagrangian Mechanics](/docs/lagrangian-mechanics.md).

1. Define the coordinates of the mass

   Let the pivot point (the ceiling) be defined as the origin of the coordinate system.
   The pendulum forms a right triangle, where the rod of length $L$ is the hypotenuse and the angle $\theta$ is measured from the vertical.
   Therefore, the horizontal and vertical positions of the mass (the end of the rod) can be written as:

   $`x_c = L \cdot \sin(\theta)`$

   $`y_c = L - L \cdot \cos(\theta)`$

2. Compute the velocity components

   The time derivatives of these coordinates are obtained using the **chain rule**, since the angle $\theta$ varies with time.
   Differentiating $x_c$ and $y_c$ with respect to time gives:

   $`\dot{x}_c = L \cdot \cos(\theta) \cdot \dot{\theta}`$

   $`\dot{y}_c = L \cdot \sin(\theta) \cdot \dot{\theta}`$

3. Write the expression for the total kinetic energy

   The total kinetic energy $T$ of the system is the translational kinetic energy of the center of mass:

   $`T = \frac{1}{2} m \left( \dot{x}_c^2 + \dot{y}_c^2 \right)`$

   We can simplify the translational kinetic energy by substituting the expressions for $\dot{x}_c$ and $\dot{y}_c$:

   $`\dot{x}_c^2 + \dot{y}_c^2 = (L \cos(\theta) \dot{\theta})^2 + (L \sin(\theta) \dot{\theta})^2`$

   Factorizing $\dot{\theta}^2 L^2$:

   $`\dot{x}_c^2 + \dot{y}_c^2 = L^2 \dot{\theta}^2 (\cos^2(\theta) + \sin^2(\theta))`$

   Using the trigonometric identity $\cos^2(\theta) + \sin^2(\theta) = 1$, this simplifies to:

   $`\dot{x}_c^2 + \dot{y}_c^2 = L^2 \dot{\theta}^2`$

   Therefore, the total kinetic energy becomes:

   $`T = \frac{1}{2} m L^2 \dot{\theta}^2`$

4. Write the expression for the potential energy

   The potential energy $V$ of the system is due to gravity:

   $`V = m \cdot g \cdot y_c`$

   Substituting $\dot{y}_c$ into the potential energy equation:

   $`V = m \cdot g \cdot L \cdot (1 - \cos(\theta))`$

   > For more details about kinetic and potential energy, see [Energy](/docs/energy.md).

5. Form the Lagrangian $(\mathcal{L})$

   The Lagrangian of the system is defined as the difference between kinetic and potential energy:

   $`\mathcal{L} = T - V`$

   Substituting the expressions for kinetic and potential energy, the Lagrangian of the system is:

   $`\mathcal{L} = \frac{1}{2} m L^2 \dot{\theta}^2 - m g L (1 - \cos(\theta))`$

6. Compute the necessary derivatives for Lagrange’s equation

   The Lagrange’s equation of motion is:

   $`\frac{d}{dt}\left(\frac{\partial \mathcal{L}}{\partial \dot{\theta}}\right) - \frac{\partial \mathcal{L}}{\partial \theta} = Q_\theta`$

   $Q_\theta$ represents a generalized torque.
   For the simple pendulum, we assume no damping or external torque, so:
   $`Q_\theta = 0`$.

   For the other terms of the equation:

   $`\frac{\partial \mathcal{L}}{\partial \dot{\theta}} = m L^2 \dot{\theta}`$

   $`\frac{d}{dt} \left( \frac{\partial \mathcal{L}}{\partial \dot{\theta}} \right) = m L^2 \ddot{\theta}`$

   $`\frac{\partial \mathcal{L}}{\partial \theta} = - m g L \sin(\theta)`$

   Substituting into Lagrange’s equation:

   $`m L^2 \ddot{\theta} + m g L \sin(\theta) = 0`$

7. Simplify and isolate $\ddot{\theta}$

   This is the **final equation of motion** for the simple pendulum.

   $`\boxed{
   \frac{d^2 \theta(t)}{dt^2} = -\frac{g}{L} \sin(\theta(t))
   }`$
