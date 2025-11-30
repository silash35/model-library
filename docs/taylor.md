# Taylor Series

The **Taylor series** allows a smooth function to be approximated as a sum of terms based on its derivatives at a point $x_0$.

The approximation is centered around $x_0$, meaning it is most accurate for values of $x$ near $x_0$.

The accuracy of the approximation depends on the function itself: some functions are well-approximated with only a few terms, while others may require higher-order terms to achieve a good approximation.

## Scalar Case

For a scalar function $f(x)$ of a scalar variable $x$:

$$f(x) = f(x_0) + f'(x_0)(x-x_0) + \frac{1}{2!}f''(x_0)(x-x_0)^2 + \dots$$

$f^{(n)}(x_0)$ is the n-th derivative at $x_0$.

## Vector Input

For a scalar function $f(\mathbf{x})$ of a vector $\mathbf{x} \in \mathbb{R}^n$:

$$
f(\mathbf{x}) =
f(\mathbf{x}_0) + \nabla f(\mathbf{x}_0)^\top (\mathbf{x}-\mathbf{x}_0) + \dots
$$

$\nabla f(\mathbf{x}_0) \in \mathbb{R}^n$ is the **gradient vector** at $\mathbf{x}_0$:

$$
\nabla f(\mathbf{x}_0) =
\left. \frac{\partial f}{\partial \mathbf{x}} \right|_{\mathbf{x}_0}^\top =
\begin{bmatrix}
  \frac{\partial f}{\partial x_1}(\mathbf{x}_0) & \frac{\partial f}{\partial x_2}(\mathbf{x}_0) & \cdots & \frac{\partial f}{\partial x_n}(\mathbf{x}_0)
\end{bmatrix}^\top
$$

## Vector Output

For a vector function $\mathbf{f}(\mathbf{x}) \in \mathbb{R}^m$ of a vector $\mathbf{x} \in \mathbb{R}^n$:

$$
\mathbf{f}(\mathbf{x}) =
\mathbf{f}(\mathbf{x}_0) + J_\mathbf{f}(\mathbf{x}_0) (\mathbf{x}-\mathbf{x}_0) + \dots
$$

$J_\mathbf{f}(\mathbf{x}_0)$ is the **Jacobian matrix** at $\mathbf{x}_0$:

$$
J_\mathbf{f}(\mathbf{x}_0) =
\frac{d \mathbf{f}}{d \mathbf{x}} =
\begin{bmatrix}
  \frac{\partial f_1}{\partial x_1}(\mathbf{x}_0) & \cdots & \frac{\partial f_1}{\partial x_n}(\mathbf{x}_0) \\
  \vdots & \ddots & \vdots \\
  \frac{\partial f_m}{\partial x_1}(\mathbf{x}_0) & \cdots & \frac{\partial f_m}{\partial x_n}(\mathbf{x}_0)
\end{bmatrix}
$$
