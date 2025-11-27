# ⚖️ Mass Balance

Many models in this repository are based on the **principle of mass conservation**.
This document explains the concept of **mass balance** and its general formulation.

## What is a Mass Balance?

A **mass balance** (or **material balance**) is a mathematical expression of the **law of conservation of mass**, which states that **mass cannot be created or destroyed** in a closed system.

It is commonly written as:

$$
\text{Accumulation} = \text{Input} - \text{Output} + \text{Generation} - \text{Consumption}
$$

Where:

- **Accumulation**: Change of mass stored in the system over time
- **Input**: Mass entering the system
- **Output**: Mass leaving the system
- **Generation**: Mass produced inside the system (e.g., by chemical reactions)
- **Consumption**: Mass consumed inside the system (e.g., by chemical reactions)

> 💡 For many physical systems, like tanks, generation, and consumption are zero unless reactions are considered.

## Differential Form

In differential form, the mass balance can be written as:

$$
\frac{dM(t)}{dt} = \dot{M}_{in}(t) - \dot{M}_{out}(t) + \dot{M}_{gen}(t) - \dot{M}_{cons}(t)
$$

Where:

- $M(t)$: Total mass inside the control volume at time $t$ [kg]
- $\dot{M}_{in}(t)$: Mass flow rate entering the system [kg/s]
- $\dot{M}_{out}(t)$: Mass flow rate leaving the system [kg/s]
- $\dot{M}_{gen}(t)$: Mass generation rate inside the system [kg/s]
- $\dot{M}_{cons}(t)$: Mass consumption rate inside the system [kg/s]
