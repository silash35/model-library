# Simple Reactor-Separator Integrated Process Network

This system describes the dynamic model of an integrated process network consisting of two continuous stirred tank reactors (CSTRs) and a liquid-vapor separator.

The physical system is illustrated in the figure:

<img src="diagram.svg" alt="Reactor-Separator Integrated Process Network"/>

This model is a simplified version of the
[Reactor-Separator Integrated Process Network](/models/reactor/two-CSTRs-and-separator/README.md) in which the volumetric holdups are treated as constant parameters rather than state variables, removing the integrating effect of the volume dynamics.

## Model Assumptions

This model builds on the assumptions of the [Reactor-Separator Integrated Process Network](/models/reactor/two-CSTRs-and-separator/README.md).

In addition, the volumetric holdups of the reactors and the separator are assumed constant.

## Model Classification

| Property                                 | Classification      |
| ---------------------------------------- | ------------------- |
| Static × Dynamic                         | **Dynamic**         |
| Linear × Nonlinear                       | **Nonlinear**       |
| SISO × SIMO × MISO × MIMO                | **MIMO**            |
| Continuous-time × Discrete-time          | **Continuous-time** |
| Time-invariant × Time-variant            | **Time-invariant**  |
| Lumped-parameters × Distributed-elements | **Lumped**          |
| Deterministic × Stochastic               | **Deterministic**   |
| Forced × Homogeneous                     | **Forced**          |

## Model Derivation

> **TODO:** Add model derivation.
