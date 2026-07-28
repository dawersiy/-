# INERTIAL PROXIMAL METHOD FOR MIXED QUASI VARIATIONAL INEQUALITIES

M. A. NOOR, M. AKHTER AND K. I. NOOR

ABSTRACT. In this paper, we use the auxiliary principle technique to suggest and analyze an inertial proximal method for a class of mixed quasi variational inequalities. We have shown that the convergence of the proposed method requires only pseudomonotonicity, which is a weaker condition than monotonicity. The proposed method includes the classical proximal method as a special case. Since the mixed quasi variational inequalities include variational and complementarity problems as special cases, the result proved in this paper continue to hold for these problems.

# 1. INTRODUCTION

Mixed quasi variational inequality is a useful and significant generalization of variational inequalities with a wide range of applications in network, industry, finance, economics, optimization, pure and applied sciences. There are several numerical methods including resolvent, operator-splitting and the auxiliary principle techniques. The auxiliary principle technique has been used to develop some very efficient and powerful numerical methods for solving mixed quasi variational inequalities, see, for example, $[3,5,7,9,13,14,17]$ and the references therein.

In this paper, we use the auxiliary principle technique to suggest and analyze an inertial proximal method for solving mixed quasi variational inequalities. Inertial proximal methods were introduced and studied by Alvarez [1] and Alvarez and Attouch [2] for maximal monotone operators via the discretization of second order differential equations in time. Noor [14] considered these methods for general variational inequalities and studied their convergence. It

Received November 28, 2002.

2000 Mathematics Subject Classification: 49J40, 90C33.

Key words and phrases: Variational inequalities, auxiliary principle, inertial proximal methods, convergence, skew-symmetric functions.

is worth mentioning that the inertial proximal methods include the classical proximal methods as special cases, which have been studied extensively in recent years, see $[3,6,8,12,15-17]$. If the nonlinear term $\varphi(\cdot,\cdot)$ involving the mixed quasi variational inequalities is skew-symmetric function, then the convergence of the proximal method requires only pseudomonotonicity of the operator, which is a weaker condition than monotonicity. Since the mixed quasi variational inequalities include the (quasi) variational inequalities and related optimization problems as special cases, so our results continue to hold for these problems. Our results can be viewed as significant extensions and improvement of the previously known results for solving variational inequalities.

# 2. PRELIMINARIES

Let $H$ be a real Hilbert space, whose inner product and norm are denoted by $\langle\cdot,\cdot\rangle$ and $\|\cdot\|$ respectively. Let $K$ be a nonempty closed convex set in $H$. Let $\varphi(\cdot,\cdot):H\times H\to R\cup\{+\infty\}$ be a continuous bifunction. For a given nonlinear operator $T:H\to H$, consider the problem of finding $u\in H$ such that

$$
\langle T u, v - u \rangle + \varphi (v, u) - \varphi (u, u) \geq 0, \quad \forall v \in H. \tag {2.1}
$$

Inequality of type (2.1) is called the mixed quasi variational inequality problem. If the bifunction $\varphi(\cdot,\cdot)$ is a proper, convex and lower semicontinuous with respect to the first argument, then it is known [11] that problem (2.1) is equivalent to the fixed-point and the resolvent equations. This fixed-point formulation has been used to suggest a number of iterative methods for solving mixed quasi variational inequalities (2.1). For recent development in this area, see Noor [11-13].

If $\varphi(v, u) \equiv \varphi(v), \forall u \in H$, then problem (2.1) is equivalent to finding $u \in H$ such that

$$
\langle T u, v - u \rangle + \varphi (v) - \varphi (u) \geq 0, \quad \forall v \in H, \tag {2.2}
$$

which is known as the variational inequality of the second kind or mixed variational inequality, see [5,7, 9-13].

We remark that if K is a closed convex set in H and

$$
\phi (u) = I _ {K} (u) = \left\{ \begin{array}{l l} 0, & \text {if} u \in K \\ + \infty , & \text {otherwise}, \end{array} \right.
$$

is the indicator function of $K$, then the problem (2.2) is equivalent to finding $u \in K$ such that

$$
\langle T u, v - u \rangle \geq 0, \quad \forall v \in K, \tag {2.3}
$$

which is called the classical variational inequality problem. It turned out that a wide class of moving, free, unilateral, obstacle and equilibrium problems can be studied by the variational inequality (2.3), see $[1-17]$ and the references therein.

We also need the following concepts and results.

Lemma 2.1. $\forall u, v \in H$,

$$
2 \langle u, v \rangle = \| u + v \| ^ {2} - \| u \| ^ {2} - \| v \| ^ {2}. \tag {2.4}
$$

Definition 2.1. The bifunction $\varphi(\cdot,\cdot):H\times H\to R\cup\{+\infty\}$ is called skew-symmetric, if,

$$
\varphi (u, u) - \varphi (u, v) - \varphi (v, u) - \varphi (v, v) \geq 0 \quad \forall u, v \in H.
$$

It is easy to see that if the bifunction $\varphi(\cdot, \cdot)$ is linear in both variables, then the bifunction $\varphi(\cdot, \cdot)$ is nonnegative.

# 3. MAIN RESULTS

In this section, we suggest and analyze an inertial proximal method for mixed quasi variational inequalities (2.1) using the auxiliary principle technique as developed by Noor [12,13].

For a given $u \in H$, consider the auxiliary problem of finding a unique $w \in H$ such that

$$
\langle \rho T w + w - u - \alpha (u - u), v - u \rangle + \rho \varphi (v, w) - \rho \varphi (w, w) \geq 0, \quad \forall v \in H, \tag {3.1}
$$

where $\rho > 0$ and $\alpha > 0$ are constants.

We note that if w = u, then clearly w is solution of the mixed quasi variational inequality (2.1). This observation enables us to suggest and analyze the following proximal method for mixed quasi variational inequality (2.1).

Algorithm 3.1. For a given $u_0 \in H$, compute the approximate solution $u_{n+1}$ by the iterative scheme

$$
\langle T u _ {n + 1} + u _ {n + 1} - u _ {n} - \alpha_ {n} (u _ {n} - u _ {n - 1}), v - u _ {n + 1} \rangle
$$

$$
+ \rho \varphi (v, u _ {n + 1}) - \rho \varphi (u _ {n + 1}, u _ {n + 1}) \geq 0, \quad \forall v \in H.
$$

Note that if $\varphi(v, u) = \varphi(v), \quad \forall u \in H$ , then Algorithm 3.1 collapses to:

Algorithm 3.2. For a given $u_{0}$, compute the approximate solution $u_{n+1}$ by the iterative scheme

$$
\begin{aligned} \langle \rho T u _ {n + 1} + u _ {n + 1} - u _ {n} - \alpha_ {n} (u _ {n} - u _ {n - 1}), v - u _ {n + 1} \rangle \\ + \rho \varphi (v) - \rho \varphi (u _ {n + 1}) &\geq 0, \quad \forall v \in H, \\ \end{aligned}
$$

If the bifunction $\varphi(\cdot,\cdot)$ is a proper, convex and lower-semicontinuous with respect to the first variable, then Algorithm 3.1 reduces to:

Algorithm 3.3. For a given $u_0 \in H$, compute the approximate solution by the iterative scheme.

$$
u _ {n + 1} = J _ {\partial \varphi (u _ {n + 1})} [ u _ {n} - \rho T u _ {n + 1} + \alpha_ {n} (u _ {n} - u _ {n - 1}) ], \quad n = 0, 1, 2, \dots
$$

where $J_{\partial\varphi(u)} = (I + \rho\partial\varphi(\cdot, u))^{-1}$ is the resolvent operator associated with the maximal monotone operator $\partial\varphi(v, u)$, the subdifferential of a convex, proper and lower-semicontinuous bifunction with respect to first variable, see Noor [11].

Algorithm 3.3 appears to be a new one.

If $\varphi$ is an indicator function of a closed convex set K in H, then Algorithm 3.2 is equivalent to the following method for solving variational inequalities (2.3), which is known as the proximal method.

Algorithm 3.4. For a given $u_{0}$, compute the approximate solution $u_{n+1}$ by the iterative scheme

$$
\rho \langle T u _ {n + 1} + u _ {n + 1} - u _ {n} - \alpha_ {n} (u _ {n} - u _ {n - 1}), v - u _ {n + 1} \rangle \geq 0, \quad \forall v \in K,
$$

which can be written as

$$
u _ {n + 1} = P _ {K} [ u _ {n} - \rho T u _ {n + 1} + \alpha_ {n} (u _ {n} - u _ {n - 1}) ], \quad n = 0, 1, 2, \dots
$$

where $P_{K}$ is the projection of H onto K. For the convergence of Algorithm 3.4, see Noor [14]. We would like to point out that for $\alpha_{n}=0$, the inertial proximal methods are equivalent to the proximal methods, which have been studied extensively.

We now study the convergence analysis of Algorithm 3.1. The analysis is in the spirit of Noor [12] and Alvarez [1].

Lemma 3.1. Let $\bar{u} \in H$ be a solution of (2.1) and $u_{n+1}$ be the approximate solution obtained from Algorithm 3.1. If the operator $T : H \to H$ is pseudomonotone and the bifunction $\varphi(\cdot, \cdot)$ is skew-symmetric, then

$$
\begin{aligned} \| u _ {n + 1} - \bar {u} \| ^ {2} &\leq \| u _ {n} - \bar {u} \| ^ {2} - \| u _ {n + 1} - u _ {n} - \alpha_ {n} \left(u _ {n} - u _ {n - 1}\right) \| ^ {2} \tag {3.3} \\ + \alpha_ {n} \{\| u _ {n} - \bar {u} \| ^ {2} - \| \bar {u} - u _ {n - 1} \| ^ {2} + 2 \| u _ {n} - u _ {n - 1} \| ^ {2} \}. \\ \end{aligned}
$$

Proof. Let $\bar{u} \in H$ be a solution of (2.1). Then

$$
\langle T \bar {u}, v - \bar {u} \rangle + \varphi (v, \bar {u}) - \varphi (\bar {u}, \bar {u}) \geq 0, \quad \forall v \in H,
$$

which implies that

$$
\langle T v, v - \bar {u} \rangle + \varphi (v, \bar {u}) - \varphi (\bar {u}, \bar {u}) \geq 0, \tag {3.4}
$$

since $T$ is a pseudomonotone operator.

Taking $v = u_{n + 1}$ in (3.4), we have

$$
\langle T u _ {n + 1}, u _ {n + 1} - \bar {u} \rangle + \varphi (u _ {n + 1}, \bar {u}) - \varphi (\bar {u}, \bar {u}) \geq 0. \tag {3.5}
$$

Now taking $v = \bar{u}$ in (3.2), we obtain

$$
\begin{aligned} \langle \rho T u _ {n + 1} + u _ {n + 1} - u _ {n} - \alpha_ {n} \left(u _ {n} - u _ {n - 1}\right), \bar {u} - u _ {n + 1} \rangle \tag {3.6} \\ + \rho \varphi (\bar {u}, u _ {n + 1}) - \rho \varphi (u _ {n + 1}, u _ {n + 1}) &\geq 0. \\ \end{aligned}
$$

From (3.5) and (3.6), we have

$$
\begin{array}{l} \langle u _ {n + 1} - u _ {n} - \alpha_ {n} (u _ {n} - u _ {n - 1}), \bar {u} - u _ {n + 1} \rangle \\ \begin{array}{l} \geq \rho \left\langle T u _ {n + 1}, u _ {n + 1} - \bar {u} \right\rangle + \rho \varphi \left(u _ {n + 1}, u _ {n + 1}\right) - \rho \varphi (\bar {u}, u _ {n + 1}) \\ > \alpha_ {2} (\bar {u}, \bar {u}) - \alpha_ {3} (\bar {u}, u _ {n + 1}) - \alpha_ {4} (u _ {n + 1}, \bar {u}) + \alpha_ {5} (u _ {n + 1}, u _ {n + 1}) \end{array} \tag {3.7} \\ \geq \rho \varphi (\bar {u}, \bar {u}) - \rho \varphi (\bar {u}, u _ {n + 1}) - \rho \varphi (u _ {n + 1}, \bar {u}) + \rho \varphi (u _ {n + 1}, u _ {n + 1}) \\ \geq 0, \\ \end{array}
$$

where we have used the fact that the bifunction $\varphi (\cdot ,\cdot)$ is skew-symmetric.

One can rewrite (3.7) in the form

$$
\langle u _ {n + 1} - u _ {n}, \bar {u} - u _ {n - 1} \rangle \geq \alpha_ {n} \langle u _ {n} - u _ {n - 1}, \bar {u} - u _ {n} + u _ {n} - u _ {n + 1} \rangle . \tag {3.8}
$$

Using Lemma 2.1 and rearranging the terms in (3.8), one can easily obtain (3.3), the required result.

Theorem 3.1. Let $H$ be a finite dimensional space. Let $u_{n+1}$ be an approximate solution obtained from Algorithm 3.1 and $\bar{u} \in H$ be a solution of (2.1). If there exists $\alpha \in (0,1)$ such that $0 \leq \alpha_n \leq \alpha, \quad \forall n \in N$ and

$$
\sum_ {n = 1} ^ {\infty} \alpha_ {n} \| u _ {n} - u _ {n - 1} \| ^ {2} \leq \infty ,
$$

then $\lim_{n\to \infty}u_n = \bar{u}$

Proof. Let $\bar{u} \in H$ be a solution of (2.1). First we consider the case $\alpha_{n} = 0$. In this case, we see from (3.3) that the sequence $\{\|\bar{u} - u_n\|\}$ is nonincreasing and consequently $\{u_n\}$ is bounded. Also from (3.3), we have

$$
\sum_ {n = 0} ^ {\infty} \left\| u _ {n + 1} - u _ {n} \right\| ^ {2} \leq \left\| u _ {0} - \bar {u} \right\| ^ {2},
$$

which implies that

$$
\lim _ {n \to \infty} \| u _ {n + 1} - u _ {n} \| = 0. \tag {3.9}
$$

Let $\hat{u}$ be a cluster point of $\{u_n\}$ and the subsequence $\{u_{n_j}\}$ of the sequence $\{u_n\}$ converge to $\hat{u} \in H$. Replacing $u_n$ by $u_{n_j}$ in (3.2) and taking the limit $n_j \to \infty$ and using (3.9), we have

$$
\langle T \hat {u}, v - \hat {u} \rangle + \varphi (v, \hat {u}) - \varphi (\hat {u}, \hat {u}) \geq 0, \quad \forall v \in H,
$$

which implies that $\hat{u}$ solves the mixed quasi variational inequality (2.1) and

$$
\| u _ {n + 1} - u _ {n} \| ^ {2} \leq \| u _ {n} - \bar {u} \| ^ {2}.
$$

Thus it follows from the above inequality that the sequence $\{u_n\}$ has exactly one cluster point $\hat{u}$ and $\lim_{n\to \infty}u_n = \hat{u}$, the required result. Now we consider the case $\alpha_{n} > 0$. From (3.3) and using the technique of Alvarez [1] and Alvarez and Attouch [2], we have

$$
\begin{aligned} \sum_ {n &= 1} ^ {\infty} \left\| u _ {n + 1} - u _ {n} - \alpha_ {n} (u _ {n} - u _ {n - 1}) \right\| ^ {2} \\ &\leq \| u _ {0} - \bar {u} \| ^ {2} + \sum_ {n = 1} ^ {\infty} (\alpha \| u _ {n} - \bar {u} \| ^ {2} + 2 \| u _ {n} - u _ {n - 1} \| ^ {2}) \\ &\leq \infty , \\ \end{aligned}
$$

which implies that

$$
\lim _ {n \to \infty} \| u _ {n + 1} - u _ {n} - \alpha_ {n} (u _ {n} - u _ {n - 1}) \| = 0.
$$

Repeating the above arguments as in the case $\alpha_{n}=0$, one can easily show that $\lim_{n\to\infty}u_{n}=\bar{u}$, the required result. ☐

# REFERENCES

1. F. Alvarez, On the minimization property of a second order dissipative system in Hilbert space, SIAM J. Control Optim. 38 (2000), 1102-1119.  
2. F. Alvarez and H. Attouch, An inertial proximal method for maximal monotone operators via discretization of a nonlinear oscillator damping, Set-Valued Anal. 9 (2001), 3-11.  
3. N. El Farouq, Pseudomonotone variational inequalities: convergence of proximal methods, J. Optim. Theory Appl. 109 (2001), 311-326.  
4. F. Giannessi, A. Maugeri and P. M. Pardalos, Equilibrium Problems: Nonsmooth Optimization and Variational inequality Models, Kluwer Academic Publishers, Dordrecht, Holland, 2001.  
5. R. Glowinski, J. L. Lions and R. Tremolieres, Numerical Analysis of Variational Inequalities, North-Holland, Amsterdam, Holland, 1981.  
6. B. S. He and L. Z. Liao, Improvement of some projection methods for monotone nonlinear variational inequalities, J. Optim. Theory Appl. 112 (2002), 111-128.  
7. D. Kinderlehrer and G. Stampacchia, An Introduction to Variational Inequalities and Their Applications, SIAM, Philadelphia, PA (2000).  
8. B. Martinet, Regularisation d'inequations variationelles par approximations successive, Rev. d'Aut. Inform, Rech. Oper. 3 (1970), 154-159.  
9. M. Aslam Noor, Some recent advances in variational inequalities, Part I, basic concepts, New Zealand J. Math. 26 (1997), 53-80.  
10. M. Aslam Noor, Some recent advances in variational inequalities, Part II, other concepts, New Zealand J. Math. 26 (1997), 229-255.  
11. M. Aslam Noor, Set-valued mixed quasi variational inequalities and implicit resolvent equations, Math. Comput. Modelling 29 (1999), 1-11.  
12. M. Aslam Noor, Proximal methods for mixed quasi variational inequalities, J. Optim. Theory Appl. 115 (2002), 447-452.  
13. M. Aslam Noor, Mixed quasi variational inequalities, to appear in Appl. Math. Comput. (2004).  
14. M. Aslam Noor, Some developments in general variational inequalities, to appear Appl. Math. Comput. (2004).  
15. R. T. Rockafellar, Monotone operators and the proximal point algorithms, SIAM J. Control Optim. 14 (1976), 877-898.  
16. P. Tseng, On linear convergence of iterative methods for variational inequality problem, J. Comput. Appl. Math. 60 (1995), 237-252.  
17. D. L. Zhu and P. Marcotte, Cocoercivity and its role in the convergence of iterative schemes for solving variational inequalities, SIAM J. Optim. 6 (1996), 714-726.

M. A. NOOR

ETISALAT COLLEGE OF ENGINEERING

SHARJAH, UNITED ARAB EMIRATES

E-mail address: noor@ece.ac.ae

M. AKHTER

ETISALAT COLLEGE OF ENGINEERING

SHARJAH, UNITED ARAB EMIRATES

E-mail address: makhter@ece.ac.ae

K. I. NOOR

DEPARTMENT OF MATHEMATICS AND COMPUTER SCIENCE
COLLEGE OF SCIENCE

P. O. Box 17551, UNITED ARAB EMIRATES UNIVERSITY, AL-AIN UNITED ARAB EMIRATES

E-mail address: khalidan@uaeu.ac.ae
