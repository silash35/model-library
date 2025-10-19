# Mechanical System Components

This section describes the fundamental components commonly used in mechanical systems.
They are characterized by their constitutive equations, which define the relationship between force, displacement, velocity, and other system variables.
Here, we assume all components are ideal, meaning they behave exactly according to these equations, without losses, or imperfections.

## Spring (Hooke’s Law)

A spring resists deformation by exerting a force proportional to its displacement from equilibrium. This is described by **Hooke’s Law**:

$$F = k x$$

Where:

- $F$: force exerted by the spring [N]

- $k$: spring constant [N/m]

- $x$: displacement from the equilibrium position [m]

## Damper (Viscous Damping)

A damper resists motion by exerting a force proportional to the velocity of the moving object. This behavior is described by the viscous damping model, expressed as:

$$F = c v$$

Where:

- $F$: damping force [N]

- $c$: damping coefficient [N·s/m]

- $v$: velocity of the object relative to the damper [m/s]

## Friction

Friction resists relative motion between two surfaces and always acts opposite to motion or its tendency.

### Static Friction

Acts when there is no relative motion.
Prevents movement until the applied force exceeds a limit:

$$F_s = \mu_s N$$

Where:

- $F_s$ = maximum static friction [N]
- $\mu_s$ = coefficient of static friction [–]
- $N$ = normal force [N]

### Kinetic Friction

Acts when surfaces slide relative to each other.
Usually smaller than static friction:

$$F_k = \mu_k N$$

where

- $F_k$ = kinetic friction [N]
- $\mu_k$ = coefficient of kinetic friction [–]
- $N$ = normal force [N]
