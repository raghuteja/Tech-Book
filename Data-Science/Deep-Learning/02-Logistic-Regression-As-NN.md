# Logistic Regression As Neural Network

### Binary Classification

**Notations :**

$$(x, y): \space -> x \space\epsilon\space \Bbb{R}^{n_x}, y \space\epsilon\space \{ 0, 1 \}$$
$$m$$: Number of training examples
$$X: X \space\epsilon\space \Bbb{R}^{n_x \mathbf{x} \space m}$$
$$Y: Y \space\epsilon\space \Bbb{R}^{1 \space \mathbf{x} \space m}$$

### Logistic Regression

Given $$x$$ we want $$\hat{y} = P(y = 1|x)$$

Parameters $$w \space\epsilon\space \Bbb{R}^{n_x}, \space b \space\epsilon\space \Bbb{R}$$

Output $$\hat{y} = \sigma(w^Tx + b)$$ where $$\sigma$$ represents sigmoid function

$$\sigma(z) = \dfrac{1}{1 + e^{-z}}$$