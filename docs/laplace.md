# Laplace Transform

The **Laplace transform** converts a time-domain function $f(t)$ into a complex frequency-domain function $F(s)$. It is defined as an integral transform:

$$
F(s) = \mathcal{L}\{f(t)\} = \int_0^\infty e^{-st} f(t) \, dt
$$

The **inverse Laplace transform** recovers the original time-domain function $f(t)$ from $F(s)$:

$$
f(t) = \mathcal{L}^{-1}\{F(s)\}.
$$

In practice, both the Laplace transform and its inverse are usually computed using standard properties and [tables of precomputed transforms](https://en.wikipedia.org/wiki/List_of_Laplace_transforms), or using software libraries that implement these operations.

The Laplace transform is commonly used for solving differential equations and analyzing linear systems, because it converts differentiation into algebraic operations in the $s$-domain, making equations easier to solve and systems easier to study.

## Laplace Properties

### Linearity

The Laplace transform is linear, meaning for constants $a$ and $b$:

$$
\mathcal{L}\{a f(t) + b g(t)\} = a \mathcal{L}\{f(t)\} + b \mathcal{L}\{g(t)\}
$$

### Differentiation in Time

Differentiation of $f(t)$ corresponds to:

$$
\mathcal{L}\left\{\frac{d f}{dt}\right\} = s F(s) - f(0)
$$

More generally, for the $n$-th derivative:

$$
\mathcal{L}\left\{\frac{d^n f}{dt^n}\right\} = s^n F(s) - s^{n-1} f(0) - s^{n-2}f'(0) - \dots - f^{(n-1)}(0)
$$

### Integration in Time

Integration of $f(t)$ corresponds to:

$$
\mathcal{L}\left\{\int_0^t f(\tau) \, d\tau\right\} = \frac{F(s)}{s}
$$

### Convolution

The Laplace transform converts **convolution** to multiplication in the $s$-domain:

$$
(f * g)(t) = \int_0^t f(\tau) g(t-\tau) \, d\tau
\quad \implies \quad
\mathcal{L}\{f * g\} = F(s) G(s)
$$
