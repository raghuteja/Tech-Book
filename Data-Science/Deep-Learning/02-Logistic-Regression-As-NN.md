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

#### Cost Function

Given $$\{ (x^{(1)}, y^{(1)}) ... (x^{(m)}, y^{(m)}) \}$$, we want $$\hat{y}^{(i)} = y^{(i)} $$

Loss function: $$L(\hat{y}, y) = \frac{1}{2}(\hat{y} - y)^2$$

But the above function is not generally used as the above optimization problem is not convex

So we define loss function as 
$$L(\hat{y}, y) = -(y \space log\hat{y} + (1-y)log(1-\hat{y}))$$

Loss function is for single training example

**Cost Function : **

$$J(w, b) = \frac{1}{m}(\displaystyle\sum_{i=1}^nL(\hat{y}^{(i)}, y^{(i)}))$$