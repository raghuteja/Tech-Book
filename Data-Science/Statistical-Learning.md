# Statistical Learning

Suppose that we observe a quantitative response $$Y$$ and p different predictors, $$X_1, X_2, . . . , X_p$$. We assume that there is some relationship between $$Y$$ and $$X = (X_1,X_2,...,X_p)$$, which can be written in the very general form

$$Y =f(X)+ε$$

Here f is some fixed but unknown function of $$X_1, . . . , X_p$$, and $$ε$$ is a random error term, which is independent of $$X$$ and has mean zero. 

### Why do we need to estimate $$f$$

#### Prediction

In many situations, a set of inputs $$X$$ are readily available, but the output $$Y$$ cannot be easily obtained. In this setting, since the error term averages to zero, we can predict $$Y$$ using

$$\hat{Y} = \hat{f}(X)$$

where $$\hat{f}$$ represents our estimate for $$f$$, and $$\hat{Y}$$ represents the resulting prediction for $$Y$$.

The accuracy of $$\hat{Y}$$ as a prediction for $$Y$$ depends on two quantities, which we will call the reducible error and the irreducible error. In general, $$\hat{f}$$ will not be a perfect estimate for $$f$$, and this inaccuracy will introduce some error. This error is reducible because we can potentially improve the accuracy of $$\hat{f}$$ by using the most appropriate statistical learning technique to estimate f.

Since $$Y$$ is a function of $$ε$$, Even if we estimate $$f$$ very well we cannot reduce this error (Irreducible error). 

**Why is there an irreducible error?**

This is because there can be unmeasurable variations and dependencies

$$ E(Y-\hat{Y})^2 = [f(X)-\hat{f}(X)]^2 + Var(ε)$$

#### Inference

One may be interested in the following questions

1. Which predictors are associated with the response?
2. What is the relationship between predictor and response?
3. Can the relationship be summarized as linear or is it more complicated?

### How to estimate $$f$$?

#### Parametric methods

We make some assumptions about $$f$$

$$f(X) = β_0 +β_1X_1 +β_2X_2 +...+β_pX_p$$

Then finding $$f$$ boils down to finding parameters $$β$$

The potential disadvantage of parametric method is if the actual $$f$$ is too far from our assumption, then our estimations will be poor. This can be reduced by using more flexible models which may cause **overfitting**

#### Non-parametric methods

It estimates $$f$$ by using near by data points. Since we are not fixing $$f$$, This is the advantage over parametric methods

Disadvantage in this method is it requires a large number of data points to get accurate estimate of $$f$$


### Supervised vs Unsupervised learning

Supervised learning is where you have input variables $$x$$ and an output variable $$Y$$ and you use an algorithm to learn the mapping function from the input to the output.

Ex: Regression, Classification

Unsupervised learning is where you only have input data $$X$$ and no corresponding output variables.

Ex: Clustering