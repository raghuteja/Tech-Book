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

### Credits

1. [Population vs Sample variance and standard deviation](http://www.macroption.com/population-sample-variance-standard-deviation/)
