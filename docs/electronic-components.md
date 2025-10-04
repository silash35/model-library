# Circuit Components

This section describes the fundamental circuit components, each assumed to be ideal, that is, they operate exactly according to their defining equations, with no losses or imperfections.

## Resistor

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

## Capacitor

A **capacitor** is a passive component that stores energy in the form of an electric field.

Its constitutive equation is defined by the voltage across its terminals as a function of the stored charge:

$$
V_C(t) = \frac{q(t)}{C}
$$

Where:

- $q(t)$: charge stored in the capacitor [C]
- $V_C(t)$: voltage across the capacitor [V]
- $C$: capacitance [F]

## Inductor

An **inductor** is a passive component that stores energy in the form of a magnetic field.
Its constitutive equation is:

$$
V_L(t) = L \cdot \frac{dI_L(t)}{dt}
$$

Where:

- $V_L(t)$: voltage across the inductor [V]
- $I_L(t)$: current through the inductor [A]
- $L$: inductance [H]
