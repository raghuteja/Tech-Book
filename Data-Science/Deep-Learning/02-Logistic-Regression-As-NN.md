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

#### Gradient Descent

$$w := w - \alpha \dfrac{\partial J(w, b)}{\partial w}$$
$$b:= b - \alpha \dfrac{\partial J(w, b)}{\partial b}$$

Here $$\alpha$$ denotes learning rate


Given $$x, y$$

$$z = (\Sigma w_ix_i) + b$$
$$a = \sigma(z)$$
$$L(a, y) = -(y \space log(a) + (1-y)log(1-a))$$

Derivatives:

$$\dfrac{\partial L}{\partial a} = \partial a = \dfrac{1-y}{1-a} - \dfrac{y}{a}$$

$$\dfrac{\partial L}{\partial z} = \partial z = a - y$$

$$\dfrac{\partial L}{\partial w_i} = \partial w_i = x_i \partial z$$

$$\partial b = \partial z$$

So final values for $$w_i := w_i - \alpha \partial w_i$$

The above is for one training example, We need to do the same process for m training examples

