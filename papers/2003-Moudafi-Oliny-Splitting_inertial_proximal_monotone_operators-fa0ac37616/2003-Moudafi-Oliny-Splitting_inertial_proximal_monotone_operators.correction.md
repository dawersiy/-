# Convergence of a splitting inertial proximal method for monotone operators

A. Moudafi*, M. Oliny

Université Antilles Guyane, DSI-GRIMAAG, 97200 Schoelcher, Martinique, France

Received 27 March 2002

# Abstract

A forward–backward inertial procedure for solving the problem of finding a zero of the sum of two maximal monotone operators is proposed and its convergence is established under a cocoercivity condition with respect to the solution set.

© 2003 Elsevier Science B.V. All rights reserved.

Keywords: Monotone operators; Enlargements; Proximal point algorithm; Cocoercivity; Splitting algorithm; Projection; Convergence

# 1. Introduction and preliminaries

The theory of maximal monotone operators has emerged as an effective and powerful tool for studying a wide class of unrelated problems arising in various branches of social, physical, engineering, pure and applied sciences in unified and general framework. In recent years, much attention has been given to develop efficient and implementable numerical methods including the projection method and its variant forms, auxiliary problem principle, proximal-point algorithm and descent framework for solving variational inequalities and related optimization problems. It is well known that the projection method and its variant forms cannot be used to suggest and analyze iterative methods for solving variational inequalities due to the presence of the nonlinear term. This fact motivated to develop another technique, which involves the use of the resolvent operator associated with maximal monotone operators, the origin of which can be traced back to Martinet [13] in the context of convex minimization and Rockafellar [19] in the general setting of maximal monotone operators. The resulting method, namely the proximal point algorithm has been extended and

generalized in different directions by using novel and innovative techniques and ideas, both for their own sake and for their applications relying, for example, on Bregman distance. Since, in general, it is difficult to evaluate the resolvent operator. One alternative is to decompose the given operator into the sum of two (or more) maximal monotone operators whose resolvent are easier to evaluate than the resolvent of the original one. Such a method is known as the operator splitting method. This can lead to the development of very efficient methods, since one can treat each part of the original operator independently. The operator splitting methods and related techniques have been analyzed and studied by many authors including Eckstein and Bertsekas [8], Chen and Rockafellar [6], Zhu and Marcotte [25], Tseng [24] and Moudafi and Théra [15]. For an excellent account of the splitting methods, see [7]. Here, we use the resolvent operator technique to suggest a forward-backward splitting method for solving the problem of finding a zero of the sum of two maximal monotone operators. It is worth mentioning that if the nonlinear term involving the variational inequalities is the indicator function of a closed convex set in a Hilbert space, then the resolvent operator is equal to the projection operator and we recover a method proposed by Antipin [3]. Our result extends and generalizes the previously known results.

In this paper we will focus our attention on the classical problem of finding a zero of the sum of two maximal monotone operators $A$ and $B$ on a real Hilbert space $\mathcal{H}$ :

$$
\text {find} x \in \mathscr {H} \quad \text {such that} (A + B) (x) \ni 0. \tag {1.1}
$$

This is a well-known problem which includes, as special cases, optimization and min–max problems, complementarity problems, and variational inequalities.

One of the fundamental approaches to solving (1.1), where $B$ is univoque, is the forward-backward method, which generates the next iterates $x_{k+1}$ by solving the subproblem

$$
0 \in \lambda_ {k} A (x) + (x - x _ {k} + \lambda_ {k} B (x _ {k})), \tag {1.2}
$$

where $x_{k}$ is the current iterate and $\lambda_{k}$ is a regularization parameter. The literature on this subject is vast (see [7] and references therein). Actually, this method was proposed by Lions and Mercier [12], Passty [17] and, in a dual form for convex programming, by Han and Lou [10]. In the case where A is the normal cone of a nonempty closed convex set, this method reduces to a projection method proposed by Sibony [20] for monotone variational inequalities and, in the further case where B is the gradient of a differentiable convex function, it amounts to a gradient projection method of Goldstein and of Levintin and Polyak [5]. This method was largely analyzed by Mercier [14] and Gabay [9]. They namely showed that if B is cocoercive with modulus $\gamma > 0$, then the iterates $x_{k}$ converge weakly to a solution on condition that $\lambda_{k}$ is constant and less than $2\gamma$. The case where $\lambda_{k}$ is nonconstant was dealt with among others in [6,8,15,23,24].

Recently, an inertial proximal algorithm was proposed by Alvarez in the context of convex minimization in [1]. Afterwards, Attouch and Alvarez considered its extension to maximal monotone operators [2]. Relying on this method, we propose a splitting procedure which works as follows. Given $x_{k-1}, x_k \in \mathcal{H}$ and two parameters $\alpha_k \in [0, 1[$ and $\lambda_k > 0$, find $x_{k+1} \in \mathcal{H}$ such that

$$
\lambda_ {k} A (x _ {k + 1}) + x _ {k + 1} - x _ {k} - \alpha_ {k} (x _ {k} - x _ {k - 1}) + \lambda_ {k} B (x _ {k}) \ni 0. \tag {1.3}
$$

When $B = 0$, the inspiration for (1.3) comes from the implicit discretization of the differential system of the second-order in time, namely

$$
\frac {\mathrm{d} ^ {2} x}{\mathrm{d} t ^ {2}} (t) + \gamma \frac {\mathrm{d} x}{\mathrm{d} t} (t) + A (x (t)) \ni 0 \quad \text {a.e.} t \geqslant 0, \tag {1.4}
$$

where $\gamma > 0$ is a damping or a friction parameter.

When $\mathcal{H} = \mathbb{R}^2$, $A$ is the gradient of a differentiable function, (1.4) is a simplified version of the differential system which describes the motion of a heavy ball rolling over the graph of $f$ and which keeps rolling under its own inertia until stopped by friction at a critical point of $f$ (see [4]). This nonlinear oscillator with damping has been considered by several authors proving different results and/or identifying situations in which the rate of convergence of (1.4) or its discrete versions is better than those of the first-order steepest descent method see [1,11,18]. Roughly speaking the second-order nature of (1.3) (respectively (1.4)) may be exploited in some situations in order to accelerate the convergence of the sequence of (1.3) (respectively the trajectories of (1.4)), see [11] where numerical simulations comparing the behavior of the standard proximal algorithm, the gradient method and the inertial proximal one are presented (for the continuous version see for example [4]).

For developing implementable computational techniques, it is of particular importance to treat the case when (1.3) is solved approximately. Before introducing our approximate method, let us recall the following concepts which are of common use in the context of convex and nonlinear analysis. Throughout, $\mathcal{H}$ is a real Hilbert space, $\langle \cdot ,\cdot \rangle$ denotes the associated scalar product and $|\cdot |$ stands for the corresponding norm. An operator is said to be monotone if

$$
\langle u - v, x - y \rangle \geqslant 0 \quad \text { whenever } u \in T (x), v \in T (y).
$$

It is said to be maximal monotone if, in addition, the graph, $\{(x,y)\in\mathcal{H}\times\mathcal{H}:y\in T(x)\}$, is not properly contained in the graph of any other monotone operator. It is well-known that for each $x\in\mathcal{H}$ and $\lambda>0$ there is a unique $z\in\mathcal{H}$ such that $x\in(I+\lambda T)z$. The single-valued operator $J_{\lambda}^{T}:=(I+\lambda T)^{-1}$ is called the resolvent of $T$ of parameter $\lambda$. It is a nonexpansive mapping which is everywhere defined and satisfies: $z=J_{\lambda}^{T}z$, if and only if, $0\in Tz$. Let us also recall a notion which is clearly inspired by the approximate subdifferential. In [21,22], Iusem, Burachik and Svaiter defined $T^{\varepsilon}(x)$, an $\varepsilon$ -enlargement of a monotone operator $T$, as

$$
T ^ {\varepsilon} (x) := \{v \in \mathscr {H}; \langle u - v, y - x \rangle \geqslant - \varepsilon \quad \forall y, u \in T (y) \}, \tag {1.5}
$$

where $\varepsilon \geqslant 0$. Since $T$ is assumed to be maximal monotone, $T^0(x) = T(x)$, for any $x$. Furthermore, directly from the definition it follows that

$$
0 \leqslant \varepsilon_ {1} \leqslant \varepsilon_ {2} \Rightarrow T ^ {\varepsilon_ {1}} (x) \subset T ^ {\varepsilon_ {2}} (x).
$$

Thus $T^{\varepsilon}$ is an enlargement of $T$. The use of elements in $T^{\varepsilon}$ instead of $T$ allows an extra degree of freedom, which is very useful in various applications. On the other hand, setting $\varepsilon = 0$ one retrieves the original operator $T$, so that the classical method can be also treated. For all these reasons, we consider the following scheme: find $x_{k+1} \in \mathcal{H}$ such that

$$
\lambda_ {k} A ^ {\varepsilon_ {k}} (x _ {k + 1}) + x _ {k + 1} - y _ {k} + \lambda_ {k} B (x _ {k}) \ni 0, \tag {1.6}
$$

where $y_{k} := x_{k} + \alpha_{k}(x_{k} - x_{k-1}), \lambda_{k}, \alpha_{k}, \varepsilon_{k}$ are nonnegative real numbers.

If $A$ is the subdifferential of the indicator function of a closed convex set $C$, then (1.1) reduces to the classical variational inequality

$$
\langle B (x), y - x \rangle \geqslant 0 \quad \forall y \in C \tag {1.7}
$$

and the resolvent operator is nothing but the projection operator. Moreover, in the case where $\varepsilon_{k} = 0\forall k$ and $B$ is the gradient of a function $f$, (1.7) reduces in turn to the constrained minimization problem $\operatorname{Min}_{x\in C}f(x)$ and we recover a method proposed in [3], namely

$$
x _ {k + 1} = \mathrm{proj} _ {C} (x _ {k} - \lambda \nabla f (x _ {k}) + \alpha (x _ {k} - x _ {k - 1})).
$$

Another interesting case is obtained by taking $B = 0$ and $A = \partial f$, $\partial f$ stands for the subdifferential of a proper convex lower-semicontinuous function $f: \mathcal{H} \to \mathbb{R} \cup \{+\infty\}$. Indeed, $\partial f$ is well-known to be a maximal monotone operator and problem (1.1) reduces to the one of finding a minimizer of the function $f$.

In [1], Alvarez proposed the following approximate inertial proximal method:

$$
\lambda_ {k} \partial_ {\varepsilon_ {k}} f (x _ {k + 1}) + x _ {k + 1} - x _ {k} - \alpha_ {k} (x _ {k} - x _ {k - 1}) \ni 0, \tag {1.8}
$$

where $\partial_{\varepsilon_k}f$ is the approximate subdifferential of $f$. Since in the case $A = \partial f$ the enlargement given in (1.5) is larger than the approximate subdifferential, i.e. $\partial_{\varepsilon}f \subset (\partial f)^{\varepsilon}$ (see [21,22]), we can write $\partial_{\varepsilon_k}f(x_{k+1}) \subset (\partial f)^{\varepsilon_k}(x_{k+1})$, which leads to

$$
\lambda_ {k} (\partial f) ^ {\varepsilon_ {k}} (x _ {k + 1}) + x _ {k + 1} - x _ {k} - \alpha_ {k} (x _ {k} - x _ {k - 1}) \ni 0, \tag {1.9}
$$

which is a particular case of the method proposed in this paper with $A = \partial f$ and B = 0.

In the sequel, we will need a cocoercivity condition with respect to the solution set, $S := (A + B)^{-1}(0)$, namely

$$
\langle B (x) - B (y), x - y \rangle \geqslant \gamma | B (x) - B (y) | ^ {2} \quad \forall x \in \mathscr {H} \forall y \in S,
$$

$\gamma$ being a positive real number. This condition is standard in the literature and is typically needed to establish weak convergence (see for example [8,9,15,25]).

# 2. The main results

To begin with let us recall, for the convenience of the reader, a well-known result on weak convergence.

Lemma 2.1 (Opial [16]). Let $\mathcal{H}$ be a Hilbert space and $\{x_k\}$ a sequence such that there exists a nonempty set $S \subset \mathcal{H}$ verifying:

- For every $\bar{x} \in S$, $\lim_{k \to +\infty} |x_k - \bar{x}|$ exists.  
- If $x_v$ weakly converges to $x \in \mathscr{H}$ for a subsequence $v \to +\infty$, then $x \in S$.

Then, there exists $\tilde{x} \in S$ such that $\{x_k\}$ weakly converges to $\tilde{x}$ in $\mathscr{H}$.

We are now able to give our main result.

Theorem 2.1. Let $\{x_k\} \subset \mathcal{H}$ be a sequence generated by (1.6), where $A, B$ are two maximal monotone operators with $B$ $\gamma$-cocoercive and suppose that the parameters $\alpha_k, \lambda_k$ and $\varepsilon_k$ satisfy:

1. $\exists \varepsilon \exists \lambda > 0$ such that $\forall k \in \mathbb{N}^*, \lambda \leqslant \lambda_k \leqslant 2\gamma - \varepsilon$.  
2. $\exists \alpha \in [0,1[$ such that $\forall k\in \mathbb{N}^*$, $0\leqslant \alpha_{k}\leqslant \alpha$.  
3. $\sum_{k=1}^{+\infty}\varepsilon_{k}<+\infty.$

If the following condition holds

$$
\sum_ {k = 1} ^ {+ \infty} \alpha_ {k} | x _ {k} - x _ {k - 1} | ^ {2} <   + \infty , \tag {2.10}
$$

then, there exists $\bar{x} \in S$ such that $\{x_k\}$ weakly converges to $\bar{x}$ as $k \to +\infty$.

Proof. Fix $x \in S = T^{-1}(0)$ and set $\varphi_k = \frac{1}{2} |x - x_k|^2$. We have

$$
\varphi_ {k} - \varphi_ {k + 1} = \frac {1}{2} | x _ {k + 1} - x _ {k} | ^ {2} + \langle x _ {k + 1} - y _ {k}, x - x _ {k + 1} \rangle + \alpha_ {k} \langle x _ {k} - x _ {k - 1}, x - x _ {k + 1} \rangle , \tag {2.11}
$$

where $y_{k} := x_{k} + \alpha_{k}(x_{k} - x_{k-1})$. Since $-x_{k+1} + y_{k} - \lambda_{k}B(x_{k}) \in \lambda_{k}A^{\varepsilon_{k}}(x_{k+1})$ and $-\lambda_{k}B(x) \in \lambda_{k}A(x)$, from definition (1.5) it follows that

$$
\langle x _ {k + 1} - y _ {k} + \lambda_ {k} (B (x _ {k}) - B (x)), x - x _ {k + 1} \rangle \geqslant - \lambda_ {k} \varepsilon_ {k}. \tag {2.12}
$$

Combining (2.11) and (2.12), we obtain

$$
\varphi_ {k} - \varphi_ {k + 1} \geqslant \frac {1}{2} \left| x _ {k + 1} - x _ {k} \right| ^ {2} + \lambda_ {k} \langle B (x _ {k}) - B (x), x _ {k + 1} - x \rangle - \alpha_ {k} \langle x _ {k} - x _ {k - 1}, x _ {k + 1} - x \rangle - \lambda_ {k} \varepsilon_ {k}.
$$

By invoking the equality

$$
\begin{aligned} \langle x _ {k} - x _ {k - 1}, x _ {k + 1} - x \rangle &= \langle x _ {k} - x _ {k - 1}, x _ {k} - x \rangle + \langle x _ {k} - x _ {k - 1}, x _ {k + 1} - x _ {k} \rangle \\ &= \varphi_ {k} - \varphi_ {k - 1} + \frac {1}{2} | x _ {k} - x _ {k - 1} | ^ {2} + \langle x _ {k} - x _ {k - 1}, x _ {k + 1} - x _ {k} \rangle , \\ \end{aligned}
$$

it follows that

$$
\begin{aligned} \varphi_ {k + 1} - \varphi_ {k} - \alpha_ {k} (\varphi_ {k} - \varphi_ {k - 1}) &\leqslant - \frac {1}{2} | x _ {k + 1} - x _ {k} | ^ {2} + \alpha_ {k} \langle x _ {k} - x _ {k - 1}, x _ {k + 1} - x _ {k} \rangle \\ + \frac {\alpha_ {k}}{2} | x _ {k} - x _ {k - 1} | ^ {2} - \lambda_ {k} \big \langle B (x _ {k}) - B (x), x _ {k + 1} - x \big \rangle + \lambda_ {k} \varepsilon_ {k}. \\ \end{aligned}
$$

On the other hand, since B is cocoercive, we get

$$
\begin{aligned} \lambda_ {k} \big \langle B (x _ {k}) - B (x), x _ {k + 1} - x \big \rangle \\ &= \lambda_ {k} (\langle B (x _ {k}) - B (x), x _ {k} - x \rangle + \langle B (x _ {k}) - B (x), x _ {k + 1} - x \rangle) \\ &\geqslant \lambda_ {k} (\gamma | B (x _ {k}) - B (x) | ^ {2} + \langle B (x _ {k}) - B (x), x _ {k + 1} - x _ {k} \rangle) \geqslant - \frac {\lambda_ {k}}{4 \gamma} | x _ {k + 1} - x _ {k} | ^ {2}. \\ \end{aligned}
$$

From which infer, by setting $\beta_{k} := 1 - \lambda_{k}/2\gamma$, the estimate (2.13) below

$$
\begin{array}{l} \varphi_ {k + 1} - \varphi_ {k} - \alpha_ {k} (\varphi_ {k} - \varphi_ {k - 1}) \\ \leqslant - \frac {1}{2} \beta_ {k} | x _ {k + 1} - x _ {k} | ^ {2} + \alpha_ {k} \langle x _ {k} - x _ {k - 1}, x _ {k + 1} - x _ {k} \rangle + \frac {\alpha_ {k}}{2} | x _ {k} - x _ {k - 1} | ^ {2} + \lambda_ {k} \varepsilon_ {k} \\ \leqslant - \frac {1}{2} \beta_ {k} \left| x _ {k + 1} - \frac {\alpha_ {k}}{\beta_ {k}} y _ {k} \right| ^ {2} + \frac {\alpha_ {k} ^ {2}}{2 \beta_ {k}} | x _ {k} - x _ {k - 1} | ^ {2} + \frac {\alpha_ {k}}{2} | x _ {k} - x _ {k - 1} | ^ {2} + \lambda_ {k} \varepsilon_ {k} \\ \leqslant - \frac {1}{2} \beta_ {k} \left| x _ {k + 1} - x _ {k} - \frac {\alpha_ {k}}{\beta_ {k}} (x _ {k} - x _ {k - 1}) \right| ^ {2} + \frac {\alpha_ {k}}{\beta_ {k}} | x _ {k} - x _ {k - 1} | ^ {2} + \lambda_ {k} \varepsilon_ {k}. \\ \end{array}
$$

By taking into account the fact that from the hypotheses $\beta_{k}$ is bounded and by setting $\theta_{k} := \varphi_{k} - \varphi_{k-1}$ and $\delta_{k} := 2\gamma\alpha_{k}/\varepsilon|x_{k} - x_{k-1}|^{2} + \lambda_{k}\varepsilon_{k}$, we obtain

$$
\theta_ {k + 1} \leqslant \alpha_ {k} \theta_ {k} + \delta_ {k} \leqslant \alpha_ {k} [ \theta_ {k} ] _ {+} + \delta_ {k},
$$

where $[t]_{+} := \max(t, 0)$, and consequently

$$
[ \theta_ {k + 1} ] _ {+} \leqslant \alpha [ \theta_ {k} ] _ {+} + \delta_ {k}
$$

with $\alpha \in [0,1[$ given by hypothesis 2.

The latter inequality yields

$$
[ \theta_ {k + 1} ] _ {+} \leqslant \alpha^ {k} [ \theta_ {1} ] _ {+} + \sum_ {i = 0} ^ {k - 1} \alpha^ {i} \delta_ {k - i}
$$

and therefore

$$
\sum_ {k = 1} ^ {\infty} [ \theta_ {k + 1} ] _ {\leqslant} \frac {1}{1 - \alpha} \left([ \theta_ {1} ] _ {+} + \sum_ {k = 1} ^ {\infty} \delta_ {k}\right),
$$

which is finite thanks to hypothesis 3 and (2.10). Consider the sequence defined by $t_k := \varphi_k - \sum_{i=1}^{k} [\theta_i]_+$. Since $\varphi_k \geqslant 0$ and $\sum_{i=1}^{k} [\theta_i]_+ < +\infty$, it follows that $t_k$ is bounded from below. But

$$
t _ {k + 1} = \varphi_ {k + 1} - [ \theta_ {k + 1} ] _ {+} - \sum_ {i = 1} ^ {k} [ \theta_ {i} ] _ {+} \leqslant \varphi_ {k + 1} - \varphi_ {k + 1} + \varphi_ {k} - \sum_ {i = 1} ^ {k} [ \theta_ {i} ] _ {+} = t _ {k},
$$

so that $\{t_k\}$ is nonincreasing. We thus deduce that $\{t_k\}$ is convergent and so is $\{\varphi_k\}$. This shows that the first condition of Opial's lemma is satisfied.

On the other hand, from (2.13) we can write

$$
\frac {1}{2} \beta_ {k} \left| x _ {k + 1} - x _ {k} - \frac {\alpha_ {k}}{\beta_ {k}} (x _ {k} - x _ {k - 1}) \right| ^ {2} \leqslant - \theta_ {k + 1} + \alpha \theta_ {k} + \delta_ {k}.
$$

By passing to the limit in the above estimate and by taking into account the conditions on the parameters and the fact that by hypothesis $|x_{k} - x_{k-1}| \to 0$, we obtain

$$
\lim _ {k \to + \infty} | x _ {k + 1} - x _ {k} - \alpha_ {k} (x _ {k} - x _ {k - 1}) | = 0.
$$

Now let $\bar{x}$ be a weak cluster point of $\{x_k\}$. There exists a subsequence $\{x_v\}$ which converges weakly to $\bar{x}$ and satisfies, thanks to (1.6),

$$
- \frac {1}{\lambda_ {v}} (x _ {v + 1} - y _ {v}) + (B (x _ {v + 1}) - B (x _ {v})) \in A ^ {\varepsilon_ {v + 1}} (x _ {v + 1}) + B (x _ {v + 1}) \subset (A + B) ^ {\varepsilon_ {v + 1}} (x _ {v + 1}).
$$

Passing to the limit, as $v \to +\infty$, using the fact that $B$ is Lipschitz continuous and thanks to the properties of the enlargements [22, Proposition 3.4], we obtain that $0 \in (A + B)(\bar{x})$, that is $\bar{x} \in S$. Thus, the second condition of Opial's lemma is also satisfied, which completes the proof.

Remark 2.1. An open problem is to investigate, theoretically as well as numerically, which are the best choices for the inertial parameter $\alpha_{k}$ in order to accelerate the convergence.

Condition (2.13) involves the iterates that are a priori unknown, in practice it is easy to enforce it by applying an appropriate on-line rule (for example, choosing $\alpha_{k} \in [0, \bar{\alpha}_{k}]$ with $\bar{\alpha}_{k} := \min\{\alpha, 1/(k|x_{k} - x_{k-1}|)^{2}\}$. Furthermore, it is worth mentioning that (2.13) is automatically satisfied in some special cases. For instance where Assumption 2) of Theorem 2.1 is replaced by $\exists \alpha \in [0, \frac{1}{3}, [\forall k \in \mathbb{N}, 0 \leqslant \alpha_{k} \leqslant \alpha$ and the sequence $\{\alpha_{k}\}$ is nondecreasing (see [2, Proposition 2.1]).

# 3. Conclusion

Our result extends classical convergence results concerning the standard forward-backward method as well as Theorem 6 of Antipin [3].

# Acknowledgements

The authors are grateful to the two anonymous referees and to Professor P.B. Monk for their valuable comments and remarks.

# References

[1] F. Alvarez, On the minimizing property of a second order dissipative system in Hilbert space, SIAM J. Control Optim. 38 (4) (2000) 1102–1119.

[2] F. Alvarez, H. Attouch, An inertial proximal method for maximal monotone operators via discretization of a nonlinear oscillator with damping, Set Valued Anal. 9 (2001) 3–11.  
[3] A.S. Antipin, Continuous and iterative process with projection operators and projection-like operators, Voprosy Kibernetiki. Vychislitel'nye Voprosy Analiza Bol'shikh Sistem, AN SSSR, Scientific Counsel on the Complex Problem "Cybernetics", Moscow, 1989, pp. 5–43.  
[4] H. Attouch, X. Goudou, P. Redont, The heavy ball with friction. I. The continuous dynamical system, Comm. Contemp. Math. 2 (1) (2000) 1–34.  
[5] D.P. Bertsekas, Constrained Optimization and Lagrange Multiplier Methods, Academic Press, New York, 1982.  
[6] H.-G. Chen, R.T. Rockafellar, Convergence rates in forward-backward splitting, SIAM J. Optim. 7 (1997) 421–444.  
[7] J. Ekstein, Splitting methods for monotone operators with application to parallel optimization, Dissertation, Massachusetts Institute of Technology, 1989.  
[8] J. Ekstein, D.P. Bertsekas, On the Douglas-Rachford splitting method and the proximal point algorithm for maximal monotone operators, Math. Programming 55 (1992) 293–318.  
[9] D. Gabay, Applications of the method of multipliers to variational inequalities, in: M. Fortin, R. Glowinski (Eds.), Augmented Lagrangian Methods: Applications to the numerical solution of Boundary Value Problems, North-Holland, Amsterdam, 1983, pp. 299–331.  
[10] S.P. Han, G. Lou, A parallel algorithm for a class of convex programs, SIAM J. Control Optim. 26 (1988) 345–355.  
[11] F. Jules, P.E. Maingé, Numerical approach to a stationary solution of a second order dissipative dynamical system, Optimization, to appear.  
[12] P.L. Lions, B. Mercier, Splitting algorithms for the sum of two nonlinear operators, SIAM J. Numer. Anal. 16 (1979) 964–979.  
[13] B. Martinet, Régularisation d'inéquations variationnelles par approximations successives, Rev. Francaise Inf. Rech. Oper. R-3 (1970) 154–159.  
[14] B. Mercier, Inéquations variationnelles de la mécanique, Pub. Math. Orsay, 80.01, Université de Paris-Sud, Orsay, 1980.  
[15] A. Moudafi, M. Théra, Finding a zero of the sum of two maximal monotone operators, J. Optim. Theory Appl. 94 (1997) 425–448.  
[16] Z. Opial, Weak convergence of the sequence of successive approximations for nonexpansive mappings, Bull. Amer. Math. Soc. 73 (1967) 591–597.  
[17] G.B. Passty, Ergodic convergence to a zero of the sum of monotone operators in Hilbert spaces, J. Math. Anal. Appl. 72 (1979) 383–390.  
[18] B.T. Polyak, Some methods of speeding up the convergence of iterative methods, Zh. Vychisl. Mat. Mat. Fiz. 4 (1964) 1–17.  
[19] R.T. Rockafellar, Monotone operator and the proximal point algorithm, SIAM J. Control. Opt. 14 (5) (1976) 877–898.  
[20] M. Sibony, Méthodes itératives pour les équations et inéquations non linéaires de type monotone, Calcolo 7 (1970) 65–183.  
[21] B.F. Svaiter, R.S. Burachik, A.N. Iusem, Enlargement of maximal monotone operators with application to variational inequalities, Set-Valued Anal. 5 (1997) 159–180.  
[22] B.F. Svaiter, R.S. Burachik, $\varepsilon$-enlargements of maximal monotone operators in Banach spaces, Set-Valued Anal. 7 (1999) 117–132.  
[23] P. Tseng, Further applications of a splitting algorithm to decomposition in variational inequalities and convex programming, Math. Programming 48 (1990) 249–263.  
[24] P. Tseng, Applications of a splitting algorithm to decomposition in convex programming and variational inequalities, SIAM J. Control Optim. 29 (1991) 119–138.  
[25] D.L. Zhu, P. Marcotte, Co-coercivity and its role in the convergence of iterative schemes for solving variational inequalities, SIAM J. Optim. 9 (3) (1996) 714–726.
