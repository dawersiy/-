Xiaojun Chen · Masao Fukushima

# Proximal quasi-Newton methods for nondifferentiable convex optimization

Received October 3, 1995 / Revised version received August 20, 1998
Published online January 20, 1999

Abstract. This paper proposes an implementable proximal quasi-Newton method for minimizing a non-differentiable convex function $f$ in $\Re^n$. The method is based on Rockafellar's proximal point algorithm and a cutting-plane technique. At each step, we use an approximate proximal point $p^a(x_k)$ of $x_k$ to define a $v_k \in \partial_{\epsilon_k} f(p^a(x_k))$ with $\epsilon_k \leq \alpha \|v_k\|$, where $\alpha$ is a constant. The method monitors the reduction in the value of $\|v_k\|$ to identify when a line search on $f$ should be used. The quasi-Newton step is used to reduce the value of $\|v_k\|$. Without the differentiability of $f$, the method converges globally and the rate of convergence is Q-linear. Superlinear convergence is also discussed to extend the characterization result of Dennis and Moré. Numerical results show the good performance of the method.

Key words. nondifferentiable convex optimization – proximal point – quasi-Newton method – cutting-plane method – bundle methods

# 1. Introduction

In this paper we consider the minimization problem

$$
\min _ {x \in \Re^ {n}} f (x), \tag {1}
$$

where $f: \Re^n \to \Re$ is a possibly nondifferentiable convex function. We particularly assume that $f$ is finite-valued and hence continuous everywhere on $\Re^n$.

This problem can be transformed into a differentiable convex minimization problem

$$
\min _ {x \in \Re^ {n}} F (x), \tag {2}
$$

where

$$
F (x) := \min \left\{f (y) + \frac {1}{2} \mu \| y - x \| ^ {2} \mid y \in \Re^ {n} \right\}. \tag {3}
$$

Here $\mu$ is a positive number and $\| \cdot \|$ denotes the Euclidean norm. The function $F$ is a differentiable convex function defined on the whole space $\Re^n$ and is called the

X. Chen: Department of Mathematics and Computer Science, Shimane University, Matsue 690-8504, Japan, e-mail: chen@math.shimane-u.ac.jp. Some of this work was supported by the Australian Research Council.

M. Fukushima: Department of Applied Mathematics and Physics, Graduate School of Informatics, Kyoto University, Kyoto 606-8501, Japan, e-mail: fuku@kuamp.kyoto-u.ac.jp. This author's work was supported in part by the Scientific Research Grant-in-Aid from the Ministry of Education, Science and Culture, Japan.

Mathematics Subject Classification (1991): 65K05, 90C30

Moreau-Yosida regularization of $f$. Minimizing $f$ and $F$ are equivalent problems, in the sense that the solution sets of problems (1) and (2) coincide with each other [13]. We denote the unique minimizer in (3) by $p(x)$ and we call it the proximal point of $x$. The derivative of $F$ is given by

$$
G (x) := \nabla F (x) = \mu (x - p (x)) \in \partial f (p (x)), \tag {4}
$$

where $\partial f$ is the subdifferential mapping of f in the sense of convex analysis [32]. The function G is globally Lipschitz continuous with modulus $\mu$ [13]. Recently some important properties of F have been studied in [20,25,28]. Proximal Newton-type methods have received a lot of attention in the literature [2–5, 12, 19, 21–23, 29, 31, 36].

A quasi-Newton method for solving (2) is defined by

$$
x _ {k + 1} = x _ {k} - \tau_ {k} B _ {k} ^ {- 1} G (x _ {k}), \tag {5}
$$

where $\tau_{k}$ is the stepsize and $B_{k}$ is generated according to a quasi-Newton formula, using

$$
s _ {k} = x _ {k + 1} - x _ {k}, \quad t _ {k} = G (x _ {k + 1}) - G (x _ {k}), \tag {6}
$$

for example, the BFGS formula:

$$
B _ {k + 1} = B _ {k} - \frac {B _ {k} s _ {k} s _ {k} ^ {T} B _ {k}}{s _ {k} ^ {T} B _ {k} s _ {k}} + \frac {t _ {k} t _ {k} ^ {T}}{t _ {k} ^ {T} s _ {k}}. \tag {7}
$$

Global convergence of the BFGS method with line search just requires Lipschitz continuity of $G$ [26]. Superlinear convergence requires the strong differentiability of $G$ at $x^{*}$ [2,6,14].

Let $\partial G(x)$ denote the set of generalized Jacobians of $G$ at $x$, which is defined by

$$
\partial G (x) = \operatorname{co} \left\{V \in \Re^ {n \times n} \mid V = \lim _ {x _ {i} \to x} \nabla G (x _ {i}), x _ {i} \in \Omega_ {G} \right\},
$$

where $\Omega_G = \{x \in \Re^n \mid G \text{ is differentiable at } x\}$ and co stands for the convex hull of a set. Then the generalized Newton method with line search for (2) is defined by

$$
x _ {k + 1} = x _ {k} - \tau_ {k} V _ {k} ^ {- 1} G (x _ {k}), \tag {8}
$$

where $V_{k} \in \partial G(x_{k})$. The superlinear convergence of (8) requires the regularity and the semismoothness of $G$ at a solution [27,30].

Now come implementation issues: Since it is usually impossible to obtain the exact proximal point $p(x_k)$ for a given $x_k$, we need to approximate it by solving the minimization problem in (3) only approximately. Rockafellar [33] gave some approximation criteria for proximal point algorithms. Recently Bonnans, Gilbert, Lemaréchal and Sagastizábal [2] explored preliminary conceptual optimization methods combining the Moreau-Yosida regularization and quasi-Newton methods (5). Zhu [36] proved that the sequence of function values generated by the method in [2] converges linearly. Lemaréchal and Sagastizábal [21] produced implementable versions of the methods and showed their good numerical behaviour even for large-scale problems. Fukushima and Qi [12] first studied Q-superlinear convergence of optimization methods combining the Moreau-Yosida regularization and the generalized Newton method (8). To ensure global

convergence, a step size $\tau_{k} = \gamma^{m_{k}}$ is determined by the following line search at each step of the algorithm in [12]: Find the smallest nonnegative integer $m = m_{k}$ satisfying

$$
F ^ {a} (x _ {k} + \gamma^ {m} d _ {k}, \epsilon_ {k + 1}) \leq F ^ {a} (x _ {k}, \epsilon_ {k}) + \sigma \gamma^ {m} G ^ {a} (x _ {k}, \epsilon_ {k}) ^ {T} d _ {k} + \epsilon_ {k}, \tag {9}
$$

where $\gamma \in (0,1),\epsilon_k > \epsilon_{k + 1}\geq 0,d_k\in \Re^n,\sigma \in (0,1)$ and $F^{a}$ and $G^{a}$ are approximations of $F$ and $G$, respectively. However, for each positive integer $m\leq m_{k}$, the inner optimization problem in (3) should be solved approximately to a required accuracy. Hence the line search (9) on $F$ is not necessarily easy to implement. Furthermore their algorithm uses an approximation $\tilde{V}_k$ of a generalized Jacobian $V_{k}\in \partial G(x_{k})$, but the choice of $\tilde{V}_k$ is not specified. Mifflin [22] presented an implementable quasi-second-order proximal bundle method, in which a line search on $f$ is used. However, convergence rate of the proximal bundle method is not given in [22]. An important question remains to be studied: Can one have a globally and superlinearly convergent algorithm for (1) without using a line search on $F$ or its approximation?

The purpose of this paper is to give an affirmative answer to this question by presenting a globally and superlinearly convergent algorithm for (1) with line search on $f$. In this algorithm, we first find an approximate proximal point $p^a(x_k)$ of $x_k$ by utilizing a cutting-plane technique such that $v_k := \mu(x_k - p^a(x_k)) \in \partial_{\epsilon_k} f(p^a(x_k))$ for some $\epsilon_k \in (0, \alpha \| v_k \|]$, where $\alpha$ is a constant, and $\partial_\epsilon f(x)$ denotes for any $\epsilon \geq 0$ the $\epsilon$ -subdifferential of $f$ at $x$, i.e.,

$$
\partial_ {\epsilon} f (x) = \{g \in \Re^ {n} \mid f (y) \geq f (x) + g ^ {T} (y - x) - \epsilon , y \in \Re^ {n} \}.
$$

Then we use $G^{a}(x_{k}) := v_{k}$ as an approximation of $G(x_{k})$ in a quasi-Newton method (5) and we construct $B_{k+1}$ by using $t_{k} := G^{a}(x_{k+1}) - G^{a}(x_{k})$ in (6) and (7). The stepsize $\tau_{k}$ is determined either from the value of $\|G^{a}(x_{k})\|$ or by performing a line search on the function f. More specifically, if the value of $\|G^{a}(x_{k})\|$ has been reduced sufficiently, we let $\tau_{k} = 1$ ; otherwise, a line search on f is used to determine $\tau_{k} \in (0, 1]$.

We establish global, Q-linear and Q-superlinear convergence of the proposed algorithm. Global convergence requires the boundedness of the level sets of f. Q-linear convergence requires the strong convexity of f and semismoothness of G at $x^{*}$. Q-superlinear convergence requires strong differentiability of G at $x^{*}$, which extends the characterization result of Dennis and Moré [8]. Furthermore if $B_{k}$ is a “good” approximation of $V_{k} \in \partial G(x_{k})$ in the sense of [12], then Q-superlinear convergence only requires semismoothness of G at $x^{*}$. Proximal quasi-Newton methods with the BFGS update and the Broyden update are studied in [4,5,23,31].

# 2. Algorithm and global convergence

In this section we present the algorithm and show some important properties and global convergence of this algorithm. The proposed algorithm is doubly iterative. Each major iteration consists of inner iterations to solve the following minimization problem approximately by utilizing a cutting-plane technique:

$$
\min _ {y \in \Re^ {n}} f (y) + \frac {1}{2} \mu \| y - x _ {k} \| ^ {2}, \tag {10}
$$

where $x_{k}$ is a current iteration point given at the beginning of the major iteration k. More specifically, the inner iteration generates a sequence $\{y_{j}\}$ as follows: For $j = 1, 2, \ldots$, let $y_{j}$ be the (unique) solution of the problem

$$
\min _ {y \in \Re^ {n}} f _ {k, j} (y) + \frac {1}{2} \mu \| y - x _ {k} \| ^ {2}, \tag {11}
$$

where $f_{k,j}$ is the polyhedral convex function defined by

$$
f _ {k, j} (y) := \max _ {i = 0, 1, \dots , j - 1} \left\{f (y _ {i}) + g _ {i} ^ {T} (y - y _ {i}) \right\} \tag {12}
$$

with the pairs of n-vectors $y_{i}$ and $g_{i} \in \partial f(y_{i})$ , $i = 0, 1, \ldots, j - 1$ , which constitute a bundle generated sequentially starting from an arbitrary point $y_{0} \in \Re^{n}$ and $g_{0} \in \partial f(y_{0})$ . Here $f_{k,j}$ is an approximation function of f around $x_{k}$ . Since $y_{j}$ is the solution of the subproblem at the jth inner iteration within the kth major iteration, it would be more appropriate to denote $y_{k,j}$ . To avoid the double subscripts, however, we simply denote $y_{j}$ , which will not cause any confusion.

Note that (11) is equivalent to the quadratic programming problem:

$$
\min _ {(y, w) \in \Re^ {n + 1}} w + \frac {1}{2} \mu \| y - x _ {k} \| ^ {2} \tag {13}
$$

subject to $f(y_{i}) + g_{i}^{T}(y - y_{i}) \leq w, \quad i = 0,1,\dots ,j - 1.$

Kiwiel [16] presented a finite algorithm for solving this special quadratic programming problem.

The inner iteration is terminated if one of the following two conditions is satisfied:

$$
f (x _ {k}) - f _ {k, j} (y _ {j}) <   \rho , \tag {14}
$$

$$
f (y _ {j}) \leq f (x _ {k}) - \sigma_ {k} (f (x _ {k}) - f _ {k, j} (y _ {j})), \tag {15}
$$

where $\rho > 0$ and $\sigma_{k} \in (0, 1)$ are parameters. Notice that the common parameter $\rho$ is used throughout the whole (major) iterations of the algorithm, while $\sigma_{k}$ is dependent on the particular iteration k and may be controlled in an appropriate manner.

Since the definition (12) of $f_{k,j}$ and the subgradient inequality imply

$$
f _ {k, j} (y) \leq f (y) \quad \text { for   all } y \in \Re^ {n}, \tag {16}
$$

we have the inequalities

$$
\begin{aligned} f _ {k, j} (y _ {j}) &\leq f _ {k, j} (y _ {j}) + \frac {1}{2} \mu \| y _ {j} - x _ {k} \| ^ {2} \\ &= \min _ {y \in \Re^ {n}} \{f _ {k, j} (y) + \frac {1}{2} \mu \| y - x _ {k} \| ^ {2} \} \\ &\leq \min _ {y \in \Re^ {n}} \{f (y) + \frac {1}{2} \mu \| y - x _ {k} \| ^ {2} \} \\ &\leq f (x _ {k}) \tag {17} \\ \end{aligned}
$$

for all $j$. Therefore if (14) is satisfied, it follows from the inequalities (17) that

$$
f (y _ {j}) + \frac {1}{2} \mu \| y _ {j} - x _ {k} \| ^ {2} \leq \min _ {y \in \Re^ {n}} \{f (y) + \frac {1}{2} \mu \| y - x _ {k} \| ^ {2} \} + \rho ,
$$

which implies that, if $\rho$ is sufficiently small, then $y_{j}$ is a good approximation to the solution of problem (10), i.e., an approximate proximal point of $x_{k}$. However, (14) implies more than that. As shown in [11, Proposition 6], if (14) holds, then we have

$$
f (x _ {k}) \leq f (x) + \sqrt {2 \mu \rho} \| x - x _ {k} \| + \rho \quad \text {for all} x \in \Re^ {n}. \tag {18}
$$

This indicates that $x_{k}$ can be considered a good approximate solution of the original problem (1), provided that $\rho$ is sufficiently small. Hence we may terminate the major iteration of the algorithm.

Now consider condition (15). It was shown in [11, Proposition 3] that, as j increases, $f(y_{j})$ and $f_{k,j}(y_{j})$ get closer to each other and $y_{j}$ approaches the proximal point $p(x_{k})$. Thus (15) will be satisfied when $y_{j}$ becomes sufficiently close to $p(x_{k})$. So, once (15) is satisfied, we put $p^{a}(x_{k}) := y_{j}$ to use it as an approximate proximal point of $x_{k}$. Note that the closer $\sigma_{k}$ is to one, the better $p^{a}(x_{k})$ approximates the proximal point $p(x_{k})$.

Remark 1. Procedure (11)-(12) is the "pure" cutting-plane algorithm without any strategy for dropping useless cutting-planes. This is only for simplicity of presentation. Any improved cutting-plane type procedure [1,7,15,17] can be used as well to generate $\{y_j\}$ converging to the proximal point $p(x_k)$. Actually we used a modified version of the cutting plane method with resetting and deleting rules [1,7,17] in our numerical experiments reported in Section 4.

Now we state the algorithm.

Algorithm 1. Choose an initial point $x_0 \in \Re^n$, parameters $\rho > 0$, $\sigma, c, \gamma \in (0,1)$, a sufficiently large constant $M \geq f(x_0)$, and a sequence $\{\sigma_k\}$ such that $\sigma < \sigma_k < 1$. Let $k := 0$.

1. Solve subproblem (10) by the procedure (11)-(12) to obtain a point $y_{j}$ satisfying either (14) or (15). If (14) is satisfied, then terminate. If (15) is satisfied, then let $j_{k} := j$ and $p^{a}(x_{k}) := y_{j}$, and proceed to step 2.

2. Let

$$
v _ {k} := \mu (x _ {k} - p ^ {a} (x _ {k})).
$$

3. If $k = 0$, let $B_0 := (1 + \mu)I$. If $k \geq 1$, construct a symmetric positive definite matrix $B_k \in \Re^{n \times n}$ by using a quasi-Newton formula with $t_{k-1} := v_k - v_{k-1}$ and $s_{k-1} := x_k - x_{k-1}$.

4. Let $d_{k} := -(B_{k}^{-1} - \mu^{-1}I)v_{k}$. If k = 0, let $\eta_{1} := \|v_{0}\|$ and go to step 5. For $k \geq 1$, if $\|v_{k}\| \leq c\eta_{k}$ and $f(p^{a}(x_{k}) + d_{k}) \leq M$, let $\tau_{k} := 1$ and $\eta_{k+1} := \|v_{k}\|$ and go to step 6; otherwise, let $\eta_{k+1} := \eta_{k}$ and go to step 5.

5. Let $m_k$ be the smallest nonnegative integer $m$ such that

$$
f (p ^ {a} (x _ {k}) + \gamma^ {m} d _ {k}) \leq f (x _ {k}) - \frac {\gamma^ {m} \sigma}{\mu} \| v _ {k} \| ^ {2}.
$$

Set $\tau_{k}:=\gamma^{m_{k}}$.

6. Set $x_{k+1} := p^{a}(x_{k}) + \tau_{k}d_{k}, k := k + 1$ and return to step 1.

Note that, since $v_{k} = \mu (x_{k} - p^{a}(x_{k}))$ and $d_{k} = -(B_{k}^{-1} - \mu^{-1}I)v_{k}$, we have

$$
\begin{aligned} x _ {k + 1} &= x _ {k} - \mu^ {- 1} v _ {k} - \tau_ {k} (B _ {k} ^ {- 1} - \mu^ {- 1} I) v _ {k} \\ &= x _ {k} - (\tau_ {k} B _ {k} ^ {- 1} + (1 - \tau_ {k}) \mu^ {- 1} I) v _ {k}. \tag {19} \\ \end{aligned}
$$

Furthermore, by Theorem 3.1 in [20], if $f$ has a Hessian $\nabla^2 f(p(x_k))$, then $\nabla^2 F(x_k) = (\nabla^2 f(p(x_k))^{-1} + \mu^{-1}I)^{-1}$, and hence

$$
\begin{aligned} d _ {k} &\approx - (\nabla^ {2} F (x _ {k}) ^ {- 1} - \mu^ {- 1} I) \nabla F (x _ {k}) \\ &= - \nabla^ {2} f (p (x _ {k})) ^ {- 1} \nabla f (p (x _ {k})) \\ \end{aligned}
$$

whenever $B_{k}\approx \nabla^{2}F(x_{k})$

The BFGS method is the most successful quasi-Newton method for solving convex optimization problems $[9,10]$ and has the property that $B_{k+1}$ is symmetric positive definite if $B_{k}$ is symmetric positive definite and $s_{k}^{T}t_{k}>0$. Therefore we recommend to use the BFGS formula in step 3 of Algorithm 1. Furthermore, if $\tau_{k}=1$, then it follows from (19) and $v_{k}=G^{a}(x_{k})$ that

$$
x _ {k + 1} = x _ {k} - B _ {k} ^ {- 1} G ^ {a} (x _ {k})
$$

and

$$
B _ {k + 1} = \left\{ \begin{array}{l l} B _ {k} - \frac {B _ {k} s _ {k} s _ {k} ^ {T} B _ {k}}{s _ {k} ^ {T} B _ {k} s _ {k}} + \frac {t _ {k} t _ {k} ^ {T}}{s _ {k} ^ {T} t _ {k}}, & \text {if} s _ {k} ^ {T} t _ {k} > 0 \\ B _ {k}, & \text {otherwise,} \end{array} \right. \tag {20}
$$

where $t_{k}=G^{a}(x_{k+1})-G^{a}(x_{k})$ and $s_{k}=x_{k+1}-x_{k}$. Note that, in this process, $s_{k}^{T}t_{k}$ is not necessarily positive. In other words, the BFGS formula (20) does not provide the property $B_{k}s_{k-1}=t_{k-1}$ for all $k\geq0$. Hence in the convergence analysis for Algorithm 1, we only require $B_{k}$ to be symmetric positive definite. Convergence theorems for Algorithm 1 with Broyden and BFGS matrix secant updating were established by Burke and Qian [5].

By Proposition 2 below, if $\tau_{k} = 1$ and $\epsilon_{k} = 0$ for all $k$, then Algorithm 1 with (20) reduces to the classical BFGS method

$$
x _ {k + 1} = x _ {k} - B _ {k} ^ {- 1} G (x _ {k})
$$

for solving $G(x) = 0$.

In order to ensure that each step of Algorithm 1 is well-defined, we need to establish a few propositions. In what follows, we denote by $f_{k}$ the polyhedral function $f_{k,j}$ for which condition (15) is satisfied. Thus $p^{a}(x_{k})$ satisfies the inequality

$$
f (p ^ {a} (x _ {k})) \leq f (x _ {k}) - \sigma_ {k} (f (x _ {k}) - f _ {k} (p ^ {a} (x _ {k}))). \tag {21}
$$

The next proposition shows that step 1 is always executed finitely.

Proposition 1. At each iteration k of the algorithm, step 1 is executed in a finite number of steps, because procedure (11)–(12) produces $y_{j}$ satisfying either (14) or (15) for some j.

Proof. Suppose (14) is never satisfied for any j, i.e.,

$$
f (x _ {k}) - f _ {k, j} (y _ {j}) > \rho > 0.
$$

But, as shown in [11, Proposition 3], we have

$$
\lim _ {j \to \infty} \{f (y _ {j}) - f _ {k, j} (y _ {j}) \} = 0.
$$

It is then easy to see that (15) must be satisfied for all $j$ sufficiently large. This completes the proof.

□

The following proposition gives the errors arising from the approximation function $f_{k}$ and the approximate proximal point $p^a (x_k)$.

Proposition 2. For each $k \geq 0$, let

$$
F ^ {a} (x _ {k}) := f (p ^ {a} (x _ {k})) + \frac {1}{2} \mu \| p ^ {a} (x _ {k}) - x _ {k} \| ^ {2}
$$

$$
G ^ {a} (x _ {k}) := v _ {k},
$$

and

$$
\epsilon_ {k} := (1 - \sigma_ {k}) (f (x _ {k}) - f _ {k} (p ^ {a} (x _ {k}))).
$$

Then we have

$$
F (x _ {k}) \leq F ^ {a} (x _ {k}) \leq F (x _ {k}) + \epsilon_ {k}, \tag {22}
$$

$$
\| p ^ {a} (x _ {k}) - p (x _ {k}) \| \leq \sqrt {\frac {2 \epsilon_ {k}}{\mu}}, \tag {23}
$$

$$
\| G ^ {a} (x _ {k}) - G (x _ {k}) \| \leq \sqrt {2 \mu \epsilon_ {k}}, \tag {24}
$$

$$
v _ {k} \in \partial_ {\epsilon_ {k}} f (p ^ {a} (x _ {k})). \tag {25}
$$

Furthermore, if the sequences $\{x_k\}$ and $\{p^a (x_k)\}$ remain in a bounded set $D$, then

$$
\epsilon_ {k} \leq \alpha \| v _ {k} \|, \tag {26}
$$

where $\alpha := (1 - \sigma)L/\sigma\mu$ and $L$ is the Lipschitz constant of $f$ relative to $D$.

Proof. Obviously, $F(x_{k}) \leq F^{a}(x_{k})$. By Proposition 3 in [11], we have

$$
f _ {k} (p ^ {a} (x _ {k})) + \frac {1}{2} \mu \| p ^ {a} (x _ {k}) - x _ {k} \| ^ {2} \leq F (x _ {k}).
$$

Hence by (21),

$$
\begin{aligned} F ^ {a} (x _ {k}) &\leq f (x _ {k}) - \sigma_ {k} (f (x _ {k}) - f _ {k} (p ^ {a} (x _ {k}))) + \frac {1}{2} \mu \| p ^ {a} (x _ {k}) - x _ {k} \| ^ {2} \\ &= (1 - \sigma_ {k}) (f (x _ {k}) - f _ {k} (p ^ {a} (x _ {k}))) + f _ {k} (p ^ {a} (x _ {k})) + \frac {1}{2} \mu \| p ^ {a} (x _ {k}) - x _ {k} \| ^ {2} \\ &\leq F (x _ {k}) + \epsilon_ {k}. \\ \end{aligned}
$$

Thus we obtain (22).

The inequalities (23) and (24) follow from Lemma 1 in [12].

Now we prove (25). Let $\lambda_i, i = 0, \ldots, j_k - 1$, be the Lagrange multipliers in the subproblem (13) whose solution is $y_{j_k} = p^a(x_k)$. Then by the KKT conditions for (13), we have

$$
\sum_ {i = 0} ^ {j _ {k} - 1} \lambda_ {i} g _ {i} = - \mu (p ^ {a} (x _ {k}) - x _ {k})
$$

and

$$
f _ {k} (p ^ {a} (x _ {k})) = \sum_ {i = 0} ^ {j _ {k} - 1} \lambda_ {i} \left(f (y _ {i}) + g _ {i} ^ {T} (p ^ {a} (x _ {k}) - y _ {i})\right).
$$

Since $g_i \in \partial f(y_i)$, $\lambda_i \geq 0$ for $i = 0, \ldots, j_k - 1$, and $\sum_{i=0}^{j_k-1} \lambda_i = 1$, we have for all $z \in \Re^n$,

$$
\begin{aligned} f (z) &\geq \sum_ {i = 0} ^ {j _ {k} - 1} \lambda_ {i} (f (y _ {i}) + g _ {i} ^ {T} (z - y _ {i})) \\ &= f _ {k} (p ^ {a} (x _ {k})) - \mu (p ^ {a} (x _ {k}) - x _ {k}) ^ {T} (z - p ^ {a} (x _ {k})). \tag {27} \\ \end{aligned}
$$

Setting $z = x_{k}$ in (27), we have

$$
\tilde {\epsilon} _ {k} := f (x _ {k}) - f _ {k} (p ^ {a} (x _ {k})) - \mu \| p ^ {a} (x _ {k}) - x _ {k} \| ^ {2} \geq 0.
$$

Then (27) can be written as

$$
f (z) \geq f (x _ {k}) - \mu (p ^ {a} (x _ {k}) - x _ {k}) ^ {T} (z - x _ {k}) - \tilde {\epsilon} _ {k}. \tag {28}
$$

By the definition of $\epsilon$ -subdifferential of $f$ at $x_{k}$, (28) implies

$$
- \mu (p ^ {a} (x _ {k}) - x _ {k}) \in \partial_ {\tilde {\epsilon} _ {k}} f (x _ {k}).
$$

Moreover, it follows from (21) and (28) that, for all $z \in \Re^n$,

$$
\begin{aligned} f (z) &\geq f (p ^ {a} (x _ {k})) - \mu (p ^ {a} (x _ {k}) - x _ {k}) ^ {T} (z - x _ {k}) - \tilde {\epsilon} _ {k} + \sigma_ {k} (f (x _ {k}) - f _ {k} (p ^ {a} (x _ {k}))) \\ &= f (p ^ {a} (x _ {k})) - \mu (p ^ {a} (x _ {k}) - x _ {k}) ^ {T} (z - p ^ {a} (x _ {k})) - (1 - \sigma_ {k}) (f (x _ {k}) - f _ {k} (p ^ {a} (x _ {k}))) \\ &= f (p ^ {a} (x _ {k})) - \mu (p ^ {a} (x _ {k}) - x _ {k}) ^ {T} (z - p ^ {a} (x _ {k})) - \epsilon_ {k}. \\ \end{aligned}
$$

Hence (25) holds.

Finally, recall that $v_{k}$ is given by $v_{k} = \mu (x_{k} - p^{a}(x_{k}))$. Then, taking into account $\sigma < \sigma_{k}$, (21) and the Lipschitz continuity of $f$, we have

$$
\begin{aligned} \epsilon_ {k} &\leq \frac {1 - \sigma_ {k}}{\sigma_ {k}} (f (x _ {k}) - f (p ^ {a} (x _ {k}))) \\ &\leq \frac {(1 - \sigma_ {k}) L}{\sigma_ {k}} \| x _ {k} - p ^ {a} (x _ {k}) \| \\ &\leq \frac {(1 - \sigma) L}{\sigma \mu} \| v _ {k} \|. \\ \end{aligned}
$$

Hence we obtain (26).

□

The line search criterion in step 5 is different from conventional line search criteria. In general, $d_{k}$ need not be a descent direction of f at $x_{k}$. Nevertheless, the following proposition shows that at each iteration k of Algorithm 1, the integer $m_{k}$ is well-defined and hence the stepsize $\tau_{k}$ can be determined finitely in step 5.

Proposition 3. For every $k$, there exists $\bar{\tau}_k > 0$ such that

$$
f (p ^ {a} (x _ {k}) + \tau d _ {k}) \leq f (x _ {k}) - \frac {\tau \sigma}{\mu} \| v _ {k} \| ^ {2} \tag {29}
$$

for all $\tau \in (0, \bar{\tau}_k]$.

Proof. Since $B_{k}$ is symmetric positive definite, $B_{k}^{-1}$ exists and $d_{k} = -(B_{k}^{-1} - \mu^{-1}I)v_{k}$ is well-defined. Since

$$
f (x _ {k}) - f _ {k} (p ^ {a} (x _ {k})) \geq \mu \| x _ {k} - p ^ {a} (x _ {k}) \| ^ {2} = \frac {1}{\mu} \| v _ {k} \| ^ {2},
$$

(21) implies

$$
f (p ^ {a} (x _ {k})) \leq f (x _ {k}) - \frac {\sigma_ {k}}{\mu} \| v _ {k} \| ^ {2} <   f (x _ {k}) - \frac {\sigma}{\mu} \| v _ {k} \| ^ {2}. \tag {30}
$$

If $v_{k} = 0$, then $d_{k} = 0$ and for any $\tau > 0$, (29) holds. If $v_{k} \neq 0$, (30) implies that there exists $\bar{\tau}_{k} \in (0,1]$ such that for any $\tau \in (0, \bar{\tau}_{k}]$

$$
f (p ^ {a} (x _ {k}) + \tau d _ {k}) <   f (x _ {k}) - \frac {\sigma}{\mu} \| v _ {k} \| ^ {2} \leq f (x _ {k}) - \frac {\tau \sigma}{\mu} \| v _ {k} \| ^ {2}.
$$

The proof is complete.

□

By Proposition 2, if $p^a(x_k) - x_k = 0$ and $\epsilon_k = 0$, then

$$
0 = v _ {k} \in \partial f (p ^ {a} (x _ {k})) = \partial f (x _ {k}).
$$

This implies that $x_{k}$ minimizes f. From $\epsilon_{k}=0$, $f(x_{k})-f_{k}(p^{a}(x_{k}))=0$, i.e., (14) holds and Algorithm 1 terminates. On the other hand, if $x_{k}$ minimizes f, then there is no $y_{j}$ such that (15) holds but (14) fails to hold. Furthermore, by Proposition 3 in [11], there is some $y_{j}$ such that (14) holds and thus Algorithm 1 terminates at $x_{k}$.

Let us denote

$$
K = \{0, 1, 2, \dots \}
$$

and

$$
K _ {0} = \{0 \} \cup \{k \in K \mid \text { step   5   is   not   applied   at   iteration   } k \}.
$$

Theorem 1. Assume that the convex function $f$ has a nonempty bounded set of minimizers and that the sequence $\{\| B_k^{-1}\| \}$ is bounded. Then Algorithm 1 terminates in a finite number of iterations.

Proof. Note that the assumption that $f$ has a bounded set of minimizers implies that both $f$ and $F$ have bounded level sets. By construction, for each $k, x_k$ and $p^a(x_k)$ remain in the bounded set $D := \{x \mid f(x) \leq M\}$. Let $\bar{f}$ denote the minimal value of $f$.

Suppose that (14) is never satisfied, i.e.

$$
f (x _ {k}) - f _ {k} (p ^ {a} (x _ {k})) > \rho \text {   for   all   } k. \tag {31}
$$

By Proposition 1, Algorithm 1 generates two sequences $\{x_k\}$ and $\{p^a(x_k)\}$. We shall prove that any accumulation point of $\{x_k\}$ and $\{p^a(x_k)\}$ minimizes $f$.

First we consider the case where $K_{0}$ is infinite. Let $K_{0}$ consist of $k_{0} = 0 < k_{1} < k_{2}, \ldots$. By construction, we have

$$
\| v _ {k _ {\ell}} \| \leq c \eta_ {k _ {\ell}} = c \| v _ {k _ {\ell - 1}} \| \quad \text { for   all } \ell = 1, 2, \dots ,
$$

which together with $v_{k} = G^{a}(x_{k})$ implies

$$
\| v _ {k _ {\ell}} \| \leq c ^ {\ell} \| G ^ {a} (x _ {0}) \| \quad \text {for all} \ell = 0, 1, 2, \dots .
$$

So we get

$$
\lim _ {\ell \to \infty} \| G ^ {a} (x _ {k _ {\ell}}) \| \leq \lim _ {\ell \to \infty} c ^ {\ell} \| G ^ {a} (x _ {0}) \| = 0. \tag {32}
$$

Let $L$ be the Lipschitz constant of $f$ relative to $D$. By (26) in Proposition 2, $\epsilon_{k_{\ell}} \leq \alpha \| G^{a}(x_{k_{\ell}})\|$, where $\alpha = (1 - \sigma)L / \sigma \mu$. By (24) in Proposition 2, we then have

$$
\begin{aligned} \| G (x _ {k _ {\ell}}) \| &\leq \| G ^ {a} (x _ {k _ {\ell}}) \| + \sqrt {2 \mu \epsilon_ {k _ {\ell}}} \\ &\leq \| G ^ {a} (x _ {k _ {\ell}}) \| + \sqrt {2 \mu \alpha \| G ^ {a} (x _ {k _ {\ell}}) \|}. \tag {33} \\ \end{aligned}
$$

Hence (32) implies

$$
\lim _ {\ell \to \infty} \| G (x _ {k _ {\ell}}) \| = 0.
$$

Since $x_{k_{\ell}}$, $p^a(x_{k_{\ell}}) \in D$ for all $\ell \geq 0$, there exists an infinite subset $K' \subset K_0$ such that $\lim_{k \to \infty, k \in K'} x_k = \bar{x}$ and $\lim_{k \to \infty, k \in K'} p^a(x_k) = \bar{p}$. Therefore from

$$
\mu \| \bar{x} -\bar{p}\| = \lim_{\substack{k\to \infty \\ k\in K'}}\| G^{a}(x_{k})\| = 0
$$

and (33), we have $\bar{x} = \bar{p}$ and $G(\bar{x}) = 0$ . Hence the accumulation point $\bar{x}$ is optimal. Now $\{\| G^a (x_{k_\ell})\|_{\ell = 0}^\infty$ is decreasing and has a limit 0. Passing to the limit in (32) with $k\in K'$ , we see that any accumulation point of the subsequence $\{x_k\}_{k\in K_0}$ is optimal.

Now let us show that any accumulation point of the entire sequence $\{x_{k}\}$ is an optimal solution. If there exists a $\bar{k}$ such that $k \in K_{0}$ for all $k \geq \bar{k}$, then from

$$
\| G ^ {a} (x _ {k + 1}) \| \leq c \| G ^ {a} (x _ {k}) \|, k \geq \bar {k},
$$

it follows that any accumulation point of $\{x_k\}$ is optimal. On the other hand, if such $\bar{k}$ does not exist, then by construction, for any $k \notin K_0$ there exists a largest number $k_\ell \in K_0$ such that $k_\ell < k$ and

$$
\bar {f} \leq f (x _ {k + 1}) \leq f (x _ {k _ {\ell} + 1}) = f (x _ {k _ {\ell}} - B _ {k _ {\ell}} ^ {- 1} v _ {k _ {\ell}}),
$$

where the last equality follows from (19). Since $\{\| B_k^{-1}\|\}$ is bounded and since $\| v_{k_\ell}\| \to 0$ and $f(x_{k_\ell})\to \bar{f}$, any accumulation point of $\{x_k\}$ is optimal.

Now we consider the case where $K_0$ is finite. Let $\hat{k} = \max_{k \in K_0} k$. Since the level sets of $f$ are bounded, the sequences $\{x_k\}$ and $\{p^a(x_k)\}$ are bounded by construction. Then

$$
\frac {\sigma}{\mu} \sum_ {k = \hat {k} + 1} ^ {\infty} \tau_ {k} \| v _ {k} \| ^ {2} \leq f (x _ {\hat {k} + 1}) - \bar {f} <   \infty , \tag {34}
$$

which implies

$$
\lim _ {k \to \infty} \tau_ {k} \| v _ {k} \| ^ {2} = 0. \tag {35}
$$

Since $\sigma < \sigma_{k}$ and $\mu \| x_{k} - p^{a}(x_{k})\|^{2}\leq f(x_{k}) - f_{k}(p^{a}(x_{k}))$, we have (cf. (30))

$$
\bar {f} \leq f (p ^ {a} (x _ {k})) \leq f (x _ {k}) - \frac {\sigma}{\mu} \| v _ {k} \| ^ {2}. \tag {36}
$$

Moreover the boundedness of $\{x_k\}$ and $\{p^a (x_k)\}$ implies that there exists a subsequence $K_{1}\subset K$ such that $\lim_{k\to \infty ,k\in K_1}p^a (x_k) = \bar{p}$, $\lim_{k\to \infty ,k\in K_1}x_k = \bar{x}$ and $\lim_{k\to \infty ,k\in K_1}v_k = \bar{v}$. Since $\{\| B_k^{-1}\|\}$ is bounded, we may suppose by taking a further subsequence if necessary that $\lim_{k\to \infty ,k\in K_1}d_k = \bar{d}$.

If $\liminf_{k\to \infty ,k\in K_1}\tau_k > 0$, then (35) immediately implies $\bar{v} = 0$. On the other hand, if $\liminf_{k\to \infty ,k\in K_1}\tau_k = 0$, then the definition of $m_{k}$ in the line search rule gives

$$
f (p ^ {a} (x _ {k}) + \gamma^ {m _ {k} - 1} d _ {k}) > f (x _ {k}) - \frac {\gamma^ {m _ {k} - 1} \sigma}{\mu} \| v _ {k} \| ^ {2}. \tag {37}
$$

Since $\gamma^{m_k - 1} = \tau_k / \gamma \to 0$, (37) implies

$$
f (\bar {p}) \geq f (\bar {x}). \tag {38}
$$

From (36), we have

$$
f (\bar {p}) \leq f (\bar {x}) - \frac {\sigma}{\mu} \| \bar {v} \| ^ {2}. \tag {39}
$$

Combining (38) and (39), we have $\bar{v}=0$ and $\bar{x}=\bar{p}$. Thus we get

$$
\begin{aligned} \bar {\epsilon} &= \lim _ {k \to \infty , k \in K _ {1}} (1 - \sigma_ {k}) (f (x _ {k}) - f _ {k} (p ^ {a} (x _ {k}))) \\ &\leq \frac {1 - \sigma}{\sigma} \lim _ {k \to \infty , k \in K _ {1}} (f (x _ {k}) - f (p ^ {a} (x _ {k}))) = 0, \\ \end{aligned}
$$

implying that $\bar{\epsilon} = 0$. Since $v_{k} \in \partial_{\epsilon_{k}} f(p^{a}(x_{k}))$, the closedness of the $\epsilon$ -subdifferential mapping implies that $0 \in \partial f(\bar{p})$. Hence $\bar{x} = \bar{p}$ minimizes $f$ and $f(\bar{x}) = \bar{f}$. Since

$$
\bar {f} \leq f (x _ {k + 1}) \leq f (x _ {k}) - \frac {\tau_ {k} \sigma}{\mu} \| v _ {k} \| ^ {2}, \text {for} k > \hat {k}, \tag {40}
$$

the sequence $\{f(x_k)\}_{k > \hat{k}}$ is non-increasing and has a limit $f^{*}$. Passing to the limit in (40) with $k \in K_1$, we obtain $f^{*} = \bar{f}$. Hence any accumulation point of $\{x_k\}$ is also optimal.

Consequently, if (31) holds for all $k$, then any accumulation point of $\{x_k\}$ and $\{p^a(x_k)\}$ minimizes $f$ and

$$
\begin{aligned} f (p ^ {a} (x _ {k})) - f (x _ {k}) &\leq - \sigma_ {k} (f (x _ {k}) - f _ {k} (p ^ {a} (x _ {k}))) \\ &\leq - \sigma (f (x _ {k}) - f _ {k} (p ^ {a} (x _ {k}))), \text { for   all } k. \\ \end{aligned}
$$

However, this contradicts (31), because $f(p^{a}(x_{k})) - f(x_{k}) \to 0$. Hence Algorithm 1 terminates finitely.

![](images/71a65c6fda8771cfad538123b20d3224f9108758cb7b04d2b9e979582364710d.jpg)

# 3. Linear and superlinear convergence

In this section, we consider the convergence rate of Algorithm 1. For this purpose, we assume that $x_{k}$ is not an optimal solution for any k and $\rho$ is set to zero in (14), so that the algorithm generates infinite sequences $\{x_{k}\}$ and $\{p^{a}(x_{k})\}$. Then by the proof of Theorem 1, we can deduce that any accumulation point of the sequences $\{x_{k}\}$ and $\{p^{a}(x_{k})\}$ minimizes f.

We say that $f$ is strongly convex with modulus $\nu > 0$, if

$$
\lambda f (x) + (1 - \lambda) f (y) - f (\lambda x + (1 - \lambda) y) \geq \frac {1}{2} \nu \lambda (1 - \lambda) \| x - y \| ^ {2}
$$

for any $\lambda \in (0,1)$ and $x,y\in \Re^n$

Lemaréchal and Sagastizábal [20] proved that strong convexity is transmitted between $f$ and $F$. More specifically, if $f$ is strongly convex with modulus $\nu > 0$, then $F$ is also strongly convex with modulus $\tilde{\nu} \geq \mu\nu/(\mu + \nu)$. In the remainder of this section, we shall assume that $f$ is strongly convex in $\Re^n$. The strong convexity of $f$ implies that there exists a unique solution $x^*$ of $G(x) = 0$. It should be noted, however, that the arguments will remain valid, even if the assumption is weakened to the local strong convexity of $f$ around the solution $x^*$. (For the local strong convexity, see [28].)

Lemma 1. Suppose that the assumptions of Theorem 1 hold. Let $x^{*}$ be an optimal solution of (1). For each $k \geq 0$, if $\tau_{k} = 1$, then

$$
\begin{aligned} \| x _ {k + 1} - x ^ {*} \| &\leq \| (I - B _ {k} ^ {- 1} V _ {k}) (x _ {k} - x ^ {*}) \| + \| B _ {k} ^ {- 1} \| \| G ^ {a} (x _ {k}) - G (x _ {k}) \| \\ + \| B _ {k} ^ {- 1} \| \| G (x _ {k}) - G (x ^ {*}) - V _ {k} (x _ {k} - x ^ {*}) \|, \tag {41} \\ \end{aligned}
$$

for any $V_{k}\in \partial G(x_{k})$

Proof. If $\tau_{k} = 1$, then it follows from (19), $v_{k} = G^{a}(x_{k})$ and $G(x^{*}) = 0$ that

$$
\begin{aligned} x _ {k + 1} - x ^ {*} &= x _ {k} - B _ {k} ^ {- 1} G ^ {a} (x _ {k}) - x ^ {*} \\ &= (I - B _ {k} ^ {- 1} V _ {k}) (x _ {k} - x ^ {*}) - B _ {k} ^ {- 1} (G ^ {a} (x _ {k}) - G (x ^ {*}) - V _ {k} (x _ {k} - x ^ {*})), \\ \end{aligned}
$$

which implies (41).

![](images/f74f608f3e1053da961c68c6dcc9c5bee1c71b560918f63aa121aa6f0289dff8.jpg)

Now we are ready to establish Q-linear convergence of the algorithm.

Theorem 2. Suppose that $f$ is strongly convex with modulus $v > 0$ and $G$ is semismooth at the minimizer $x^{*}$ of (1). Assume that there exist $\tilde{k} \geq 0, \delta \geq 0, \beta \geq 0,$ and $\kappa > 0$, such that for any $k \geq \tilde{k}$, it holds that

$$
\epsilon_ {k} \leq \frac {1}{2 \mu} \delta^ {2} \min \{\| G (x _ {k}) \| ^ {2}, \| G ^ {a} (x _ {k}) \| ^ {2} \}, \tag {42}
$$

$\| B_k^{-1}\| \leq \kappa$ and $\| I - B_k^{-1}V_k\| \leq \beta$ for some $V_{k}\in \partial G(x_{k})$. Moreover, assume

$$
(1 + \delta) ^ {2} (\beta + \kappa \mu \delta) (\nu + \mu) <   \nu c, \tag {43}
$$

where $c$ is the parameter used in Algorithm 1. Then there exists an integer $\hat{k} \geq \tilde{k}$ such that for all $k \geq \hat{k}$, we have $\tau_k \equiv 1$ and

$$
\| x _ {k + 1} - x ^ {*} \| \leq c \| x _ {k} - x ^ {*} \|, \tag {44}
$$

i.e., the sequence $\{x_k\}$ converges to $x^{*}$ $Q$-linearly.

Proof. Since the strong monotonicity of $f$ implies that the level sets of $f$ are compact, the sequence $\{x_k\}$ has at least one accumulation point. Moreover by the strong convexity of $f$ and the proof of Theorem 1, $f$ has the unique minimizer $x^{*}$ and $\{x_k\}$ converges to $x^{*}$.

Since G is semismooth at $x^{*}$, by Theorem 2.3 in [30], we have

$$
\| G (x ^ {*} + h) - G (x ^ {*}) - V h \| = o (\| h \|), \tag {45}
$$

where $V \in \partial G(x^{*} + h)$. Therefore there exists an open ball $S(x^{*}, r)$ with the center $x^{*}$ and radius $r$ such that for any $x \in S(x^{*}, r)$,

$$
\kappa \| G (x) - G (x ^ {*}) - V (x - x ^ {*}) \| \leq \left(\frac {c \nu}{(1 + \delta) ^ {2} (\nu + \mu)} - \beta - \kappa \mu \delta\right) \| x - x ^ {*} \|, \tag {46}
$$

where $V\in \partial G(x)$

Since the sequences $\{p^a(x_k)\}$ and $\{x_k\}$ converge to $x^{*}$, there exists a $\bar{k} \geq \tilde{k}$ such that $x_k$, $p^a(x_k) \in S(x^*, r)$ and $f(p^a(x_k) + d_k) \leq M$ for all $k \geq \bar{k}$, where $M$ is the parameter used in Algorithm 1. By Theorem 2.2 in [20], the strong convexity of $f$ with modulus $\nu$ implies that

$$
(G (x) - G (y)) ^ {T} (x - y) \geq \tilde {\nu} \| x - y \| ^ {2}, \text {for} x, y \in \Re^ {n},
$$

where

$$
\tilde {\nu} \geq \frac {\mu \nu}{\mu + \nu}.
$$

It then follows that

$$
\tilde {\nu} \| x _ {k} - x ^ {*} \| ^ {2} \leq G (x _ {k}) ^ {T} (x _ {k} - x ^ {*}) \leq \| G (x _ {k}) \| \| x _ {k} - x ^ {*} \|,
$$

and hence

$$
\| x _ {k} - x ^ {*} \| \leq \tilde {\nu} ^ {- 1} \| G (x _ {k}) \| \leq \frac {\mu + \nu}{\mu \nu} \| G (x _ {k}) \|. \tag {47}
$$

By Proposition 2 and (47), the condition (42) implies

$$
\begin{aligned} \| x _ {k} - x ^ {*} \| &\leq \frac {\mu + \nu}{\mu \nu} (\| G ^ {a} (x _ {k}) \| + \sqrt {2 \mu \epsilon_ {k}}) \\ &\leq \frac {\mu + \nu}{\mu \nu} (\| G ^ {a} (x _ {k}) \| + \delta \| G ^ {a} (x _ {k}) \|) \\ &\leq \frac {\mu + \nu}{\nu \mu} (1 + \delta) \| G ^ {a} (x _ {k}) \|. \tag {48} \\ \end{aligned}
$$

Since $\|G^{a}(x_{k})\|\to0$, there exists $\hat{k}\geq\bar{k}$ such that $\|v_{\hat{k}}\|\leq c\eta_{k}$, i.e., $\hat{k}\in K_{0}$. Then $\tau_{\hat{k}}=1$ and by (19),

$$
x _ {\hat {k} + 1} = x _ {\hat {k}} - B _ {\hat {k}} ^ {- 1} G ^ {a} (x _ {\hat {k}}).
$$

By Lemma 3.2, (46) and (48), we have

$$
\begin{array}{l} \| G ^ {a} (x _ {\hat {k} + 1}) \| \leq \| G ^ {a} (x _ {\hat {k} + 1}) - G (x _ {\hat {k} + 1}) \| + \| G (x _ {\hat {k} + 1}) - G (x ^ {*}) \| \\ \leq \sqrt {2 \mu \epsilon_ {\hat {k} + 1}} + \mu \| x _ {\hat {k} + 1} - x ^ {*} \| \\ \leq \delta \| G (x _ {\hat {k} + 1}) \| + \mu \| x _ {\hat {k} + 1} - x ^ {*} \| \\ \leq (1 + \delta) \mu \| x _ {\hat {k} + 1} - x ^ {*} \| \\ \leq (1 + \delta) \mu (\beta \| x _ {\hat {k}} - x ^ {*} \| + \kappa \| G (x _ {\hat {k}}) - G (x ^ {*}) - V _ {\hat {k}} (x _ {\hat {k}} - x ^ {*}) \| \\ + \kappa \| G ^ {a} (x _ {\hat {k}}) - G (x _ {\hat {k}}) \|\left. \right) \\ \leq (1 + \delta) \mu (\beta \| x _ {\hat {k}} - x ^ {*} \| + \kappa \| G (x _ {\hat {k}}) - G (x ^ {*}) - V _ {\hat {k}} (x _ {\hat {k}} - x ^ {*}) \| \\ + \kappa \delta \| G (x _ {\hat {k}}) \|\left. \right) \\ \leq \frac {c \nu \mu}{(1 + \delta) (\nu + \mu)} \| x _ {\hat {k}} - x ^ {*} \| \\ \leq c \| G ^ {a} (x _ {\hat {k}}) \|, \\ \end{array}
$$

where the third inequality follows from (42), the fourth inequality follows from the Lipschitz continuity of G, and the last inequality follows from (48).

Hence $\hat{k} + 1 \in K_0$ and $\tau_{\hat{k} + 1} = 1$. This implies that for all $k \geq \hat{k}$, we have $k \in K_0$ and $\tau_k \equiv 1$. Furthermore for all $k \geq \hat{k}$,

$$
\| x _ {k + 1} - x ^ {*} \| \leq \frac {c \nu}{(1 + \delta) ^ {2} (\nu + \mu)} \| x _ {k} - x ^ {*} \| \leq c \| x _ {k} - x ^ {*} \|,
$$

where the first inequality follows from (41) and (46).

![](images/0db4950175d72ba5077aa8b50da5c7531c0536bd73cc322a64e710511a50cda3.jpg)

Now we proceed to establish superlinear convergence results for the algorithm. Besides the semismoothness of G, Fukushima and Qi [9, Theorem 5.4] assumed the following three conditions in their superlinear convergence theorem.

(i) $\epsilon_{k} = o(\| G(x_{k})\|^{2}),$  
(ii) $\lim_{k\to \infty}\mathrm{dist}(B_k,\partial G(x_k)) = 0.$  
(iii) the sequence $\{\| B_k^{-1}\|\}$ is bounded.

We can also show that $\tau_{k} \equiv 1$ for all k large enough and Algorithm 1 converges to $x^{*}$ superlinearly if the above three conditions hold. Furthermore, by (24) in Proposition 2.2, $\epsilon_{k} = o(\|G(x_{k})\|^{2})$ if and only if $\epsilon_{k} = o(\|G^{a}(x_{k})\|^{2})$. This fact follows from

$$
\left| \frac {\| G ^ {a} (x _ {k}) \|}{\| G (x _ {k}) \|} - 1 \right| \leq \frac {\sqrt {2 \mu \epsilon_ {k}}}{\| G (x _ {k}) \|}
$$

and

$$
\left| \frac {\| G (x _ {k}) \|}{\| G ^ {a} (x _ {k}) \|} - 1 \right| \leq \frac {\sqrt {2 \mu \epsilon_ {k}}}{\| G ^ {a} (x _ {k}) \|}.
$$

From the viewpoint of implementation, we use the condition $\epsilon_{k}=o(\|G^{a}(x_{k})\|^{2})$, rather than condition (i) above, in the following discussion.

Theorem 3. Suppose that $f$ is strongly convex with modulus $\nu > 0$ and $G$ is semismooth at the minimizer $x^{*}$ of $f$. If $\epsilon_{k} = o(\|G^{a}(x_{k})\|^{2})$, $\lim_{k\to \infty}\mathrm{dist}(B_k,\partial G(x_k)) = 0$, and the sequence $\{\| B_k^{-1}\| \}$ is bounded, then there exists an integer $\hat{k}\geq 0$ such that $\tau_{k}\equiv 1$ for all $k\geq \hat{k}$, and the sequence $\{x_k\}$ converges to $x^{*}$ Q-superlinearly.

Proof. We first show that the conditions of Theorem 2 hold. By the boundedness of $\{\| B_k^{-1}\|\}$, there exists a constant $\kappa > 0$ such that $\| B_k^{-1}\| \leq \kappa$ for all $k$. The condition $\epsilon_k = o(\| G^a (x_k)\|^2)$ implies that for any $\delta > 0$ there is a $k_{\delta} > 0$ such that for all $k \geq k_{\delta}$, (42) holds. The condition $\lim_{k \to \infty} \text{dist}(B_k, \partial G(x_k)) = 0$, together with $\| B_k^{-1}\| \leq \kappa$, implies that for any $\beta > 0$ there is a $k_{\beta} > 0$ such that for all $k \geq k_{\beta}$,

$$
\| I - B _ {k} ^ {- 1} V _ {k} \| \leq \| B _ {k} ^ {- 1} \| \| B _ {k} - V _ {k} \| \leq \beta
$$

for some $V_{k} \in \partial G(x_{k})$. We choose $\delta > 0$ and $\beta > 0$ satisfying (43). Let $\tilde{k} = \max(k_{\delta}, k_{\beta})$. Then all conditions of Theorem 2 hold. Hence there exists an integer $\hat{k} \geq 0$ such that $\tau_{k} \equiv 1$ for all $k \geq \hat{k}$.

Now we prove that the sequence $\{x_k\}$ converges to $x^{*}$ Q-superlinearly. By Lemma 1, we have

$$
\begin{aligned} \| x _ {k + 1} - x ^ {*} \| &\leq \| I - B _ {k} ^ {- 1} V _ {k} \| \| x _ {k} - x ^ {*} \| + \| B _ {k} ^ {- 1} \| \| G ^ {a} (x _ {k}) - G (x _ {k}) \| \\ + \| B _ {k} ^ {- 1} \| \| G (x _ {k}) - G (x ^ {*}) - V _ {k} (x _ {k} - x ^ {*}) \| \\ \end{aligned}
$$

for all $k \geq \hat{k}$, where $V_k \in \partial G(x_k)$ is such that $\|B_k - V_k\| = \mathrm{dist}(B_k, \partial G(x_k))$. By assumption, we have $\|B_k^{-1}\| \leq \kappa$ for $k \geq \hat{k}$, and $\|I - B_k^{-1}V_k\| \to 0$ as $k \to \infty$. By (24) and $\epsilon_k = o(\|G(x_k)\|^2)$, we have

$$
\begin{aligned} \| G ^ {a} (x _ {k}) - G (x _ {k}) \| &\leq \sqrt {2 \mu \epsilon_ {k}} \\ &= o (\| G (x _ {k}) \|) \\ &= o (\| G (x _ {k}) - G (x ^ {*}) \|) \\ &= o (\| x _ {k} - x ^ {*} \|), \\ \end{aligned}
$$

where the last equality follows from the Lipschitz continuity of $G$. Moreover, by the semismoothness of $G$, we have

$$
\| G (x _ {k}) - G (x ^ {*}) - V _ {k} (x _ {k} - x ^ {*}) \| = o (\| x _ {k} - x ^ {*} \|)
$$

(see Theorem 2.3 in [30]). Hence we have $\| x_{k + 1} - x^{*}\| = o(\| x_{k} - x^{*}\|)$.

![](images/8e08b6d6450a09f19583d69c9e3b80164d3da8ac421b178a979fd6f03ad00aac.jpg)

Now we consider the generalization of the well-known result of Dennis and Moré [8], which characterizes the Q-superlinear convergence of quasi-Newton methods for a system of differentiable equations.

We say that $G$ is strongly differentiable at $x$ if

$$
\lim_{\substack{y\to x\\ z\to x}}\frac{\|G(z) - G(y) - G'(x)(z - y)\|}{\|z - y\|} = 0.
$$

Theorem 4. Suppose that $f$ is strongly convex with modulus $\nu > 0$ and $G$ is strongly differentiable at the minimizer $x^{*}$ of $f$. If the sequences $\{\| B_k \| \}$ and $\{\| B_k^{-1} \| \}$ are bounded, $\epsilon_{k} = o(\| G^{a}(x_{k})\|^{2})$ and $\tau_{k} \equiv 1$ for all $k$ large enough, then the sequence $\{x_{k}\}$ converges $Q$ -superlinearly to $x^{*}$ if and only if

$$
\lim _ {k \to \infty} \frac {\| (B _ {k} - G' (x ^ {*})) s _ {k} \|}{\| s _ {k} \|} = 0. \tag {49}
$$

Proof. Since $f$ is strongly convex, $f$ has a unique minimizer. This together with the boundedness of $\{\| B_k^{-1}\| \}$ implies that the conditions of Theorem 1 are satisfied. Then, as noted in the first paragraph of this section, the proof of Theorem 1 indicates that any sequence $\{x_k\}$ generated by the algorithm without the termination criterion (14) is bounded and its accumulation point is a solution of $G(x) = 0$. Since the solution of $G(x) = 0$ is unique by the strong convexity of $f$, the entire sequence $\{x_k\}$ converges to $x^*$.

Since $\tau_{k} \equiv 1$ for all large $k$, we have $x_{k+1} = x_{k} - B_{k}^{-1} G^{a}(x_{k})$, which implies $\|x_{k+1} - x_{k}\| \geq \|G^{a}(x_{k})\| / \|B_{k}\|$. The boundedness of $\|B_{k}\|$ together with $\epsilon_{k} = o(\|G^{a}(x_{k})\|^{2})$ implies that $\epsilon_{k} = o(\|x_{k+1} - x_{k}\|^{2})$. Thus it follows from (24) that

$$
\| G ^ {a} (x _ {k}) - G (x _ {k}) \| \leq \sqrt {2 \mu \epsilon_ {k}} = o (\| x _ {k + 1} - x _ {k} \|). \tag {50}
$$

Assume first that (49) holds. By construction,

$$
\begin{array}{l} (B _ {k} - G' (x ^ {*})) s _ {k} = B _ {k} (x _ {k + 1} - x _ {k}) - G' (x ^ {*}) (x _ {k + 1} - x _ {k}) \\ = G (x _ {k + 1}) - G (x _ {k}) - G' (x ^ {*}) (x _ {k + 1} - x _ {k}) \\ - G (x _ {k + 1}) + G (x _ {k}) - G ^ {a} (x _ {k}). \tag {51} \\ \end{array}
$$

The strong differentiability of $G$ at $x^{*}$ implies that

$$
\| G (x _ {k + 1}) - G (x _ {k}) - G' (x ^ {*}) (x _ {k + 1} - x _ {k}) \| = o (\| x _ {k + 1} - x _ {k} \|). \tag {52}
$$

Hence (49), (50) and (51) imply

$$
\lim _ {k \to \infty} \frac {\| G (x _ {k + 1}) \|}{\| x _ {k + 1} - x _ {k} \|} = 0. \tag {53}
$$

By Theorem 2.2 in [20], the strong convexity of $f$ with modulus $\nu$ implies that $F$ is strongly convex with modulus $\tilde{\nu} \geq \mu \nu / (\mu + \nu)$, which in turn implies that $G$ is strongly monotone with modulus $\tilde{\nu}$. Thus

$$
\| G (x _ {k}) - G (x ^ {*}) \| \geq \tilde {\nu} \| x _ {k} - x ^ {*} \|, \text { for   all   large } k.
$$

Hence for all large $k$,

$$
\begin{aligned} \frac {\| G (x _ {k + 1}) \|}{\| x _ {k + 1} - x _ {k} \|} &= \frac {\| G (x _ {k + 1}) - G (x ^ {*}) \|}{\| x _ {k + 1} - x _ {k} \|} \\ &\geq \frac {\tilde {\nu} \| x _ {k + 1} - x ^ {*} \|}{\| x _ {k + 1} - x ^ {*} \| + \| x _ {k} - x ^ {*} \|} \\ &= \tilde {\nu} \frac {\| x _ {k + 1} - x ^ {*} \| / \| x _ {k} - x ^ {*} \|}{1 + \| x _ {k + 1} - x ^ {*} \| / \| x _ {k} - x ^ {*} \|}. \\ \end{aligned}
$$

It then follows from (53) that

$$
\lim _ {k \to \infty} \frac {\| x _ {k + 1} - x ^ {*} \|}{\| x _ {k} - x ^ {*} \|} = 0.
$$

Conversely, assume that $\{x_k\}$ converges Q-superlinearly to $x^{*}$. By Lemma 2.1 in [8], $\lim_{k\to \infty}\| x_k - x^*\| /\| x_{k + 1} - x_k\| = 1$. Since $\| G(x_{k + 1}) - G(x^{*})\| \leq \mu \| x_{k + 1} - x^{*}\|$,

$$
\frac {\| G (x _ {k + 1}) \|}{\| x _ {k + 1} - x _ {k} \|} = \frac {\| G (x _ {k + 1}) - G (x ^ {*}) \|}{\| x _ {k} - x ^ {*} \|} \cdot \frac {\| x _ {k} - x ^ {*} \|}{\| x _ {k + 1} - x _ {k} \|} \to 0, \text {as} k \to \infty .
$$

From (50), (51) and (52), condition (49) holds.

![](images/ebfa049a9d2eb1dc50fc0450cd83511aa40ef1081134338a92f2b034d34bf36e.jpg)

Corollary 1. Suppose that $f$ is strongly convex with modulus $\nu > 0$ and $G$ is strongly differentiable at the minimizer $x^{*}$ of $f$. If the sequences $\{\| B_k \| \}$ and $\{\| B_k^{-1} \| \}$ are bounded, $\epsilon_{k} = o(\| G^{a}(x_{k})\|^{2})$ and $\| I - B_k^{-1}G'(x^*) \| < vc / (\nu + \mu)$ for all $k$ large enough, then the sequence $\{x_{k}\}$ converges $Q$ -superlinearly to $x^{*}$ if and only if condition (49) holds.

Proof. Conditions $\epsilon_{k}=o(\|G^{a}(x_{k})\|^{2})$ and $\|I-B_{k}^{-1}G'(x^{*})\|<vc/(\nu+\mu)$ imply that there exist $\tilde{k}\geq0$, $\delta\geq0$, $\beta\geq0$, and $\kappa>0$, such that (42) and (43) hold for $k\geq\tilde{k}$. By Theorem 2, $\tau_{k}\equiv1$ for $k\geq\tilde{k}$. Then the conclusion follows from Theorem 4.

![](images/3efb198678f9013bfbb2e52d7c51989c3e7a9e9f9e335bfba47e37a640f558a8.jpg)

Theorem 2 in [8] requires the continuous differentiability of G at $x^{*}$ and $G(x_{k}) = G^{a}(x_{k})$ for all k. Theorem 4 relaxes these two conditions. Note that the condition that G is strongly differentiable at the minimizer $x^{*}$ of f implies the existence of $\nabla^{2}F(x^{*})$ and the semismoothness of G at $x^{*}$, but neither of the latter two conditions implies the other [28,30].

It may be worth mentioning that Burke and Qian [5] recently established the boundedness of $\{\| B_k\|\}$ and $\{\| B_k^{-1}\|\}$ and superlinear convergence of Algorithm 1 with the BFGS update.

# 4. Numerical experiments

In this section we report results of numerical experiments with Algorithm 1 on a Sun 2000 workstation using Matlab 5.1.

Consider the convex function $f : R^{n} \rightarrow R$ defined by

$$
f (x) := \max \left\{h _ {i} (x) \mid i = 1, 2, \dots , m \right\},
$$

where

$$
h _ {i} (x) = x ^ {T} Q _ {i} x + q _ {i} ^ {T} x + a _ {i}.
$$

Here for each i, $Q_{i}$ is an $n \times n$ symmetric positive semidefinite matrix, $q_{i}$ is an n-dimensional vector and $a_{i}$ is a real number. Many important problems in electrical engineering can be modelled as such problems.

To solve the subproblem (10) at each major iteration, we used a modified version of Auslender's cutting plane algorithm with resetting and deleting rules [1,7,17]. In particular, the sequence $\{y_j\}$ is generated by the following procedure: $y_0 := x_k$, and $y_{j+1}$ is the solution of the problem

$$
\min _ {(y, w) \in \Re^ {n + 1}} w + \frac {1}{2} \mu \| y - x _ {k} \| ^ {2}
$$

$$
\text {subject to} \quad \phi_ {j} (y _ {j}) + \pi_ {j} ^ {T} (y - y _ {j}) \leq w, \tag {54}
$$

$$
\phi_ {j} (y _ {j}) + \xi_ {j} ^ {T} (y - y _ {j}) \leq w,
$$

$$
f (y _ {l}) + g _ {l} ^ {T} (y - y _ {l}) \leq w, \quad l \in J _ {j},
$$

where $J_{j}$ is an index set, $g_{l} \in \partial f(y_{l})$ for $l \in J_{j}$, $\phi_{0}(y) := f(y)$, $\pi_{0}$, $\xi_{0} \in \partial f(y_{0})$,

$$
\phi_ {j} (y) := \max \left\{\phi_ {j - 1} \left(y _ {j - 1}\right) + \pi_ {j - 1} ^ {T} \left(y - y _ {j - 1}\right), \phi_ {j - 1} \left(y _ {j - 1}\right) + \xi_ {j - 1} ^ {T} \left(y - y _ {j - 1}\right), \right.
$$

$$
f (y _ {l}) + g _ {l} ^ {T} (y - y _ {l}), l \in J _ {j - 1} \}
$$

for $j \geq 1$, and $\pi_j, \xi_j \in \partial \phi_j(y_j)$ are calculated as follows:

(i) Let

$$
\mathcal {U} _ {j} := \{(\phi_ {j - 1} (y _ {j - 1}), \pi_ {j - 1}), (\phi_ {j - 1} (y _ {j - 1}), \xi_ {j - 1}) \} \cup \{(f (y _ {l}), g _ {l}), l \in J _ {j - 1} \}
$$

and choose $(\zeta, u) \in \mathcal{U}_j$ such that

$$
\zeta + u ^ {T} (y _ {j} - y _ {r}) = \phi_ {j} (y _ {j}),
$$

where $r = j - 1$ or $r\in J_{j - 1}$. Set $\pi_j:= u$

(ii) Let $\lambda_{j,1}, \lambda_{j,2}$, and $\lambda_{j,l}, l \in J_j$, be nonnegative Lagrange multipliers in the quadratic programming problem (54). Set

$$
\xi_ {j + 1} := \lambda_ {j, 1} \pi_ {j} + \lambda_ {j, 2} \xi_ {j} + \sum_ {l \in J _ {j}} \lambda_ {j, l} g _ {l}. \tag {55}
$$

The aggregate linearization (55) is based on the techniques proposed by Kiwiel [17].

We store a fixed number of function values and subgradients to form the index set $J_{j}$. Specifically the function values and subgradients at $x_{k}$ and $x_{i}^{*}, i = 1, 2, \ldots, m$, are used at the initial step of the inner iteration at each iteration k, where

$$
x _ {i} ^ {*} := \operatorname{argmin} _ {x \in \Re^ {n}} \left\{x ^ {T} Q _ {i} x + q _ {i} ^ {T} x + a _ {i} \right\}, \quad i = 1, 2, \dots , m.
$$

Thereafter, at each step in the inner iteration, we drop from $\mathcal{U}_j$ two pairs that define the smallest and second smallest elements in

$$
\begin{aligned} \{\phi_ {j - 1} (y _ {j - 1}) + \pi_ {j - 1} ^ {T} (y _ {j} - y _ {j - 1}), \phi_ {j - 1} (y _ {j - 1}) + \xi_ {j - 1} ^ {T} (y _ {j} - y _ {j - 1}), \\ f (y _ {l}) + g _ {l} ^ {T} (y _ {j} - y _ {l}), l &\in J _ {j - 1} \}, \\ \end{aligned}
$$

which yields the new index set $J_{j}$.

We used the BFGS formula (20) to update $B_{k}$. The parameters in Algorithm 1 were chosen as $\rho = 10^{-6}$, $\sigma = 0.25$, c = 0.96, $\gamma = 0.75$, $\sigma_{k} = 0.26$, M = $\max\{1000, f(x_{0})\}$. The value of $\mu$ is defined by

$$
\mu = \frac {1}{m} \sum_ {i = 1} ^ {m} \| Q _ {i} \|.
$$

It is interesting to notice that Kiwiel proposed an efficient technique for choosing $\mu_{k}$ adaptively in bundle methods [17], which estimates the curvature of f between $x_{k}$ and $x_{k+1}$. In Algorithm 1, we use a bundle method in the inner iteration with a fixed $\mu$, and update the quasi-Newton matrix $B_{k+1}$ in the outer iteration, which approximates the generalized Jacobian of $\nabla F$ between $x_{k}$ and $x_{k+1}$.

We used four different starting points:

$$
\begin{aligned} x _ {0} ^ {1} &= (0, 0, \dots , 0), \qquad x _ {0} ^ {2} = (1, 1, \dots , 1) \\ x _ {0} ^ {3} &= \frac {1}{m} \sum_ {i = 1} ^ {m} x _ {i} ^ {*}, \qquad x _ {0} ^ {4} = \frac {1}{m} \sum_ {i = 1} ^ {m} q _ {i}. \\ \end{aligned}
$$

The first three examples are taken from the NDO collection of nondifferentiable optimization test problems [17].

Example 1 (Shor's minimax problem). Let $n = 5, m = 10$. Let $b \in \Re^m$ and $A \in \Re^{m \times n}$ be given as in [34, pages 137-138]. For $i = 1, 2, \ldots, m$,

$$
Q _ {i} = b _ {i} I, \quad q _ {i} = - 2 b _ {i} A _ {i} ^ {T}, \quad a _ {i} = b _ {i} \sum_ {j = 1} ^ {n} a _ {i j} ^ {2},
$$

where $b_{i} > 0$ and $A_{i}$ is the ith row of A. The optimal value is $f(x^{*}) = 22.60016$.

Example 2 (Lemaréchal's minimax problem, [18], pp.151–153). Let n = 10 and m = 5. Define $Q_{i}, q_{i}$, and $a_{i}$ as follows. For $i = 1, 2, \ldots, m$ and $\ell, j = 1, 2, \ldots, n$,

$$
\begin{aligned} Q _ {i} (\ell , j) &= Q _ {i} (j, \ell) = e ^ {j / \ell} \cos (j \ell) \sin (i), \quad j <   \ell , \\ Q _ {i} (j, j) &= \frac {j}{n} | \sin (i) | + \sum_ {\ell \neq j} | Q _ {i} (j, \ell) |, \\ q _ {i} (j) &= e ^ {j / i} \sin (i j), \\ \end{aligned}
$$

and

$$
a _ {i} = 0.
$$

The optimal value is $f(x^{*}) = -0.841408$.

Example 3 (Polak-Wiest's ill-scaled minimax problem). Let $n = 3$, $m = 3$. Define $a_1 = a_2 = a_3 = 0$, and

$$
Q _ {1} = \frac {1}{2} \mathrm{diag} (1, 0, 0), \quad Q _ {2} = \frac {1}{2} \mathrm{diag} (0. 0 0 0 1, 1, 25), \quad Q _ {3} = \frac {1}{2} \mathrm{diag} (0. 0 0 0 1, 1, 0)
$$

$$
q _ {1} = (- 1, 0, 0) ^ {T}, \quad q _ {2} = (0, - 1, 0) ^ {T}, \quad q _ {3} = (0, 1, 0) ^ {T}.
$$

The optimal value is $f(x^{*}) = 0.0$.

Example 4 (Polak-Wiest's ill-conditioned minimax problem, [24]). Let $n = 4$, $m = 2$. Define $a_1 = a_2 = 0$, and

$$
Q _ {1} = \mathrm{diag} (1 0 ^ {2}, 1, 1 0 ^ {- 2}, 0), \qquad Q _ {2} = \mathrm{diag} (1 0 ^ {4}, 1, 1, 0),
$$

$$
q _ {1} = (0, 0, - 0. 2, 0) ^ {T}, \quad q _ {2} = (0, 0, 2, 0) ^ {T}.
$$

The optimal value is $f(x^{*}) = 0.0$.

Table 1. Computational results for Examples 1–4

<table><tr><td rowspan="2">Initial Final</td><td colspan="2"> $x_0^1$ </td><td colspan="2"> $x_0^2$ </td><td colspan="2"> $x_0^3$ </td><td colspan="2"> $x_0^4$ </td></tr><tr><td> $f(x_k)$ </td><td>k</td><td> $f(x_k)$ </td><td>k</td><td> $f(x_k)$ </td><td>k</td><td> $f(x_k)$ </td><td>k</td></tr><tr><td>Ex 4.1</td><td>22.600161</td><td>36</td><td>22.600162</td><td>28</td><td>22.600163</td><td>37</td><td>22.600162</td><td>36</td></tr><tr><td>Ex 4.2</td><td>-0.8414075</td><td>39</td><td>-0.8414078</td><td>42</td><td>-0.8414079</td><td>61</td><td>-0.8414079</td><td>52</td></tr><tr><td>Ex 4.3</td><td>0.0</td><td>1</td><td>5.0E-5</td><td>14</td><td>2.2E-5</td><td>1</td><td>9.8E-7</td><td>6</td></tr><tr><td>Ex 4.4</td><td>0.0</td><td>1</td><td>2.3E-8</td><td>54</td><td>9.6E-7</td><td>19</td><td>1.2E-10</td><td>12</td></tr></table>

Example 5. The elements of $q_i, i = 1, \ldots, m$, were randomly generated from the intervals $(i - 1, i)$. Matrices $Q_i$ were generated as follows. Randomly generate an orthogonal matrix $U_i$ [35], and a diagonal matrix $D_i$ whose diagonal elements are in the interval (0.65, 4.8i). Set $Q_i := U_i D_i U_i^T$. Then $Q_i$ is a symmetric positive definite matrix and all eigenvalues of $Q_i$ are in the interval (0.65, 4.8i). Let $\bar{x} = -\frac{1}{2} Q_m^{-1} q_m$. We chose

$$
a _ {i} = - \bar {x} ^ {T} Q _ {i} \bar {x} - q _ {i} ^ {T} \bar {x}, \quad i = 1, 2, \dots , m.
$$

This problem has an optimal solution $x^{*} = \bar{x}$ with optimal value $f(x^{*}) = 0$. A notable feature of this example is that all functions $f_{i}, i = 1, 2, \ldots, m$, are active at $x^{*}$, which may make the problem challenging. The number of stored subgradients is $m + \frac{1}{5}n$. We summarize the numerical results in Table 2, where #iter is the number of major iterations, #cuts is the total number of inner iterations in the cutting-plane procedure, and #ls is the total number of iterations in the line search. We solved three randomly generated test examples for each problem size varying from n = 50 up to n = 400. The numbers shown in the table are the average of the three runs.

Table 2. Computational results for Example 5, $x_0 = x_0^2$, $m = 5$

<table><tr><td>n</td><td>50</td><td>100</td><td>150</td><td>200</td><td>250</td><td>300</td><td>400</td></tr><tr><td>#iter</td><td>30</td><td>27</td><td>35</td><td>51</td><td>35</td><td>46</td><td>34</td></tr><tr><td>#cuts</td><td>72</td><td>67</td><td>81</td><td>101</td><td>92</td><td>91</td><td>96</td></tr><tr><td>#ls</td><td>37</td><td>10</td><td>55</td><td>68</td><td>37</td><td>179</td><td>37</td></tr><tr><td> $\|x_k - x^*\|$ </td><td>3.1E-4</td><td>5.0E-4</td><td>5.0E-4</td><td>8.5E-4</td><td>9.0E-4</td><td>8.6E-4</td><td>1.0E-3</td></tr><tr><td> $\|f(x_k)\|$ </td><td>2.6E-7</td><td>7.9E-7</td><td>8.5E-7</td><td>1.0E-6</td><td>1.0E-6</td><td>9.2E-7</td><td>1.8E-6</td></tr><tr><td> $\|f(x_0)\|$ </td><td>5.6E+3</td><td>1.6E+3</td><td>2.9E+3</td><td>4.7E+3</td><td>4.8E+3</td><td>7.3E+3</td><td>6.1E+3</td></tr></table>

# 5. Concluding remarks

In this paper, we have proposed an algorithm for solving nondifferentiable convex optimization problems. The proposed algorithm is related to the recent algorithms developed in $[2–5, 12, 19, 21–23, 29, 31, 36]$. In $[2]$, Bonnans, Gilbert, Lemaréchal and Sagastizábal proposed a proximal quasi-Newton method and established its convergence properties. In $[21]$, Lemaréchal and Sagastizábal gave its implementation forms and numerical illustrations. In $[22]$, Mifflin presented an implementable quasi-second-order proximal bundle algorithm, but the rate of convergence is not discussed. In $[12]$, Fukushima and Qi proposed a global and superlinear convergent algorithm for minimizing the Moreau-Yosida regularization F. However, this algorithm makes use of the generalized Jacobian of F, instead of matrices $B_{k}$ generated by a quasi-Newton formula. Moreover, the line search is performed on the function F, rather than f, which is usually quite expensive. In $[29]$, a modification of the algorithm of $[12]$ is presented and its local convergence properties are studied. The algorithm proposed in this paper uses a quasi-Newton update of $B_{k}$ and line search is done on the function f. The resulting algorithm is globally and superlinearly convergent under suitable conditions, and it is implementable. Numerical results show its good performance for piecewise quadratic optimization problems.

Acknowledgements. We are grateful to J. Burke, R. Mifflin, L. Qi, M. Qian, R. Womersley and two referees for their helpful comments. We thank K. Kiwiel for providing his FORTRAN NDO test problems and related references.

# References

1. Auslender, A. (1987): Numerical methods for nondifferentiable convex optimization. Math. Program. Study 30, 102–126  
2. Bonnans, J., Gilbert, J., Lemaréchal, C., Sagastizábal, C. (1995): A family of variable metric proximal methods. Math. Program. 68, 15–47  
3. Burke, J.V., Qian, M.: The variable metric proximal point algorithm for monotone operators, to appear in SIAM J. Control Optim.  
4. Burke, J.V., Qian, M. (1998): On the local super-linear convergence of a matrix secant implementation of the variable metric proximal point algorithm. In: Fukushima, M., Qi, L., eds., Reformulation – Nonsmooth, Piecewise Smooth, Semismooth and Smoothing Methods, pp. 317–334. Kluwer Academic Publishers, Dordrecht  
5. Burke, J.V., Qian, M.: On the superlinear convergence of the variable metric proximal point algorithm using Broyden and BFGS matrix secant updating, to appear in Math. Program.  
6. Chen, X. (1996): Convergence of the BFGS method for $LC^{1}$ convex constrained optimization. SIAM J. Control Optim. 34, 2051–2063  
7. Correa, R., Lemaréchal, C. (1993): Convergence of some algorithms for convex minimization. Math. Program. 62, 261–275  
8. Dennis, J.E. Jr., Moré, J.J. (1974): A characterization of superlinear convergence and its applications to quasi-Newton methods. Math. Comput. 28, 549–560  
9. Dennis, J.E. Jr., Schnabel, R.B. (1983): Numerical Methods for Unconstrained Optimization and Nonlinear Equations. Prentice-Hall, Englewood Cliffs, N.J.  
10. Fletcher, R. (1987): Practical Methods of Optimization, second edition. Wiley, Chichester, New York  
11. Fukushima, M. (1984): A descent algorithm for nonsmooth convex optimization. Math. Program. 30, 163–175  
12. Fukushima, M., Qi, L. (1996): A globally and superlinearly convergent algorithm for nonsmooth convex minimization. SIAM J. Optim. 6, 1106–1120  
13. Hiriart-Urruty, J.-B., Lemaréchal, C. (1993): Convex Analysis and Minimization Algorithms. Springer  
14. Ip, C.M., Kyparisis, J. (1992): Local convergence of quasi-Newton methods for B-differentiable equations. Math. Program. 56, 71–89  
15. Kiwiel, K.C. (1983): An aggregate subgradient method for nonsmooth convex minimization. Math. Program. 27, 320–341  
16. Kiwiel, K.C. (1986): A method for solving certain quadratic programming problems arising in nonsmooth optimization. IMA J. Num. Anal. 6, 153–172  
17. Kiwiel, K.C. (1990): Proximity control in bundle methods for convex nondifferentiable minimization. Math. Program. 46, 105–122  
18. Lemaréchal, C., Mifflin, R., eds. (1978): Nonsmooth Optimization. Pergamon Press, Oxford  
19. Lemaréchal, C., Sagastizábal, C. (1994): An approach to variable metric bundle methods. In: Henry, J., Yvon, J.-P., eds., Proceedings of the 16th IFIP Conference on System Modelling and Optimization, pp. 144–162. Springer  
20. Lemaréchal, C., Sagastizábal, C. (1997): Practical aspects of the Moreau-Yosida regularization: Theoretical preliminaries. SIAM J. Optim. 7, 367–385  
21. Lemaréchal, C., Sagastizábal, C. (1997): Variable metric bundle methods: From conceptual to implementable forms. Math. Program. 76, 393–410  
22. Mifflin, R. (1996): A quasi-second-order proximal bundle algorithm. Math. Program. 73, 51-72  
23. Mifflin, R., Sun, D., Qi, L. (1998): Quasi-Newton bundle-type methods for nondifferentiable convex optimizations. SIAM J. Optim. 8, 583–603  
24. Polak, E., Wiest, E.J. (1990): Variable-metric technique for the solution of affinely parametrized nondifferentiable optimal design problems. J. Optimization Theory Appl. 66, 391–414  
25. Poliquin, R.A., Rockafellar, R.T. (1996): Generalized Hessian properties of regularized nonsmooth functions. SIAM J. Optim. 6, 1121–1137  
26. Powell, M.J.D. (1976): Some global convergence properties of a variable metric algorithm for minimization without exact line searches. In: Cottle, R.W., Lemke, C.E., eds., Nonlinear Programming, SIAM-AMS Proceedings, Vol. IX, pp. 53–72. American Mathematical Society, Providence, RI  
27. Qi, L. (1993): Convergence analysis of some algorithms for solving nonsmooth equations. Math. Oper. Res. 18, 227–244  
28. Qi, L. (1994): Second-order analysis of the Moreau-Yosida approximation of a convex function. Applied Mathematics Report. Department of Applied Mathematics, The University of New South Wales  
29. Qi, L., Chen, X. (1997): A preconditioning proximal Newton method for nondifferentiable convex optimization. Math. Program. 76, 411–429  
30. Qi, L., Sun, J. (1993): A nonsmooth version of Newton's method. Math. Program. 58, 353-368  
31. Rauf, A.I., Fukushima, M.: A globally convergent BFGS method for nonsmooth convex optimization, to appear in J. Optimization Theory Appl.  
32. Rockafellar, R.T. (1970): Convex Analysis. Princeton University Press, Princeton, N.J.  
33. Rockafellar, R.T. (1976): Augmented Lagrangians and applications of the proximal point algorithm in convex programming. Math. Oper. Res. 1, 97–116  
34. Shor, N.Z. (1985): Minimization Methods for Nondifferentiable Functions. Springer  
35. Stewart, G.W. (1980): The efficient generation of random orthogonal matrices with an application to condition estimators. SIAM J. Num. Anal. 17, 403–409  
36. Zhu, C. (1996): Asymptotic convergence analysis of some inexact proximal point algorithms for minimization. SIAM J. Optim. 6, 626–637
