# Van der Pol Oscillator (unforced)

The **Van der Pol oscillator** is a classical nonlinear dynamical system that exhibits self-sustained oscillations, where energy is alternately stored and dissipated depending on the system state.

Its dynamics are governed by the **Van der Pol differential equation**:

$$
\frac{d^2x(t)}{dt^2} + \mu (x(t)^2 - 1)\frac{dx(t)}{dt} + x(t) = 0
$$

Where:

- $x(t)$: state variable
- $\mu$: nonlinearity parameter ($\mu > 0$)

The state variable $x(t)$ can represent many different physical quantities depending on the context. For example, it can represent the position (in meters) of an oscillating mass, with $\frac{dx(t)}{dt}$ representing its velocity (meters per second).

> Note: This is a **second-order ODE**, so some numerical solvers may require reducing it to a system of first-order equations.
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
