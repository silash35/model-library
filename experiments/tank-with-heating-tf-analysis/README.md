# Heated Tank System: Transfer Function Analysis

This experiment extends the previous study on the [linearization of the heated tank](/experiments/tank-with-heating-linearization/README.md).
Now that we have the linearized state-space model, we derive the transfer functions and analyze the stability of the tank as a linear system.

## 📎 Related Model

- [**Heated Tank**](/models/tank/with-heating/README.md)

## 🧪 Methodology

### 1. Constructing the Transfer Function Matrix

Starting from the linearized state-space model obtained in the previous experiment ([Heated Tank System: Linearization Comparison](/experiments/tank-with-heating-linearization/README.md)):

$$
\dot{\bar{\mathbf{x}}} =
\mathbf{A} \bar{\mathbf{x}} + \mathbf{B} \bar{\mathbf{u}}
$$

> [!IMPORTANT]
> To keep notation light, from now on we will drop the deviation bar and simply write $\mathbf{x}$ and $\mathbf{u}$ for the deviation variables. All expressions below refer to deviations from the operating point.

We apply the Laplace transform:

$$
\mathcal{L}\{\dot{\mathbf{x}} = \mathbf{A} \mathbf{x} + \mathbf{B} \mathbf{u}\}
$$

$$
\mathcal{L}\{\dot{\mathbf{x}}\} = \mathcal{L}\{\mathbf{A} \mathbf{x} + \mathbf{B} \mathbf{u}\},
$$

so the transformed state equation becomes:

$$
s\mathbf{X}(s) = \mathbf{A}\,\mathbf{X}(s) + \mathbf{B}\,\mathbf{U}(s).
$$

Rearrange terms:

$$
s\mathbf{X}(s) - \mathbf{A}\,\mathbf{X}(s) = \mathbf{B}\,\mathbf{U}(s).
$$

Factor out $\mathbf{X}(s)$:

$$
(s\mathbf{I} - \mathbf{A})\,\mathbf{X}(s) = \mathbf{B}\,\mathbf{U}(s)
$$

Here, $\mathbf{I}$ is the **identity matrix**.
Then we solve for $\mathbf{X}(s)$ by multiplying both sides by the inverse of $(s\mathbf{I} - \mathbf{A})$:

$$
\mathbf{X}(s) = (s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B}\,\mathbf{U}(s)
$$

Finally, we define the transfer matrix $\mathbf{G}(s)$. The transfer matrix is defined as the ratio between the Laplace transform of the outputs and the Laplace transform of the inputs:

$$
\mathbf{G}(s) = \frac{\mathbf{X}(s)}{\mathbf{U}(s)}
= (s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B}.
$$

### 2. Transfer Matrix Analysis

Given the transfer function matrix obtained in the previous step:

$$
\mathbf{G}(s) =
\begin{bmatrix}
G_{L,q_{\text{in}}}(s) & G_{L,q_j}(s) & G_{L,T_{\text{in}}}(s) \\
G_{T,q_{\text{in}}}(s) & G_{T,q_j}(s) & G_{T,T_{\text{in}}}(s)
\end{bmatrix},
$$

each entry of the matrix is a single-input, single-output (SISO) transfer function that we can analyze individually.
For each SISO transfer function $G(s)$:

$$
G(s) = \frac{N(s)}{D(s)},
$$

the **characteristic polynomial** is the denominator $D(s)$.
We can compute the poles by solving the characteristic equation:

$$
D(s) = 0, \qquad \lambda_i = \beta_i + j\omega_i.
$$

The real part $\beta_i$ and imaginary part $\omega_i$ of each pole determine the stability of the system:

| Condition on the poles                     | Classification        |
| ------------------------------------------ | --------------------- |
| $\beta_i < 0,\; \forall i$                 | **Stable**            |
| $\beta_i = 0,\; \forall i$                 | **Marginally stable** |
| $\beta_i > 0,\; \exists i$                 | **Unstable**          |
| $\beta_i = 0,\; \omega_i = 0,\; \exists i$ | **Pure integrator**   |

## 📊 Results and Conclusions

By computing the poles of each transfer function using SymPy, we obtain real and negative values for all poles, and since they satisfy the stability condition ($\beta_i < 0,\; \forall i$), the linearized system is asymptotically stable according to the standard pole-based classification.

Because the heated tank model is nonlinear, the stability result obtained here is local and valid only in a neighborhood of the linearization point.
The system may exhibit different dynamics outside this operating region.

In addition, it is worth noting that all transfer functions have the **same characteristic polynomial**. This is expected, since the denominator of each transfer function depends only on the system matrix $\mathbf{A}$, meaning that stability is a property of the linearized system as a whole rather than of individual input–output channels.
