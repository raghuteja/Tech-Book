# Multivariable Calculus

### Vectors

* Magnitude
* Direction

**Sample 3d vector notation** : 

$$\vec{A} = a_1\hat{i} + a_2\hat{j} + a_3\hat{k}$$
$$\vec{B} = b_1\hat{i} + b_2\hat{j} + b_3\hat{k}$$

Length of the vector : $$|\vec{A}| = \sqrt{a_1^2 + a_2^2 + a_3^2}$$

#### Addition

Sum of two vectors is the diagonal of the parallelogram formed with those two vectors 

$$\vec{A} + \vec{B} = (a_1 + b_1)\hat{i} + (a_2 + b_2)\hat{j} + (a_3 + b_3)\hat{k}$$

#### Dot Product

It is a scalar

$$\vec{A} \centerdot \vec{B} = \sum{a_ib_i}$$

Geometrically $$\vec{A} \centerdot \vec{B} = |\vec{A}||\vec{B}| cos(\theta)$$

#### Cross Product

It is a vector

$$\vec{A} X \vec{B} = det(\vec{A}, \vec{B})$$

$$\vec{A} X \vec{B}$$ signifies the area of the parallelogram formed with those two vectors

Magnitude = $$|\vec{A}||\vec{B}| sin(\theta)$$
Direction = perpendicular to both the vectors (Right hand thumb rule)

In case of three dimensions $$\vec{A} X \vec{B} X \vec{C}$$ signifies the volume of paralleopiped formed by A, B, C


Cross product of two vectors in 3d space
$$
\vec{A} X \vec{B} = 
\begin{vmatrix}
   \hat{i} & \hat{j} & \hat{k} \\
   a_1 & a_2 & a_3 \\
   b_1 & b_2 & b_3
\end{vmatrix}
$$

#### Planes

Given three points in a plane $$P_1, P_2, P_3$$. Let $$P$$ is a point in the plane then,

$$\vec{P_1P}\centerdot(\vec{P_1P_2}X\vec{P_1P_3}) = 0$$

$$\equiv det(\vec{P_1P}, \vec{P_1P_2}, \vec{P_1P_3}) = 0$$

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

$$ AX = B \equiv X = A^{-1}B$$

$$ A^{-1} = adj(A)/det(A)$$

In 3D system, in general two planes intersect a line and third plane intersects the line at a point

Other possible solutions are a line, a plane
