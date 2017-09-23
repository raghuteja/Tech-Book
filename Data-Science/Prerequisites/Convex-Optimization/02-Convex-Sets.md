# Convex Sets

### Affine Set

Line through $$x_1, x_2$$; all points

$$x = \theta x_1 + (1-\theta)x_2, \space\space\space \theta \in \mathbb{R}$$

Contains the line through any two distinct points in the set

### Convex Set

Line segment between $$x_1$$ and $$x_2$$; all points

$$x = \theta x_1 + (1-\theta)x_2, \space\space\space 0 \le \theta \le 1$$

So all affine sets are convex but converse may not be true

### Convex combination and Convex hull

Convex combination of $$x_1, x_2, ... x_k$$: any point $$x$$ of the form

$$x = \theta_1x_1 + \theta_2x_2 + ... + \theta_kx_k$$

with $$\theta_1 + \theta_2 + ... + \theta_k = 1, \theta_i \ge 0$$

Convex hull $$S$$ :  Set of all convex combinations of points in $$S$$

### Convex Cone

Conic(non negative) combination of $$x_1$$ and $$x_2$$; any point of the form

$$x = \theta_1x_1 + \theta_2x_2, \space\space\space \theta_1 \ge 0, \theta_2 \ge 0$$

### Hyperplanes

Set of the form $$\{x \space | \space a^Tx = b\} (a \ne 0)$$

### Half spaces

Set of the form $$\{x \space | \space a^Tx = b\} (a \le 0)$$

### Euclidian Balls

Ball with center $$x_c$$ and radius $$r$$

$$B(x_c, r) = \{ x \space | \space \lVert x - x_c \rVert_2 \le r \}$$

### Ellipsoid 

Set of the form 

$$\{ x \space | \space (x - x_c)^TP^{-1}(x - x_c) \le 1 \}$$

with $$P \in S_{++}^n$$ i.e, symmetric positive definite 

### Norm balls and Norm cones

**Norm : ** A function $$\lVert \space \cdot \space \rVert$$ that satisfies

* $$\lVert x \rVert \ge 0; \lVert x \rVert = 0 \space \iff  \space x = 0$$
* $$\lVert tx \rVert = |t|\lVert x \rVert; t \in 	\mathbb{R}$$
* $$\lVert x + y \rVert \le \lVert x \rVert + \lVert y \rVert$$

Euclidian ball is the special case of norm ball with two norm

Norm ball with center $$x_c$$ and radius $$r$$ is defined as $$\{ x \space | \space \lVert x - x_c \rVert \le r \}$$

Norm cone is $$\{(x, t) \space | \space \lVert x \rVert \le t\}$$

Both norm balls and norm cones are convex

### Polyhedra

Solution set of finitely many equalities and inequalities 

$$Ax \preceq b, Cx = d$$
$$A \in \mathbb{R}^{m X n}, C \in \mathbb{R}^{p X n}, \preceq $$ is component wise inequality

Polyhedra is an intersection of finate number of halfspaces and hyperplanes

### Positive semidefinate cone

* $$S_n$$ is set of symmetric n X n matrices
* $$S_+^n = \{X \in S_n\ \space | \space X \succeq 0 \}$$

$$X \in S_n^+ \iff z^TXz \ge 0 \space \forall \space z$$

$$S_n^+$$ is a convex cone

* $$S_+^n = \{X \in S_n\ \space | \space X \succ 0 \}$$


### Intersection

Intersection of any number of convex sets is convex

### Affine function

Suppose $$f : \mathbb{R}^n \to \mathbb{R}^m$$ is affine $$(f(x) = Ax + b); A \in \mathbb{R}^{mXn}, B \in \mathbb{R}^m$$

Convex set under affine function $$f$$ is convex
$$S \subseteq \mathbb{R}^n$$ convex $$\iff f(S) = \{f(x) | x \in S \}$$ is convex

Convex set under inverse of affine function is also convex
$$S \subseteq \mathbb{R}^m$$ convex $$\iff f^{-1}(S) = \{f^{-1}(x) | x \in S \}$$ is convex

### Perspective and linear-fractional function

