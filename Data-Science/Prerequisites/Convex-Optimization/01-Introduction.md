# Introduction

### Mathematical Optimization

##### Optimization Problem

$$minimize \space f_0(x)$$
$$subject \space to \space f_i(x) \le b_i, i = 1,...,m$$

* $$x = (x_1, x_2 ... x_n)$$ : Optimization variables

* $$f_0 : R^n \to R$$ : Objective function

* $$f_i : R^n \to R, i = 1,...,m$$ : Constraint functions

##### Optimal Solution

$$x^*$$ is the smallest value of $$f_0$$ among all vectors that satisfy the constraints


### Solving optimization problems

##### General optimization problem

* Very difficult to solve

* Not always finding the solution

##### Exception

* Least-Squares problems

* Linear programming problems

* Convex optimization problems

#### Least Squares

$$minimize \space \lVert Ax - b \rVert_2^2$$

* Analytical Solution : $$x^* = (A^TA)^{-1}A^Tb$$

#### Linear Programming

$$minimize \space c^Tx$$
$$subject \space to \space a_i^Tx \le b_i, i = 1,...,m$$

#### Convex Optimizatiom

Objective and Constraint functions should be convex