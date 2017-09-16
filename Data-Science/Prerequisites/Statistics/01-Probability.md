# Probability

### Basic Rules

* **Union : **
$$p(A \lor B) = p(A)+p(B)-p(A \land B)$$

* **Joint : **
$$p(A, B) = p(A \land B) = p(A|B)p(B)$$
$$p(A) = \displaystyle\sum_b p(A, B) = \displaystyle\sum_bp(A|B = b)p(B = b)$$

* **Conditional : **
$$p(A|B) = \dfrac{p(A, B)}{p(B)} \space \space if \space p(B) > 0$$

* **Bayes-Rule : **
$$p(X =x|Y =y) = \dfrac{p(X =x,Y =y)}{p(Y =y)} = \dfrac{p(X =x)p(Y =y|X =x)}{\sum_{x'}p(X ={x'})p(Y =y|X =x')}$$

* **Un-conditional Independent : **
$$p(X,Y)=p(X)p(Y)$$

* **Conditional Independent : **
$$p(X, Y |Z) = p(X|Z)p(Y |Z)$$


### Density function
For continues data

**Examples**

* Uniform Distribution
* Normal/Gaussian Distribution
* Exponential Distribution

### Mass function
For discrete data

**Examples**

* Binomial probability mass function
* Poisson probability mass function

### Percentiles and Moments

#### Percentiles

In a dataset the point at which x% of the data is less than that value

#### Moments

Moments in mathematical statistics involve a basic calculation. These calculations can be used to find a probability distribution's mean, variance and skewness.

In a discrete random variable,
The $$s$$th moment of the data set with values $$x_1, x_2, x_3,...x_n$$ is given by the formula:

$$(x_1^s + x_2^s + x_3^s + ... + x_n^s)/n$$

First Moment is Simple Mean

**Moments about the mean**

$$((x_1-\mu)^s + (x_2-\mu)^s + (x_3-\mu)^s + ... + (x_n-\mu)^s)/n$$

1. First moment about mean is zero
2. Second moment about mean is variance
3. Third moment about mean is skew
4. Fourth moment about mean is kurtosis

The above applies same for continues random variable

### Covariance and Corelation

Describe the degree to which two random variables or sets of random variables tend to deviate from their expected values in similar ways

#### Covariance

$$Cov(X, Y) = \sigma_{XY} = E[X - E[X]]E[Y - E[Y]]$$
$$Cov(X, Y) = E[XY] - E[X]E[Y]$$

#### Corelation

$$Cor(X, Y) = \dfrac{Cov(X, Y)}{\sigma_X\sigma_Y}$$
