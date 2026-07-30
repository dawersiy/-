# A METHOD OF SOLVING A CONVEX PROGRAMMING PROBLEM WITH CONVERGENCE RATE $O(1/k^{2})$

UDC 51

YU. E. NESTEROV

1. In this note we propose a method of solving a convex programming problem in a Hilbert space E. Unlike the majority of convex programming methods proposed earlier, this method constructs a minimizing sequence of points $\{x_{k}\}_{0}^{\infty}$ that is not relaxational. This property allows us to reduce the amount of computation at each step to a minimum. At the same time, it is possible to obtain an estimate of convergence rate that cannot be improved for the class of problems under consideration (see [1]).  
2. Consider first the problem of unconstrained minimization of a convex function $f(x)$. We will assume that $f(x)$ belongs to the class $C^{1,1}(E)$, i.e. that there exists a constant $L > 0$ such that for all $x, y \in E$

$$
\| f' (x) - f' (y) \| \leqslant L \| x - y \|. \tag {1}
$$

From (1) it follows that for all $x, y \in E$

$$
f (y) \leqslant f (x) + \left\langle f ^ {\prime} (x), y - x \right\rangle + 0.5 L \| y - x \| ^ {2}. \tag {2}
$$

To solve the problem $\min\{f(x) | x \in E\}$ with a nonempty set $X^{*}$ of minima we propose the following method.

0) Select a point $y_{0} \in E$. Put

$$
k = 0, \quad a _ {0} = 1, \quad x _ {- 1} = y _ {0}, \quad \alpha_ {- 1} = \| y _ {0} - z \| / \| f' (y _ {0}) - f' (z) \|, \tag {3}
$$

where z is an arbitrary point in $E, z \neq y_{0}$ and $f'(z) \neq f'(y_{0})$.

1) kth iteration. a) Calculate the smallest index $i \geqslant 0$ for which

$$
f (y _ {k}) - f \big (y _ {k} - 2 ^ {- i} \alpha_ {k - 1} f' (y _ {k}) \big) \geqslant 2 ^ {- i - 1} \alpha_ {k - 1} \| f' (y _ {k}) \| ^ {2}. \tag {4}
$$

b) Put

$$
\begin{array}{l} \alpha_ {k} = 2 ^ {- i} \alpha_ {k - 1}, \quad x _ {k} = y _ {k} - \alpha_ {k} f ^ {\prime} (y _ {k}), \\ a _ {k + 1} = \left(1 + \sqrt {4 a _ {k} ^ {2} + 1}\right) / 2, \tag {5} \\ y _ {k + 1} = x _ {k} + (a _ {k} - 1) (x _ {k} - x _ {k - 1}) / a _ {k + 1}. \\ \end{array}
$$

The way in which the one-dimensional search (4) is halted is similar to that proposed in [2]. The difference is only that in (4) the subdivision in the $k$ th iteration is done starting with $\alpha_{k-1}$ (and not with 1 as in [2]). In view of this (see the proof of Theorem 1), when the sequence $\{x_k\}_0^\infty$ is constructed by method (3)-(5), no more than $O(\log_2 L)$ such subdivisions will be made. The recalculation of the points $y_k$ in (5) is done using a "ravine" step.

Let us also remark that method (3)-(5) does not guarantee a monotone decrease of $f(x)$ on the sequences $\{x_k\}_0^\infty$ and $\{y_k\}_0^\infty$.

THEOREM 1. Let $f(x)$ be a convex function in $C^{1,1}(E)$, and suppose $X^{*} \neq \emptyset$. If the sequence $\{x_k\}_0^\infty$ is constructed by method (3)-(5), then the following assertions are true:

1) For any $k \geqslant 0$ ;

$$
f (x _ {k}) - f ^ {*} \leqslant C / (k + 2) ^ {2}, \tag {6}
$$

where $C = 4L\| y_0 - x^*\|^2$ and $f^{*} = f(x^{*}),x^{*}\in X^{*}$

2) In order to achieve accuracy $\varepsilon$ with respect to the functional, one needs  
a) to compute the gradient of the objective function no more than $NG = \sqrt{C/\varepsilon}$ [times, and b) to evaluate the objective function no more than $NF = 2NG + \log_{2}(2L\alpha_{-1})[ + 1 \text{ times.}$

Here and in what follows, ](·)[ is the integer part of the number (·).

PROOF. Let $y_{k}(\alpha) = y_{k} - \alpha f'(y_{k})$. From (2) we obtain

$$
f (y _ {k}) - f (y _ {k} (\alpha)) \geqslant 0.5 \alpha (2 - \alpha L) \| f ^ {\prime} (y _ {k}) \| ^ {2}.
$$

Consequently, as soon as $2^{-i}\alpha_{k-1}$ becomes less than $L^{-1}$, inequality (4) will be satisfied and $\alpha_{k}$ will not be further decreased. Thus $\alpha_{k} \geqslant 0.5L^{-1}$ for all $k \geqslant 0$.

Let $p_k = (a_k - 1)(x_{k-1} - x_k)$. Then $p_{k+1} - x_{k+1} = p_k - x_k + a_{k+1}\alpha_{k+1}f'(y_{k+1})$. Consequently,

$$
\begin{array}{l} \| p _ {k + 1} - x _ {k + 1} + x ^ {*} \| ^ {2} = \| p _ {k} - x _ {k} + x ^ {*} \| ^ {2} + 2 (a _ {k + 1} - 1) \alpha_ {k + 1} \left\langle f' (y _ {k + 1}), p _ {k} \right\rangle \\ + 2 a _ {k + 1} \alpha_ {k + 1} \left\langle f' (y _ {k + 1}), x ^ {*} - y _ {k + 1} \right\rangle + a _ {k + 1} ^ {2} \alpha_ {k + 1} ^ {2} \| f' (y _ {k + 1}) \| ^ {2}. \\ \end{array}
$$

Using inequality (4) and the convexity of $f(x)$, we obtain

$$
\begin{array}{l} \left\langle f' (y _ {k + 1}), y _ {k + 1} - x ^ {*} \right\rangle \geqslant f (x _ {k + 1}) - f ^ {*} + 0. 5 \alpha_ {k + 1} \| f' (y _ {k + 1}) \| ^ {2}, \\ 0. 5 \alpha_ {k + 1} \| f' (y _ {k + 1}) \| ^ {2} \leqslant f (y _ {k + 1}) - f (x _ {k + 1}) \leqslant f (x _ {k}) - f (x _ {k + 1}) \\ - a _ {k + 1} ^ {- 1} \left\langle f' (y _ {k + 1}), p _ {k} \right\rangle . \\ \end{array}
$$

We substitute these two inequalities into the preceding equality:

$$
\begin{array}{l} \left\| p _ {k + 1} - x _ {k + 1} + x ^ {*} \right\| ^ {2} - \left\| p _ {k} - x _ {k} + x ^ {*} \right\| ^ {2} \leqslant 2 (a _ {k + 1} - 1) \alpha_ {k + 1} \left\langle f ^ {\prime} (y _ {k + 1}), p _ {k} \right\rangle \\ - 2 a _ {k + 1} \alpha_ {k + 1} \left(f \left(x _ {k + 1}\right) - f ^ {*}\right) + \left(a _ {k + 1} ^ {2} - a _ {k + 1}\right) \alpha_ {k + 1} ^ {2} \| f ^ {\prime} \left(y _ {k + 1}\right) \| ^ {2} \right. \\ \leqslant - 2 a _ {k + 1} \alpha_ {k + 1} \left(f \left(x _ {k + 1}\right) - f ^ {*}\right) + 2 \left(a _ {k + 1} ^ {2} - a _ {k + 1}\right) \alpha_ {k + 1} \left(f \left(x _ {k}\right) - f \left(x _ {k + 1}\right)\right) \\ = 2 \alpha_ {k + 1} a _ {k} ^ {2} (f (x _ {k}) - f ^ {*}) - 2 \alpha_ {k + 1} a _ {k + 1} ^ {2} (f (x _ {k + 1}) - f ^ {*}) \\ \leqslant 2 \alpha_ {k} a _ {k} ^ {2} \left(f \left(x _ {k}\right) - f ^ {*}\right) - 2 \alpha_ {k + 1} a _ {k + 1} ^ {2} \left(f \left(x _ {k + 1}\right) - f ^ {*}\right). \\ \end{array}
$$

Thus

$$
\begin{array}{l} 2 \alpha_ {k + 1} a _ {k + 1} ^ {2} (f (x _ {k + 1}) - f ^ {*}) \leqslant 2 \alpha_ {k + 1} a _ {k + 1} ^ {2} (f (x _ {k + 1}) - f ^ {*}) + \| p _ {k + 1} - x _ {k + 1} + x ^ {*} \| ^ {2} \\ \leqslant 2 \alpha_ {k} a _ {k} ^ {2} \left(f (x _ {k}) - f ^ {*}\right) + \left\| p _ {k} - x _ {k} + x ^ {*} \right\| ^ {2} \\ \leqslant 2 \alpha_ {0} a _ {0} ^ {2} (f (x _ {0}) - f ^ {*}) + \| p _ {0} - x _ {0} + x ^ {*} \| ^ {2} \leqslant \| y _ {0} - x ^ {*} \| ^ {2}. \\ \end{array}
$$

It remains to observe that $a_{k+1} \geqslant a_{k} + 0.5 \geqslant 1 + 0.5(k + 1)$.

It follows from the estimate of the convergence rate (6) that the number of iterations method (3)-(5) needs to achieve accuracy $\varepsilon$ will be no greater than $\sqrt{C / \varepsilon}[-1$. During each iteration, one gradient and at least two values of the objective function will have to

be calculated. Let us remark, however, that to each additional evaluation of the objective function corresponds a halving of $\alpha_{k}$. Therefore the total number of such evaluations will not exceed $\lceil \log_2(2L\alpha_{-1})[+1.$ This completes the proof of the theorem.

If the Lipschitz constant $L$ is known for the gradient of the objective function, then one can take $\alpha_k \equiv L^{-1}$ in the method (3)-(5) for any $k \geqslant 0$. In this case inequality (4) is certain to hold, and therefore Theorem 1 remains valid for $C = 2L \| y_0 - x^* \|^2$, $Ng = \| y_0 - x^* \| \sqrt{2L / \varepsilon} [-1]$ and $NF = 0$.

To conclude this section we will show how one may modify the method (3)-(5) to solve the problem of minimizing a strictly convex function.

Assume that $f(x)-f^{*}\geqslant0.5m\|x-x^{*}\|^{2}$ for all $x\in E$, where m>0, and suppose the constant m is known.

We introduce the following halting rule in the method (3)-(5):

c) We stop when

(7) $k \geqslant 2\sqrt{2 / (m\alpha_k)} - 2.$

Suppose that the halting has occurred in the Nth step. Since $\alpha_{k} \geqslant 0.5L^{-1}$ in the method (3)-(5), one has $N \leqslant 4\sqrt{L/m}[-1]$. At the same time,

$$
f (x _ {N}) - f ^ {*} \leqslant \frac {2 \| y _ {0} - x ^ {*} \| ^ {2}}{\alpha_ {N} (N + 2) ^ {2}} \leqslant 0.25 m \| y _ {0} - x ^ {*} \| ^ {2} \leqslant 0.5 (f (y _ {0}) - f ^ {*}).
$$

After the point $x_{N}$ has been obtained, it is necessary to restart the method and again begin calculating, by the method (3)–(5), (7), from the point $x_{N}$ as the initial point, etc.

As a result we obtain that after each $4\sqrt{L/m}[-1$ iterations the residual with respect to the function decreases by a factor of 2. Thus the method (3)–(5) with renewal (7) cannot be improved (up to a dimensionless constant) among methods of first order on the class of strictly convex functions in $C^{1,1}(E)$ (see [1]).

3. Consider the following extremal problem:

(8) $\min \left\{F(\bar{f}(x)) \mid x \in Q\right\}$,

where $Q$ is a convex closed set in $E$, $F(u)$, with $u \in R^{m}$, is a function convex on all of $R^{m}$, positive homogeneous of degree one, and $\bar{f}(x) = (f_{1}(x), \ldots, f_{m}(x))$ is a vector of convex continuously differentiable functions on $E$. The set $X^{*}$ of solutions of (8) is always assumed to be nonempty. In addition to this, we will always assume that the system of functions $\{F(\cdot), \bar{f}(\cdot)\}$ has the following property:

(\*) If there exists a vector $\lambda \in \partial F(0)$ such that $\lambda^{(k)} < 0$, then $f_{k}(x)$ is a linear function.

The notation $\partial F(0)$ means the subdifferential of the function $F(u)$ at 0.

As is well known, the identity $F(u) \equiv \max\{\langle \lambda, u \rangle | \lambda \in \partial F(0)\}$ holds for convex functions that are positive homogeneous of degree one. Therefore the assumption (\*) implies the convexity of the function $F(\bar{f}(x))$ on all of $E$.

Problem (8) can be written in minimax form:

(9) $\min \left\{\max \left\{\langle \lambda ,\bar{f} (x)\rangle |\lambda \in \partial F(0)\right\} |x\in Q\right\} .$

One can show that the fact that the set $X^{*}$ is nonempty and the assumption (\*) imply the existence of a saddle point ( $\lambda^{*}, x^{*}$ ) for problem (9). Therefore the set of saddle points of problem (9) can be written as $\Omega^{*} = \Lambda^{*} \times X^{*}$, where

$$
\Lambda^ {*} = \operatorname{Arg} \max \{\Psi (\lambda) | \lambda \in \partial F (0) \}, \quad \Psi (\lambda) = \min \{\langle \lambda , f (x) \rangle | x \in Q \}.
$$

The problem

$$
\max \{\Psi (\lambda) | \lambda \in \partial F (0) \cap \operatorname{dom} \Psi (\cdot) \}
$$

will be called the problem dual to (8).

Suppose the functions $f_{k}(x), k = 1, \ldots, m$, in problem (8) belong to the class $C^{[1,1]}(E)$ with constants $L^{(k)} \geqslant 0$. Let $\bar{L} = (L^{(1)}, \ldots, L^{(m)})$.

Consider the function

$$
\Phi (y, A, z) = F (\bar {f} (y, z)) + 0. 5 A \| y - z \| ^ {2},
$$

where

$$
\bar{f}(y,z) = (f^{(1)}(y,z), \dots, f^{(m)}(y,z)),
$$

$$
f^{(k)}(y,z) = f_k(y) + \langle f'_k(y), z - y \rangle , \quad k = 1, 2, \dots , m,
$$

and $A$ is a positive constant. Let

$$
\Phi^ {*} (y, A) = \min \{\Phi (y, A, z) | z \in Q \}, \quad T (y, A) = \arg \min \{\Phi (y, A, z) | z \in Q \}.
$$

Observe that the mapping $y \rightarrow T(y, a)$ is a natural generalization, for problem (8), of the “gradient” mapping introduced in [1] in connection with the investigation of methods of minimizing functions of the form $\max_{1 \leqslant k \leqslant m} f_k(x)$. For the mapping $y \rightarrow T(y, A)$ (as well as for the “gradient” mapping of [1]) we have

$$
\Phi^ {*} (y, A) + A \big \langle y - T (y, A), x - y \big \rangle + 0. 5 A \| y - T (y, A) \| ^ {2} \leqslant F (\bar {f} (x)), \tag {10}
$$

for all $x \in Q, y \in E$ and $A \geqslant 0$, and if $A \geqslant F(L)$, then

$$
\Phi^*(y, A) \geqslant F(\bar{f}(T(y, A))).
$$

To solve problem (8) we propose the following method.

0) Select a point $y_{0} \in E$. Put

$$
k = 0, a _ {0} = 1, x _ {- 1} = y _ {0}, A _ {- 1} = F (\bar {L} _ {0}), \tag {11}
$$

where $\bar{L}_{0}=(L_{0}^{(1)},\ldots,L_{0}^{(m)}),L_{0}^{(k)}=\|f_{k}'(y_{0})-f_{k}'(z)\|/\|y_{0}-z\|$ and z is an arbitrary point in $E,z\neq y_{0}$ .

1) kth iteration. a) Calculate the smallest index $i \geqslant 0$ for which

$$
\Phi^ {*} \big (y _ {k}, 2 ^ {i} A _ {k - 1} \big) \geqslant F \big (\bar {f} \big (T \big (y _ {k}, 2 ^ {i} A _ {k - 1} \big) \big) \big). \tag {12}
$$

b) Put $A_{k} = 2^{i}A_{k-1}, x_{k} = T(y_{k}, A_{k})$ and

$$
\begin{aligned} a _ {k + 1} &= \left(1 + \sqrt {4 a _ {k} ^ {2} + 1}\right) / 2, \tag {13} \\ y _ {k + 1} &= x _ {k} + (a _ {k} - 1) (x _ {k} - x _ {k - 1}) / a _ {k + 1}. \\ \end{aligned}
$$

It is not hard to see that the method (3)-(5) is simply another form of writing the method (11)-(13) for the unconstrained minimization problem (i.e., when $m=1$, $F(y)=y$ and $Q=E$ in (8)).

THEOREM 2. If the sequence $\{x_k\}_{0}^{\infty}$ is constructed by method (11)-(13), then the following assertions are true:

1) For any $k \geqslant 0$

$$
F \big (\bar {f} (x _ {k}) \big) - F \big (\bar {f} (x ^ {*}) \big) \leqslant C _ {1} / (k + 2) ^ {2},
$$

where $C_1 = 4F(\bar{L})\| y_0 - x^*\| ^2, x^* \in X^*$.

2) To obtain accuracy ε with respect to the functional, one needs

a) to solve an auxiliary problem $\min\{\Phi(y_{k}, A, x) | x \in Q\}$ no more than

$$
\lceil \sqrt{C_1/\varepsilon} \rceil + \max\{\log_2(F(\bar{L})/A_{-1}), 0\}
$$

times,

b) to evaluate the collection of gradients $f_1(y), \ldots, f_m'(y)$ no more than $]\sqrt{C_1 / \varepsilon}$ [ times, and c) to evaluate the vector-valued function $\bar{f}(x)$ at most

$$
2 ] ] \sqrt {C _ {1} / \varepsilon} [ + ] \max \left\{\log_ {2} (F (\bar {L}) / A _ {- 1}), 0 \right\} [
$$

times.

Theorem 2 is proved in essentially the same way as Theorem 1. It is only necessary to use (10) instead of (2), while the analogue of $\alpha_{k}f'(y_{k})$ will be the vector $y_{k}-T(y_{k},A_{k})$, and the analogue of $\alpha_{k}$ the values of $A_{k}^{-1}$.

Just as in the method (3)-(5), in the method (11)-(13) one can take into account information about the constant $F(\bar{L})$ and the parameter of strict convexity of the function $F(\bar{f}(x)) - m$ (for this, of course, we must have $y_0 \in Q$ ).

In conclusion let us mention two important special cases of problem (8) in which the auxiliary problem $\min\{\Phi(y_{k}, A, x) | x \in Q\}$ turns out to be rather simple.

a) Minimization of a smooth function on a simple set. By a simple set we understand a set for which the projection operator can be written in explicit form. In this case m = 1 and $F(y) = y$ in problem (8), and

$$
\Phi^ {*} (y, A) = f (y) - 0. 5 A ^ {- 1} \| f' (y) \| ^ {2} + 0. 5 A \| T (y, A) - y + A ^ {- 1} f' (y) \| ^ {2},
$$

in the method (11)-(13), where

$$
T (y, A) = \arg \min \left\{\| y - A ^ {- 1} f' (y) - z \| | z \in Q \right\}.
$$

b) Unconstrained minimization (in problem (8), $Q \equiv E$ ). In this case the auxiliary problem $\min\{\Phi(y, A, x) | x \in E\}$ is equivalent to the following dual problem:

$$
\max \left\{- 0. 5 A ^ {- 1} \left\| \sum_ {k = 1} ^ {m} \lambda^ {(k)} f _ {k} ^ {\prime} (y) \right\| ^ {2} + \sum_ {k = 1} ^ {m} \lambda^ {(k)} f _ {k} (y) \mid (\lambda^{(1)}, \lambda^{(2)}, \dots, \lambda^{(m)}) \in \partial F(0) \right\}. \tag {14}
$$

Here

$$
T (y, A) = y - A ^ {- 1} \sum_ {k = 1} ^ {m} \lambda^ {(k)} (y) f _ {k}' (y),
$$

where the $\lambda^{(k)}(y)$, $k = 1, \ldots, m$, are solutions of problem (14) for fixed $y \in E$. Let us remark that the set $\partial F(0)$ is usually given by simple constraints—linear or quadratic. In such cases problem (14) is the standard quadratic programming problem.

The author expresses his sincere appreciation to A. S. Nemirovskii for discussions that stimulated his interest in the questions considered here.

Central Economico-Mathematical Institute Academy of Sciences of the USSR

Received 19/JULY/82

# BIBLIOGRAPHY

1. A. S. Nemirovskii and D. B. Yudin, Complexity of problems and efficiency of optimization methods, "Nauka" Moscow, 1979. (Russian)  
2. B. N. Pshenichnyī and Yu, M. Danilin, Numerical methods in extremal problems, “Nauka”, Moscow, 1975; French transl., “Mir”, Moscow, 1977.

Translated by A. ROSA
