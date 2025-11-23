# Cubic Tank with Gravity-Driven Outlet

> 💡 This model also applies to other tanks with a **constant cross-sectional area**, such as tanks with a rectangular or circular base.
> You just need to replace the numerical value of $A$ with the correct base area.

This section describes the model of a **cubic tank** with a **pumped inlet**, where the outlet flow is **gravity-driven** and influenced by the liquid level.
The liquid level inside the tank changes according to the balance between the inflow and outflow rates.

The physical system is illustrated in the figure below:

<img src="diagram.svg" alt="Modeled Tank Diagram"/>

The liquid level dynamics can be mathematically described by the following equation:

$$\frac{dh(t)}{dt}=\frac{Q_{in}(t) - \alpha \sqrt{h(t)}}{A}$$

Where:

- $h(t)$: liquid level [m]
- $Q_{in}(t)$: inlet volumetric flow rate [m³/s]
- $A = L^2$: tank cross-sectional area [m²]
- $\alpha$: outlet discharge parameter [m $^{2.5}$/s]

Since the tank is cubic, the liquid level is naturally constrained by its physical height:

$$0 \le h(t) \le L$$

## Model Assumptions

This model follows the assumptions established in [Cubic Tank with Gravity-Driven Outlet (With Momentum)](/models/tank/cubic-gravity-and-momentum/README.md), with a single additional simplification:

- The outlet pipe velocity is assumed constant (the momentum dynamics in the pipe are neglected).

All other assumptions from the original model remain valid and unchanged.

## Model Classification

| Property                                 | Classification      |
| ---------------------------------------- | ------------------- |
| Static × Dynamic                         | **Dynamic**         |
| Linear × Nonlinear                       | **Nonlinear**       |
| SISO × SIMO × MISO × MIMO                | **SISO**            |
| Continuous-time × Discrete-time          | **Continuous-time** |
| Time-invariant × Time-variant            | **Time-invariant**  |
| Lumped-parameters × Distributed-elements | **Lumped**          |
| Deterministic × Stochastic               | **Deterministic**   |
| Forced × Homogeneous                     | **Forced**          |

## Model Derivation

1. Approximation of the Outlet Velocity

   Following the derivation of the [Cubic Tank With Gravity-Driven Outlet (With Momentum)](/models/tank/cubic-gravity-and-momentum/README.md), we apply the additional assumption that the outlet pipe velocity remains constant, effectively neglecting the momentum dynamics in the pipe:

   $\frac{dv_p(t)}{dt} = 0.$

   Applying this to the original momentum balance,

   $m_p \frac{dv_p}{dt} = \gamma A_p h(t) - k_f v_p^2(t),$

   gives the steady-state relation:

   $0 = \gamma A_p h(t) - k_f v_p^2(t),$

   from which the outlet velocity follows:

   $v_p(t) = \sqrt{\frac{\gamma A_p}{k_f}\, h(t)}.$

2. Substituting into the Mass Balance

   $\frac{dh(t)}{dt} = \frac{Q_{in}(t) - A_p \, v_p(t)}{A},$

   yields

   $\frac{dh(t)}{dt} = \frac{Q_{in}(t) - A_p \sqrt{\frac{\gamma A_p}{k_f}\, h(t)}}{A}.$

   Defining the effective discharge coefficient

   $\alpha = A_p \sqrt{\frac{\gamma A_p}{k_f}},$

   the final reduced nonlinear model becomes:

   $\boxed{\frac{dh(t)}{dt}=\frac{Q_{in}(t) - \alpha \sqrt{h(t)}}{A}}.$
