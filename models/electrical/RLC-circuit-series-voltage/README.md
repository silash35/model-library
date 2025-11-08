# Series RLC Circuit (Voltage)

> This model follows the general assumptions of **electronic circuit models**.
> For details, see [Electrical Circuits](/models/electrical/README.md).

This section describes a simple electrical circuit composed of a **voltage source**, a **resistor**, an **inductor**, and a **capacitor** connected in series.
The physical system is illustrated in the figure below:

<img src="diagram.svg" alt="Series RLC Circuit Diagram"/>

The dynamics of the circuit are described in terms of the voltage across the capacitor $V_C(t)$:

$$
\frac{d^2V_C(t)}{dt^2} = \frac{1}{LC}\varepsilon(t) - \frac{R}{L}\frac{dV_C(t)}{dt} - \frac{1}{LC}V_C(t)
$$

Where:

- $\varepsilon(t)$: applied voltage [V]
- $V_C(t)$: voltage across the capacitor [V]
- $R$: resistance [Ω]
- $L$: inductance [H]
- $C$: capacitance [F]

> Note: This model contains one or more **second-order ODEs**.
> Most numerical solvers require the system to be expressed as first-order equations.
> For details on how to do this, see [Reducing Higher-Order ODEs](/docs/ode-reduction.md).

## Model Classification

| Property                                 | Classification      |
| ---------------------------------------- | ------------------- |
| Static × Dynamic                         | **Dynamic**         |
| Linear × Nonlinear                       | **Linear**          |
| SISO × SIMO × MISO × MIMO                | **SISO**            |
| Continuous-time × Discrete-time          | **Continuous-time** |
| Time-invariant × Time-variant            | **Time-invariant**  |
| Lumped-parameters × Distributed-elements | **Lumped**          |
| Deterministic × Stochastic               | **Deterministic**   |

## Model Derivation

1. Applying [Kirchhoff’s Voltage Law](/docs/kirchhoff-laws.md) to the loop:

   $`\varepsilon(t) - V_R(t) - V_L(t) - V_C(t) = 0,`$

   where $V_R(t)$, $V_L(t)$, and $V_C(t)$ are the voltage drops across the resistor, inductor, and capacitor, respectively.

2. Applying the [constitutive equations](/docs/electronic-components.md) of the components:

   $`\varepsilon(t) - R I(t) - L \frac{dI(t)}{dt} - V_C(t) = 0,`$

   where $I(t)$ is the current through the circuit.

3. By the **definition of electric current**, the current is the time derivative of charge:

   $`I(t) = \frac{dq(t)}{dt}.`$

   For a capacitor, the charge is related to the voltage by $q(t) = C \cdot V_C(t)$. Substituting into the definition of current:

   $`I(t) = \frac{d}{dt}[C \cdot V_C(t)].`$

   As $C$ is a **constant**, it can be taken outside of the derivative:

   $`I(t) = C \frac{dV_C(t)}{dt}.`$

4. Substitute $I(t) = C \frac{dV_C(t)}{dt}$ into the loop equation:

   $`\varepsilon(t) - R C \frac{dV_C(t)}{dt} - L \frac{d}{dt}[C \frac{dV_C(t)}{dt}] - V_C(t) = 0.`$

5. Simplifying:

   $`\varepsilon(t) - R C \frac{dV_C(t)}{dt} - L C \frac{d^2V_C(t)}{dt^2} - V_C(t) = 0.`$

6. Solving for the second derivative of the capacitor voltage:

   $`L C \frac{d^2V_C(t)}{dt^2} = \varepsilon(t) - R C \frac{dV_C(t)}{dt} - V_C(t),`$

   $`\boxed{\frac{d^2V_C(t)}{dt^2} = \frac{1}{LC}\varepsilon(t) - \frac{R}{L}\frac{dV_C(t)}{dt} - \frac{1}{LC}V_C(t)}`$
