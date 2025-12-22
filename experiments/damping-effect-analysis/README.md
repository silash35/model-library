# Mass–Spring–Damper: Effect of Damping on System Response

This experiment explores how the **mass–spring–damper system** behaves under different damping conditions.

## 📎 Related Model

- [**Mass–Spring–Damper System**](/models/mechanical/mass–spring–damper/README.md)

## 🧪 Methodology

We simulate the mass–spring–damper system **seven times**, varying the **damping coefficient** $c$ while keeping the other parameters constant.

The **damping ratio** $\xi$ is a dimensionless parameter that characterizes how the system dissipates energy:

$$\xi = \frac{c}{2 \sqrt{k m}}$$

The chosen damping coefficients result in damping ratios that demonstrate different behaviors:

1. **Monotonically unstable:** $\xi \le -1$
2. **Oscillatory unstable:** $-1 < \xi < 0$
3. **Undamped:** $\xi = 0$
4. **Underdamped:** $0 < \xi < 1$
5. **Critically damped:** $\xi = 1$
6. **Overdamped:** $\xi > 1$

Each case is simulated over the same time interval using a numerical solver, allowing a direct comparison of how the system response changes with the damping.

## 📊 Results and Conclusions

<img src="results/scipy.png" alt="Mass–Spring–Damper System Response (SciPy)"/>

The simulation shows the system response for different damping ratios under a constant external force:

- **$\xi$ = -1.8**: Monotonically unstable, the response diverges without oscillations.
- **$\xi$ = -1**: Monotonically unstable, the response diverges without oscillations, but more slowly than for $\xi = -1.8$.
- **$\xi$ = -0.2**: Oscillatory unstable, the system oscillates, but the amplitude grows over time.
- **$\xi$ = 0**: Undamped, oscillates indefinitely around equilibrium.
- **$\xi$ = 0.2**: Underdamped, oscillates but gradually settles.
- **$\xi$ = 1**: Critically damped, returns to equilibrium fastest without oscillations.
- **$\xi$ = 1.8**: Overdamped, returns to equilibrium slowly without oscillations.

> Note: $\xi = 0$ represents an ideal undamped system, which oscillates indefinitely without losing energy.
> Negative damping ratios ($\xi < 0$), however, are non-physical in real mass–spring–damper systems, as they would imply the system gains energy over time.

These results illustrate not only how damping changes the transient response of the system, but also how the system's behavior can change **dramatically** depending on its parameters.
