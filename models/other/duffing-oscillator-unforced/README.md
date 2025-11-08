# Duffing Oscillator (unforced)

The **Duffing oscillator** is a nonlinear dynamic system that describes the motion of a damped or undamped oscillator with a **nonlinear restoring force**.
Its dynamics are governed by the **Duffing differential equation**:

$$
\frac{d^2x(t)}{dt^2} + \alpha x(t) + x(t)^3 = 0
$$

Where:

- $x(t)$: state variable
- $\alpha$: linear stiffness coefficient

The state variable $x(t)$ can represent many different physical quantities depending on the context. For example, it can represent the position (in meters) of an oscillating mass, with $\frac{dx(t)}{dt}$ representing its velocity (meters per second).

> Note: This model contains one or more **second-order ODEs**.
> Most numerical solvers require the system to be expressed as first-order equations.
> For details on how to do this, see [Reducing Higher-Order ODEs](/docs/ode-reduction.md).

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
