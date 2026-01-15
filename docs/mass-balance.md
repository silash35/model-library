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

> [!NOTE]
> 💡 For many physical systems, like tanks, generation, and consumption are zero unless reactions are considered.

### Differential Form

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

## Component (Species) Mass Balance

In addition to tracking the **total mass**, many engineering systems also require tracking the mass (or concentration) of **individual chemical species** inside the control volume.

A component balance applies the same conservation principles, but for each species separately.
Just like the overall mass balance, it can be expressed as:

$$
\text{Accumulation of species } i = \text{Input of } i - \text{Output of } i + \text{Generation of } i - \text{Consumption of } i
$$

### Differential Form

For a species $i$, the general differential balance is:

$$
\frac{d(n_i(t))}{dt} = \dot{n}_{i,in}(t) - \dot{n}_{i,out}(t) + \dot{n}_{i,gen}(t) - \dot{n}_{i,cons}(t)
$$

Where:

- $n_i(t)$: Moles or mass of species $i$ inside the system
- $\dot{n}_{i,in}(t)$: Flow rate of species $i$ entering the system
- $\dot{n}_{i,out}(t)$: Flow rate of species $i$ leaving the system
- $\dot{n}_{i,gen}(t)$: Rate of formation of species $i$ by chemical reaction
- $\dot{n}_{i,cons}(t)$: Rate of consumption of species $i$ by chemical reaction
