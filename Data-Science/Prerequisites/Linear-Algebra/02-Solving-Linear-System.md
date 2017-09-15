# Linear System

### Solving 2 unknowns with 2 equations

**Example**

Solve the following linear equations
$$2x - y = 0, -x + 2y = 3$$

The above equation can be represented as linear combination of columns

$$
x
\begin{bmatrix}
   2 \\
   -1
\end{bmatrix}
+ y
\begin{bmatrix}
   -1 \\
   2
\end{bmatrix}
 = 
\begin{bmatrix}
   0 \\
   3
\end{bmatrix}
$$

The matrix representation of above equations is 
$$
AX = b \\[.5em]
\begin{bmatrix}
   2 & -1 \\
   -1 & 2
\end{bmatrix}
\begin{bmatrix}
   x \\
   y
\end{bmatrix}
=
\begin{bmatrix}
   0 \\
   3
\end{bmatrix}
$$

The above equation solving is simple, Can we solve for $$AX = b$$ for every $$b$$ ?

Maybe, It depends on A we had chosen, Suppose if we consider three dimensional and all the equations are in the same plane then the linear combination of it also lies in the same plane. So in that case we may not be able to cover all $$b$$'s

### How to solve AX = b

#### Elimination and Back substution

Convert $$A$$ to upper triangular matrix $$U$$

Once we got upper triangular matrix from $$A$$ we can back substitute values and find $$X$$

i.e, the above equation is converted to $$AU = b'$$

#### Matrices

$$
AX = b\\[.5em]
X = A^{-1}b
$$