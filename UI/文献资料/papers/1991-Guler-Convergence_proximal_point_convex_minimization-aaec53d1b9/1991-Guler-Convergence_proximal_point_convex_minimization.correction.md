# ON THE CONVERGENCE OF THE PROXIMAL POINT ALGORITHM FOR CONVEX MINIMIZATION*

OSMAN GÜLER†

Abstract. The proximal point algorithm (PPA) for the convex minimization problem $\min_{x\in H}f(x)$ , where $f\colon H\to \mathbf{R}\cup\{\infty\}$ is a proper, lower semicontinuous (lsc) function in a Hilbert space H is considered. Under this minimal assumption on f, it is proved that the PPA, with positive parameters $\{\lambda_{k}\}_{k=1}^{\infty}$, converges in general if and only if $\sigma_{n}=\sum_{k=1}^{n}\lambda_{k}\to\infty$. Global convergence rate estimates for the residual $f(x_{n})-f(u)$, where $x_{n}$ is the nth iterate of the PPA and $u\in H$ is arbitrary are given. An open question of Rockafellar is settled by giving an example of a PPA for which $x_{n}$ converges weakly but not strongly to a minimizer of f.

Key words. proximal point algorithm, convex programming, strong convergence

AMS(MOS) subject classifications. primary 90C25; secondary 49D45, 49D37

1. Introduction. Let $H$ be a real Hilbert space. We consider the minimization problem

$$
\min _ {x \in H} f (x), \tag {1.1}
$$

where $f: H \to \mathbf{R} \cup \{\infty\}$ is a proper, lower semicontinuous (lsc) convex function, where we follow the terminology established in Aubin and Ekeland [1] or Rockafellar [16]. Many convex programming problems with or without constraints can be reduced to (1.1).

One method for solving (1.1) is the proximal point algorithm (PPA) first introduced by Martinet [10]. The PPA is based on the notion of proximal mapping $J_{\lambda}$,

$$
J _ {\lambda} (x) = x _ {\lambda} = \underset {z \in H} {\arg \min} \left\{f (z) + \frac {1}{2 \lambda} \| z - x \| ^ {2} \right\}, \tag {1.2}
$$

introduced by Moreau [12]. The PPA is an iterative procedure, which starts at a point $x_{0} \in H$ , and generates recursively a sequence of points $x_{k+1} = J_{\lambda_{k+1}}(x_{k})$ , where $\{\lambda_{k}\}_{k=1}^{\infty}$ is a sequence of positive numbers.

It turns out that a proximal mapping can be defined for an arbitrary maximal monotone operator $A: H \to H$. Recall that a multivalued mapping $A: H \to H$ is said to be a monotone operator if $w' \in A(x')$ and $w \in A(x)$ imply $\langle w' - w, x' - x \rangle \geq 0$. Clearly, if $A$ is a monotone operator, then

$$
w \in A (x), w' \in A (x') \Rightarrow \| (x' + w') - (x + w) \| ^ {2} \tag {1.3}
$$

$$
\geq \left\| x' - x \right\| ^ {2} + \left\| w' - w \right\| ^ {2};
$$

in particular

$$
x' \neq x \Rightarrow (I + A) (x) \cap (I + A) (x') = \emptyset . \tag {1.4}
$$

A monotone operator $A$ is said to be maximal monotone if the graph $G(A) = \{(w, x) \in H \times H \mid w \in A(x)\}$ is not properly contained in the graph of any other monotone operator $A': H \to H$. A solution to $A$ is a point $x^* \in H$ such that $0 \in A(x^*)$.

Many problems that involve convexity can be formulated as finding the solution of a maximal monotone operator. For example, convex minimization, concave-convex

saddle-point problems, and solutions of games can be formulated in this way. In particular, the subdifferential $A = \partial f$ is a maximal monotone operator, and a point $x^{*} \in H$ minimizes $f$ if and only if $0 \in \partial f(x^{*})$. The classical result of Minty [11] states that a monotone operator $A$ is maximal if and only if $I + A$ is surjective. If $A$ is a maximal monotone operator and $\lambda > 0$, the operator $J_{\lambda}$, defined by $J_{\lambda}(x) = (I + \lambda A)^{-1}(x)$, is called the resolvent of $A$. It follows from (1.4) that the resolvent $J_{\lambda}$ is a single-valued operator on $H$. Moreover, (1.3) implies that $J_{\lambda}$ is nonexpansive: that is, if $x, y \in H$, $\| J_{\lambda}(y) - J_{\lambda}(x) \| \leq \| y - x \|$. Also, the Yosida approximation $A_{\lambda}$, $A_{\lambda}(x) = (x - J_{\lambda}(x)) / \lambda$, is Lipschitz continuous with constant $1 / \lambda$. That is, for $x, y \in H$, $\| A_{\lambda}(y) - A_{\lambda}(x) \| \leq \| y - x \| / \lambda$.

The PPA for a maximal monotone operator is an iterative procedure that starts at a point $x_0 \in H$, and generates recursively a sequence of points $x_{k+1} = J_{\lambda_{k+1}}(x_k)$, where $\{\lambda_k\}_{k=1}^{\infty}$ is a sequence of positive numbers. It is treated in the papers [4], [7], [10], [17], and [18]. The important paper of Brézis and Lions [4] contains many interesting results. Rockafellar [18] shows how the PPA can be applied in convex programming. We stress that when $A = \partial f$, the PPA described here reduces to the iteration described above in the context of (1.1).

Notation. We use the following notation in the paper. If $f$ is a proper, lsc convex function on $H$, the effective domain of $f$ is the set $\{x \in H : f(x) < \infty\}$, which we denote by $D(f)$. We will sometimes refer to lsc convex functions as closed functions. The infimum of $f$ is denoted by $f^* = \inf_{x \in H} f(x)$, and the set of minimizers of $f$ (possibly empty) is denoted by $X^* = \{x \in H : f(x) = f^*\}$. If $A : H \to H$ is a multivalued operator, the domain of $A$ is the set $D(A) = \{x \in H : A(x) \neq \emptyset\}$, and the range of $A$ is the set $R(A) = \bigcup \{A(x) : x \in D(A)\}$. If the sequence $\{\lambda_k\}_{k=1}^{\infty}$ of positive numbers lists the proximal parameters, we define $\sigma_n = \sum_{k=1}^{n} \lambda_k$. By convention $\sigma_0 = 0$. If the sequence $\{x_k\}_{k=0}^{\infty}$ is the trajectory of a PPA, we will write $y_k \equiv A_{\lambda_k}(x_{k-1}) = (x_{k-1} - x_k)/\lambda_k$. We use $J_\lambda(x)$ and $x_\lambda$ interchangeably. If $A$ is maximal monotone then $A(x)$ is closed and convex (see Aubin and Ekeland [1, Prop. 3, §6.7]. In this case, if $A(x) \neq \emptyset$, we denote the least norm element of $A(x)$ by $A^0 x$. For any set $S \subseteq H$, we define the distance function $\rho(x, S) = \inf \{ \| x - s \| : s \in S\}$.

Every maximal monotone operator engenders a nonlinear contractive semigroup $\{S(t): t \geq 0\}$ of maps $S(t): \overline{D(A)} \to \overline{D(A)}$, satisfying the following properties for $t, s \geq 0$ and $x, y \in \overline{D(A)}$ :

(i) $S(0)x = x,$  
(ii) $S(t + s)x = S(t)S(s)x$ (semigroup property), and  
(iii) $\| S(t)x - S(t)y\| \leq \| x - y\|$.

Indeed, $S(t)x = u(t)$, where $u(t)$ is the unique solution to the differential inclusion

$$
\frac {d u}{d t} \in - A u (t), \quad u (0) = x. \tag {1.5}
$$

For an excellent treatment of nonlinear contractive semigroups in a Hilbert space, the reader is referred to Brézis [3].

There is an intimate relationship between nonlinear (contractive) semigroups and the proximal point algorithm. If we discretize the differential inclusion (1.5) by the backward Euler differencing, we obtain

$$
\frac {x _ {k} - x _ {k - 1}}{\lambda_ {k}} \in - A (x _ {k}), \tag {1.6}
$$

and we obtain $x_{k} = (I + \lambda_{k} A)^{-1} x_{k-1} \equiv J_{\lambda_{k}}(x_{k-1})$. Therefore, PPA is just the backward Euler discretization of the differential inclusion (1.5). It is important to keep this

connection in mind, since PPA inherits many of the nice properties of the contractive semigroup $S(t)$ and vice versa. See §5 for details.

In this paper, we restrict our attention to the case $A = \partial f$ for two reasons. The first reason is subdifferentials of convex functions form an important subclass of maximal monotone operators. The second, and perhaps the more important reason, is that the operator $\partial f$ has special properties (for example, demipositivity; see Bruck [5]) not shared by other maximal monotone operators. We exploit the special properties of $\partial f$ to obtain sharper results.

In the literature, the convergence properties of the PPA are studied only in the case where $f$ has a minimizer, and the convergence rate of the algorithm is given only in the case where $f$ is strongly convex. Moreover, the convergence rate is given in terms of the closeness of $x_{k}$ to a minimizer of $f$. We depart from this tradition. We give convergence of the PPA under the weakest conditions, even in cases where $f$ has no minimizer, or is unbounded from below. Our convergence rate results are in terms of the residual $f(x_{k}) - f(u)$ where $u$ is an arbitrary point in $H$.

The organization of the rest of the paper is as follows. In §2, we establish the convergence properties of the PPA under the weakest possible assumptions. We establish global convergence rate results along with some interesting results which we use in later sections. In §3, we sharpen the convergence rate result for the residual $f(x_{n}) - f^{*}$ in the case where the PPA trajectory converges strongly to a minimizer of $f$. In §4, we present a fundamental estimate due to Kobayashi. In §5, we answer an open question posed by Rockafellar [17]: Does the PPA always converge strongly? We give a proper, closed function in an infinite-dimensional Hilbert space for which the PPA converges weakly but not strongly.

2. The convergence of the proximal point algorithm. Let $H$ be a Hilbert space and $f: H \to \mathbf{R} \cup \{\infty\}$ be a proper, closed convex function. We are concerned with the convergence properties of the PPA applied to the minimization of $f$. In the literature, convergence results for the PPA are given only in the case where $f$ has a minimizer, and convergence rate results are given in the case in which $f$ enjoys strong convexity properties. Moreover, the convergence rate results are only asymptotic.

In this section, we prove the convergence of the PPA under the weakest possible conditions and provide global convergence rate estimates for the residual $f(x_{n}) - f(u)$, where $x_{n}$ is the nth iterate of the PPA and u is any point in H. The behavior of $x_{n}$ and $y_{n} = (x_{n-1} - x_{n}) / \lambda_{n}$ is also studied.

The following result is well known. Since the proof is short, we include it.

LEMMA 2.1. $\{\| y_n\| \}_{n = 1}^{\infty}$ is a decreasing sequence.

Proof. Since $y_n \in \partial f(x_n)$, $y_{n+1} \in \partial f(x_{n+1})$, and $\partial f$ is a monotone operator, we have $\langle y_{n+1} - y_n, x_{n+1} - x_n \rangle \geq 0$. Since $y_{n+1} = (x_n - x_{n+1}) / \lambda_{n+1}$, we obtain $\langle y_{n+1} - y_n, y_{n+1} \rangle \leq 0$, which implies $\|y_{n+1}\|^2 \leq \langle y_n, y_{n+1} \rangle \leq \|y_n\| \cdot \|y_{n+1}\|$. The lemma is proved.

The following result contains the fundamental estimate from which we derive most of the convergence results of this section.

LEMMA 2.2. Let $\{\lambda_j\}_{j=1}^{\infty}$ be an arbitrary sequence of positive numbers. Suppose the PPA starts at $x_0$ and generates the sequence $\{x_n\}_{n=0}^{\infty}$, where $x_n = J_{\lambda_n}(x_{n-1})$. Then for any $u \in H$,

$$
f (x _ {n}) - f (u) \leqslant \frac {\left\| u - x _ {0} \right\| ^ {2}}{2 \sigma_ {n}} - \frac {\left\| u - x _ {n} \right\| ^ {2}}{2 \sigma_ {n}} - \frac {\sigma_ {n}}{2} \left\| y _ {n} \right\| ^ {2}. \tag {2.1}
$$

Proof. Recall that $y_{k} = (x_{k - 1} - x_{k}) / \lambda_{k}\in \partial f(x_{k})$. By the convexity of $f$ we have

$$
f (u) - f (x _ {k}) \geq \langle y _ {k}, u - x _ {k} \rangle = \lambda_ {k} ^ {- 1} \langle x _ {k - 1} - x _ {k}, u - x _ {k} \rangle . \tag {2.2}
$$

Therefore,

$$
2 \lambda_ {k} (f (u) - f (x _ {k})) \geq 2 \langle x _ {k - 1} - x _ {k}, u - x _ {k} \rangle
$$

$$
= \left\| x _ {k - 1} - x _ {k} \right\| ^ {2} + \left\| u - x _ {k} \right\| ^ {2} - \left\| u - x _ {k - 1} \right\| ^ {2} \tag {2.3}
$$

$$
= \lambda_ {k} ^ {2} \left\| y _ {k} \right\| ^ {2} + \left\| u - x _ {k} \right\| ^ {2} - \left\| u - x _ {k - 1} \right\| ^ {2}.
$$

Summing (2.3) for $k=1,\cdots,n$, we obtain

$$
2 \sigma_ {n} f (u) - 2 \sum_ {k = 1} ^ {n} \lambda_ {k} f (x _ {k}) \geqq \sum_ {k = 1} ^ {n} \lambda_ {k} ^ {2} \| y _ {k} \| ^ {2} + \| u - x _ {n} \| ^ {2} - \| u - x _ {0} \| ^ {2}. \tag {2.4}
$$

Setting $x_{k - 1}$ for $u$ in (2.2) yields

$$
f (x _ {k - 1}) - f (x _ {k}) \geq \lambda_ {k} ^ {- 1} \| x _ {k - 1} - x _ {k} \| ^ {2} = \lambda_ {k} \| y _ {k} \| ^ {2}. \tag {2.5}
$$

Recall that $\sigma_{k} = \sum_{j=1}^{k} \lambda_{j}$, for $k \geq 1$. Multiplying (2.5) by $\sigma_{k-1}$, we obtain

$$
\sigma_ {k - 1} f (x _ {k - 1}) - \sigma_ {k} f (x _ {k}) + \lambda_ {k} f (x _ {k}) \geq \sigma_ {k - 1} \lambda_ {k} \left\| y _ {k} \right\| ^ {2}.
$$

Summing the last inequality for $k=1,\cdots,n$ and noting $\sigma_{0}=0$, we obtain

$$
- \sigma_ {n} f (x _ {n}) + \sum_ {k = 1} ^ {n} \lambda_ {k} f (x _ {k}) \geqq \sum_ {k = 2} ^ {n} \sigma_ {k - 1} \lambda_ {k} \| y _ {k} \| ^ {2}. \tag {2.6}
$$

Adding twice (2.6) to (2.4) yields

$$
\begin{aligned} 2 \sigma_ {n} (f (u) - f (x _ {n})) &\geq 2 \sum_ {k = 2} ^ {n} \sigma_ {k - 1} \lambda_ {k} \| y _ {k} \| ^ {2} + \sum_ {k = 1} ^ {n} \lambda_ {k} ^ {2} \| y _ {k} \| ^ {2} + \| u - x _ {n} \| ^ {2} - \| u - x _ {0} \| ^ {2} \\ &\geq \left(\sum_ {k = 1} ^ {n} \lambda_ {k} ^ {2} + 2 \sum_ {k = 2} ^ {n} \sigma_ {k - 1} \lambda_ {k}\right) \| y _ {n} \| ^ {2} + \| u - x _ {n} \| ^ {2} - \| u - x _ {0} \| ^ {2} \\ &= \sigma_ {n} ^ {2} \| y _ {n} \| ^ {2} + \| u - x _ {n} \| ^ {2} - \| u - x _ {0} \| ^ {2}, \\ \end{aligned}
$$

where the second inequality follows from Lemma 2.1. Rearranging the terms of the inequality above gives (2.1). □

The next theorem contains the convergence properties of the PPA under the weakest possible assumptions. It is the main result of this section.

THEOREM 2.1. Let the sequence $\{x_{n}\}_{n=0}^{\infty}$ be the trajectory of a PPA. For any $u\in H$ the following global convergence estimate holds:

$$
f (x _ {n}) - f (u) \leqslant \frac {\left\| u - x _ {0} \right\| ^ {2}}{2 \sigma_ {n}}. \tag {2.7}
$$

Consequently, if $\sigma_{n} \to \infty$ , then $f(x_{n}) \downarrow f^{*} = \inf_{x \in H} f(x) or \inf_{z \in H} f(z)$ . If $X^{*} \neq \emptyset$ , then $x_{n}$ converges weakly to a minimizer of $f$ . Moreover,

$$
f (x _ {n}) - f ^ {*} \leqslant \frac {\rho (x _ {0} , X ^ {*}) ^ {2}}{2 \sigma_ {n}}. \tag {2.8}
$$

Proof. The estimate (2.7) follows immediately from (2.1). In order to prove that $f(x_{n})$ converges to $f^{*}$, we first consider the case $f^{*} > -\infty$. Let $\varepsilon > 0$ be arbitrary, and choose a point $x^{\varepsilon}$ such that $f(x^{\varepsilon}) \leq f^{*} + \varepsilon$. From (2.7) we obtain $f(x_{n}) \leq f^{*} + \varepsilon + \|x^{\varepsilon} - x_{0}\|^{2} / (2\sigma_{n})$ . Since $\sigma_{n} \to \infty$ as $n \to \infty$, we have $f(x_{n}) \leq f^{*} + 2\varepsilon$ for large enough $n$. Line (2.5) shows that $f(x_{n})$ is nonincreasing. Since $\varepsilon$ is arbitrary, $f(x_{n}) \downarrow f^{*}$. The proof of the convergence in the case $f^{*} = -\infty$ is similar.

It remains to prove the assertions about the case $X^{*} \neq \emptyset$ . In this case, the weak convergence of $x_{n}$ to a minimizer of $f$ is proved in Brézis and Lions [4, Thm. 9]. Formula (2.8) follows by substituting $x^{*}$ for $u$ in (2.7), where $x^{*}$ is the point in $X^{*}$ closest to $x_0$ .

Remark 2.1. The condition $\sigma_{n} \to \infty$ is the weakest condition in order to ensure that $f(x_{n}) \downarrow f^{*}$. If $\sigma_{n} \to \sigma < \infty$, then $x_{n}$ always converges strongly:

$$
\begin{aligned} \| x _ {n + p} - x _ {n} \| &\leq \sum_ {j = n + 1} ^ {n + p} \| x _ {j - 1} - x _ {j} \| = \sum_ {j = n + 1} ^ {n + p} \lambda_ {j} \| y _ {j} \| \tag {2.9} \\ &\leq \left(\sum_ {j = n + 1} ^ {n + p} \lambda_ {j}\right) \left\| y _ {n + 1} \right\|. \\ \end{aligned}
$$

Since $\sigma_{n} \to \sigma$, (2.9) shows that $x_{n}$ is a Cauchy sequence, and therefore converges strongly to some point $x^{\infty}$, even if $f$ does not have a minimizer! Even if $X^{*} \neq \emptyset$, we have

$$
\| x - x ^ {\infty} \| \leqslant \sum_ {j = 1} ^ {\infty} \| x _ {j - 1} - x _ {j} \| = \sum_ {j = 1} ^ {\infty} \lambda_ {j} \| y _ {j} \| \leqslant \sigma \| y _ {1} \|,
$$

so that $\rho(x^{\infty},X^{*})\geqslant\rho(x,X^{*}) - \| x - x^{\infty}\| \geqslant \rho (x,X^{*}) - \sigma \| y_{1}\|$. If $\sigma$ is small, then $\rho (x^{\infty},X^{*}) > 0$, and $x^{\infty}\notin X^{*}$.

Remark 2.2. In [7], Güler introduced new proximal point algorithms for minimizing $f$. The first of these algorithms converges under the condition $\sum_{k=1}^{\infty} \lambda_k^{1/2} = \infty$. Note that under this condition, which is weaker than $\sigma_n \to \infty$, the standard PPA need not converge.

By setting $x_0$ for $u$ in (2.1), we obtain the following result.

COROLLARY 2.1. In a proximal point algorithm the following estimate holds:

$$
f (x _ {n}) \leq f (x _ {0}) - \frac {\left\| x _ {0} - x _ {n} \right\| ^ {2}}{2 \sigma_ {n}}. \tag {2.10}
$$

The next result will be useful in this section as well as in §5.

THEOREM 2.2. Let $A = \partial f$ and $u \in D(A)$. In a proximal point algorithm the following estimates hold:

$$
\| y _ {n} \| \leqslant \frac {\| x _ {n} - x _ {0} \|}{\sigma_ {n}}, \tag {2.11}
$$

$$
\| y _ {n} \| \leq \| A ^ {0} u \| + \frac {\| u - x _ {0} \|}{\sigma_ {n}}. \tag {2.12}
$$

Proof. Formula (2.11) follows by substituting $x_{n}$ for $u$ in (2.1). From the convexity of $f$ we obtain $f(x_{n}) \geq f(u) + \langle A^{0}u, x_{n} - u \rangle$, which implies $f(u) - f(x_{n}) \leq \| A^{0}u\| \cdot \| x_{n} - u\|$. Using this inequality in (2.1), we obtain

$$
\begin{array}{l} \sigma_ {n} ^ {2} \| y _ {n} \| ^ {2} \leq \| u - x _ {0} \| ^ {2} - \| u - x _ {n} \| ^ {2} + 2 \sigma_ {n} \| A ^ {0} u \| \cdot \| x _ {n} - u \| \\ \leq \left\| u - x _ {0} \right\| ^ {2} - \left\| u - x _ {n} \right\| ^ {2} + (\sigma_ {n} ^ {2} \| A ^ {0} u \| ^ {2} + \| x _ {n} - u \| ^ {2}) \\ = \left\| u - x _ {0} \right\| ^ {2} + \sigma_{n}^{2} \|A^{0}u\|^{2} \\ \leq (\| u - x _ {0} \| + \sigma_ {n} \| A ^ {0} u \|) ^ {2}. \\ \end{array}
$$

The theorem is proved. □

Remark 2.3. In Theorem 9 of [4] Brézis and Lions prove a weaker version of (2.12), in a special case. In particular, they prove that if $X^{*} \neq \emptyset$, then $\|y_{n}\| \leq \sqrt{2} \rho(x, X^{*}) / \sigma_{n}$. However, their proof can be modified along the lines of the proof of

our Lemma 2.2 so as to eliminate the factor $\sqrt{2}$. Our stronger estimate (2.12) is essential to prove (i) of Theorem 2.3 below.

The following continuous version of Theorem 2.2 can be obtained from it by passing to the limit. It will be needed in §5.

COROLLARY 2.2. Let $A = \partial f$. For any $x \in \overline{D(A)}$ and $u \in D(A)$, we have

$$
\| A ^ {0} S (t) x \| \leq \frac {\| S (t) x - x \|}{t}, \tag {2.13}
$$

$$
\| A ^ {0} S (t) x \| \leq \| A ^ {0} u \| + \frac {\| u - x \|}{t}. \tag {2.14}
$$

Remark 2.4. A different proof of Corollary 2.2 is given in Brézis [3, Thm. 2.3.2].

The following result gives information about the behavior of $x_{n}$ and $y_{n}$ in a PPA.

THEOREM 2.3. Let $A=\partial f$ and let $v$ be the least norm element of $\overline{R(\partial f)}$. If $\sigma_{n}\to\infty$, then:

(i) $y_{n}$ converges strongly to $v$,  
(ii) $x_{n} / \sigma_{n}$ converges strongly to $-v$.  
(iii) $\{x_{n}\}_{n = 0}^{\infty}$ is bounded if and only if $f$ has a minimizer, that is, $X^{*}\neq \emptyset$. We have $\| x_{n}\| \to \infty$ if and only if $X^{*} = \emptyset$.

Proof. $\overline{R(\partial f)}$ is a closed convex set. See, for example, Brézis [3, Thm. 2.2.2]. Therefore, the least norm element, $v \in \overline{R(\partial f)}$ exists and is the projection of zero onto $\overline{R(\partial f)}$ . Let $\varepsilon > 0$ be arbitrary, and choose $x^{\varepsilon} \in D(\partial f)$ such that $\|A^{0}x^{\varepsilon}\| \leq \|v\| + \varepsilon$ . Substituting $x^{\varepsilon}$ for $u$ in (2.12), and letting $n \to \infty$ , we obtain

$$
\lim _ {n \to \infty} \| y _ {n} \| = \inf _ {n \geq 1} \| y _ {n} \| \leq \| A ^ {0} x ^ {\varepsilon} \| \leq \| v \| + \varepsilon,
$$

where we use the fact that $\sigma_{n}\to\infty$ in the first inequality above. Since $\varepsilon$ is arbitrary, $\lim_{n\to\infty}\|y_{n}\|=\|v\|$. By the parallelogram identity, $\|y_{n}-v\|^{2}+\|y_{n}+v\|^{2}=2\|y_{n}\|^{2}+2\|v\|^{2}$, which implies

$$
\| y _ {n} - v \| ^ {2} = 2 \| y _ {n} \| ^ {2} + 2 \| v \| ^ {2} - 4 \| (y _ {n} + v) / 2 \| ^ {2}. \tag {2.15}
$$

Now, since $\overline{R(\partial f)}$ is convex, $(y_{n} + v) / 2\in \overline{R(\partial f)}$, and thus we have $\| (y_n + v) / 2\| \geq \| v\|$. By triangular inequality we also have $\| (y_n + v) / 2\| \leq \| y_n\| /2 + \| v\| /2\to \| v\|$ as $n\to \infty$. Therefore $\| (y_n + v) / 2\| \to \| v\|$. Letting $n\to \infty$ in (2.15), we conclude that $y_{n}$ converges strongly to $v$ and (i) is proved.

To prove (ii), we note that $(x-x_{n})/\sigma_{n}=\sigma_{n}^{-1}\sum_{i=1}^{n}(x_{i-1}-x_{i})=\sigma_{n}^{-1}\sum_{i=1}^{n}\lambda_{i}y_{i}$. Since $y_{n}\to v$ strongly, by an application of the Silverman-Toeplitz theorem (see, for example, Dunford and Schwartz [6]), we obtain that $(x-x_{n})/\sigma_{n}$ converges strongly to v. Since $\sigma_{n}\to\infty$, $x_{n}/\sigma_{n}$ converges strongly to -v. This proves (ii). Part (iii) is known in the literature, See, for example, Reich [15] for a proof. ☐

Remark 2.5. Reich [15] actually proves (ii) for an arbitrary maximal monotone operator by a different method.

COROLLARY 2.3. Let $A = \partial f$. Suppose a PPA generates the sequence $\{x_n\}_{n=0}^{\infty}$, where $\sigma_n = \sum_{k=1}^{n} \lambda_k \to \infty$. Then, if $f^* > -\infty$, $y_n$ converges strongly to zero. Consequently, if $f^* > -\infty$, then $0 \in \overline{R(\partial f)}$.

Proof. Summing (2.5) for $k=1,\cdots,n$, we obtain

$$
\infty > f (x) - f ^ {*} \geq f (x) - f (x _ {n}) \geq \sigma_ {n} \| y _ {n} \| ^ {2}.
$$

Since $\sigma_{n}\rightarrow \infty$, we have $y_{n}\rightarrow 0 = v$, where $v$ is the least norm element of $\overline{R(\partial f)}$.

Remark 2.6. Ekeland's $\varepsilon$ -variational principle (see Aubin and Ekeland [1, Chap. 5]) can be used to prove the fact that if $f^{*} > -\infty$, then there exists $x_{n}$, $y_{n}$ with $y_{n} \in \partial f(x_{n})$, $f(x_{n}) \downarrow f^{*}$, and $y_{n} \to 0$. Corollary 2.3 shows that such $x_{n}$ and $y_{n}$ can be generated by a PPA.

Remark 2.7. It is tempting to conjecture the converse of Corollary 2.3, namely, if $0 \in \overline{R(\partial f)}$, then $f^{*} > -\infty$. However, this conjecture is false. In the first draft of the paper we had a counterexample. One of the referees suggested the following simple counterexample:

$$
f (x) = \left\{ \begin{array}{l l} - \sqrt {x} & \text {if} x \geq 0, \\ + \infty & \text {otherwise.} \end{array} \right.
$$

Observe that $f(x) \to -\infty$ as $x \to \infty$, while $\partial f(x) \to 0$. The other referee suggested another simple counterexample:

$$
f (x) = \left\{ \begin{array}{l l} 1 - x & \text {if} x \leq 1, \\ - \log (x) & \text {if} x \geq 1. \end{array} \right.
$$

Again $f(x) \to -\infty$ as $x \to \infty$, while $\partial f(x) \to 0$.

3. The convergence rate of the proximal point algorithm. Let $f: H \to \mathbf{R} \cup \{\infty\}$ be a proper, closed convex function. Assume that $X^* \neq \emptyset$, that is, $f$ has minimizers. Let $\{\lambda_j\}_{j=1}^{\infty}$ be a sequence of positive numbers with $\sigma_n \to \infty$. Consider the proximal point algorithm for minimizing $f$, with parameters $\{\lambda_k\}$, starting at an initial point $x_0 \in H$. We saw in §2 that the points $x_k$ generated by the PPA converge weakly to a minimizer of $f$. Using Theorem 2.1, we have $f(x_n) - f^* \leqq \rho(x, X^*)^2 / (2\sigma_n)$, which implies $f(x_n) - f^* = O(\sigma_n^{-1})$. We shall see in §5 that $x_n$ need not converge strongly to any minimizer of $f$. However, if $x_n$ does converge strongly to a minimizer of $f$, we can improve the converge rate $O(\sigma_n^{-1})$ above to $o(\sigma_n^{-1})$.

THEOREM 3.1. Let $\{\lambda_n\}_{n=1}^{\infty}$ be a sequence of positive numbers and $\sigma_n \to \infty$. Let $f: H \to \mathbf{R} \cup \{\infty\}$ be a proper, closed convex function which has a minimizer. Consider the PPA starting at $x = x_0$ and generating the points $x_n = (x_{n-1})_{\lambda_n}$. If $x_n$ converges strongly to a minimizer of $f$, then the convergence rate estimate

$$
f (x _ {n}) - f ^ {*} = o \left(\frac {1}{\sigma_ {n}}\right),
$$

holds, that is, $\sigma_{n}(f(x_{n}) - f^{*})\rightarrow 0$

Proof. Suppose $x_{n}$ converges strongly to $x^{*} \in X^{*}$. For brevity, we denote that $W_{k} = f(x_{k}) - f(x^{*}) = f(x_{k}) - f^{*}$. We can rewrite (2.5) as

$$
W _ {k - 1} - W _ {k} \geqq \lambda_ {k} ^ {- 1} \| x _ {k - 1} - x _ {k} \| ^ {2}. \tag {3.1}
$$

Substituting $x^{*}$ for $u$ in (2.2), we obtain

$$
\begin{array}{l} f (x ^ {*}) \geq f (x _ {k}) + \lambda_ {k} ^ {- 1} \langle x _ {k - 1} - x _ {k}, x ^ {*} - x _ {k} \rangle \\ = f (x _ {k}) + \lambda_ {k} ^ {- 1} \langle x _ {k - 1} - x _ {k}, x ^ {*} - x _ {k - 1} \rangle + \lambda_ {k} ^ {- 1} \| x _ {k - 1} - x _ {k} \| ^ {2} \\ \geq f (x _ {k}) - \lambda_ {k} ^ {- 1} \| x _ {k - 1} - x _ {k} \| \cdot \| x _ {k - 1} - x ^ {*} \| \\ \end{array}
$$

Therefore, $\| x_{k - 1} - x_k\| \geq \lambda_kW_k\| x_{k - 1} - x^*\|^{-1}$. Using this inequality in (3.1), we obtain

$$
\begin{aligned} W _ {k - 1} \geqq W _ {k} + \frac {1}{\lambda_ {k}} \left(\lambda_ {k} W _ {k} \left\| x _ {k - 1} - x ^ {*} \right\| ^ {- 1}\right) ^ {2} \\ &= W _ {k} + \frac {\lambda_ {k}}{\| x _ {k - 1} - x ^ {*} \| ^ {2}} W _ {k} ^ {2} = W _ {k} \left(1 + \frac {\lambda_ {k}}{\| x _ {k - 1} - x ^ {*} \| ^ {2}} W _ {k}\right). \\ \end{aligned}
$$

Inverting this inequality, we obtain

$$
W _ {k - 1} ^ {- 1} \leqq W _ {k} ^ {- 1} \left(1 + \frac {\lambda_ {k}}{\| x _ {k - 1} - x ^ {*} \| ^ {2}} W _ {k}\right) ^ {- 1}. \tag {3.2}
$$

We want to obtain a recursive inequality from (3.2). We have from (1.2),

$$
f (x _ {k}) \leq f (x _ {k}) + \frac {1}{2 \lambda_ {k}} \left\| x _ {k} - x _ {k - 1} \right\| ^ {2} \leq f (x ^ {*}) + \frac {1}{2 \lambda_ {k}} \left\| x ^ {*} - x _ {k - 1} \right\| ^ {2},
$$

so that $0 \leq W_{k}\lambda_{k}\|x^{*} - x_{k-1}\|^{-2} \leq \frac{1}{2}$. The function $(1+t)^{-1}$ is convex for $t > -1$, hence $(1+t)^{-1} \leq 1 - 2t/3$, for $t \in [0, \frac{1}{2}]$. Using this fact, we obtain from (3.2) that

$$
W _ {k - 1} ^ {- 1} \leq W _ {k} ^ {- 1} \left(1 - \frac {2 \lambda_ {k}}{3 \left\| x _ {k - 1} - x ^ {*} \right\| ^ {2}} W _ {k}\right) = W _ {k} ^ {- 1} - \frac {2 \lambda_ {k}}{3 \left\| x _ {k - 1} - x ^ {*} \right\| ^ {2}},
$$

or equivalently,

$$
W _ {k} ^ {- 1} - W _ {k - 1} ^ {- 1} \geqslant \frac {2 \lambda_ {k}}{3 \| x _ {k - 1} - x ^ {*} \| ^ {2}}. \tag {3.3}
$$

This is the desired recursive inequality. Summing (3.3) for $k=1,\cdots,n$, we obtain

$$
W _ {n} ^ {- 1} \geq W _ {n} ^ {- 1} - W _ {0} ^ {- 1} \geq \frac {2}{3} \sum_ {k = 1} ^ {n} \frac {\lambda_ {k}}{\| x _ {k - 1} - x ^ {*} \| ^ {2}},
$$

which implies

$$
f (x _ {n}) - f (x ^ {*}) \equiv W _ {n} \leqslant \frac {3}{2} \frac {1}{\sum_ {k = 1} ^ {n} \lambda_ {k} \| x _ {k - 1} - x ^ {*} \| ^ {- 2}}. \tag {3.4}
$$

Multiplying (3.4) by $\sigma_{n}$ gives

$$
\sigma_ {n} (f (x _ {n}) - f (x ^ {*})) \leqslant \frac {3}{2} \frac {1}{\sigma_ {n} ^ {- 1} \sum_ {k = 1} ^ {n} \lambda_ {k} \| x _ {k - 1} - x ^ {*} \| ^ {- 2}}.
$$

Since $\| x_n - x^* \| \to 0$, $\| x_n - x^* \|^{-1} \to \infty$. Therefore, using the Silverman-Toeplitz theorem (see Dunford and Schwartz [6]), $\sigma_n^{-1} \sum_{k=1}^{n} \lambda_k \| x_{k-1} - x^* \|^{-2} \to \infty$ also. Consequently, $f(x_n) - f(x^*) = o(\sigma_n^{-1})$.

4. A fundamental estimate. Let $A: H \to H$ be a maximal monotone operator. Consider two proximal trajectories $\{x_k\}_{k=0}^{\infty}$, and $\{\hat{x}_k\}_{k=0}^{\infty}$. A remarkable estimate due to Kobayasi, Kobayashi, and Oharu [8], [9] (see also Pavel [14]) gives an estimate for the distance $\|x_k - \hat{x}_l\|$ between an arbitrary point $x_k$ in the first trajectory and the point $\hat{x}_l$ on the second trajectory. This estimate can be used as the basis for the theory of nonlinear contractive semigroups and nonlinear evolution equations in Banach spaces. We shall use it in §5 to help settle a question posed by Rockafellar [17] on the strong convergence of the PPA. Since Kobayashi's estimate does not seem to be known in the optimization literature, but is likely to have further applications in optimization, we develop a special version of it here which will be enough for our purposes. The interested reader should consult Kobayasi, Kobayashi, and Oharu [9], or Pavel [14] for the general version of the estimate.

We will use two simple lemmas, valid for any monotone operator (not necessarily maximal).

LEMMA 4.1. If $A:H\to H$ is a monotone operator, then for any $\lambda >0$, and $y_{i}\in A(x_{i})$, $i = 1,2$,

$$
\| x _ {1} - x _ {2} \| \leq \| x _ {1} - x _ {2} + \lambda (y _ {1} - y _ {2}) \|. \tag {1}
$$

Lemma 4.1 follows from the application of (1.3) to the operator $\lambda A$.

LEMMA 4.2. If $A$ is a monotone operator, then for any $\lambda, \mu \geq 0$, and $y_i \in A(x_i)$, $i = 1, 2$, the following inequality holds:

$$
(\lambda + \mu) \| x _ {1} - x _ {2} \| \leq \lambda \| x _ {2} + \mu y _ {2} - x _ {1} \| + \mu \| x _ {1} + \lambda y _ {1} - x _ {2} \|.
$$

Proof. We have

$$
\mu (x _ {1} + \lambda y _ {1} - x _ {2}) - \lambda (x _ {2} + \mu y _ {2} - x _ {1}) = (\lambda + \mu) (x _ {1} - x _ {2}) + \lambda \mu (y _ {1} - y _ {2}). \tag {4.1}
$$

By Lemma 4.1,

$$
\| x _ {1} - x _ {2} \| \leq \left\| (x _ {1} - x _ {2}) + \frac {\lambda \mu}{\lambda + \mu} (y _ {1} - y _ {2}) \right\|,
$$

so that

$$
\begin{aligned} (\lambda + \mu) \| x _ {1} - x _ {2} \| &\leq \| (\lambda + \mu) (x _ {1} - x _ {2}) + \lambda \mu (y _ {1} - y _ {2}) \| \\ &= \left\| \mu (x _ {1} + \lambda y _ {1} - x _ {2}) - \lambda (x _ {2} + \mu y _ {2} - x _ {1}) \right\| \\ &\leq \lambda \left\| x _ {2} + \mu y _ {2} - x _ {1} \right\| + \mu \left\| x _ {1} + \lambda y _ {1} - x _ {2} \right\|, \\ \end{aligned}
$$

where the equality follows from (4.1). The proof is complete.

We now return to the PPA. In the remainder of this section we assume that a maximal monotone operator $A: H \to H$ is given, and that it generates the proximal trajectory $\{x_k\}_{k=0}^{\infty}$, with $x_0 = x$ and parameters $\{\lambda_k\}_{k=1}^{\infty}$.

LEMMA 4.3. For any $u \in D(A)$, and $k \geq 0$,

$$
\| x _ {k} - u \| \leq \| x _ {0} - u \| + \sigma_ {k} \| A ^ {0} u \|. \tag {4.2}
$$

Proof. Let $v$ be an arbitrary element of $A(u)$. Since $y_{j} = (x_{j-1} - x_{j}) / \lambda_{j} \in A(x_{j})$, we have $x_{j-1} = x_{j} + \lambda_{j}y_{j}$. From Lemma 4.1,

$$
\| x _ {j} - u \| \leq \| x _ {j} - u + \lambda_ {j} (y _ {j} - v) \| = \| x _ {j - 1} - u - \lambda_ {j} v \| \tag {4.3}
$$

$$
\leq \left\| x _ {j - 1} - u \right\| + \lambda_ {j} \| v \|
$$

The lemma follows by summing (4.3) for $j=1,\cdots,k$ and noting that $v\in A(u)$ is arbitrary. ☐

Consider two proximal trajectories $\{x_{k}\}_{k = 0}^{\infty}$, and $\{\hat{x}_l\}_{l = 0}^{\infty}$. We will derive an estimate for the distance $\| x_{k} - \hat{x}_{l}\|$ for arbitrary $k$ and $l$. This estimate will be obtained recursively.

We first prove some preliminary results. Denote the mesh of the first proximal trajectory by $d = \max_{1 \leq k \leq N} \lambda_k$. Similarly, the mesh of the second proximal trajectory is defined by $\hat{d} = \max_{1 \leq l \leq \hat{N}} \hat{\lambda}_l$. Also, we define $\alpha_{k,l} = \hat{\lambda}_l / (\lambda_k + \hat{\lambda}_l)$ and $\beta_{k,l} = 1 - \alpha_{k,l} = \lambda_k / (\lambda_k + \hat{\lambda}_l)$. Finally, we define

$$
c _ {k, l} = \sqrt {\left(\sigma_ {k} - \hat {\sigma} _ {l}\right) ^ {2} + d \sigma_ {k} + \hat {d} \hat {\sigma} _ {l}}.
$$

LEMMA 4.4. $\alpha_{k,l}c_{k - 1,l} + \beta_{k,l}c_{k,l - 1}\leq c_{k,l}$

Proof. We have

$$
\begin{aligned} \alpha_ {k, l} c _ {k - 1, l} + \beta_ {k, l} c _ {k, l - 1} &= \alpha_ {k, l} ^ {1 / 2} (\alpha_ {k, l} ^ {1 / 2} c _ {k - 1, l}) + \beta_ {k, l} ^ {1 / 2} (\beta_ {k, l} ^ {1 / 2} c _ {k, l - 1}) \\ &\leq \sqrt {\alpha_ {k , l} c _ {k - 1 , l} ^ {2} + \beta_ {k , l} c _ {k , l - 1} ^ {2}}, \\ \end{aligned}
$$

where the inequality follows from the Cauchy-Schwarz inequality and the fact that

$\alpha_{k,l} + \beta_{k,l} = 1$. Therefore,

$$
\begin{array}{l} (\alpha_ {k, l} c _ {k - 1, l} + \beta_ {k, l} c _ {k, l - 1}) ^ {2} \leq \alpha_ {k, l} c _ {k - 1, l} ^ {2} + \beta_ {k, l} c _ {k, l - 1} ^ {2} \\ = \alpha_ {k, l} ((\sigma_ {k - 1} - \hat {\sigma} _ {l}) ^ {2} + d \sigma_ {k - 1} + \hat {d} \hat {\sigma} _ {l}) \\ + \beta_ {k, l} ((\sigma_ {k} - \hat {\sigma} _ {l - 1}) ^ {2} + d \sigma_ {k} + \hat {d} \hat {\sigma} _ {l - 1}) \\ = \alpha_ {k, l} ((\sigma_ {k} - \hat {\sigma} _ {l} - \lambda_ {k}) ^ {2} + d (\sigma_ {k} - \lambda_ {k}) + \hat {d} \hat {\sigma} _ {l}) \\ + \beta_ {k, l} ((\sigma_ {k} - \hat {\sigma} _ {l} + \hat {\lambda} _ {l}) ^ {2} + d \sigma_ {k} + \hat {d} (\hat {\sigma} _ {l} - \hat {\lambda} _ {l})) \\ = \frac {\hat {\lambda} _ {l}}{\lambda_ {k} + \hat {\lambda} _ {l}} (c _ {k, l} ^ {2} + \lambda_ {k} ^ {2} - 2 \lambda_ {k} (\sigma_ {k} - \hat {\sigma} _ {l}) - d \lambda_ {k}) \\ + \frac {\lambda_ {k}}{\lambda_ {k} + \hat {\lambda} _ {l}} (c _ {k, l} ^ {2} + \hat {\lambda} _ {l} ^ {2} + 2 \hat {\lambda} _ {l} (\sigma_ {k} - \hat {\sigma} _ {l}) - \hat {d} \hat {\lambda} _ {l}) \\ = c _ {k, l} ^ {2} + \frac {\lambda_ {k} \hat {\lambda} _ {l}}{\lambda_ {k} + \hat {\lambda} _ {l}} \left((\lambda_ {k} - d) + (\hat {\lambda} _ {l} - \hat {d})\right) \leq c _ {k, l} ^ {2}. \\ \end{array}
$$

The lemma is proved. □

THEOREM (Kobayashi) 4.1. Let $u \in D(A)$ be an arbitrary point. Then, for any $k = 0, \cdots, N$ and $l = 0, \cdots, \hat{N}$,

$$
\| x _ {k} - \hat {x} _ {l} \| \leq \| x _ {0} - u \| + \| \hat {x} _ {0} - u \| + \sqrt {\left(\sigma_ {k} - \hat {\sigma} _ {l}\right) ^ {2} + d \sigma_ {k} + \hat {d} \hat {\sigma} _ {l}} \cdot \| A ^ {0} u \|.
$$

Proof. Observe that the coefficient of $\|A^{0}u\|$ in the desired estimate is simply $c_{k,l}$. The proof will be by induction. We start by proving the theorem for the pairs $(k,0)$ and $(0,l)$. We have

$$
\begin{aligned} \| x _ {k} - \hat {x} _ {0} \| &\leq \| x _ {k} - u \| + \| \hat {x} _ {0} - u \| \\ &\leq \| x _ {0} - u \| + \| \hat {x} _ {0} - u \| + \sigma_ {k} \| A ^ {0} u \| \\ &\leq \| x _ {0} - u \| + \| \hat {x} _ {0} - u \| + c _ {k, 0} \| A ^ {0} u \|, \\ \end{aligned}
$$

where the second inequality follows from Lemma 4.3, and the last inequality follows from the fact that $\sigma_{k} \leq c_{k,0}$ , which is easy to see. This proves the theorem for $(k,0)$ . By symmetry, the theorem is also true for the pair $(0,l)$ .

Suppose we have proved the theorem for the pairs $(k - 1, l)$ and $(k, l - 1)$. From Lemma 4.2, we obtain

$$
(\lambda_ {k} + \hat {\lambda} _ {l}) \| x _ {k} - \hat {x} _ {l} \| \leq \lambda_ {k} \| \hat {x} _ {l} + \hat {\lambda} _ {l} \hat {y} _ {l} - x _ {k} \| + \hat {\lambda} _ {l} \| x _ {k} + \lambda_ {k} y _ {k} - \hat {x} _ {l} \|.
$$

Noting that $\hat{x}_{l-1}=\hat{x}_{l}+\hat{\lambda}_{l}\hat{y}_{l}$ and $x_{k-1}=x_{k}+\lambda_{k}y_{k}$, we have

$$
\begin{array}{l} \| x _ {k} - \hat {x} _ {l} \| \leq \frac {\hat {\lambda} _ {l}}{\lambda_ {k} + \hat {\lambda} _ {l}} \| x _ {k - 1} - \hat {x} _ {l} \| + \frac {\lambda_ {k}}{\lambda_ {k} + \hat {\lambda} _ {l}} \| x _ {k} - \hat {x} _ {l - 1} \| \\ = \alpha_ {k, l} \| x _ {k - 1} - \hat {x} _ {l} \| + \beta_ {k, l} \| x _ {k} - \hat {x} _ {l - 1} \| \\ \leq \alpha_ {k, l} (\| x _ {0} - u \| + \| \hat {x} _ {0} - u \| + c _ {k - 1, l} \| A ^ {0} u \|) \\ + \beta_ {k, l} (\| x _ {0} - u \| + \| \hat {x} _ {0} - u \| + c _ {k, l - 1} \| A ^ {0} u \|) \\ \leq \| x _ {0} - u \| + \| \hat {x} _ {0} - u \| + \left(\alpha_ {k, l} c _ {k - 1, l} + \beta_ {k, l} c _ {k, l - 1}\right) \| A ^ {0} u \| \\ \leq \| x _ {0} - u \| + \| \hat {x} _ {0} - u \| + c _ {k, l} \| A ^ {0} u \|, \\ \end{array}
$$

where the second inequality follows from the induction hypothesis, and the last inequality follows from Lemma 4.4. The theorem is proved. □

Theorem 4.1 can be used to prove that as the mesh of the backward discretization $\max_{k\geq 1}\lambda_k\to 0$ in (1.6), the proximal trajectory converges to a (unique) discrete scheme solution to the differential inclusion (1.5). It turns out that this solution coincides with the usual solution $u(t) = S(t)x$ (also called the strong solution) discussed in §1. See Kobayashi [8], or Pavel [14, Chap. 1, §3] for more details.

COROLLARY 4.1. The following estimates hold:

$$
\| x _ {k} - S (t) x \| \leq \sqrt {(\sigma_ {k} - t) ^ {2} + d \sigma_ {k}} \cdot \| A ^ {0} x \|, \tag {4.4}
$$

$$
\| S (t) x - S (s) x \| \leq | t - s | \cdot \| A ^ {0} x \|. \tag {4.5}
$$

Proof. Choose $\hat{x}_{0}=x$ and apply Theorem 4.1. As $\hat{d}\to0$, the second proximal trajectory converges to the continuous path $S(t)x$, and (4.4) follows. Estimate (4.5) is proved similarly. ☐

5. On the strong convergence of the proximal point algorithm. We noted in §2 that the trajectory of the PPA converges weakly to a minimizer of a proper, closed convex function, provided that $X^{*} \neq \emptyset$ and $\sigma_k \to \infty$. In [17], Rockafellar posed the question of whether weak convergence can be strengthened to strong convergence. This question is also important for us since strong convergence has a bearing on the rate of convergence of the PPA. By Theorem 2.1, $f(x_n) - f^* = O(\sigma_n^{-1})$ in the case of weak convergence; however, by Theorem 3.1 $f(x_n) - f^* = o(\sigma_n^{-1})$ in the case of strong convergence. Of course, in finite dimensions, weak and strong convergence are equivalent. There are also cases (see, for example, [4], [5]) where we can show strong convergence.

In this section, we answer Rockafellar's open question in the negative. In particular, we prove that in $l^2$ there is a function $f$ such that given any positive bounded sequence $\{\lambda_j\}_{j=1}^{\infty}$, there is a starting point $x \in D(f)$, and the PPA starting from $x$ with $x_{k+1} = (x_k)_{\lambda_{k+1}}$ converges weakly, but not strongly.

We proceed in the following way. A well-known result of Bruck [5] states that $S(t)x$ converges weakly to a minimizer of $f$. Baillon [2], following a suggestion of Komura, constructed a proper, closed convex function in $l^2$ and a point $x \in \overline{D(f)}$ such that $S(t)x$ converges weakly, but not strongly, to a minimizer of $f$. In [13], Passty showed that the strong (respectively, weak) convergence of $S(t)x$ is equivalent to the strong (respectively, weak) convergence of a PPA trajectory under very restrictive conditions. By using the special properties of the monotone operator $\partial f$ outlined in §2, and the fundamental estimate of Kobayashi described in §4, we show the asymptotic equivalence of the trajectory of a PPA and $S(t)$ under the condition that the sequence $\{\lambda_k\}_{k=1}^\infty$ is bounded.

DEFINITION 5.1. Let $C$ be convex subset of $H$. A contractive evolution system on $C$ is a two-parameter family of maps $\{U(t,s): 0 \leq s \leq t\}$ from $C$ into $C$ satisfying:

(i) $U(t, t)x = x$ for all $x \in C$ and $t \geq 0$,  
(ii) $U(t,s)U(s,r)x = U(t,r)x$ for all $x\in C$ and $0\leq r\leq s\leq t$, and  
(iii) $\| U(t,s)x - U(t,s)y\| \leq \| x - y\|$ for all $x,y\in C$ and $0\leq s\leq t$.

DEFINITION 5.2. A contractive evolution system $U(t, s)$ is asymptotically equal to a contractive semigroup $S(t)$ if, for all $x \in C$, we have

(i) $\lim_{t\to \infty}\| U(t + h,s)x - S(h)U(t,s)x\| = 0$ for all $s\geq 0$ , uniformly in $h\geq 0$ , and  
(ii) $\lim_{t\to \infty}\| U(t + h,t)S(t)x - S(t + h)x\| = 0$ uniformly in $h\geq 0$. The system $U$ is called an asymptotic semigroup if there is a semigroup to which it is asymptotically equal.

Intuitively, that $U$ and $S$ are asymptotically equal means the following: if we follow one of the trajectories, say $S$, for a sufficiently long time $t$ and arrive at the

point $S(t)x$, then it matters little whether we follow $S$ or $U$ for any length of time $h$ in the future, because the two trajectories will be close to each other.

The concept of asymptotic equality is important because of the following result proved in Passty [13].

LEMMA 5.1. Let A be a maximal monotone operator on H, and let $S(t)$ be the contractive semigroup generated by A on $\bar{C}$. Let $U(t, s)$ be a contractive evolution system which is asymptotically equal to $S(t)$ on $D(A)$. Then the following are equivalent:

(i) $S(t)x$ converges strongly (respectively weakly) as $t\to \infty$ for all $x\in D(A)$,  
(ii) $U(t, s)x$ converges strongly (respectively weakly) as $t \to \infty$ for all $x \in D(A)$, and $s \geq 0$.

Remark 5.1. From the proof given in Passty [13], it can be seen that in proving (i) implies (ii) in the lemma, only condition (i) of Definition 5.2 is needed. Similarly, only condition (ii) of Definition 5.2 is needed for proving that (ii) implies (i).

LEMMA 5.2. Let $\{k(n)\}_{n=0}^{\infty}$ be a sequence of strictly increasing positive integers, where $k(0)=0$ . Define $\sigma_{m}^{n}=\sum_{j=k(m)+1}^{k(n)}\lambda_{j}$ , and $\prod_{m}^{n}=\prod_{j=k(m)+1}^{k(n)}J_{\lambda_{j}}$ . (If $n=m$ , we define $\sigma_{m}^{n}=0$ and $\prod_{m}^{n}x=x$ .) Then, for any $n,p\geq1$ ,

$$
\left\| S (\sigma_ {n} ^ {n + p}) x - \prod_ {n} ^ {n + p} x \right\| \leqq \sum_ {m = n + 1} ^ {n + p} \left\| S (\sigma_ {m - 1} ^ {m}) \left(\prod_ {n} ^ {m - 1} x\right) - \prod_ {m - 1} ^ {m} \left(\prod_ {n} ^ {m - 1} x\right) \right\|, \tag {5.1}
$$

$$
\left\| S (\sigma_ {n} ^ {n + p}) x - \prod_ {n} ^ {n + p} x \right\| \leqq \sum_ {m = n + 1} ^ {n + p} \left\| S (\sigma_ {m - 1} ^ {m}) S (\sigma_ {n} ^ {m - 1}) x - \prod_ {m - 1} ^ {m} S (\sigma_ {n} ^ {m - 1}) x \right\|. \tag {5.2}
$$

Proof. We prove the lemma by induction on $p$. We first prove (5.1). It is evidently true for $p = 1$. Assuming it is true for $p$, we prove it for $p + 1$. We have

$$
\begin{array}{l} \left\| S \left(\sigma_ {n} ^ {n + p + 1}\right) x - \prod_ {n} ^ {n + p + 1} x \right\| = \left\| S \left(\sigma_ {n + p} ^ {n + p + 1}\right) S \left(\sigma_ {n} ^ {n + p}\right) x - \prod_ {n + p} ^ {n + p + 1} \left(\prod_ {n} ^ {n + p} x\right) \right\| \\ \leq \left\| S (\sigma_ {n + p} ^ {n + p + 1}) S (\sigma_ {n} ^ {n + p}) x - S (\sigma_ {n + p} ^ {n + p + 1}) \left(\prod_ {n} ^ {n + p} x\right) \right\| \\ + \left\| S (\sigma_ {n + p} ^ {n + p + 1}) \left(\prod_ {n} ^ {n + p} x\right) - \prod_ {n + p} ^ {n + p + 1} \left(\prod_ {n} ^ {n + p} x\right) \right\| \\ \leq \left\| S (\sigma_ {n} ^ {n + p}) x - \prod_ {n} ^ {n + p} x \right\| + \left\| S (\sigma_ {n + p} ^ {n + p + 1}) \left(\prod_ {n} ^ {n + p} x\right) - \prod_ {n + p} ^ {n + p + 1} \left(\prod_ {n} ^ {n + p} x\right) \right\| \\ \leq \sum_ {m = n + 1} ^ {n + p} \left\| S \left(\sigma_ {m - 1} ^ {m}\right) \left(\prod_ {n} ^ {m - 1} x\right) - \prod_ {m - 1} ^ {m} \left(\prod_ {n} ^ {m - 1} x\right) \right\| \\ + \left\| S (\sigma_ {n + p} ^ {n + p + 1}) \left(\prod_ {n} ^ {n + p} x\right) - \prod_ {n + p} ^ {n + p + 1} \left(\prod_ {n} ^ {n + p} x\right) \right\| \\ = \sum_ {m = n + 1} ^ {n + p + 1} \left\| S (\sigma_ {m - 1} ^ {m}) \left(\prod_ {n} ^ {m - 1} x\right) - \prod_ {m - 1} ^ {m} \left(\prod_ {n} ^ {m - 1} x\right) \right\|, \\ \end{array}
$$

where the second inequality follows since $S(t)$ is contractive, and the last inequality follows from the induction hypothesis. This proves (5.1).

We now prove (5.2). The proof is again by induction on $p$. Equation (5.2) is clearly true for $p = 1$. Assuming it is true for $p$, we prove it for $p + 1$. We have

$$
\begin{array}{l} \left\| S \left(\sigma_ {n} ^ {n + p + 1}\right) x - \prod_ {n} ^ {n + p + 1} x \right\| = \left\| \prod_ {n + p} ^ {n + p + 1} \prod_ {n} ^ {n + p} x - S \left(\sigma_ {n + p} ^ {n + p + 1}\right) S \left(\sigma_ {n} ^ {n + p}\right) x \right\| \\ \leq \left\| \prod_ {n + p} ^ {n + p + 1} \left(\prod_ {n} ^ {n + p} x\right) - \prod_ {n + p} ^ {n + p + 1} S (\sigma_ {n} ^ {n + p}) x \right\| \\ + \left\| \prod_ {n + p} ^ {n + p + 1} S (\sigma_ {n} ^ {n + p}) x - S (\sigma_ {n + p} ^ {n + p + 1}) S (\sigma_ {n} ^ {n + p}) x \right\| \\ \leq \left\| \prod_ {n} ^ {n + p} x - S \left(\sigma_ {n} ^ {n + p}\right) x \right\| + \left\| \prod_ {n + p} ^ {n + p + 1} S \left(\sigma_ {n} ^ {n + p}\right) x \right. \\ \left. - S \left(\sigma_ {n + p} ^ {n + p + 1}\right) S \left(\sigma_ {n} ^ {n + p}\right) x \right\Vert \\ \leq \sum_ {m = n + 1} ^ {n + p} \left\| S \left(\sigma_ {m - 1} ^ {m}\right) S \left(\sigma_ {n} ^ {m - 1}\right) x - \prod_ {m - 1} ^ {m} S \left(\sigma_ {n} ^ {m - 1}\right) x \right\| \\ + \left\| \prod_ {n + p} ^ {n + p + 1} S (\sigma_ {n} ^ {n + p}) x - S (\sigma_ {n + p} ^ {n + p + 1}) S (\sigma_ {n} ^ {n + p}) x \right\| \\ = \sum_ {m = n + 1} ^ {n + p + 1} \left\| S (\sigma_ {m - 1} ^ {m}) S (\sigma_ {n} ^ {m - 1}) x - \prod_ {m - 1} ^ {m} S (\sigma_ {n} ^ {m - 1}) x \right\|, \\ \end{array}
$$

where the second inequality follows since $\prod_{n+p}^{n+p+1}$ is contractive, and the last inequality follows from the induction hypothesis. This proves (5.2). $\square$

Let the sequence $\{\lambda_{j}\}_{j=1}^{\infty}$ of positive numbers be the parameters of a PPA such that $\sigma_{n}\to\infty$. We define an integer-valued function $n(t)$ for $t\geq0$ as follows: $n(0)=0$, and for t>0, $n(t)$ is the integer satisfying

$$
\sigma_ {n (t) - 1} <   t \leq \sigma_ {n (t)}.
$$

We are interested in the contractive evolution system $U(t, s)$, defined for $0 \leq s \leq t$ by the formula $U(t, s)x = (\prod_{i=n(s)+1}^{n(t)} J_{\lambda_i})x$, where we let $(\prod_{i=1}^0 J_{\lambda_i})x = x$. It is easy to show that $U(t, s)$ is a contractive evolution system using the fact that $J_\lambda$ is a contractive mapping.

The following theorem is the main result of this section. This sharpens Theorem 1 in Passty [13] in the case where $A = \partial f$ in that our conditions on the parameters $\{\lambda_k\}_{k=1}^{\infty}$ are much more relaxed than Passty's. Our relaxed conditions are possible because of the special properties of the operator $A = \partial f$ given in §2. However, Passty's Theorem 1 applies to an arbitrary maximal monotone operator.

THEOREM 5.1. Suppose $f: H \to \mathbf{R} \cup \{\infty\}$ is a closed convex function and assume that $f$ has a minimizer. Let $\{\lambda_j\}_{j=1}^{\infty}$ be a bounded sequence of positive numbers such that $\sigma_n \to \infty$. Then the contractive evolution system $U(t, s)$ defined above is asymptotically equal to the contractive semigroup $S(t)$ generated by $\partial f$.

Proof. By Lemma 5.1, we need to verify the conditions (i) and (ii) in Definition 5.2.

For the sake of simple notation, we define $\sigma_s^t = \sum_{j=n(s)+1}^{n(t)}\lambda_j$, and $\prod_s^t = \prod_{j=n(s)+1}^{n(t)}J_{\lambda_j}$. If $t \leq s$, we let $\sigma_s^t = 0$, and $\prod_s^t x = x$. Note that we also define $\sigma_m^n$ in Lemma 5.2. However, no confusion should arise, since it will be clear from the context which definition is intended.

Let us first verify condition (i) in Definition 5.2. Without loss of generality, we may assume that $s = 0$. Fix $t > 0$. For an arbitrary $h > 0$, we have

$$
\begin{aligned} \left\| U (t + h, 0) x - S (h) U (t, 0) x \right\| &= \left\| \prod_ {0} ^ {t + h} x - S (h) \prod_ {0} ^ {t} x \right\| \\ &= \left\| \prod_ {t} ^ {t + h} \left(\prod_ {0} ^ {t} x\right) - S (h) \left(\prod_ {0} ^ {t} x\right) \right\| \\ &\leq \left\| \prod_ {t} ^ {t + h} \left(\prod_ {0} ^ {t} x\right) - S (\sigma_ {t} ^ {t + h}) \left(\prod_ {0} ^ {t} x\right) \right\| \\ + \left\| S (\sigma_ {t} ^ {t + h}) \left(\prod_ {0} ^ {t} x\right) - S (h) \prod_ {0} ^ {t} x \right\|. \\ \end{aligned}
$$

We first estimate the second term in the last expression above:

$$
\begin{aligned} \left\| S \left(\sigma_ {t} ^ {t + h}\right) \prod_ {0} ^ {t} x - S (h) \prod_ {0} ^ {t} x \right\| &\leq \left| \sigma_ {t} ^ {t + h} - h \right| \cdot \left\| A ^ {0} \prod_ {0} ^ {t} x \right\| \\ &\leq \frac {\left| \sigma_ {t} ^ {t + h} - h \right|}{\sigma_ {n (t)}} \rho (x, X ^ {*}) \\ &\leq \frac {\max \left\{\lambda_ {n (t)} , \lambda_ {n (t + h)} \right\}}{\sigma_ {n (t)}} \rho (x, X ^ {*}) \tag {5.3} \\ &\leq \frac {\Lambda}{\sigma_ {n (t)}} \rho (x, X ^ {*}), \\ \end{aligned}
$$

where $\Lambda=\max_{j\ge 1}\lambda_{j}$ . Here the first inequality follows from (4.5), and the second inequality follows from (2.12) with $x^{*}$ replacing u, where $x^{*}$ is the element of $X^{*}$ closest to x. The third inequality follows easily from the definition of $\sigma_{t}^{t+h}$ . Since $\sigma_{n(t)}\to\infty$ as $t\to\infty$ , the last term in (5.3) can be made as small as desired by choosing t large enough.

It remains to estimate the first term:

$$
\left\| S (\sigma_ {t} ^ {t + h}) \left(\prod_ {0} ^ {t} x\right) - \prod_ {t} ^ {t + h} \left(\prod_ {0} ^ {t} x\right) \right\|.
$$

The idea is to partition the interval $[0, \sigma_{n(t+h)}]$ into subintervals and use Lemma 5.2 on each subinterval. The subintervals will be of the form $[\sigma_{k(i)}, \sigma_{k(i+1)}]$, for $i = 0, \cdots, n + p$, such that $k(i) = n(t)$ for some t, where we assume $n(t) = k(n)$ (note the two meanings of n here) and $n(t + h) = k(n + p)$. We will impose more conditions on the sequence $k(i)$ later. We have

$$
\begin{array}{l} \left\| S \left(\sigma_ {t} ^ {t + h}\right) \left(\prod_ {0} ^ {t} x\right) - \prod_ {t} ^ {t + h} \left(\prod_ {0} ^ {t} x\right) \right\| = \left\| S \left(\sigma_ {n} ^ {n + p}\right) \left(\prod_ {0} ^ {n} x\right) - \prod_ {n} ^ {n + p} \left(\prod_ {0} ^ {n} x\right) \right\| \\ \leq \sum_ {m = n + 1} ^ {n + p} \left\| S \left(\sigma_ {m - 1} ^ {m}\right) \prod_ {n} ^ {m - 1} \left(\prod_ {0} ^ {n} x\right) - \prod_ {m - 1} ^ {m} \prod_ {n} ^ {m - 1} \left(\prod_ {0} ^ {n} x\right) \right\| \\ = \sum_ {m = n + 1} ^ {n + p} \left\| S \left(\sigma_ {m - 1} ^ {m}\right) \left(\prod_ {0} ^ {m - 1} x\right) - \prod_ {m - 1} ^ {m} \left(\prod_ {0} ^ {m - 1} x\right) \right\| \\ \leq \sum_ {m = n + 1} ^ {n + p} \sqrt {d _ {m} \sigma_ {m - 1} ^ {m}} \left\| A ^ {0} \left(\prod_ {0} ^ {m - 1} x\right) \right\| \\ \leq \sum_ {m = n + 1} ^ {n + p} \sqrt {d _ {m} \sigma_ {m - 1} ^ {m}} \frac {\rho (x , X ^ {*})}{\sigma_ {0} ^ {m - 1}} \\ \leq \sqrt {\Lambda} \rho (x, X ^ {*}) \sum_ {m = n + 1} ^ {n + p} \frac {\sqrt {\sigma_ {m - 1} ^ {m}}}{\sigma_ {0} ^ {m - 1}}, \\ \end{array}
$$

where the first inequality follows from (5.1), and the second inequality from (4.4). The third inequality follows from (2.12), with $x^{*}$ replacing $u$, where $x^{*}$ is the element of $X^{*}$ closest to $x$. Here $d_{m} = \max_{j = k(m - 1) + 1}^{k(m)}\lambda_{j}$. We are interested in making the term

$$
\sum_ {m = n + 1} ^ {n + p} \frac {\sqrt {\sigma_ {m - 1} ^ {m}}}{\sigma_ {0} ^ {m - 1}}
$$

small. Clearly, if $t \to \infty$, then $n(t) \to \infty$ also. Therefore, if we can ensure that

$$
\sum_ {m = 1} ^ {\infty} \frac {\sqrt {\sigma_ {m - 1} ^ {m}}}{\sigma_ {0} ^ {m - 1}} <   \infty ,
$$

we are done. There are many choices for $k(i)$ which can accomplish this. For example, if we choose $k(i)$ such that

$$
\sigma_ {k (i) - 1} <   i ^ {2} \leq \sigma_ {k (i)} \tag {5.4}
$$

we can easily check that

$$
\sqrt {\sigma_ {m - 1} ^ {m}} / \sigma_ {0} ^ {m - 1} \leq \sqrt {2 m - 1 + \Lambda} / (m - 1) ^ {2}
$$

and therefore the infinite series above converges. This proves (i) of Definition 5.2.

Next, we need to verify condition (ii) in Definition 5.2. We have

$$
\begin{aligned} \| U (t + h, t) S (t) x - S (t + h) x \| &= \left\| \prod_ {t} ^ {t + h} S (t) x - S (t + h) x \right\| \\ &\leq \left\| \prod_ {t} ^ {t + h} S (t) x - S \left(\sigma_ {t} ^ {t + h}\right) S (t) x \right\| \\ + \left\| S (\sigma_ {t} ^ {t + h}) S (t) x - S (h) S (t) x \right\|. \\ \end{aligned}
$$

The second term above can be estimated as follows:

$$
\begin{aligned} \| S (\sigma_ {t} ^ {t + h}) x - S (h) S (t) x \| &\leq \left| \sigma_ {t} ^ {t + h} - h \right| \cdot \| A ^ {0} S (t) x \| \\ &\leq \frac {\left| \sigma_ {t} ^ {t + h} - h \right|}{t} \rho (x, X ^ {*}) \\ \end{aligned}
$$

$$
\leq \frac {\Lambda}{t} \rho (x, X ^ {*}),
$$

where the first inequality follows from (4.5), and the second one from (2.14). Therefore, the last term in (5.5) can be made as small as desired by choosing $t$ large enough.

Finally, we estimate the remaining term:

$$
\begin{array}{l} \left\| \prod_ {t} ^ {t + h} S (t) x - S \left(\sigma_ {t} ^ {t + h}\right) S (t) x \right\| = \left\| \prod_ {n} ^ {n + p} S (t) x - S \left(\sigma_ {n} ^ {n + p}\right) S (t) x \right\| \\ \leq \sum_ {m = n + 1} ^ {n + p} \left\| S \left(\sigma_ {m - 1} ^ {m}\right) S \left(\sigma_ {n} ^ {m - 1}\right) S (t) x - \prod_ {m - 1} ^ {m} S \left(\sigma_ {n} ^ {m - 1}\right) S (t) x \right\| \\ = \sum_ {m = n + 1} ^ {n + p} \left\| S \left(\sigma_ {m - 1} ^ {m}\right) S \left(\sigma_ {n} ^ {m - 1} + t\right) x - \prod_ {m - 1} ^ {m} S \left(\sigma_ {n} ^ {m - 1} + t\right) x \right\| \\ \leq \sum_ {m = n + 1} ^ {n + p} \sqrt {d _ {m} \sigma_ {m - 1} ^ {m}} \| A ^ {0} S (\sigma_ {n} ^ {m - 1} + t) x \| \\ \leq \sum_ {m = n + 1} ^ {n + p} \sqrt {d _ {m} \sigma_ {m - 1} ^ {m}} \frac {\rho (x , X ^ {*})}{\sigma_ {n} ^ {m - 1} + t} \\ \leqq \sqrt {\Lambda} \rho (x, X ^ {*}) \sum_ {m = n + 1} ^ {n + p} \frac {\sqrt {\sigma_ {m - 1} ^ {m}}}{\sigma_ {0} ^ {m - 1} - \lambda_ {k (n)}} \\ \leq \sqrt {\Lambda} \rho (x, X ^ {*}) \sum_ {m = n + 1} ^ {n + p} \frac {\sqrt {\sigma_ {m - 1} ^ {m}}}{\sigma_ {0} ^ {m - 1} - \Lambda}, \\ \end{array}
$$

where the first inequality follows from (5.2), the second inequality from (4.4), and the third one from (2.14). If $k(i)$ is chosen as in (5.4), it is easy to check, as above, that

$$
\sum_ {m = n + 1} ^ {n + p} \frac {\sqrt {\sigma_ {m - 1} ^ {m}}}{\sigma_ {0} ^ {m - 1} - \Lambda} \leqq \sum_ {m = n + 1} ^ {n + p} \frac {\sqrt {2 m - 1 + \Lambda}}{(m - 1) ^ {2} - \Lambda} \rightarrow 0
$$

as $n\to \infty$. This proves (ii) of Definition 5.2.

COROLLARY 5.1. There exists a proper, closed convex function $f$ in $l^2$ such that given any bounded positive sequence $\{\lambda_j\}_{j=1}^\infty$, there exists a point $x \in D(f)$ for which PPA starting at $x$, $x_{k+1} = (x_k)_{\lambda_{k+1}}$ converges weakly, but not strongly to a minimizing point of $f$.

Proof. By Baillon's theorem [2], there exists a function $f$ in $H = l^2$ and a starting point $x$ such that $S(t)x$ converges weakly but not strongly to a minimizer of $f$. By Theorem 5.1, $U(t, s)$, defined above, is asymptotically equivalent to $S(t)$. Therefore, by Lemma 5.1, there exists a point $\bar{x}$ such that $U(t, s)\bar{x}$ also converges weakly but not strongly to a minimizer of $f$.

Acknowledgments. The author thanks the two anonymous referees for their helpful comments.

# REFERENCES

[1] J. P. AUBIN AND I. EKELAND, Applied Nonlinear Analysis, Interscience Publications, John Wiley, New York, 1984.  
[2] J. B. BAILLON, Un exemple concernant le comportement asymptotique de la solution due problème $du/dt + \partial\varphi(u) \ni 0$, J. Funct. Anal., 28 (1978), pp. 369–376.  
[3] H. BRÈZIS, Opérateurs Maximaux Monotones, Mathematics Studies No. 5, North-Holland, Amsterdam 1973.  
[4] H. BRÉZIS AND P. L. LIONS, Produits infinis de résolvantes, Israel J. Math., 29 (1978), pp. 329-345.  
[5] R. E. BRUCK, Asymptotic convergence of nonlinear contraction semigroups in Hilbert spaces, J. Funct. Anal., 18 (1975), pp. 15-26.  
[6] N. DUNFORD AND J. T. SCHWARTZ, Linear Operators, Part I: General Theory, Interscience Publications, John Wiley, New York, 1988.  
[7] O. GÜLER, New proximal point algorithms for convex minimization, Math. Programming, submitted.  
[8] Y. KOBAYASHI, Difference approximation of Cauchy problems for quasidissipative operators and generation of nonlinear semigroups, J. Math. Society Japan, 27 (1975), 640–665.  
[9] K. KOBAYASI, Y. KOBAYASHI, AND S. OHARU, Nonlinear evolution operators in Banach spaces, Osaka. J. Math., 21 (1984), pp. 281-310.  
[10] B. MARTINET, Regularisation, d'inéquations variationelles par approximations successives, Revue Française d'Informatique et de Recherche Operationnelle, 1970, pp. 154–159.  
[11] G. MINTY, Monotone (nonlinear) operators in a Hilbert space, Duke Math. J., 29 (1962), pp. 341-348.  
[12] J. J. MOREAU, Proximité et dualité dans un espace Hilbertien, Bull. Soc. Math., France, 93 (1965), pp. 273–299.  
[13] G. B. PASSTY, Preservation of the asymptotic behavior of a nonlinear contraction semigroup by backward differencing, Houston J. Math., 7 (1981), pp. 103-110.  
[14] N. H. PAVEL, Nonlinear Evolution Operators and Semigroups, Lecture Notes in Mathematics, Vol. 1260, Springer-Verlag, New York, 1987.  
[15] S. REICH, On infinite products of resolvents, Atti. Accad. Naz. Lincei, 63 (1977), pp. 338-340.  
[16] R. T. ROCKAFELLAR, Convex Analysis, Princeton University Press, Princeton, NJ, 1970.  
[17] ——, Monotone operators and the proximal point algorithm, SIAM J. Control Optim., 14 (1976), pp. 877–898.  
[18] ——, Augmented Lagrangians and applications of the proximal point algorithm in convex programming, Math. Oper. Res., 1 (1976), pp. 97–116.
