# Probability and Statistics

### Types of data

1. Numerical
    1. Discrete
    2. Continues
2. Categorical
3. Ordinal (Ex: Movie ratings)

### Measures of central tendency

1. Mean
2. Median
3. Mode


* **Variance : ** Signifies how spread out the data is, Mathematically variance($$\sigma^2$$) is sum of squared differences from the mean

* **Standard Deviation : ** Its just square root of variance($$\sigma$$), Usually used to identify outliers

### Population vs Sample

Population is whole group where as sample is part of a population that is used to describe the characteristics like mean, standard deviation etc...


#### Population variance and Sample variance

* **Population variance**

$$
\sigma^2 = \dfrac{\displaystyle\sum_{i=1}^n	(X_i - \mu)^2}{N} 
$$

* **Sample variance**

$$
s^2 = \dfrac{\displaystyle\sum_{i=1}^n	(X_i - \overline{X})^2}{n-1}
$$

**Why there is n-1 in denominator of sample variance as an estimate of population variance?**

This correction is called Bessel's correction.

* **Theoretical Explanation** :  The standard deviation calculated with a divisor of $$n-1$$ is a standard deviation calculated from the sample as an estimate of the standard deviation of the population from which the sample was drawn. Because the observed values fall, on average, closer to the sample mean than to the population mean, the standard deviation which is calculated using deviations from the sample mean underestimates the desired standard deviation of the population. Using $$n-1$$ instead of $$n$$ as the divisor corrects for that by making the result a little bit bigger.

* **Degrees of Freedom** : It is the number of values in the calculation that are free to vary.

In the above case of $$n$$ values the degrees of freedom is $$n-1$$, For estimating population variance from sample variance we typically divide by degrees of freedom as opposed by sample size.

* **Mathematical Proof** : Check [here](https://en.wikipedia.org/wiki/Bessel%27s_correction)

### Other measures

* **Z-Score : ** How many standard deviations away from the mean is a data point 

$$
Z = \dfrac{data point - mean value}{standard deviation} = \dfrac{x - \mu}{\sigma}
$$

* **Coefficient of variation : ** Relative measure of variability (Standard deviation relative to the mean)

$$
Coefficient-of-variation = \bigg(\dfrac{\sigma}{\mu}*100\bigg)\%
$$

### Probability

#### Density function
For continues data

**Examples**

* Uniform Distribution
* Normal/Gaussian Distribution
* Exponential Distribution

#### Mass function
For discrete data

**Examples**

* Binomial probability mass function
* Poisson probability mass function

### Percentiles and Moments

#### Percentiles

In a dataset the point at which x% of the data is less than that value

#### Moments

Moments in mathematical statistics involve a basic calculation.  These calculations can be used to find a probability distribution's mean, variance and skewness.

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

### Conditional Probability

$$P(B|A) = \dfrac{P(A,B)}{P(B)}$$

### Bayes Theorem

$$P(B|A) = \dfrac{P(A)P(A|B)}{P(B)}$$

### Credits

1. [Population vs Sample variance and standard deviation](http://www.macroption.com/population-sample-variance-standard-deviation/)
