# Reducing Higher-Order ODEs

When solving higher-order ordinary differential equations (ODEs) numerically, most solvers (such as `solve_ivp` in Python) can only handle **first-order systems**.
Therefore, a standard technique is to perform a **variable substitution** (also known as the **reduction of order**) to rewrite the equation.

For example, consider:

$$
y''(t) + y(t) = 0
$$

This equation involves the **second derivative** of $y(t)$. To transform this into a system of first-order equations, we first define a new variable:

$$
x(t) = y'(t)
$$

Now, the derivative of $x(t)$ is exactly the second derivative of $y(t)$:

$$
\dot{x}(t) = y''(t)
$$

Substituting $x(t)$ into the original equation, we get:

$$
\dot{x}(t) + y(t) = 0 \quad \Rightarrow \quad \dot{x}(t) = -y(t)
$$

Thus, the second-order equation is transformed into a **system of two first-order equations**:

$$
\begin{cases}
  \dot{y}(t) = x(t)\\
  \dot{x}(t) = -y(t)
\end{cases}
$$
