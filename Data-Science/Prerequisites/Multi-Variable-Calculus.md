# Multivariable Calculus

### Vectors

* Magnitude
* Direction

**Sample 3d vector notation** : 

$$\overrightarrow{A} = a_1\hat{i} + a_2\hat{j} + a_3\hat{k}$$
$$\overrightarrow{B} = b_1\hat{i} + b_2\hat{j} + b_3\hat{k}$$

Length of the vector : $$|\overrightarrow{A}| = \sqrt{a_1^2 + a_2^2 + a_3^2}$$

#### Addition

Sum of two vectors is the diagonal of the parallelogram formed with those two vectors 

$$\overrightarrow{A} + \overrightarrow{B} = (a_1 + b_1)\hat{i} + (a_2 + b_2)\hat{j} + (a_3 + b_3)\hat{k}$$

#### Dot Product

It is a scalar

$$\overrightarrow{A} \centerdot \overrightarrow{B} = \sum{a_ib_i}$$

Geometrically $$\overrightarrow{A} \centerdot \overrightarrow{B} = |\overrightarrow{A}||\overrightarrow{B}| cos(\theta)$$

#### Cross Product

It is a vector

$$\overrightarrow{A} X \overrightarrow{B} = det(\overrightarrow{A}, \overrightarrow{B})$$

$$\overrightarrow{A} X \overrightarrow{B}$$ signifies the area of the parallelogram formed with those two vectors

Magnitude = $$|\overrightarrow{A}||\overrightarrow{B}| sin(\theta)$$
Direction = perpendicular to both the vectors (Right hand thumb rule)

In case of three dimensions $$\overrightarrow{A} X \overrightarrow{B} X \overrightarrow{C}$$ signifies the volume of paralleopiped formed by A, B, C


Cross product of two vectors in 3d space
$$
\overrightarrow{A} X \overrightarrow{B} = 
\begin{vmatrix}
   \hat{i} & \hat{j} & \hat{k} \\
   a_1 & a_2 & a_3 \\
   b_1 & b_2 & b_3
\end{vmatrix}
$$

#### Planes

Given three points in a plane $$P_1, P_2, P_3$$. Let $$P$$ is a point in the plane then,

$$\overrightarrow{P_1P}\centerdot(\overrightarrow{P_1P_2}X\overrightarrow{P_1P_3}) = 0$$

$$\implies det(\overrightarrow{P_1P}, \overrightarrow{P_1P_2}, \overrightarrow{P_1P_3}) = 0$$

#### Equations of planes

$$ ax + by + cz = d $$

Normal vector to the plane : $$\langle \hat{a}, \hat{b}, \hat{c} \rangle$$

#### Parametric equations of line

$$
x(t) = a_1t+b_1,
y(t) = a_2t+b_2,
z(t) = a_3t+b_3
$$

#### Matrices

$$ AX = B \implies X = A^{-1}B$$

$$ A^{-1} = adj(A)/det(A)$$

In 3D system, in general two planes intersect a line and third plane intersects the line at a point

Other possible solutions are a line, a plane