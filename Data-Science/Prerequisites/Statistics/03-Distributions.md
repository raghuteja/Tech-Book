# Distributions

## Discrete Distributions

### Binomial distribution

Suppose we toss a coin n times. Let $$X \in {0, . . . , n}$$ be the number of heads. If the probability of heads is $$\theta$$, then we say $$X$$ has a binomial distribution

$$Bin(k|n,\theta) \triangleq \dbinom{n}{k} \theta^k(1−\theta)^{n−k}$$

**Mean :** $$\theta$$

**Variance :** $$n\theta(1 − \theta)$$

### Bernoulli distribution

$$Ber(x|\theta) = \begin{cases}
   \theta &\text{if } x = 1  \\
   1 - \theta &\text{if } x = 0
\end{cases}$$

Bernoulli distribution is a special case of binomial distribution with n = 1

### Multinomial and multinoulli distributions

These are similar to above instead of two sided coin assume multi sided die

### Poission distribution

$$X \in {0,1,2,...}$$ has poission distribution with $$\lambda > 0$$ written as $$X ~ Poi(\lambda)$$ iff

$$Poi(x|\lambda) = e^{-\lambda} \dfrac{\lambda^x}{x!}$$

## Continues Distributions

### Gaussian (normal) distribution

