### Linear Regression

#### Simple linear regression

$$Y \approx \beta_0 + \beta_1X$$

sometimes called as regressing $$Y$$ onto $$X$$

##### Estimating the coefficients

Let $$y_i = \hat{\beta_0} + \hat{\beta_1}x_i$$ be the prediction for Y based on the ith value of X. Then $$e_i = y_i − \hat{y_i}$$ represents the ith residual, This is the difference between the ith observed response value and the ith response value that is predicted by our linear model. We define the residual sum of squares (RSS) as

$$RSS = e_1^2 + e_2^2 + ... + e_n^2$$

If we minimize RSS by using calculus we get

$$
\hat{\beta_1} = \dfrac{\textstyle\sum_{i=1}^n(x_i - \bar{x})(y_i - \bar{y})}{\textstyle\sum_{i=1}^n(x_i - \bar{x})^2}
$$

$$
\hat{\beta_0} = \bar{y} - \hat{\beta_1}\bar{x}
$$

where $$\bar{y} \equiv 	\frac{1}{n} \textstyle\sum_{i=1}^ny_i$$ and $$\bar{x} \equiv 	\frac{1}{n} \textstyle\sum_{i=1}^nx_i$$

##### Accessing accuracy of coefficient estimates

