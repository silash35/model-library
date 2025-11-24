# Cubic Tank With Gravity-Driven Outlet (With Momentum)

> 💡 This model also applies to other tanks with a **constant cross-sectional area**, such as tanks with a rectangular or circular base.
> You just need to replace the numerical value of $A$ with the correct base area.

This section describes the model of a **cubic tank** with a **pumped inlet**, where the outlet flow is **gravity-driven** and influenced by both the liquid level and by the **momentum** dynamics within the discharge pipe.
The liquid level inside the tank changes according to the balance between the inflow and outflow rates.

The physical system is illustrated in the figure below:

<img src="diagram.svg" alt="Modeled Tank Diagram"/>

The dynamics of the system are described in terms of the liquid level in the tank $h(t)$ and the fluid velocity in the outlet pipe $v_p(t)$:

$$
\begin{cases}
  \displaystyle \frac{dh(t)}{dt} = \frac{Q_{in}(t) - A_p \cdot v_p(t)}{A} \\
  \displaystyle \frac{dv_p(t)}{dt} = \frac{\gamma A_p \cdot h(t) - k_f \cdot v_p^2(t)}{m_p}
\end{cases}
$$

Where:

- $h(t)$: liquid level [m]
- $Q_{in}(t)$: inlet volumetric flow rate [m³/s]
- $v_p(t)$: fluid velocity in the outlet pipe [m/s]
- $A = L^2$: tank cross-sectional area [m²]
- $A_p$: pipe cross-sectional area [m²]
- $m_p$: fluid mass inside the pipe [kg]
- $\gamma$: specific weight of the fluid [N/m³]
- $k_f$: friction coefficient in the pipe [kg/m]

Since the tank is cubic, the liquid level is naturally constrained by its physical height:

$$0 \le h(t) \le L$$

## Model Assumptions

- The tank has a constant square cross-section with side length $L$.
- The fluid is incompressible, with constant density.
- No chemical reactions, leaks, or evaporation are considered.
- Mass accumulation varies only inside the tank. The mass inside the outlet pipe is constant (the pipe is always full).
- Momentum accumulation occurs only inside the outlet pipe.
- The inlet flow is pumped.
- The outlet flow does not reverse direction: the fluid velocity in the outlet pipe is always non-negative.
- The outlet pipe is connected at the bottom of the tank, so the hydrostatic driving pressure is proportional to the liquid level.

## Model Classification

| Property                                 | Classification      |
| ---------------------------------------- | ------------------- |
| Static × Dynamic                         | **Dynamic**         |
| Linear × Nonlinear                       | **Nonlinear**       |
| SISO × SIMO × MISO × MIMO                | **SIMO**            |
| Continuous-time × Discrete-time          | **Continuous-time** |
| Time-invariant × Time-variant            | **Time-invariant**  |
| Lumped-parameters × Distributed-elements | **Lumped**          |
| Deterministic × Stochastic               | **Deterministic**   |
| Forced × Homogeneous                     | **Forced**          |

## Model Derivation

We want to model the coupled dynamics of the liquid level $h(t)$ in the tank and the fluid velocity $v_p(t)$ in the outlet pipe.

### Mass Balance in the Tank

1. Write the [mass balance](/docs/mass-balance.md) of the liquid in the tank:

   $`\frac{dM(t)}{dt} = \dot{M}_{in}(t) - \dot{M}_{out}(t)`$

   Where $M(t)$ is the mass of the liquid [kg], and $\dot{M}_{in}$, $\dot{M}_{out}$ are the mass flow rates [kg/s].

   In this case, there are no generation or consumption terms, since the liquid does not undergo any chemical reactions and there are no internal sources or sinks of mass.
   Therefore, the balance reduces to a simple relation between the inlet and outlet flows.

2. Expanding the mass terms:

   To rewrite the mass balance using measurable physical quantities, we expand each mass term using the definitions of **mass**, **density**, **volume**, and **volumetric flow rate**:

   $`M(t) = \rho \cdot V(t)`$

   $`\dot{M}_{in}(t) = \rho \cdot Q_{in}(t)`$

   For the outlet, the volumetric flow through the pipe is given by the pipe cross-sectional area multiplied by the fluid velocity:

   $`Q_{out}(t) = A_p \cdot v_p(t)`$

   Therefore, the outlet mass flow rate becomes:

   $`\dot{M}_{out}(t) = \rho \cdot Q_{out}(t) = \rho \cdot A_p \cdot v_p(t)`$

   Substituting these expressions into the mass balance gives:

   $`\frac{d(\rho V(t))}{dt} = \rho \cdot Q_{in}(t) - \rho \cdot A_p \cdot v_p(t)`$

3. Simplifying the Balance

   For an **incompressible fluid** with constant density $\rho$, we can take $\rho$ out of the derivative:

   $`\rho \frac{d(V(t))}{dt} = \rho \cdot Q_{in}(t) - \rho \cdot A_p \cdot v_p(t)`$

   And then simplify the equation by dividing both sides by $\rho$:

   $`\frac{dV(t)}{dt} = Q_{in}(t) - A_p \cdot v_p(t)`$

4. Express in Terms of Liquid Height

   To relate the liquid volume to the liquid height, we use the fact that the tank has a constant cross-sectional area $A$. Thus:

   $`V(t) = A \cdot h(t)`$

   Substituting this relation into the volumetric balance:

   $`\frac{d(A \cdot h(t))}{dt} = Q_{in}(t) - A_p \cdot v_p(t)`$

   Since the area $A$ is constant:

   $`A\frac{dh(t)}{dt} = Q_{in}(t) - A_p \cdot v_p(t)`$

   Finally, dividing both sides by $A$ gives the **dynamic equation for the liquid level**:

   $`\boxed{\frac{dh(t)}{dt} = \frac{Q_{in}(t) - A_p \cdot v_p(t)}{A}}`$

### Momentum Balance in the Outlet Pipe

1. Apply [Newton’s Second Law](/docs/newton-laws.md) to the fluid contained in the outlet pipe:

   According to Newton’s Second Law, the sum of axial forces acting on the fluid column equals its mass times its acceleration:

   $`F_{net}(t) = m_p \cdot \frac{dv_p(t)}{dt}`$

   The net force $F_{net}(t)$ is given by the hydrostatic driving force at the tank outlet minus the pipe resistive (friction) force:

   $`F_{net}(t) = F_{pressure}(t) - F_{friction}(t)`$

   Where:

   - $F_{pressure}(t)$: driving force generated by the hydrostatic pressure at the bottom of the tank.
   - $F_{friction}(t)$: resistive force due to viscous and turbulent friction along the pipe walls.

2. Modeling the pressure and friction force:

   Since the pressure at the tank outlet is $\gamma \cdot h(t)$, multiplying this pressure by the pipe cross-sectional area $A_p$ gives the total axial force pushing the fluid through the pipe:

   $`F_{pressure}(t) = \gamma \cdot A_p \cdot h(t)`$

   A simple lumped model for pipe friction (see [Hydrodynamic Friction](/docs/mechanical-components.md)) is:

   $`F_{friction}(t) = k_f \cdot v_p(t) \cdot |v_p(t)|`$

   Since reverse flow does not occur in this system, the outlet velocity is always non-negative, allowing the simplification $v_p(t) \cdot |v_p(t)| = v_p^2(t)$.

3. Final expression:

   Combining the expressions above into Newton’s Second Law gives:

   $`\boxed{\frac{dv_p(t)}{dt} = \frac{\gamma A_p \cdot h(t) - k_f \cdot v_p^2(t)}{m_p}}`$
