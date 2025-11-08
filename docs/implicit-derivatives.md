# Solving Systems with Implicit Derivatives

Some differential equation systems contain derivatives that cannot be easily expressed explicitly as functions of the state variables.
In other words, it can be difficult to isolate certain derivatives manually, which can be a challenge to simulate because most numerical solvers require the system to be written in explicit first-order form.

In such cases, it is often necessary to solve the system **numerically** using an algebraic equation solver at each time step.

There are various types of algebraic solvers available, depending on the programming language and the type of equations (linear, nonlinear, sparse, dense, etc.). For example, in Python, popular libraries provide solvers like `numpy.linalg.solve` for linear systems and `scipy.optimize.fsolve` for nonlinear systems.

An alternative approach is to use numerical solvers that **support implicit differential equations directly**. These solvers can handle systems where derivatives are not easily isolated, solving the algebraic constraints internally at each integration step.

## Linear Systems

If the algebraic equations for the derivatives are linear, it is often more convenient to rewrite the system in **matrix form**.
This allows numerical solvers to compute the derivatives efficiently and consistently.

For example:

$$
\begin{cases}
a_{11} \dot{y}_1 + a_{12} \dot{y}_2 = b_1 \\
a_{21} \dot{y}_1 + a_{22} \dot{y}_2 = b_2
\end{cases}
$$

Here:

- $\dot{y}_1$ and $\dot{y}_2$ are the derivatives we want to compute.
- $a_{ij}$ are constants (or functions of the state variables).
- $b_1$, $b_2$ are known terms (inputs or functions of the state).

To write the system in **matrix form**, we need to express all derivatives and coefficients as vectors and matrices.
The default format for a linear algebraic system is:

$$
\mathbf{A} \cdot \mathbf{\dot{y}} = \mathbf{b},
$$

In our example, this becomes:

$$
\mathbf{A} = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix}, \quad
\mathbf{\dot{y}} = \begin{bmatrix} \dot{y}_1 \\ \dot{y}_2 \end{bmatrix}, \quad
\mathbf{b} = \begin{bmatrix} b_1 \\ b_2 \end{bmatrix}
$$
