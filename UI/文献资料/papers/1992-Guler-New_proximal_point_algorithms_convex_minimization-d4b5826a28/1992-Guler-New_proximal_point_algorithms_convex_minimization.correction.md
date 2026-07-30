# NEW PROXIMAL POINT ALGORITHMS FOR CONVEX MINIMIZATION*

OSMAN GÜLER†

Abstract. This paper introduces two new proximal point algorithms for minimizing a proper, lower-semicontinuous convex function $f: \mathbf{R}^n \to R \cup \{\infty\}$. Under this minimal assumption on $f$, the first algorithm possesses the global convergence rate estimate $f(x_k) - \min_{x \in \mathbf{R}^n} f(x) = O(1 / (\sum_{j=0}^{k-1} \sqrt{\lambda_j})^2)$, where $\{\lambda_k\}_{k=0}^{\infty}$ are the proximal parameters. It is shown that this algorithm converges, and global convergence rate estimates for it are provided, even if minimizations are performed inexactly at each iteration. Both algorithms converge even if $f$ has no minimizers or is unbounded from below. These algorithms and results are valid in infinite-dimensional Hilbert spaces.

Key words. proximal point algorithms, global convergence rates, augmented Lagrangian algorithms, convex programming

AMS(MOS) subject classifications. primary 90C25; secondary 49D45, 49D37

1. Introduction. In this paper we present two new proximal point algorithms for the minimization problem

$$
\min _ {x \in \mathbf {R} ^ {n}} f (x), \tag {1.1}
$$

where $f: \mathbf{R}^n \to R \cup \{\infty\}$ is a proper lower-semicontinuous convex function, using the terminology established in Aubin and Ekeland [1] and Rockafellar [17].

The classical proximal point algorithm was introduced into optimization literature by Martinet [11]. It is based on the notion of proximal mapping $J_{\lambda}$,

$$
J _ {\lambda} x := \arg \min _ {z \in \mathbb {R} ^ {n}} \left\{f (z) + \frac {1}{2 \lambda} \left\| z - x \right\| ^ {2} \right\}, \tag {1.2}
$$

introduced earlier by Moreau [12]. The proximal point algorithm solves a single optimization problem by solving a sequence of optimization problems (1.2): it starts from a point $x_0 \in \mathbf{R}^n$ and generates the sequence $\{x_k\}_{k=0}^\infty$, where

$$
x _ {k + 1} = J _ {\lambda_ {k}} x _ {k} := \arg \min _ {x \in \mathbf {R} ^ {n}} \left\{f (x) + \frac {1}{2 \lambda_ {k}} \left\| x - x _ {k} \right\| ^ {2} \right\}, \tag {1.3}
$$

and where $\{\lambda_k\}_{k=0}^{\infty}$ is a sequence of positive numbers. The proximal point algorithm was popularized by Rockafellar [18], who showed that the algorithm converges even if the auxiliary minimizations in (1.3) are performed inexactly, which is an important consideration in practice. Güler [7] analyzed the algorithm further and provided global convergence rate estimates for it in terms of the objective residual $f(x_k) - \min_{x \in \mathbf{R}^n} f(x)$.

The minimization problem (1.1) is general enough to include the generic convex programming problem

$$
\min _ {x \in C} f _ {0} (x) \quad \text {s.t.} f _ {i} (x) \leq 0, \quad i = 1, \dots , m, \tag {1.4}
$$

where $C$ is a closed convex subset of $\mathbf{R}^n$ and $f_i: \mathbf{R}^n \to \mathbf{R}$, $i = 0, 1, \ldots, m$ are convex functions; see Rockafellar [19].

The usual application of the proximal point algorithm to convex programming is not to the primal program (1.4), but to its dual

$$
\max _ {y \in \mathbb {R} ^ {m}} \left\{\inf _ {x \in C} f _ {0} (x) + \sum_ {i = 1} ^ {m} y _ {i} f _ {i} (x) \right\} \quad \text {s.t.} y \geqslant 0. \tag {1.5}
$$

The resulting algorithm is called the augmented Lagrangian method. It was introduced into optimization literature independently by Hestenes [9] and Powell [16]. Augmented Lagrangian methods have many advantages over penalty methods; see Bertsekas [2] and Rockafellar [19].

The algorithms developed here are close in spirit to the classical proximal point algorithm discussed above. The only difference is that our algorithms generate an additional sequence $\{y_{k}\}_{k=0}^{\infty}$ of points in $R^{n}$, and calculate $x_{k+1}$ from

$$
x _ {k + 1} = J _ {\lambda_ {k}} y _ {k} := \arg \min _ {x \in \mathbf {R} ^ {n}} \left\{f (x) + \frac {1}{2 \lambda_ {k}} \left\| x - y _ {k} \right\| ^ {2} \right\}. \tag {1.6}
$$

The main work in the new algorithm is in the calculation of $x_{k+1}$ in (1.6), the calculation of $y_k$ being trivial. As with the classical algorithm, we show that the minimization in (1.6) can be performed inexactly.

For any feasible $x \in \mathbf{R}^n$, the algorithms here possess the global convergence rate estimate

$$
f (x _ {k}) - f (x) = O \left(\frac {1}{\left(\sum_ {j = 0} ^ {k - 1} \sqrt {\lambda_ {j}}\right) ^ {2}}\right). \tag {1.7}
$$

This is faster than the available rate

$$
f (x _ {k}) - f (x) = O \left(\frac {1}{\sum_ {j = 0} ^ {k - 1} \lambda_ {j}}\right) \tag {1.8}
$$

obtained by Güler [7] for the classical proximal point algorithm.

The paper is organized as follows. In § 2 we present the first proximal point algorithm for (1.1). We state the algorithm and estimate its convergence rate under the assumption that exact minimizations are performed in (1.6). In § 3, we present a version of the algorithm that requires only inexact minimizations in (1.6). In § 4, we show that the algorithms in §§ 2 and 3 have the property that $f(x_k) \to \inf_{x \in \mathbf{R}^n} f(x)$, even in cases where $f$ has no minimizers or is unbounded from below. We also present a monotonic version of the algorithm in which $f(x_{k+1}) \leq f(x_k)$. Some concluding remarks are made in § 5. In the Appendix, we present our second proximal point algorithm.

2. The proximal point algorithm. In this section we develop a new proximal point algorithm for problem (1.1). The inspiration for the algorithm comes from a paper by Nesterov [14] in which an optimal algorithm is developed for smooth convex minimization.

The idea of the algorithm is to generate recursively a sequence $\{\varphi_k\}_{k=0}^{\infty}$ of simple convex quadratic functions (with a diagonal matrix in the quadratic term) that approximate $f(x)$ in such a way that at step $k\geq 0$, the difference $\varphi_{k}(x)-f(x)$ is reduced by a fraction $1-\alpha_{k}$, that is, for all $x\in\mathbf{R}^{n}$,

$$
\varphi_ {k + 1} (x) - f (x) \leq (1 - \alpha_ {k}) (\varphi_ {k} (x) - f (x)), \tag {2.1}
$$

where $\alpha_{k}$ is a number in the interval [0, 1).

If (2.1) is satisfied for each $k \geq 0$, we obtain by induction

$$
\varphi_ {k} (x) - f (x) \leq \left(\prod_ {j = 0} ^ {k - 1} \left(1 - \alpha_ {j}\right)\right) (\varphi_ {0} (x) - f (x)).
$$

Defining

$$
\beta_ {k} = \prod_ {j = 0} ^ {k - 1} (1 - \alpha_ {j}), \tag {2.2}
$$

we have

$$
\varphi_ {k} (x) - f (x) \leq \beta_ {k} (\varphi_ {0} (x) - f (x)). \tag {2.3}
$$

If, at step $k$, we have at hand a point $x_{k}$ such that

$$
f (x _ {k}) \leq \varphi_ {k} ^ {*} := \min _ {z \in \mathbf {R} ^ {n}} \varphi_ {k} (z), \tag {2.4}
$$

then we obtain from (2.3) the global convergence estimate

$$
f (x _ {k}) - f (x) \leq \beta_ {k} (\varphi_ {0} (x) - f (x)). \tag {2.5}
$$

This is a significant bound only if $f(x) < \infty$, that is, if $x$ is feasible. If $f$ has a minimizer $x^*$, (2.5) specializes to

$$
f (x _ {k}) - f ^ {*} \leq \beta_ {k} (\varphi_ {0} (x ^ {*}) - f ^ {*}). \tag {2.6}
$$

If $\beta_{k} \to 0$, then $\{x_{k}\}$ is a minimizing sequence for $f$. The magnitude of the constant $\beta_{k}$ is a measure of the convergence rate of $f(x_{k})$ to $f^{*}$.

We define the quadratic functions $\varphi_{k}(x)$, $k \geq 0$, recursively, as follows:

$$
\varphi_ {0} (x) := f (x _ {0}) + \frac {A}{2} \left\| x - x _ {0} \right\| ^ {2},
$$

$$
\begin{aligned} \varphi_ {k + 1} (x) :&= (1 - \alpha_ {k}) \varphi_ {k} (x) \tag {2.7} \\ + \alpha_ {k} (f (J _ {\lambda_ {k}} y _ {k}) + \langle (y _ {k} - J _ {\lambda_ {k}} y _ {k}) / \lambda_ {k}, x - J _ {\lambda_ {k}} y _ {k} \rangle). \\ \end{aligned}
$$

Here $A$ and $\lambda_k$ are positive numbers and $\alpha_k$ is a number in the interval [0,1). The point $x_0$ is feasible, that is, $f(x_0) < \infty$. Here the point $y_k \in \mathbb{R}^n$ can be arbitrary. Later, it will be chosen to satisfy certain desirable properties.

LEMMA 2.1. For all $k \geq 0$, the quadratic functions $\varphi_k(x)$ defined above satisfy inequality (2.1), that is,

$$
\varphi_ {k + 1} (x) - f (x) \leq (1 - \alpha_ {k}) (\varphi_ {k} (x) - f (x)).
$$

Proof. Since $J_{\lambda_k}y_k$ is the minimizer in (1.6), we have by the subdifferentiation formula (see Rockafellar [18, pp. 889]), $0 \in \partial f(J_{\lambda_k}y_k) + (J_{\lambda_k}y_k - y_k) / \lambda_k$, that is,

$$
(y _ {k} - J _ {\lambda_ {k}} y _ {k}) / \lambda_ {k} \in \partial f (J _ {\lambda_ {k}} y _ {k}). \tag {2.8}
$$

Since $f$ is convex, for any $x \in \mathbf{R}^n$, we have

$$
f (x) \geq f (J _ {\lambda_ {k}} y _ {k}) + \langle (y _ {k} - J _ {\lambda_ {k}} y _ {k}) / \lambda_ {k}, x - J _ {\lambda_ {k}} y _ {k} \rangle . \tag {2.9}
$$

Thus

$$
\begin{aligned} \varphi_ {k + 1} (x) - f (x) &= (1 - \alpha_ {k}) (\varphi_ {k} (x) - f (x)) \\ + \alpha_ {k} (f (J _ {\lambda_ {k}} y _ {k}) + \langle (y _ {k} - J _ {\lambda_ {k}} y _ {k}) / \lambda_ {k}, x - J _ {\lambda_ {k}} y _ {k} \rangle - f (x)) \\ &\leq (1 - \alpha_ {k}) (\varphi_ {k} (x) - f (x)). \\ \end{aligned}
$$

□

It is not obvious a priori how points $x_{k} \in \mathbf{R}^{n}$ can be chosen to satisfy inequality (2.4). Toward this goal, we first note that the quadratic function $\varphi_{k}(x)$ can be written in the canonical form

$$
\varphi_ {k} (x) = \varphi_ {k} ^ {*} + \frac {A _ {k}}{2} \| x - \nu_ {k} \| ^ {2}, \tag {2.10}
$$

where $\varphi_k^*$ is the minimum value of the function $\varphi_k(x)$ in $\mathbf{R}^n$ and $\nu_{k}$ is its minimizer. Clearly $A_0 = A$ and $\nu_0 = x_0$. Using (2.7) and (2.10) it is easy to show that for $k\geq 0$,

$$
A _ {k + 1} = (1 - \alpha_ {k}) A _ {k} = \beta_ {k + 1} A, \tag {2.11}
$$

$$
\nu_ {k + 1} = \nu_ {k} - \frac {\alpha_ {k}}{A _ {k + 1} \lambda_ {k}} (y _ {k} - J _ {\lambda_ {k}} y _ {k}). \tag {2.12}
$$

We will determine the points $\{x_k\}$ satisfying (2.4) recursively. Suppose we already have a point $x_{k}$ satisfying inequality (2.4). The following result indicates how $y_{k}$ and $x_{k + 1}$ can be chosen such that $x_{k + 1}$ also satisfies (2.4). It is the main result of this section and uses ideas from Nesterov [14, Lemma 1].

THEOREM 2.1. If, for some $k \geq 0$, $x_k$ satisfies the inequality (2.4), that is, $f(x_k) \leq \varphi_k^*$, then for any $y_k \in \mathbf{R}^n$, $\lambda_k > 0$, and $\alpha_k \in [0,1)$, the following inequality holds:

$$
Replace \cong with \geq or \ge
$$

$$
+ \frac {1}{\lambda_ {k}} \langle y _ {k} - J _ {\lambda_ {k}} y _ {k}, (1 - \alpha_ {k}) x _ {k} + \alpha_ {k} \nu_ {k} - y _ {k} \rangle .
$$

Proof. We obtain from (2.7), (2.10), and (2.11)

$$
\begin{aligned} \varphi_ {k + 1} ^ {*} :&= \varphi_ {k + 1} (\nu_ {k + 1}) \\ &= (1 - \alpha_ {k}) \varphi_ {k} (\nu_ {k + 1}) + \alpha_ {k} f (J _ {\lambda_ {k}} y _ {k}) \\ &= (1 - \alpha_ {k}) \varphi_ {k} ^ {*} + \frac {A _ {k + 1}}{2} \| \nu_ {k + 1} - \nu_ {k} \| ^ {2} + \alpha_ {k} f (J _ {\lambda_ {k}} y _ {k}) \\ + \frac {\alpha_ {k}}{\lambda_ {k}} \langle y _ {k} - J _ {\lambda_ {k}} y _ {k}, \nu_ {k + 1} - J _ {\lambda_ {k}} y _ {k} \rangle . \\ \end{aligned}
$$

$$
+ \frac {\alpha_ {k}}{\lambda_ {k}} \langle y _ {k} - J _ {\lambda_ {k}} y _ {k}, \nu_ {k + 1} - J _ {\lambda_ {k}} y _ {k} \rangle \tag {2.14}
$$

Since by assumption $\varphi_k^* \geq f(x_k)$, we obtain from (2.9) that

$$
\varphi_ {k} ^ {*} \geq f (x _ {k}) \geq f (J _ {\lambda_ {k}} y _ {k}) + \langle (y _ {k} - J _ {\lambda_ {k}} y _ {k}) / \lambda_ {k}, x _ {k} - J _ {\lambda_ {k}} y _ {k} \rangle .
$$

Using this in (2.14), we obtain

$$
\begin{aligned} \varphi_ {k + 1} ^ {*} &\geq f (J _ {\lambda_ {k}} y _ {k}) + \frac {A _ {k + 1}}{2} \| \nu_ {k + 1} - \nu_ {k} \| ^ {2} \tag {2.15} \\ + \frac {1}{\lambda_ {k}} \langle y _ {k} - J _ {\lambda_ {k}} y _ {k}, (1 - \alpha_ {k}) x _ {k} + \alpha_ {k} \nu_ {k + 1} - J _ {\lambda_ {k}} y _ {k} \rangle . \\ \end{aligned}
$$

The term $(1 - \alpha_{k})x_{k} + \alpha_{k}\nu_{k + 1} - J_{\lambda_{k}}y_{k}$ above can be written as

$$
((1 - \alpha_ {k}) x _ {k} + \alpha_ {k} \nu_ {k} - y _ {k}) + \alpha_ {k} (\nu_ {k + 1} - \nu_ {k}) + (y _ {k} - J _ {\lambda_ {k}} y _ {k}).
$$

Substituting the value of $\nu_{k + 1} - \nu_k$ from the formula (2.12) into the second term above, we see that the scalar product term in (2.15) can be written as

$$
\langle y _ {k} - J _ {\lambda_ {k}} y _ {k}, (1 - \alpha_ {k}) x _ {k} + \alpha_ {k} \nu_ {k} - y _ {k} \rangle + \left(1 - \frac {\alpha_ {k} ^ {2}}{A _ {k + 1} \lambda_ {k}}\right) \| y _ {k} - J _ {\lambda_ {k}} y _ {k} \| ^ {2}. \tag {2.16}
$$

Also, substituting the value of $\nu_{k+1}-\nu_{k}$ in (2.12) into the second term of (2.15), we obtain

$$
\frac {A _ {k + 1}}{2} \left\| \nu_ {k + 1} - \nu_ {k} \right\| ^ {2} = \frac {\alpha_ {k} ^ {2}}{2 A _ {k + 1} \lambda_ {k} ^ {2}} \left\| y _ {k} - J _ {\lambda_ {k}} y _ {k} \right\| ^ {2}. \tag {2.17}
$$

We obtain (2.13) by using lines (2.16) and (2.17) in (2.15). This proves the theorem. $\square$

COROLLARY 2.1. If, in Theorem 2.1, we choose

$$
y _ {k} = (1 - \alpha_ {k}) x _ {k} + \alpha_ {k} \nu_ {k}, \tag {2.18}
$$

then

$$
\varphi_ {k + 1} ^ {*} \geq f (J _ {\lambda_ {k}} y _ {k}) + \frac {1}{2 \lambda_ {k}} \left(2 - \frac {\alpha_ {k} ^ {2}}{A _ {k + 1} \lambda_ {k}}\right) \| y _ {k} - J _ {\lambda_ {k}} y _ {k} \| ^ {2}. \tag {2.19}
$$

Corollary 2.1 suggests many possibilities for obtaining convergent proximal point algorithms. For example, we can choose

$$
x _ {k + 1} = J _ {\lambda_ {k}} y _ {k} := \arg \min _ {z \in \mathbf {R} ^ {n}} \left\{f (z) + \frac {1}{2 \lambda_ {k}} \left\| z - y _ {k} \right\| ^ {2} \right\}, \tag {2.20}
$$

$$
\alpha_ {k} ^ {2} = A _ {k + 1} \lambda_ {k} := (1 - \alpha_ {k}) A _ {k} \lambda_ {k}. \tag {2.21}
$$

COROLLARY 2.2. If $y_{k}$ is chosen as in (2.18), $x_{k+1}$ is chosen as in (2.20), and $\alpha_{k}$ is chosen as in (2.21), then

$$
\varphi_ {k + 1} ^ {*} \geq f (x _ {k + 1}) + \frac {1}{2 \lambda_ {k}} \left\| y _ {k} - x _ {k + 1} \right\| ^ {2} \geq f (x _ {k + 1}). \tag {2.22}
$$

Our proximal point algorithm chooses $y_{k}, x_{k+1}$, and $\alpha_{k}$ according to Corollary 2.2.

THE PROXIMAL POINT ALGORITHM.

Initialization. Choose a feasible starting point $x_0 \in \mathbf{R}^n$ ( $f(x_0) < \infty$ ), and constants $\lambda_0 > 0$ and $A > 0$. Define $\nu_0 := x_0$, $A_0 := A$.

Step $k, k \geq 0$ :

(a) Choose $\lambda_{k} > 0$, and calculate $\alpha_{k} > 0$ from the equation $\alpha_{k}^{2} = (1 - \alpha_{k})A_{k}\lambda_{k}$, that is,

$$
\alpha_ {k} = \frac {\sqrt {(A _ {k} \lambda_ {k}) ^ {2} + 4 A _ {k} \lambda_ {k}} - A _ {k} \lambda_ {k}}{2}. \tag {2.23}
$$

(b) Define

$$
\begin{aligned} y _ {k} &= (1 - \alpha_ {k}) x _ {k} + \alpha_ {k} \nu_ {k}, \\ x _ {k + 1} :&= J _ {\lambda_ {k}} y _ {k} = \arg \min _ {z \in \mathbf {R} ^ {n}} \left\{f (z) + \frac {1}{2 \lambda_ {k}} \| z - y _ {k} \| ^ {2} \right\}, \end{aligned} \tag {2.24}
$$

$$
\nu_ {k + 1} = \nu_ {k} + \frac {1}{\alpha_ {k}} (x _ {k + 1} - y _ {k}),
$$

$$
A _ {k + 1} = (1 - \alpha_ {k}) A _ {k}.
$$

Remark 2.1. In the algorithm above, the starting point $x_0$ must be feasible. However, this is not a serious restriction since one preliminary iteration of the classical proximal point algorithm can generate such a feasible point $x_0$.

In order to estimate the convergence rate of the algorithm, we must estimate the magnitude of $\beta_{k}$, as the inequality (2.6) shows. The following result gives tight bounds for $\beta_{k}$. The upper bound below is an extension of a result in Nesterov [14]. The lower bound is needed in §3, Lemma 3.3.

LEMMA 2.2.

$$
\frac {1}{(1 + \sqrt {A} \sum_ {j = 0} ^ {k - 1} \sqrt {\lambda_ {j}}) ^ {2}} \leqq \beta_ {k} \leqq \frac {1}{(1 + (\sqrt {A} / 2) \sum_ {j = 0} ^ {k - 1} \sqrt {\lambda_ {j}}) ^ {2}}. \tag {2.25}
$$

Proof. We first prove the upper bound on $\beta_{k}$ in (2.25). From (2.2), we obtain $\beta_{k+1} = (1 - \alpha_k)\beta_k$, which implies $\alpha_{k} = 1 - \beta_{k+1}/\beta_{k}$. Also, from (2.11), $A_{k+1} = \beta_{k+1}A$. Substituting this in (2.21) results in

$$
\left(1 - \frac {\beta_ {k + 1}}{\beta_ {k}}\right) ^ {2} = \beta_ {k + 1} A \lambda_ {k}.
$$

We make the substitution $\beta_{k}=\mu_{k}^{-2}$ in the equality above. Taking the square roots of both sides of this equality and then multiplying both sides of the resulting equality by $\mu_{k+1}^{2}$, we obtain

$$
\mu_ {k + 1} ^ {2} - \mu_ {k} ^ {2} = \mu_ {k + 1} \sqrt {A \lambda_ {k}}. \tag {2.26}
$$

It is easy to show that $2\mu_{k + 1}(\mu_{k + 1} - \mu_k)\geqslant \mu_{k + 1}^2 -\mu_k^2$. Using this in (2.26) results in

$$
2 \mu_ {k + 1} (\mu_ {k + 1} - \mu_ {k}) \geq \mu_ {k + 1} \sqrt {A \lambda_ {k}},
$$

which implies $\mu_{k+1} - \mu_k \geq \sqrt{A\lambda_k}/2$. Summing this inequality for $j = 0, 1, \ldots, k-1$ and noting $\mu_0 = 1$, we obtain

$$
\mu_ {k} \geqq 1 + \frac {\sqrt {A}}{2} \sum_ {j = 0} ^ {k - 1} \sqrt {\lambda_ {j}}.
$$

Substituting $\mu_{k}=\beta_{k}^{-1/2}$ above proves the upper bound on $\beta_{k}$.

It remains to prove the lower bound on $\beta_{k}$. Note that $\beta_{k+1} \leq \beta_{k}$ implies $\mu_{k+1} \geq \mu_{k}$. Thus $\mu_{k+1}(\mu_{k+1} - \mu_{k}) \leq \mu_{k+1}^{2} - \mu_{k}^{2}$. Using this in (2.26), we obtain $\mu_{k+1} - \mu_{k} \leq \sqrt{A\lambda_{k}}$. As above, summing this inequality for $j = 0, 1, \ldots, k-1$, we obtain

$$
\mu_ {k} \leqq 1 + \sqrt {A} \sum_ {j = 0} ^ {k - 1} \sqrt {\lambda_ {j}}.
$$

Substituting $\mu_{k}=\beta_{k}^{-1/2}$ above proves the lower bound on $\beta_{k}$.

From Corollary 2.2 and inequality (2.3), we obtain the following basic convergence rate result.

THEOREM 2.2. For any feasible point $x \in \mathbb{R}^n$, the proximal point algorithm stated above has the global convergence rate estimate

$$
\begin{aligned} f (x _ {k}) - f (x) + \frac {1}{2 \lambda_ {k - 1}} \| y _ {k - 1} - x _ {k} \| ^ {2} &\leq \frac {f (x _ {0}) - f (x) + (A / 2) \| x - x _ {0} \| ^ {2}}{(1 + (\sqrt {A} / 2) \sum_ {j = 0} ^ {k - 1} \sqrt {\lambda_ {j}}) ^ {2}} \tag {2.27} \\ &= O \left(\frac {1}{\left(\sum_ {j = 0} ^ {k - 1} \sqrt {\lambda_ {j}}\right) ^ {2}}\right). \\ \end{aligned}
$$

Remark 2.2. The convergence rate estimate above is given in terms of the objective function gap $f(x_{k}) - f^{*}$. The convergence of the points $\{x_{k}\}$ is a future research topic.

Even if we can show that the sequence $\{x_{k}\}$ converges to an optimal solution $x^{*}$, it is unlikely that a convergence rate can be provided for $\{\|x_{k}-x^{*}\|\}$ without further assumptions on f. Of course, if f is strongly convex, then, using the standard properties of strongly convex functions, we can show that $\{x_{k}\}$ converges to the unique optimal solution of f and that

$$
\| x _ {k} - x ^ {*} \| = O \bigg (\frac {1}{\sum_ {j = 0} ^ {k - 1} \sqrt {\lambda_ {j}}} \bigg).
$$

Also, in certain problems (for example, linear programming) we can prove that $\{x_k\}$ converges to the optimal set and provide an estimate of the convergence rate; see Güler [8].

Remark 2.3. The term $\|y_{k-1}-x_{k}\|^{2}/(2\lambda_{k-1})$ in (2.27) is not strictly necessary to obtain convergence estimates for the algorithm presented in this section. However, it will be crucial in the next section where we present a relaxed proximal point algorithm in which $x_{k+1}$ is calculated only approximately:

$$
x _ {k + 1} \approx J _ {\lambda_ {k}} y _ {k} := \arg \min _ {z \in \mathbf {R} ^ {n}} \left\{f (z) + \frac {1}{2 \lambda_ {k}} \left\| z - y _ {k} \right\| ^ {2} \right\}.
$$

It is also crucial in proving the finite termination of the augmented Lagrangian algorithm for linear programming in Güler [8], which is an application of the algorithm presented in this section.

The convergence rate of the proximal point algorithm is summarized below.

THEOREM 2.3. Suppose $f$ has a minimizer $x^*$ and $f^* = f(x^*) = \min_{z \in \mathbb{R}^n} f(z)$. Denote the set of minimizers of $f$ by $X^*$. The proximal point algorithm above possesses the global convergence rate estimate

$$
f (x _ {k}) - f ^ {*} \leq \frac {4}{A (\sum_ {j = 0} ^ {k - 1} \sqrt {\lambda_ {j}}) ^ {2}} \left(f (x _ {0}) - f ^ {*} + \frac {A}{2} \rho (x _ {0}, X ^ {*}) ^ {2}\right). \tag {2.28}
$$

The algorithm converges, that is, $f(x_{k}) \to f^{*}$ if

$$
\sum_ {k = 0} ^ {\infty} \sqrt {\lambda_ {k}} = \infty . \tag {2.29}
$$

In particular, if $\lambda_{k} \cong \lambda > 0$, we have the convergence rate estimate

$$
\begin{aligned} f (x _ {k}) - f ^ {*} &\leq \frac {4 / (A \lambda)}{k ^ {2}} \left(f (x _ {0}) - f ^ {*} + \frac {A}{2} \rho (x _ {0}, X ^ {*}) ^ {2}\right) \tag {2.30} \\ &= O \left(\frac {1}{k ^ {2}}\right). \\ \end{aligned}
$$

Remark 2.4. The convergence rate of our proximal point algorithm given in (2.26) compares favorably with the convergence rate estimate

$$
f (x _ {k}) - f ^ {*} \leqslant \frac {\rho (x _ {0} , X ^ {*}) ^ {2}}{2 \sum_ {j = 0} ^ {k - 1} \lambda_ {j}} \tag {2.31}
$$

obtained in Güler [7] for the classical proximal point algorithm. It is clear that the convergence rate estimate (2.28) is faster than (2.31). Moreover, it is shown in Güler [7] (Remark 2.1) that the condition $\sum_{k=0}^{\infty}\lambda_{k}=\infty$ is necessary and sufficient for the convergence of the classical proximal point algorithm. In contrast, the algorithm presented here converges under the weaker condition (2.29).

Further properties of the algorithm are given below. Note that (2.34) follows from (2.32) because of (2.8).

COROLLARY 2.3. If (2.29) holds true in the proximal point algorithm, then

$$
\frac {\| x _ {k + 1} - y _ {k} \| ^ {2}}{\lambda_ {k}} \to 0. \tag {2.32}
$$

If the sequence $\{\lambda_k\}$ is bounded from above, then

$$
\| x _ {k + 1} - y _ {k} \| \to 0. \tag {2.33}
$$

Also,

$$
\lambda_ {k} \rho (0, \partial f (x _ {k + 1})) ^ {2} \to 0. \tag {2.34}
$$

If the sequence $\{\lambda_k\}$ is bounded away from 0, then

$$
\rho (0, \partial f (x _ {k})) \to 0. \tag {2.35}
$$

If $f$ is differentiable, (2.35) means that

$$
\| f' (x _ {k}) \| \to 0. \tag {2.36}
$$

Remark 2.5. Ekeland's $\varepsilon$ -variational principle (see Aubin and Ekeland [1, Chap. 5]) can be used to prove that if $f$ is bounded from below, that is, $f^{*} := \inf_{x \in \mathbb{R}^{n}} f(x) > -\infty$, then there exist $x_{k}$ and $w_{k} \in \partial f(x_{k})$ such that $f(x_{k}) \to f^{*}$ and $w_{k} \to 0$. A slight generalization of Corollary 2.3 shows that such $x_{k}$ and $w_{k}$ can be generated by our proximal point algorithm.

3. The algorithm with inexact minimization. In the proximal point algorithm presented in §2, $x_{k+1}$ is given by

$$
x _ {k + 1} = J _ {\lambda_ {k}} y _ {k} := \arg \min _ {z \in \mathbb {R} ^ {n}} \left\{f (z) + \frac {1}{2 \lambda_ {k}} \left\| z - y _ {k} \right\| ^ {2} \right\}. \tag {3.1}
$$

The point $x_{k+1}$ is thus the exact minimum of the augmented function

$$
\phi_ {k} (z) := f (z) + \frac {1}{2 \lambda_ {k}} \left\| z - y _ {k} \right\| ^ {2}. \tag {3.2}
$$

The calculation of $x_{k+1}$ can be almost as difficult to solve as the original minimization problem (1.1). In this section, we show that a modification of the algorithm in §2, which requires only an approximate minimization of $\phi_{k}$, that is,

$$
x _ {k + 1} \approx J _ {\lambda_ {k}} y _ {k} := \arg \min _ {z \in \mathbf {R} ^ {n}} \phi_ {k} (z), \tag {3.3}
$$

still yields a convergent proximal point algorithm.

DEFINITION 3.1. We will say that $x_{k+1}$ is an approximation minimizer of $\phi_k$ if the following criterion $\mathbf{A}'$ in Rockafellar [18, pp. 880] is satisfied:

$$
\rho (0, \partial \phi_ {k} (x _ {k + 1})) \leqslant \frac {\varepsilon_ {k}}{\lambda_ {k}}. \tag {$A^{\prime$}}
$$

Note that if $f$ is differentiable, condition $\mathbf{A}'$ means that

$$
\| \phi_ {k}' (x _ {k + 1}) \| \leq \frac {\varepsilon_ {k}}{\lambda_ {k}}.
$$

We will give conditions on the magnitude of the errors $\varepsilon_{k}$ which are sufficient to obtain convergent algorithms.

The result below shows that $x_{k+1}$ is in fact an approximate minimizer of $\phi_k$. It will be needed later in this section.

LEMMA 3.1. Let $\phi_k^* = \min_{z\in \mathbf{R}^n}\phi_k(z)$. If $x_{k + 1}$ satisfies condition $\mathbf{A}'$, then

$$
\frac {1}{2 \lambda_ {k}} \left\| x _ {k + 1} - J _ {\lambda_ {k}} y _ {k} \right\| ^ {2} \leq \phi_ {k} (x _ {k + 1}) - \phi_ {k} ^ {*} \leq \frac {\varepsilon_ {k} ^ {2}}{2 \lambda_ {k}}. \tag {3.4}
$$

Proof. We start by proving the first inequality. By definition, $J_{\lambda_k}y_k$ is the exact minimizer of $\phi_k$. Since $\phi_k$ is strongly convex with modulus $1 / \lambda_k$ and $0 \in \phi_k(J_{\lambda_k}y_k)$, it follows from Proposition 6(c) of Rockafellar [18] that

$$
\begin{aligned} \phi_ {k} (x _ {k + 1}) - \phi_ {k} ^ {*} &= \phi_ {k} (x _ {k + 1}) - \phi_ {k} (J _ {\lambda_ {k}} y _ {k}) \\ \geqq \langle 0, x _ {k + 1} - J _ {\lambda_ {k}} y _ {k} \rangle + \frac {1}{2 \lambda_ {k}} \left\| x _ {k + 1} - J _ {\lambda_ {k}} y _ {k} \right\| ^ {2} \\ &= \frac {1}{2 \lambda_ {k}} \left\| x _ {k + 1} - J _ {\lambda_ {k}} y _ {k} \right\| ^ {2}. \\ \end{aligned}
$$

This proves the first inequality.

It remains to prove the second inequality. Let $w_{k} \in \partial \phi_{k}(x_{k + 1})$ be such that $\| w_{k} \| \leq \varepsilon_{k} / \lambda_{k}$. Since $\phi_{k}$ is strongly convex with modulus $1 / \lambda_{k}$, and $\| w_{k} \| \leq \varepsilon_{k} / \lambda_{k}$, we have

$$
\begin{array}{l} \phi_ {k} (J _ {\lambda_ {k}} y _ {k}) - \phi_ {k} (x _ {k + 1}) \geq \langle w _ {k}, J _ {\lambda_ {k}} y _ {k} - x _ {k + 1} \rangle + \frac {1}{2 \lambda_ {k}} \left\| J _ {\lambda_ {k}} y _ {k} - x _ {k + 1} \right\| ^ {2} \\ \geqq - \left\| w _ {k} \right\| \left\| J _ {\lambda_ {k}} y _ {k} - x _ {k + 1} \right\| + \frac {1}{2 \lambda_ {k}} \left\| J _ {\lambda_ {k}} y _ {k} - x _ {k + 1} \right\| ^ {2} \\ \geq - \frac {\varepsilon_ {k}}{\lambda_ {k}} \left\| J _ {\lambda_ {k}} y _ {k} - x _ {k + 1} \right\| + \frac {1}{2 \lambda_ {k}} \left\| J _ {\lambda_ {k}} y _ {k} - x _ {k + 1} \right\| ^ {2} \\ \geq \frac {1}{\lambda_ {k}} \min _ {t \in \mathbf {R}} \left\{\frac {1}{2} t ^ {2} - \varepsilon_ {k} t \right\} \\ = - \frac {\varepsilon_ {k} ^ {2}}{2 \lambda_ {k}}, \\ \end{array}
$$

where the first inequality again follows from Proposition 6 in Rockafellar [18]. This proves the lemma. $\square$

COROLLARY 3.1. If $x_{k+1}$ is chosen according to criterion $\mathbf{A}'$, then

$$
\| x _ {k + 1} - J _ {\lambda_ {k}} y _ {k} \| \leq \varepsilon_ {k}. \tag {3.5}
$$

Corollary 3.1 is proved in a more general context in Rockafellar [18, Prop. 3].

We will need the following slight generalization of Theorem 2.1. Its proof is similar to that of the original Theorem 2.1.

LEMMA 3.2. If, for some $k \geq 0$, $x_k$ satisfies the inequality

$$
f (x _ {k}) \leq \varphi_ {k} ^ {*} + \delta_ {k}, \tag {3.6}
$$

then for any $y_{k}\in \mathbf{R}^{n}$, $\lambda_{k} > 0$, and $\alpha_{k}\in [0,1)$, the following inequality holds true:

$$
\begin{aligned} \varphi_ {k + 1} ^ {*} + (1 - \alpha_ {k}) \delta_ {k} &\geq f (J _ {\lambda_ {k}} y _ {k}) + \frac {1}{2 \lambda_ {k}} \left(2 - \frac {\alpha_ {k} ^ {2}}{A _ {k + 1} \lambda_ {k}}\right) \| y _ {k} - J _ {\lambda_ {k}} y _ {k} \| ^ {2} \tag {3.7} \\ + \frac {1}{\lambda_ {k}} \langle y _ {k} - J _ {\lambda_ {k}} y _ {k}, (1 - \alpha_ {k}) x _ {k} + \alpha_ {k} \nu_ {k} - y _ {k} \rangle . \\ \end{aligned}
$$

Also, Corollary 2.2 generalizes to Corollary 3.2.

COROLLARY 3.2. If $y_{k}$ is chosen as in (2.18) and $\alpha_{k}$ is chosen as in (2.21), then

$$
\varphi_ {k + 1} ^ {*} + (1 - \alpha_ {k}) \delta_ {k} \geq f (J _ {\lambda_ {k}} y _ {k}) + \frac {1}{2 \lambda_ {k}} \| J _ {\lambda_ {k}} y _ {k} - y _ {k} \| ^ {2} = \phi_ {k} ^ {*} \tag {3.8}
$$

The following result estimates how the individual errors $\{\varepsilon_{j}\}_{j=0}^{k-1}$ at each step accumulate to a total error $\delta_{k}$ at step k.

THEOREM 3.1. If, in the algorithm in §2, $x_{k+1}$ is calculated according to criterion A' instead of (2.20), then

$$
f (x _ {k}) \leq \varphi_ {k} ^ {*} + \delta_ {k}, \tag {3.9}
$$

where $\{\delta_k\}_{k=0}^{\infty}$ satisfies the difference equation

$$
\delta_ {0} = 0, \quad \delta_ {k + 1} = (1 - \alpha_ {k}) \delta_ {k} + \frac {\varepsilon_ {k} ^ {2}}{2 \lambda_ {k}}, \quad k = 0, 1, \dots . \tag {3.10}
$$

Proof. We prove (3.9) and (3.10) by induction. Since $f(x_0) = \varphi_0^*$, they are true for $k = 0$. Suppose (3.9) and (3.10) hold true for $k$. We will show that they also hold true for $k + 1$. We have

$$
\begin{aligned} \varphi_ {k + 1} ^ {*} + (1 - \alpha_ {k}) \delta_ {k} &\geq \phi_ {k} ^ {*} \quad (\text {from} (3. 8)) \\ &\geq \phi_ {k} (x _ {k + 1}) - \frac {\varepsilon_ {k} ^ {2}}{2 \lambda_ {k}} \quad (\text {from Lemma 3.1}) \\ &= f (x _ {k + 1}) + \frac {1}{2 \lambda_ {k}} \left\| x _ {k + 1} - y _ {k} \right\| ^ {2} - \frac {\varepsilon_ {k} ^ {2}}{2 \lambda_ {k}}, \\ \end{aligned}
$$

which implies

$$
f (x _ {k + 1}) + \frac {1}{2 \lambda_ {k}} \left\| x _ {k + 1} - y _ {k} \right\| ^ {2} \leq \varphi_ {k + 1} ^ {*} + \delta_ {k + 1}.
$$

This proves the theorem. $\square$

Note that Lemma 2.1 still holds true, so that (2.3) is valid. Combining (2.3) and Theorem 3.1 results in the following theorem.

THEOREM 3.2. In the modified proximal point algorithm in which the point $x_{k}$ is calculated according to criterion A', we have for any $x \in \mathbb{R}^n$, the convergence rate estimate

$$
f (x _ {k}) - f (x) \leq \beta_ {k} (\varphi_ {0} (x) - f (x)) + \delta_ {k},
$$

where $\{\delta_k\}$ satisfies the difference equation (3.10). In particular, we have the convergence rate estimate

$$
f (x _ {k}) - f ^ {*} \leq \beta_ {k} \bigg (f (x _ {0}) - f ^ {*} + \frac {A}{2} \rho (x _ {0}, X ^ {*}) ^ {2} \bigg) + \delta_ {k}. \tag {3.11}
$$

From (3.11) we see that in order for the modified algorithm to converge, we must have $\delta_k \to 0$. In the next result, we obtain bounds on $\delta_k$.

LEMMA 3.3. The solution to the difference equation (3.10) is given by

$$
\delta_ {k} = \frac {\beta_ {k}}{2} \cdot \sum_ {j = 0} ^ {k - 1} \frac {\varepsilon_ {j} ^ {2} / \lambda_ {j}}{\beta_ {j + 1}}. \tag {3.12}
$$

Moreover,

$$
\delta_ {k} \leqq 2 \sum_ {j = 0} ^ {k - 1} \frac {\varepsilon_ {j} ^ {2}}{\lambda_ {j}} \left(\frac {1 + \sqrt {A} \sum_ {i = 0} ^ {j} \sqrt {\lambda_ {i}}}{1 + \sqrt {A} \sum_ {j = 0} ^ {k - 1} \sqrt {\lambda_ {j}}}\right) ^ {2}. \tag {3.13}
$$

Assume $\{\lambda_k\}_{k=0}^{\infty}$ is an increasing sequence or, more generally, that there exists a constant $M > 0$ such that

$$
\lambda_ {i} \leq M \lambda_ {j} \quad \text { whenever } i \leq j, \tag {3.14}
$$

and that for some $\sigma > 0$

$$
\varepsilon_ {k} = O (1 / k ^ {\sigma}), \quad k = 1, 2, \dots ; \tag {3.15}
$$

that is, there is a constant $c > 0$ such that $\varepsilon_{k} \cong c / k^{\sigma}$ for all $k \geq 1$. Then

$$
\delta_ {k} = O \left(\frac {1}{k ^ {2 \sigma - 1}}\right). \tag {3.16}
$$

Proof. Since $1 - \alpha_{j} = \beta_{j + 1} / \beta_{j}$, for any $j\geq 0$, (3.10) can be written as $\delta_{j + 1} = (\beta_{j + 1} / \beta_j)\delta_j + \varepsilon_j^2 /(2\lambda_j)$. Dividing this equality by $\beta_{j + 1}$, and rearranging its terms, we obtain

$$
\frac {\delta_ {j + 1}}{\beta_ {j + 1}} - \frac {\delta_ {j}}{\beta_ {j}} = \frac {\varepsilon_ {j} ^ {2} / \lambda_ {j}}{2 \beta_ {j + 1}}. \tag {3.17}
$$

Summing (3.17) for $j=0,1,\ldots,k-1$, and noting $\delta_{0}=0$, we obtain (3.12).

Inequality (3.13) is obtained from (3.12) by using the lower bound on $\beta_{j+1}$ given in Lemma 2.2.

It remains to prove (3.16). If (3.14) is true, then $\sum_{k=0}^{\infty}\sqrt{\lambda_{k}}=\infty$. Thus there exists a constant c>0 such that $1+\sqrt{A}\sum_{i=0}^{j}\sqrt{\lambda_{i}}\leqq c\sqrt{A}\sum_{i=0}^{j}\sqrt{\lambda_{i}}$. We deduce from (3.13) that there are constants c>0 (not the same constant c above) and $\bar{c}>0$ such that

$$
\delta_ {k} \leq c \sum_ {j = 0} ^ {k - 1} \varepsilon_ {j} ^ {2} \left(\frac {\sum_ {i = 0} ^ {j} \sqrt {\lambda_ {i} / \lambda_ {j}}}{\sum_ {j = 0} ^ {k - 1} \sqrt {\lambda_ {j}}}\right) ^ {2} \leq \bar {c} \cdot \frac {\sum_ {j = 0} ^ {k - 1} \left(j \varepsilon_ {j}\right) ^ {2}}{k ^ {2}}. \tag {3.18}
$$

If $\varepsilon_{k}$ satisfies (3.15), there exists a constant $\tilde{c} > 0$ such that

$$
\sum_ {j = 0} ^ {k - 1} (j \varepsilon_ {j}) ^ {2} \leq \tilde {c} \int_ {0} ^ {k} t ^ {2 - 2 \sigma} d t = \frac {\tilde {c}}{3 - 2 \sigma} k ^ {3 - 2 \sigma}.
$$

Using this estimate in (3.18) proves (3.16).

The theorem below, which summarizes the results of this section, gives the convergence rate estimates for the proximal point with errors. It is obtained from Theorem 3.2 and Lemmas 2.2 and 3.3.

THEOREM 3.3. Consider a proximal point algorithm that differs from the one stated in §2 only in that the point $x_{k}$ is approximately calculated according to criterion $\mathbf{A}'$ with an error $\varepsilon_{k}$. Assume that errors $\{\varepsilon_k\}$ satisfy condition (3.15) for some $\sigma > \frac{1}{2}$, and that parameters $\{\lambda_k\}$ are chosen according to condition (3.14). Then, for any feasible $x \in \mathbb{R}^n$,

$$
f (x _ {k}) - f (x) \leq O \bigg (\frac {1}{k ^ {2}} \bigg) + O \bigg (\frac {1}{k ^ {2 \sigma - 1}} \bigg) \to 0.
$$

In particular,

$$
f (x _ {k}) - f ^ {*} = O \bigg (\frac {1}{k ^ {2}} \bigg) + O \bigg (\frac {1}{k ^ {2 \sigma - 1}} \bigg),
$$

and if $\sigma \geq \frac{3}{2}$,

$$
f (x _ {k}) - f ^ {*} = O \bigg (\frac {1}{k ^ {2}} \bigg).
$$

Remark 3.1. Theorem 3.3 can be compared with results in Rockafellar [18] (see also Brézis and Lions [3, pp. 343]). Rockafellar proves that under condition A' or condition (3.5) (which he calls condition A) together with the condition

$$
\sum_ {k = 0} ^ {\infty} \varepsilon_ {k} <   \infty , \tag {3.19}
$$

the classical proximal point algorithm converges for a maximal monotone operator. In [3] and [18] convergence means that $x_{k} \rightarrow x^{*}$ to some solution of the maximal monotone operator. Rockafellar shows that (3.19) is a necessary and sufficient condition for convergence. Our sense of convergence is different from the one in [3] and [18] in that we require only that $f(x_{k}) \rightarrow f^{*}$. However, our condition (3.15) on $\{\varepsilon_{k}\}$ is somewhat weaker than (3.19) and we are able to prove the convergence rates in Theorem 3.3. It is interesting to note that such convergence rates for $f(x_{k}) - f^{*}$ are not currently available for the inexact minimization version of the classical proximal minimization algorithm.

4. Further properties of the algorithms. In this section, we develop monotonic versions of the algorithms presented in §§ 2 and 3. We also show that all algorithms minimize $f$ even if $f$ has no minimizers or is unbounded from below.

The proximal point algorithm developed in the previous sections need not be monotonic, that is, we may have $f(x_{k+1}) > f(x_k)$. Here we present monotonic versions of the algorithms and discuss their convergence properties.

We obtain the monotonic version of the algorithm in § 2 simply by replacing the equation defining $x_{k+1}$ in (2.24) with the following:

$$
\bar {x} _ {k + 1} = J _ {\lambda_ {k}} y _ {k}, \quad x _ {k + 1} = \arg \min \{f (\bar {x} _ {k + 1}), f (x _ {k}) \}.
$$

THE MONOTONIC PROXIMAL POINT ALGORITHM.

Initialization. Choose a feasible starting point $x_0 \in \mathbf{R}^n$ ( $f(x_0) < \infty$ ), and constants $\lambda_0 > 0$ and $A > 0$. Define $\nu_0 := x_0$, $A_0 := A$.

Step $k, k \geq 0$ :

(a) Choose $\lambda_{k} > 0$, and set

$$
\alpha_ {k} = \frac {\sqrt {\left(A _ {k} \lambda_ {k}\right) ^ {2} + 4 A _ {k} \lambda_ {k}} - A _ {k} \lambda_ {k}}{2}.
$$

(b) Define

$$
y _ {k} = (1 - \alpha_ {k}) x _ {k} + \alpha_ {k} \nu_ {k},
$$

$$
\bar {x} _ {k + 1} = J _ {\lambda_ {k}} y _ {k} := \arg \min _ {z \in \mathbf {R} ^ {n}} \left\{f (z) + \frac {1}{2 \lambda_ {k}} \left\| z - y _ {k} \right\| ^ {2} \right\},
$$

$$
x _ {k + 1} = \arg \min \left\{f (\bar {x} _ {k + 1}), f (x _ {k}) \right\},
$$

$$
\nu_ {k + 1} = \nu_ {k} + \frac {1}{\alpha_ {k}} \left(x _ {k + 1} - y _ {k}\right),
$$

$$
A _ {k + 1} = (1 - \alpha_ {k}) A _ {k}.
$$

It is easy to verify that the algorithm stated above possesses the same global convergence rate estimates as the original version in § 2. The statement and the properties of the algorithm of § 3 are similar.

The next result shows that the algorithms in this paper minimize $f$ in the case when $f$ has no minimizers or is even unbounded from below.

THEOREM 4.1. Suppose $f$ has no minimizers or is unbounded from below. The original proximal point algorithms in §§2 and 3, and their monotonic versions discussed above, minimize $f$, that is,

$$
\lim _ {k \to \infty} f (x _ {k}) = \inf _ {x \in \mathbf {R} ^ {n}} f (x). \tag {4.1}
$$

Proof. Since the algorithm in § 2 is a special case of the algorithm in § 3, we prove (4.1) only for the latter. The proofs of (4.1) for the monotonic versions are similar.

We first consider the case $f^{*} > -\infty$. Suppose $\varepsilon > 0$ is given. Let $x^{\varepsilon}$ be a point satisfying $f(x^{\varepsilon}) - f^{*} \leq \varepsilon / 2$. If $k$ is large enough, from (3.23) we obtain $f(x_{k}) - f(x^{\varepsilon}) \leq \varepsilon / 2$. Thus $f(x_{k}) - f^{*} \leq \varepsilon$, and (4.1) holds true.

If $f^{*} = -\infty$, let $M$ be an arbitrary number and $x^{M}$ be a point satisfying $f(x^{M}) \leq M$. If $k$ is large enough, from (3.23) we have $f(x_{k}) - f(x^{M}) \leq \varepsilon$. Thus $f(x_{k}) \leq M + \varepsilon$ and (4.1) holds true.

5. Concluding remarks. In this paper, we presented new proximal point algorithms for the convex minimization problem (1.1). We presented an exact minimization algorithm in § 2, and an inexact minimization algorithm in § 3. The algorithm in § 3 is important in practice, since the exact minimization of the auxiliary function that occurs at each step is impractical, and may in fact be almost as difficult to solve as the original minimization problem. We demonstrated the convergence of our algorithms and supplied global convergence rates for them. These rates are faster than the rates the author obtained [7] for the classical proximal point algorithm. Thus our algorithms accelerate the classical proximal point algorithm.

The algorithms developed here are general enough to solve the general convex program (1.4). When applied to the dual program (1.5), they give rise to the so-called augmented Lagrangian methods discussed in Bertsekas [2], Rockafellar [19], and others. In [8], the author applies the algorithm in § 2 to linear programming and obtains an algorithm that accelerates the augmented Lagrangian method of Polyak and Tret'iakov [15]. As is true of the algorithm of Polyak and Treti'akov [15], the application of the exact minimization algorithm in § 2 to linear programming terminates in finitely many iterations.

For simplicity's sake we have kept our discussion to finite-dimensional Euclidean spaces $\mathbf{R}^n$, however our results and algorithms are valid in any Hilbert space. Thus our algorithms may be applied to infinite-dimensional variational problems; see [4], [5], [6] and [10].

6. Appendix. Another proximal point algorithm. In this appendix, we present a second proximal point algorithm for problem (1.1). This algorithm uses ideas from Nesterov [13], where the first optimal algorithm for smooth convex programming is introduced.

The algorithm generates a sequence $\{x_{k}\}_{k=0}^{\infty}$ of approximations to an optimal point $x^{*}\in\mathbf{R}^{n}$ of problem (1.1), as well as an auxiliary sequence of points $\{y_{k}\}_{k=1}^{\infty}$.

THE SECOND PROXIMAL POINT ALGORITHM.

Initialization. Choose a point $x_0 \in \mathbb{R}^n$, and a constant $\lambda > 0$. Define $y_1 := x_0, \lambda_1 := \lambda$, and $\beta_1 := 1$.

Step $\mathbf{k}, k \geq 1$. Choose $\lambda_k \geq \lambda_{k-1}$ and define

$$
\beta_ {k + 1} = \frac {1 + \sqrt {1 + 4 \beta_ {k} ^ {2}}}{2}, \tag {6.1}
$$

$$
x _ {k} = J _ {\lambda_ {k}} y _ {k} := \arg \min _ {x \in \mathbf {R} ^ {n}} \left\{f (x) + \frac {1}{2 \lambda_ {k}} \left\| x - y _ {k} \right\| ^ {2} \right\}, \tag {6.2}
$$

$$
y _ {k + 1} = x _ {k} + \frac {\beta_ {k} - 1}{\beta_ {k + 1}} (x _ {k} - x _ {k - 1}) + \frac {\beta_ {k}}{\beta_ {k + 1}} (x _ {k} - y _ {k}). \tag {6.3}
$$

THEOREM 6.1. The proximal point algorithm stated above possesses the global convergence rate estimate

$$
f (x _ {k}) - \min _ {x \in \mathbf {R} ^ {n}} f (x) \leqslant \frac {1}{\lambda (k + 1) ^ {2}} \rho (x _ {0}, X ^ {*}) ^ {2}, \tag {6.4}
$$

where $X^{*}$ is the set of minimizers of $f$.

Proof. From (2.8) and (6.2), we have

$$
\frac {y _ {i + 1} - x _ {i + 1}}{\lambda_ {i + 1}} \in \partial f (x _ {i + 1}), \qquad i = 0, 1, \dots .
$$

Since $f$ is convex, we have

$$
f (x _ {i}) - f (x _ {i + 1}) \geqq \frac {1}{\lambda_ {i + 1}} \langle y _ {i + 1} - x _ {i + 1}, x _ {i} - x _ {i + 1} \rangle , \tag {6.5}
$$

$$
f (x ^ {*}) - f (x _ {i + 1}) \geqslant \frac {1}{\lambda_ {i + 1}} \langle y _ {i + 1} - x _ {i + 1}, x ^ {*} - x _ {i + 1} \rangle . \tag {6.6}
$$

Note that (6.1) implies

$$
\beta_ {i + 1} (\beta_ {i + 1} - 1) = \beta_ {i} ^ {2}. \tag {6.7}
$$

For brevity, we define $W_{i} := f(x_{i}) - f(x^{*})$. Multiplying (6.5) by $\beta_{i}^{2} = \beta_{i+1}(\beta_{i+1} - 1)$ and (6.6) by $\beta_{i+1}$, and using (6.7), we obtain

$$
\beta_ {i} ^ {2} (W _ {i} - W _ {i + 1}) \geqq \frac {1}{\lambda_ {i + 1}} \langle \beta_ {i + 1} (y _ {i + 1} - x _ {i + 1}), (\beta_ {i + 1} - 1) (x _ {i} - x _ {i + 1}) \rangle , \tag {6.8}
$$

$$
- \beta_ {i + 1} W _ {i + 1} \geqslant \frac {1}{\lambda_ {i + 1}} \langle \beta_ {i + 1} (y _ {i + 1} - x _ {i + 1}), x ^ {*} - x _ {i + 1} \rangle . \tag {6.9}
$$

Adding (6.8) and (6.9), and using (6.7), we obtain

$$
\beta_ {i} ^ {2} W _ {i} - \beta_ {i + 1} ^ {2} W _ {i + 1} \geqslant \frac {1}{\lambda_ {i + 1}} \langle \beta_ {i + 1} (y _ {i + 1} - x _ {i + 1}), \beta_ {i + 1} (x _ {i} - x _ {i + 1}) + x ^ {*} - x _ {i} \rangle . \tag {6.10}
$$

Using the polarization identity $4\langle x, y \rangle = \| x + y \|^2 - \| x - y \|^2$, the scalar product term in (6.10) can be expressed as

$$
\frac {1}{4} \| \beta_ {i + 1} (x _ {i} + y _ {i + 1} - 2 x _ {i + 1}) + x ^ {*} - x _ {i} \| ^ {2} - \frac {1}{4} \| \beta_ {i + 1} (x _ {i} - y _ {i + 1}) + x ^ {*} - x _ {i} \| ^ {2}. \tag {6.11}
$$

Let us define

$$
\theta_ {i} := \beta_ {i + 1} (x _ {i} - y _ {i + 1}) + x ^ {*} - x _ {i}, \quad i = 0, 1, \dots . \tag {6.12}
$$

Using (6.3), it is easy to show that

$$
\theta_ {i} = \beta_ {i} (x _ {i - 1} + y _ {i} - 2 x _ {i}) + x ^ {*} - x _ {i - 1}, \quad i = 1, 2, \dots . \tag {6.13}
$$

From (6.12) and (6.13), respectively, we see that the second term in (6.11) equals $\theta_{i}$ and the first term in (6.11) equals $\theta_{i+1}$. Using these facts and the fact that $\lambda_{i+1} \geq \lambda_{i}$ in (6.10), we obtain

$$
\beta_ {i} ^ {2} W _ {i} - \beta_ {i + 1} ^ {2} W _ {i + 1} \cong \frac {1}{4 \lambda_ {i + 1}} \left\| \theta_ {i + 1} \right\| ^ {2} - \frac {1}{4 \lambda_ {i}} \left\| \theta_ {i} \right\| ^ {2}. \tag {6.14}
$$

Summing (6.14) for $i=1,\ldots,k-1$, we obtain

$$
\beta_ {1} ^ {2} W _ {1} - \beta_ {k} ^ {2} W _ {k} \geq \frac {1}{4 \lambda_ {k}} \left\| \theta_ {k} \right\| ^ {2} - \frac {1}{4 \lambda_ {1}} \left\| \theta_ {1} \right\| ^ {2} \geq - \frac {1}{4 \lambda_ {1}} \left\| \theta_ {1} \right\| ^ {2}.
$$

Since $\lambda_{1} = \lambda$ and $\beta_{1} = 1$, we obtain from the last inequality,

$$
\beta_ {k} ^ {2} W _ {k} \leqq W _ {1} + \frac {1}{4 \lambda} \left\| \theta_ {1} \right\| ^ {2}. \tag {6.15}
$$

Using (6.6) with $i=0$, and noting $x_{0}=y_{1}$, we have

$$
\begin{aligned} - W _ {1} &\geq \frac {1}{\lambda} \left\langle y _ {1} - x _ {1}, x ^ {*} - x _ {1} \right\rangle \\ &= \frac {1}{4 \lambda} \left\| \theta_ {1} \right\| ^ {2} - \frac {1}{4 \lambda} \left\| x ^ {*} - x _ {0} \right\| ^ {2} \quad (\text {using (6.13)}). \\ \end{aligned}
$$

$$
= \frac {1}{4 \lambda} \left\| x ^ {*} + y _ {1} - 2 x _ {1} \right\| ^ {2} - \frac {1}{4 \lambda} \left\| x ^ {*} - x _ {0} \right\| ^ {2} \tag {6.16}
$$

Thus, from (6.15) and (6.16), we obtain

$$
\beta_ {k} ^ {2} W _ {k} \leqslant \frac {1}{4 \lambda} \left\| x _ {0} - x ^ {*} \right\| ^ {2}. \tag {6.17}
$$

It is easy to show by induction that $\beta_{k}\cong(k+1)/2$. Since $x^{*}\in X^{*}$ is arbitrary, the theorem follows from (6.17). ☐

Acknowledgments. The author is grateful to Dr. Nesterov for providing him with a copy of [14]. The author also thanks a referee for helpful remarks.

# REFERENCES

[1] J. P. AUBIN AND I. EKELAND, Applied Nonlinear Analysis, Interscience Publications, John Wiley, New York, 1984.  
[2] D. P. BERTSEKAS, Constrained Optimization and Lagrange Multiplier Methods, Academic Press, New York, 1982.  
[3] H. BRÉZIS AND P. L. LIONS, Produits infinis de résolvantes, Israel J. Math., 29 (1978), pp. 329-345.  
[4] M. FORTIN AND R. GLOWINSKI, Augmented Lagrangian Methods: Applications to Numerical Solutions of Boundary Value Problems, North-Holland, Amsterdam, 1983.  
[5] R. GLOWINSKI, Numerical Methods for Nonlinear Variational Problems, Springer-Verlag, New York, 1984.  
[6] R. GLOWINSKI, J. L. LIONS, AND R. TREMOLIERES, Numerical Analysis of Variational Inequalities, North-Holland, Amsterdam, 1981.  
[7] O. GÜLER, On the convergence of the proximal point algorithm for convex minimization, SIAM J. Control Optim., 29 (1991), pp. 403-419.  
[8] ——, Augmented Lagrangian algorithms for linear programming, Working Paper Series 91-3, Dept. of Management Sciences, The Univ. of Iowa, Iowa City, IA, 1991; J. Optim. Theory Appl., to appear.  
[9] M. R. HESTENES, Multiplier and gradient methods, J. Optim. Theory Appl., 4 (1969), pp. 303-320.  
[10] K. ITO AND K. KUNISCH, The augmented Lagrangian method for parameter estimation in elliptic systems, SIAM J. Control Optim., 28 (1990), pp. 113-136.  
[11] B. MARTINET, Regularisation, d'inéquations variationelles par approximations successives, Rev. Française d'Inform. Recherche Oper., 4 (1970), pp. 154–159.  
[12] J. J. MOREAU, Proximité et dualité dans un espace Hilbertien, Bull. Soc. Math. France, 93 (1965), pp. 273-299.  
[13] YU. E. NESTEROV, A method of solving a convex programming problem with convergence rate $O(1 / k^2)$, Dokl. Akad. Nauk, 269 (1983), pp. 543-547. (In Russian.) (Translated in Soviet Math. Dokl., 27 (1983), pp. 372-376.)  
[14] ——, On an approach to the construction of optimal methods of minimization of smooth convex functions, Ekonom. i Mat. Metody, 24 (1988), pp. 509–517.  
[15] B. T. POLYAK AND N. V. TRETIAKOV, An iterative method for linear programming and its economic interpretation, Ekonom. i Mat. Metody, 8 (1972), pp. 740–751. (In Russian.) (Translated in Matekon, 8 (1972), pp. 81–100.)  
[16] M. J. D. POWELL, A method for nonlinear constraints in minimization problems, in Optimization, R. Fletcher, ed., Academic Press, New York, 1969, pp. 283–298.  
[17] R. T. ROCKAFELLAR, Convex Analysis, Princeton University Press, Princeton, NJ, 1970.  
[18] ——, Monotone operators and the proximal point algorithm, SIAM J. Control Optim., 14 (1976), pp. 877-898.  
[19] ——, Augmented Lagrangians and applications of the proximal point algorithm in convex programming, Math. Oper. Res., 1 (1976), pp. 97-116.
