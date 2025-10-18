# Circuit Components

This section describes the fundamental circuit components commonly used in electrical and electronic circuits.
Each component is assumed to be ideal, meaning it operates exactly according to its defining equations, without losses or imperfections.

## Linear Components

Linear components are circuit elements whose voltage-current relationship is linear.
They are passive (do not generate energy) and form the basic building blocks of linear circuits.

### Resistor

A **resistor** is a passive component that opposes the flow of electric current.
Its constitutive equation is given by **Ohm’s Law**:

$$
V_R(t) = R \cdot I_R(t)
$$

Where:

- $V_R(t)$: voltage across the resistor [V]
- $I_R(t)$: current through the resistor [A]
- $R$: resistance [Ω]

In an ideal model, $R$ is constant and independent of temperature, frequency, or current. A resistor that behaves this way is called ohmic, producing a linear relationship between voltage and current, as described by Ohm’s Law.

### Capacitor

A **capacitor** is a passive component that stores energy in the form of an electric field.

Its constitutive equation is defined by the voltage across its terminals as a function of the stored charge:

$$
V_C(t) = \frac{q(t)}{C}
$$

Where:

- $q(t)$: charge stored in the capacitor [C]
- $V_C(t)$: voltage across the capacitor [V]
- $C$: capacitance [F]

### Inductor

An **inductor** is a passive component that stores energy in the form of a magnetic field.
Its constitutive equation is:

$$
V_L(t) = L \cdot \frac{dI_L(t)}{dt}
$$

Where:

- $V_L(t)$: voltage across the inductor [V]
- $I_L(t)$: current through the inductor [A]
- $L$: inductance [H]

## Non Linear Components

Nonlinear components have nonlinear behavior, and their characteristics cannot be described accurately by simple linear equations.

### Diode

A diode is a semiconductor device that primarily allows current to flow in one direction, blocking it (ideally) in the reverse direction.

The diode’s behavior can be described by several models and equations, depending on the desired level of accuracy.
A common model for the diode is the **Shockley diode equation**, which describes its current-voltage behavior as:

$$
i_D = i_S \left(e^{V_D / (n V_T)} - 1 \right)
$$

Where:

- $i_D$: diode current [A]
- $V_D$: voltage across the diode [V]
- $i_S$: reverse saturation current [A]
- $n$: ideality factor
- $V_T$: thermal voltage (~26 mV at room temperature)
