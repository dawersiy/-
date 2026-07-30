# Yu. Nesterov $^{*}$

# Smooth minimization of non-smooth functions

Received: February 4, 2003 / Accepted: July 8, 2004

Published online: December 29, 2004 – © Springer-Verlag 2004

Abstract. In this paper we propose a new approach for constructing efficient schemes for non-smooth convex optimization. It is based on a special smoothing technique, which can be applied to functions with explicit max-structure. Our approach can be considered as an alternative to black-box minimization. From the viewpoint of efficiency estimates, we manage to improve the traditional bounds on the number of iterations of the gradient schemes from $O\left(\frac{1}{\epsilon^2}\right)$ to $O\left(\frac{1}{\epsilon}\right)$, keeping basically the complexity of each iteration unchanged.

Key words. Non-smooth optimization – Convex optimization – Optimal methods – Complexity theory – Structural optimization

# 1. Introduction

Motivation. Historically, the subgradient methods were the first numerical schemes for non-smooth convex minimization (see [11] and [7] for historical comments). Very soon it was proved that the efficiency estimate of these schemes is of the order

$$
O \left(\frac {1}{\epsilon^ {2}}\right), \tag {1.1}
$$

where $\epsilon$ is the desired absolute accuracy of the approximate solution in function value (see also [3]).

Up to now some variants of these methods remain attractive for researchers (e.g. [4, 1]). This is not too surprising since the main drawback of these schemes, the slow rate of convergence, is compensated by the very low complexity of each iteration. Moreover, it was shown in [8] that the efficiency estimate of the simplest subgradient method cannot be improved uniformly in dimension of the space of variables. Of course, this statement is valid only for the black-box oracle model of the objective function. However, its proof is constructive; namely, it was shown that the problem

$$
\min _ {x} \left\{\max _ {1 \leq i \leq n} x ^ {(i)}: \sum_ {i = 1} ^ {n} (x ^ {(i)}) ^ {2} \leq 1 \right\}
$$

Y. Nesterov: Center for Operations Research and Econometrics (CORE), Catholic University of Louvain (UCL), 34 voie du Roman Pays, 1348 Louvain-la-Neuve, Belgium. e-mail: nesterov@core.ucl.ac.be

* This paper presents research results of the Belgian Program on Interuniversity Poles of Attraction initiated by the Belgian State, Prime Minister's Office, Science Policy Programming. The scientific responsibility is assumed by the author.

is difficult for all numerical schemes. This demonstration possibly explains a common belief that the worst-case complexity estimate for finding an $\epsilon$-approximation of a minimum of a piece-wise linear function by gradient schemes is given by (1.1).

Actually, it is not the case. In practice, we never meet a pure black box model. We always know something about the structure of the underlying objects. And the proper use of the structure of the problem can and does help in finding the solution.

In this paper we discuss such a possibility. Namely, we present a systematic way to approximate the initial non-smooth objective function by a function with Lipschitz-continuous gradient. After that we minimize the smooth function by an efficient gradient method of type [9], [10]. It is known that these methods have an efficiency estimate of the order $O\left(\sqrt{\frac{L}{\epsilon}}\right)$, where $L$ is the Lipschitz constant for the gradient of the objective function. We show that in constructing a smooth $\epsilon$ -approximation of the initial function, $L$ can be chosen of the order $\frac{1}{\epsilon}$. Thus, we end up with a gradient scheme with efficiency estimate of the order $O\left(\frac{1}{\epsilon}\right)$. Note that our approach is different from the smoothing technique used in constrained optimization for updating Lagrange multipliers (see [6] and references therein).

Contents. The paper is organized as follows. In Section 2 we study a simple approach for creating smooth approximations of non-smooth functions. In some aspects, our approach resembles an old technique used in the theory of Modified Lagrangians [5, 2]. It is based on the notion of an adjoint problem, which is a specification of the notion of a dual problem. An adjoint problem is not uniquely defined and its dimension is different from the dimension of the primal space. We can expect that the increase of the dimension of the adjoint space makes the structure of the adjoint problem simpler. In Section 3 we present a fast scheme for minimizing smooth convex functions. One of the advantages of this scheme consists in a possibility to use a specific norm, which is suitable for measuring the curvature of a particular objective function. This ability is similar to that of the mirror descent methods [8, 1]. In Section 4 we apply the results of the previous section to particular problem instances: solution of a matrix game, a continuous location problem, a variational inequality with linear operator and a problem of the minimization of a piece-wise linear function (see Section 11.3 [7] for interpretation of some examples). For all cases we give the upper bounds on the complexity of finding $\epsilon$ -solutions for the primal and dual problems. In Section 5 we discuss implementation issues and some modifications of the proposed algorithm. Preliminary computational results are given in Section 6. In this section we compare our computational results with theoretical complexity of a cutting plane scheme and a short-step path-following scheme. We show that on our family of test problems the new gradient schemes can indeed compete with the most powerful polynomial-time methods.

Notation. In what follows we work with different primal and dual spaces equipped with corresponding norms. We use the following notation. The (primal) finite-dimensional real vector space is always denoted by $E$, possibly with an index. This space is endowed with a norm $\| \cdot \|$, which has the same index as the corresponding space. The space of linear functions on $E$ (the dual space) is denoted by $E^{*}$. For $s \in E^{*}$ and $x \in E$ we denote $\langle s, x \rangle$ the value of $s$ at $x$. The scalar product $\langle \cdot, \cdot \rangle$ is marked by the same index as $E$. The norm for the dual space is defined in the standard way:

$$
\| s \| ^ {*} = \max _ {x} \{\langle s, x \rangle : \| x \| = 1 \}.
$$

For a linear operator $A: E_1 \to E_2^*$ we define the adjoint operator $A^*: E_2 \to E_1^*$ in the following way:

$$
\langle A x, u \rangle_ {2} = \langle A ^ {*} u, x \rangle_ {1} \quad \forall x \in E _ {1}, u \in E _ {2}.
$$

The norm of such an operator is defined as follows:

$$
\| A \| _ {1, 2} = \max _ {x, u} \{\langle A x, u \rangle_ {2}: \| x \| _ {1} = 1, \| u \| _ {2} = 1 \}.
$$

Clearly,

$$
\| A \| _ {1, 2} = \| A ^ {*} \| _ {2, 1} = \max _ {x} \{\| A x \| _ {2} ^ {*}: \| x \| _ {1} = 1 \} = \max _ {u} \{\| A ^ {*} u \| _ {1} ^ {*}: \| u \| _ {2} = 1 \}.
$$

Hence, for any $u\in E_2$ we have

$$
\| A ^ {*} u \| _ {1} ^ {*} \leq \| A \| _ {1, 2} \cdot \| u \| _ {2}. \tag {1.2}
$$

# 2. Smooth approximations of non-differentiable functions

In this paper our main problem of interest is as follows:

$$
\text {Find} f ^ {*} = \min _ {x} \{f (x): x \in Q _ {1} \}, \tag {2.1}
$$

where $Q_{1}$ is a bounded closed convex set in a finite-dimensional real vector space $E_{1}$ and $f(x)$ is a continuous convex function on $Q_{1}$. We do not assume $f$ to be differentiable.

Quite often, the structure of the objective function in (2.1) is given explicitly. Let us assume that this structure can be described by the following model:

$$
f (x) = \hat {f} (x) + \max _ {u} \{\langle A x, u \rangle_ {2} - \hat {\phi} (u): u \in Q _ {2} \}, \tag {2.2}
$$

where the function $\hat{f}(x)$ is continuous and convex on $Q_{1}$, $Q_{2}$ is a closed convex bounded set in a finite-dimensional real vector space $E_{2}$, $\hat{\phi}(u)$ is a continuous convex function on $Q_{2}$ and the linear operator A maps $E_{1}$ to $E_{2}^{*}$. In this case the problem (2.1) can be written in an adjoint form:

$$
\begin{aligned} \max _ {u} \{\phi (u): u &\in Q _ {2} \}, \\ \phi (u) &= - \hat {\phi} (u) + \min _ {x} \{\langle A x, u \rangle_ {2} + \hat {f} (x): x \in Q _ {1} \}. \tag {2.3} \\ \end{aligned}
$$

However, note that this possibility is not completely similar to (2.2) since in our case we implicitly assume that the function $\hat{\phi}(u)$ and the set $Q_{2}$ are so simple that the solution of the optimization problem in (2.2) can be found in a closed form. This assumption may be not valid for the objects defining the function $\phi(u)$.

Note that for a convex function $f(x)$ the representation (2.2) is not uniquely defined. If we take, for example,

$$
Q _ {2} \equiv E _ {2} = E _ {1} ^ {*}, \quad \hat {\phi} (u) \equiv f _ {*} (u) = \max _ {x} \{\langle u, x \rangle_ {1} - f (x): x \in E _ {1} \},
$$

then $\hat{f}(x) \equiv 0$, and A is equal to I, the identity operator. However, in this case the function $\hat{\phi}(u)$ may be too complicated for our goals. Intuitively, it is clear that the bigger the dimension of space $E_{2}$ is, the simpler the structures of the adjoint objects, the function $\hat{\phi}(u)$ and the set $Q_{2}$ are. Let us see that in an example.

Example 1. Consider $f(x) = \max_{1 \leq j \leq m} |\langle a_j, x \rangle_1 - b^{(j)}|$. Then we can set $A = I$, $E_2 = E_1^* = R^n$ and

$$
\begin{aligned} \hat {\phi} (u) &= \max _ {x} \left\{\langle u, x \rangle_ {1} - \max _ {1 \leq j \leq m} | \langle a _ {j}, x \rangle_ {1} - b ^ {(j)} | \right\} \\ &= \max _ {x} \min _ {s \in R ^ {m}} \left\{\langle u, x \rangle_ {1} - \sum_ {j = 1} ^ {m} s ^ {(j)} [ \langle a _ {j}, x \rangle_ {1} - b ^ {(j)} ]: \sum_ {j = 1} ^ {m} | s ^ {(j)} | \leq 1 \right\} \\ &= \min _ {s \in R ^ {m}} \left\{\sum_ {j = 1} ^ {m} s ^ {(j)} b ^ {(j)}: u = \sum_ {j = 1} ^ {m} s ^ {(j)} a _ {j}, \sum_ {j = 1} ^ {m} | s ^ {(j)} | \leq 1 \right\}. \\ \end{aligned}
$$

It is clear that the structure of such a function can be very complicated.

Let us look at another possibility. Note that

$$
f (x) = \max _ {1 \leq j \leq m} | \langle a _ {j}, x \rangle_ {1} - b ^ {(j)} | = \max _ {u \in R ^ {m}} \left\{\sum_ {j = 1} ^ {m} u ^ {(j)} [ \langle a _ {j}, x \rangle_ {1} - b ^ {(j)} ]: \sum_ {j = 1} ^ {m} | u ^ {(j)} | \leq 1 \right\}.
$$

In this case $E_2 = R^m$, $\hat{\phi}(u) = \langle b, u \rangle_2$ and $Q_2 = \{u \in R^m : \sum_{j=1}^{m} |u^{(j)}| \leq 1\}$.

Finally, we can represent $f(x)$ also as follows:

$$
\begin{aligned} f (x) &= \max _ {u = (u _ {1}, u _ {2}) \in R ^ {2 m}} \left\{\sum_ {j = 1} ^ {m} (u _ {1} ^ {(j)} - u _ {2} ^ {(j)}) \cdot [ \langle a _ {j}, x \rangle_ {1} - b ^ {(j)} ]: \right. \\ \left. \sum_ {j &= 1} ^ {m} (u _ {1} ^ {(j)} + u _ {2} ^ {(j)}) = 1, u \geq 0 \right\}. \\ \end{aligned}
$$

In this case $E_2 = R^{2m}$, $\hat{\phi}(u)$ is a linear function and $Q_2$ is a simplex. In Section 4.4 we will see that this representation is the best.

Let us show that the knowledge of the structure (2.2) can help in solving both problems (2.1) and (2.3). We are going to use this structure to construct a smooth approximation of the objective function in (2.1).

Consider a prox-function $d_{2}(u)$ of the set $Q_{2}$. This means that $d_{2}(u)$ is continuous and strongly convex on $Q_{2}$ with some convexity parameter $\sigma_{2} > 0$. Denote by

$$
u _ {0} = \arg \min _ {u} \{d _ {2} (u): u \in Q _ {2} \}
$$

its prox-center. Without loss of generality we assume that $d_2(u_0) = 0$. Thus, for any $u \in Q_2$ we have

$$
d _ {2} (u) \geq \frac {1}{2} \sigma_ {2} \| u - u _ {0} \| _ {2} ^ {2}. \tag {2.4}
$$

Let $\mu$ be a positive smoothness parameter. Consider the following function:

$$
f _ {\mu} (x) = \max _ {u} \{\langle A x, u \rangle_ {2} - \hat {\phi} (u) - \mu d _ {2} (u): u \in Q _ {2} \}. \tag {2.5}
$$

Denote by $u_{\mu}(x)$ the optimal solution of the above problem. Since the function $d_{2}(u)$ is strongly convex, this solution is unique.

Theorem 1. The function $f_{\mu}(x)$ is well defined and continuously differentiable at any $x \in E_1$. Moreover, this function is convex and its gradient

$$
\nabla f _ {\mu} (x) = A ^ {*} u _ {\mu} (x) \tag {2.6}
$$

is Lipschitz continuous with constant

$$
L _ {\mu} = \frac {1}{\mu \sigma_ {2}} \| A \| _ {1, 2} ^ {2}.
$$

Proof. Indeed, $f_{\mu}(x)$ is convex as a maximum of functions, which are linear in x. It is differentiable since $u_{\mu}(x)$ is unique. Let us prove that its gradient is Lipschitz continuous. Consider two points $x_{1}$ and $x_{2}$. For the sake of notation, without loss of generality we assume that the functions $\hat{\phi}(\cdot)$ and $d_{2}(\cdot)$ are differentiable. From the first-order optimality conditions we have

$$
\langle A x _ {1} - \nabla \hat {\phi} (u _ {\mu} (x _ {1})) - \mu \nabla d _ {2} (u _ {\mu} (x _ {1})), u _ {\mu} (x _ {2}) - u _ {\mu} (x _ {1}) \rangle_ {2} \leq 0,
$$

$$
\langle A x _ {2} - \nabla \hat {\phi} (u _ {\mu} (x _ {2})) - \mu \nabla d _ {2} (u _ {\mu} (x _ {2})), u _ {\mu} (x _ {1}) - u _ {\mu} (x _ {2}) \rangle_ {2} \leq 0.
$$

Adding these inequalities and using convexity of $\hat{\phi} (\cdot)$ and strong convexity of $d_{2}(\cdot)$, we continue as follows:

$$
\begin{array}{l} \langle A (x _ {1} - x _ {2}), u _ {\mu} (x _ {1}) - u _ {\mu} (x _ {2}) \rangle_ {2} \\ \geq \left\langle \nabla \hat {\phi} \left(u _ {\mu} \left(x _ {1}\right)\right) - \nabla \hat {\phi} \left(u _ {\mu} \left(x _ {2}\right)\right) + \mu \left(\nabla d _ {2} \left(u _ {\mu} \left(x _ {1}\right)\right) \right. \right. \\ - \nabla d _ {2} (u _ {\mu} (x _ {2}))), u _ {\mu} (x _ {1}) - u _ {\mu} (x _ {2}) \rangle_ {2} \\ \geq \mu \langle \nabla d _ {2} (u _ {\mu} (x _ {1})) - \nabla d _ {2} (u _ {\mu} (x _ {2})), u _ {\mu} (x _ {1}) \\ \left. - u _ {\mu} \left(x _ {2}\right) \right\rangle_ {2} \geq \mu \sigma_ {2} \| u _ {\mu} \left(x _ {1}\right) - u _ {\mu} \left(x _ {2}\right) \| _ {2} ^ {2}. \\ \end{array}
$$

Thus, in view of (1.2), we have

$$
\begin{aligned} (\| A ^ {*} u _ {\mu} (x _ {1}) - A ^ {*} u _ {\mu} (x _ {2})) \| _ {1} ^ {*}) ^ {2} &\leq \| A \| _ {1, 2} ^ {2} \cdot \| u _ {\mu} (x _ {1}) - u _ {\mu} (x _ {2}) \| _ {2} ^ {2} \\ &\leq \frac {1}{\mu \sigma_ {2}} \| A \| _ {1, 2} ^ {2} \langle A ^ {*} (u _ {\mu} (x _ {1}) - u _ {\mu} (x _ {2})), x _ {1} - x _ {2} \rangle_ {1} \\ &\leq \frac {1}{\mu \sigma_ {2}} \| A \| _ {1, 2} ^ {2} \cdot \| A ^ {*} u _ {\mu} (x _ {1}) - A ^ {*} u _ {\mu} (x _ {2}) \| _ {1} ^ {*} \cdot \| x _ {1} - x _ {2} \| _ {1}. \\ \end{aligned}
$$

□

Denote $D_{2} = \max_{u}\{d_{2}(u): u \in Q_{2}\}$ and $f_{0}(x) = \max_{u}\{\langle Ax, u \rangle_{2} - \hat{\phi}(u): u \in Q_{2}\}$. Then, for any $x \in E_{1}$ we have

$$
f _ {\mu} (x) \leq f _ {0} (x) \leq f _ {\mu} (x) + \mu D _ {2}. \tag {2.7}
$$

Thus, for $\mu > 0$ the function $f_{\mu}(x)$ can be seen as a uniform smooth approximation of the function $f_0(x)$.

In the next section we present an efficient scheme for minimizing a convex function with Lipschitz continuous gradient.

# 3. Optimal scheme for smooth optimization

Let us fix a function $f(x)$, which is differentiable and convex on a closed convex set $Q \subseteq E$. Assume that the gradient of this function is Lipschitz continuous:

$$
\| \nabla f (x) - \nabla f (y) \| ^ {*} \leq L \| x - y \|, \quad \forall x, y \in Q,
$$

(notation: $f \in C_L^{1,1}(Q)$ ). In this case for any $x, y \in Q$ we have

$$
f (y) \leq f (x) + \langle \nabla f (x), y - x \rangle + \frac {1}{2} L \| y - x \| ^ {2}. \tag {3.1}
$$

Denote by $T_{Q}(x) \in Q$ the optimal solution of the following minimization problem:

$$
\min _ {y} \left\{\langle \nabla f (x), y - x \rangle + \frac {1}{2} L \| y - x \| ^ {2}: y \in Q \right\}. \tag {3.2}
$$

If the norm $\| \cdot \|$ is not strictly convex, the problem (3.2) can have multiple solutions. In this case we stick the notation $T_{Q}(x)$ to any of them. In view of inequality (3.1), for any $x \in Q$ we have

$$
f (T _ {Q} (x)) \leq f (x) + \min _ {y} \left\{\langle \nabla f (x), y - x \rangle + \frac {1}{2} L \| y - x \| ^ {2}: y \in Q \right\}. \tag {3.3}
$$

Denote by $d(x)$ a prox-function of the set $Q$. We assume that $d(x)$ is continuous and strongly convex on $Q$ with convexity parameter $\sigma > 0$. Let $x_0$ be the center of the set $Q$ :

$$
x _ {0} = \arg \min _ {x} \{d (x): x \in Q \}.
$$

Without loss of generality assume that $d(x_0) = 0$. Thus, for any $x \in Q$ we have

$$
d (x) \geq \frac {1}{2} \sigma \| x - x _ {0} \| ^ {2}. \tag {3.4}
$$

In this section we consider an optimization scheme for solving the following problem:

$$
\min _ {x} \{f (x): x \in Q \}, \tag {3.5}
$$

with $f \in C_L^{1,1}(Q)$. For simplicity, we assume that the constant $L > 0$ is known. Recall that the standard gradient projection method at this problem converges as $O(\frac{1}{k})$, where $k$ is the iteration counter (see, e.g. [7]).

In our scheme we update recursively two sequences of points $\{x_k\}_{k=0}^{\infty} \subset Q$ and $\{y_k\}_{k=0}^{\infty} \subset Q$ in such a way that they satisfy the following relation:

$$
A _ {k} f (y _ {k}) \leq \psi_ {k} \equiv \min _ {x} \left\{\frac {L}{\sigma} d (x) + \sum_ {i = 0} ^ {k} \alpha_ {i} [ f (x _ {i}) + \langle \nabla f (x _ {i}), x - x _ {i} \rangle ]: x \in Q \right\}, \quad (\mathcal {R} _ {k})
$$

where $A_{k} = \sum_{i=0}^{k} \alpha_{i}$ and $\{\alpha_{i}\}_{i=0}^{\infty}$ are some positive step-size parameters. Let us present the way this can be done.

Indeed, for $k = 0$ let us take some $\alpha_0 \in (0,1]$ and $y_0 = T_Q(x_0)$. Then, in view of inequalities (3.4) and (3.3), we have:

$$
\begin{aligned} \min _ {x} \left\{\frac {L}{\sigma} d (x) + \alpha_ {0} [ f (x _ {0}) + \langle \nabla f (x _ {0}), x - x _ {0} \rangle ]: x &\in Q \right\} \\ &\geq \alpha_ {0} \min _ {x} \left\{\frac {L}{2 \alpha_ {0}} \| x - x _ {0} \| ^ {2} + f (x _ {0}) + \langle \nabla f (x _ {0}), x - x _ {0} \rangle : x \in Q \right\} \geq \alpha_ {0} f (y _ {0}), \\ \end{aligned}
$$

and that is $(\mathcal{R}_0)$.

Denote

$$
z _ {k} = \arg \min _ {x} \left\{\frac {L}{\sigma} d (x) + \sum_ {i = 0} ^ {k} \alpha_ {i} [ f (x _ {i}) + \langle \nabla f (x _ {i}), x - x _ {i} \rangle ]: x \in Q \right\}.
$$

Lemma 1. Let some sequence $\{\alpha_k\}_{k=0}^{\infty}$ satisfy the condition:

$$
\alpha_ {0} \in (0, 1 ], \quad \alpha_ {k + 1} ^ {2} \leq A _ {k + 1}, k \geq 0. \tag {3.6}
$$

Suppose that $(\mathcal{R}_k)$ holds for some $k\geq 0$. Let us choose $\tau_{k} = \frac{\alpha_{k + 1}}{A_{k + 1}}$ and

$$
x _ {k + 1} = \tau_ {k} z _ {k} + (1 - \tau_ {k}) y _ {k},
$$

$$
y _ {k + 1} = T _ {Q} (x _ {k + 1}). \tag {3.7}
$$

Then the relation $(\mathcal{R}_{k + 1})$ holds.

Proof. Indeed, assume $(\mathcal{R}_k)$ holds. Then, since function $d(x)$ is strongly convex, we have

$$
\begin{aligned} \psi_ {k + 1} &= \min _ {x} \left\{\frac {L}{\sigma} d (x) + \sum_ {i = 0} ^ {k + 1} \alpha_ {i} [ f (x _ {i}) + \langle \nabla f (x _ {i}), x - x _ {i} \rangle ]: x \in Q \right\} \\ &\geq \min _ {x} \left\{\psi_ {k} + \frac {1}{2} L \| x - z _ {k} \| ^ {2} + \alpha_ {k + 1} [ f (x _ {k + 1}) + \langle \nabla f (x _ {k + 1}), x - x _ {k + 1} \rangle ]: x \in Q \right\}. \\ \end{aligned}
$$

Further, in view of relation $(\mathcal{R}_k)$ and the first rule in (3.7), we have

$$
\begin{aligned} \psi_ {k} + \alpha_ {k + 1} [ f (x _ {k + 1}) + \langle \nabla f (x _ {k + 1}), x - x _ {k + 1} \rangle ] \\ &\geq A _ {k} f (y _ {k}) + \alpha_ {k + 1} [ f (x _ {k + 1}) + \langle \nabla f (x _ {k + 1}), x - x _ {k + 1} \rangle ] \\ &\geq A _ {k} [ f (x _ {k + 1}) + \langle \nabla f (x _ {k + 1}), y _ {k} - x _ {k + 1} \rangle ] \\ + \alpha_ {k + 1} [ f (x _ {k + 1}) + \langle \nabla f (x _ {k + 1}), x - x _ {k + 1} \rangle ] \\ &= A _ {k + 1} f (x _ {k + 1}) + \alpha_ {k + 1} \langle \nabla f (x _ {k + 1}), x - z _ {k} \rangle . \tag {3.8} \\ \end{aligned}
$$

In view of condition (3.6), $A_{k+1}^{-1} \geq \tau_k^2$. Therefore, we can continue as follows:

$$
\begin{array}{l} \psi_ {k + 1} \geq A _ {k + 1} f (x _ {k + 1}) + \min _ {x} \left\{\frac {1}{2} L \| x - z _ {k} \| ^ {2} + \alpha_ {k + 1} \langle \nabla f (x _ {k + 1}), x - z _ {k} \rangle : x \in Q \right\} \\ = A _ {k + 1} \left[ f (x _ {k + 1}) + \min _ {x} \left\{\frac {L}{2 A _ {k + 1}} \| x - z _ {k} \| ^ {2} + \tau_ {k} \langle \nabla f (x _ {k + 1}), x - z _ {k} \rangle : x \in Q \right\} \right] \\ \geq A _ {k + 1} \left[ f (x _ {k + 1}) + \min _ {x} \left\{\frac {1}{2} \tau_ {k} ^ {2} L \| x - z _ {k} \| ^ {2} + \tau_ {k} \langle \nabla f (x _ {k + 1}), x - z _ {k} \rangle : x \in Q \right\} \right]. \tag {3.9} \\ \end{array}
$$

Finally, note that $\tau_{k}\in [0,1]$. For arbitrary $x\in Q$ define

$$
y = \tau_ {k} x + (1 - \tau_ {k}) y _ {k}.
$$

Then, in view of the first relation in (3.7) we have

$$
y - x _ {k + 1} = \tau_ {k} (x - z _ {k}).
$$

Hence, in view of (3.3) and the second rule in (3.7) we conclude that

$$
\begin{aligned} \min _ {x} \left\{\frac {1}{2} \tau_ {k} ^ {2} L \| x - z _ {k} \| ^ {2} + \tau_ {k} \langle \nabla f (x _ {k + 1}), x - z _ {k} \rangle : x &\in Q \right\} \\ &= \min _ {y} \left\{\frac {1}{2} L \| y - x _ {k + 1} \| ^ {2} + \langle \nabla f (x _ {k + 1}), y - x _ {k + 1} \rangle : y \in \tau_ {k} Q + (1 - \tau_ {k}) y _ {k} \right\} \\ &\geq \min _ {y} \left\{\frac {1}{2} L \| y - x _ {k + 1} \| ^ {2} + \langle \nabla f (x _ {k + 1}), y - x _ {k + 1} \rangle : y \in Q \right\} \\ &\geq f (y _ {k + 1}) - f (x _ {k + 1}). \\ \end{aligned}
$$

Combining this bound with the final estimate in (3.9) we get the result.

Clearly, there are many ways to satisfy the conditions (3.6). Let us give an example.

Lemma 2. For $k \geq 0$ define $\alpha_k = \frac{k + 1}{2}$. Then

$$
\tau_ {k} = \frac {2}{k + 3}, \quad A _ {k} = \frac {(k + 1) (k + 2)}{4}, \tag {3.10}
$$

and the conditions (3.6) are satisfied.

Proof. Indeed, $\tau_k^2 = \frac{\alpha_{k + 1}^2}{A_{k + 1}^2} = \frac{4}{(k + 3)^2} \leq \frac{4}{(k + 2)(k + 3)} = \frac{1}{A_{k + 1}}$, and that is (3.6).

![](images/5cda6730f77cb191351c6eaaa745ef5a4b9ed38a744583cf775f3ddea06ae1bf.jpg)

Now we can analyze the behavior of the following scheme.

# For $k \geq 0$ do

1. Compute $f(x_{k})$ and $\nabla f(x_{k})$.  
2. Find $y_{k} = T_{Q}(x_{k})$.  
3. Find $z_k = \arg \min_x \left\{ \frac{L}{\sigma} d(x) + \sum_{i=0}^{k} \frac{i+1}{2} [f(x_i) + \langle \nabla f(x_i), x - x_i \rangle] : x \in Q \right\}$.  
4. Set $x_{k+1} = \frac{2}{k+3} z_k + \frac{k+1}{k+3} y_k$. (3.11)

Theorem 2. Let the sequences $\{x_k\}_{k=0}^{\infty}$ and $\{y_k\}_{k=0}^{\infty}$ be generated by the method (3.11). Then for any $k \geq 0$ we have

$$
\begin{aligned} \frac {(k + 1) (k + 2)}{4} f (y _ {k}) \\ &\leq \min _ {x} \left\{\frac {L}{\sigma} d (x) + \sum_ {i = 0} ^ {k} \frac {i + 1}{2} [ f (x _ {i}) + \langle \nabla f (x _ {i}), x - x _ {i} \rangle ]: x \in Q \right\}. \tag {3.12} \\ \end{aligned}
$$

Therefore,

$$
f (y _ {k}) - f (x ^ {*}) \leq \frac {4 L d (x ^ {*})}{\sigma (k + 1) (k + 2)}, \tag {3.13}
$$

where $x^{*}$ is an optimal solution to the problem (3.5).

Proof. Indeed, let us choose the sequence $\{\alpha_k\}_{k=0}^{\infty}$ as in Lemma 2. Then, in view of Lemma 1 and convexity of $f(x)$ we have

$$
A _ {k} f (y _ {k}) \leq \psi_ {k} \leq \frac {L}{\sigma} d (x ^ {*}) + A _ {k} f (x ^ {*}).
$$

It remains to use (3.10).

Note that, in general, method (3.11) does not ensure a monotone decrease of the objective function during the minimization process. However, sometimes this property is quite useful. To achieve that, we need to introduce a minor change in the scheme.

Indeed, in the proof of Lemma 1 we need only the following condition on $y_{k+1}$ :

$$
f (y _ {k + 1}) \leq f (T _ {Q} (x _ {k + 1})).
$$

Let us change the rules of Step 2 in (3.11) as follows:

2'. Find $y_{k}'=T_{Q}(x_{k})$ . Compute $f(y_{k}')$ .

$$
\text {Set} y _ {k} = \arg \min _ {x} \left\{f (x): x \in \{y _ {k - 1}, x _ {k}, y _ {k}' \} \right\}. \tag {3.14}
$$

Clearly, in this case we will have

$$
f (y _ {k}) \leq f (y _ {k - 1}) \leq \dots \leq f (x _ {0}). \tag {3.15}
$$

# 4. Application examples

Let us put the results of Sections 2 and 3 together. Let us assume that the function $\hat{f} (\cdot)$ in (2.2) is differentiable and its gradient is Lipschitz-continuous with some constant $M\geq 0$. Then the smoothing technique as applied to the problem (2.1) gives us the following objective function:

$$
\bar {f} _ {\mu} (x) = \hat {f} (x) + f _ {\mu} (x) \quad \rightarrow \quad \min: x \in Q _ {1}. \tag {4.1}
$$

In view of Theorem 1, the gradient of this function is Lipschitz continuous with the constant

$$
L _ {\mu} = M + \frac {1}{\mu \sigma_ {2}} \| A \| _ {1, 2} ^ {2}.
$$

Let us choose some prox-function $d_{1}(x)$ for the set $Q_{1}$ with the convexity parameter $\sigma_{1}$. Recall that we assume the set $Q_{1}$ to be bounded:

$$
\max _ {x} \{d _ {1} (x): x \in Q _ {1} \} \leq D _ {1}.
$$

Theorem 3. Let us apply method (3.11) to the problem (4.1) with the following value of smoothness parameter:

$$
\mu = \mu (N) = \frac {2 \| A \| _ {1 , 2}}{N + 1} \cdot \sqrt {\frac {D _ {1}}{\sigma_ {1} \sigma_ {2} D _ {2}}}.
$$

Then after $N$ iterations we can generate the approximate solutions to the problems (2.1) and (2.3), namely,

$$
\hat {x} = y _ {N} \in Q _ {1}, \quad \hat {u} = \sum_ {i = 0} ^ {N} \frac {2 (i + 1)}{(N + 1) (N + 2)} u _ {\mu} \left(x _ {i}\right) \in Q _ {2}, \tag {4.2}
$$

which satisfy the following inequality:

$$
0 \leq f (\hat {x}) - \phi (\hat {u}) \leq \frac {4 \| A \| _ {1 , 2}}{N + 1} \cdot \sqrt {\frac {D _ {1} D _ {2}}{\sigma_ {1} \sigma_ {2}}} + \frac {4 M D _ {1}}{\sigma_ {1} \cdot (N + 1) ^ {2}}. \tag {4.3}
$$

Thus, the complexity of finding an $\epsilon$-solution to the problems (2.1), (2.3) by the smoothing technique does not exceed

$$
4 \| A \| _ {1, 2} \sqrt {\frac {D _ {1} D _ {2}}{\sigma_ {1} \sigma_ {2}}} \cdot \frac {1}{\epsilon} + 2 \sqrt {\frac {M D _ {1}}{\sigma_ {1} \epsilon}}. \tag {4.4}
$$

Proof. Let us fix an arbitrary $\mu > 0$. In view of Theorem 2, after $N$ iterations of the method (3.11) we can deliver a point $\hat{x} = y_N$ such that

$$
\begin{aligned} \bar {f} _ {\mu} (\hat {x}) &\leq \frac {L _ {\mu} D _ {1}}{\sigma_ {1} (N + 1) ^ {2}} + \min _ {x} \left\{\sum_ {i = 0} ^ {N} \frac {2 (i + 1)}{(N + 1) (N + 2)} [ \bar {f} _ {\mu} (x _ {i}) \right. \\ \left. + \left\langle \nabla \bar {f} _ {\mu} \left(x _ {i}\right), x - x _ {i} \right\rangle_ {1} \right]: x &\in Q _ {1} \Bigg \}. \tag {4.5} \\ \end{aligned}
$$

Note that

$$
\begin{aligned} f _ {\mu} (x) &= \max _ {u} \{\langle A x, u \rangle_ {2} - \hat {\phi} (u) - \mu d _ {2} (u): u \in Q _ {2} \} \\ &= \langle A x, u _ {\mu} (x) \rangle_ {2} - \hat {\phi} (u _ {\mu} (x)) - \mu d _ {2} (u _ {\mu} (x)), \\ \end{aligned}
$$

$$
\langle \nabla f _ {\mu} (x), x \rangle_ {1} = \langle A ^ {*} u _ {\mu} (x), x \rangle_ {1}.
$$

Therefore

$$
f _ {\mu} (x _ {i}) - \langle \nabla f _ {\mu} (x _ {i}), x _ {i} \rangle_ {1} = - \hat {\phi} (u _ {\mu} (x _ {i})) - \mu d _ {2} (u _ {\mu} (x _ {i})), \quad i = 0, \dots , N. \tag {4.6}
$$

Thus, in view of (2.6) and (4.6) we have

$$
\begin{array}{l} \sum_ {i = 0} ^ {N} (i + 1) [ \bar {f} _ {\mu} (x _ {i}) + \langle \nabla \bar {f} _ {\mu} (x _ {i}), x - x _ {i} \rangle_ {1} ] \\ \leq \sum_ {i = 0} ^ {N} (i + 1) [ f _ {\mu} (x _ {i}) - \langle \nabla f _ {\mu} (x _ {i}), x _ {i} \rangle_ {1} ] + \frac {1}{2} (N + 1) (N + 2) (\hat {f} (x) + \langle A ^ {*} \hat {u}, x \rangle_ {1}) \\ \leq - \sum_ {i = 0} ^ {N} (i + 1) \hat {\phi} (u _ {\mu} (x _ {i})) + \frac {1}{2} (N + 1) (N + 2) (\hat {f} (x) + \langle A ^ {*} \hat {u}, x \rangle_ {1}) \\ \leq \frac {1}{2} (N + 1) (N + 2) [ - \hat {\phi} (\hat {u}) + \hat {f} (x) + \langle A x, \hat {u} \rangle_ {2} ]. \\ \end{array}
$$

Hence, using (4.5), (2.3) and (2.7), we get the following bound:

$$
\frac {L _ {\mu} D _ {1}}{\sigma_ {1} (N + 1) ^ {2}} \geq \bar {f} _ {\mu} (\hat {x}) - \phi (\hat {u}) \geq f (\hat {x}) - \phi (\hat {u}) - \mu D _ {2}.
$$

That is

$$
0 \leq f (\hat {x}) - \phi (\hat {u}) \leq \mu D _ {2} + \frac {4 \| A \| _ {1 , 2} ^ {2} D _ {1}}{\mu \sigma_ {1} \sigma_ {2} (N + 1) ^ {2}} + \frac {4 M D _ {1}}{\sigma_ {1} (N + 1) ^ {2}}. \tag {4.7}
$$

Minimizing the right-hand side of this inequality in $\mu$ we get inequality (4.3).

Note that the efficiency estimate (4.4) is much better than the standard bound $O(\frac{1}{\epsilon^{2}})$. In accordance with the above theorem, for M = 0 the optimal dependence of the parameters $\mu$, $L_{\mu}$ and N in $\epsilon$ is as follows:

$$
\mu = \frac {\epsilon}{2 D _ {2}}, \quad L _ {\mu} = \frac {D _ {2}}{2 \sigma_ {2}} \cdot \frac {\| A \| _ {1 , 2} ^ {2}}{\epsilon}, \quad N + 1 = 4 \| A \| _ {1, 2} \sqrt {\frac {D _ {1} D _ {2}}{\sigma_ {1} \sigma_ {2}}} \cdot \frac {1}{\epsilon}. \tag {4.8}
$$

Let us look now at some examples.

# 4.1. Minimax strategies for matrix games

Denote by $\Delta_{n}$ the standard simplex in $R^n$ :

$$
\Delta_ {n} = \{x \in R ^ {n}: x \geq 0, \sum_ {i = 1} ^ {n} x ^ {(i)} = 1 \}.
$$

Let $A: R^n \to R^m$, $E_1 = R^n$ and $E_2 = R^m$. Consider the following saddle point problem:

$$
\min _ {x \in \Delta_ {n}} \max _ {u \in \Delta_ {m}} \{\langle A x, u \rangle_ {2} + \langle c, x \rangle_ {1} + \langle b, u \rangle_ {2} \}. \tag {4.9}
$$

From the viewpoint of players, this problem is reduced to a problem of non-smooth minimization:

$$
\begin{aligned} \min _ {x &\in \Delta_ {n}} f (x), f (x) = \langle c, x \rangle_ {1} + \max _ {1 \leq j \leq m} [ \langle a _ {j}, x \rangle_ {1} + b ^ {(j)} ], \\ \max _ {u &\in \Delta_ {m}} \phi (u), \phi (u) = \langle b, u \rangle_ {2} + \min _ {1 \leq i \leq n} [ \langle \hat {a} _ {i}, u \rangle_ {2} + c ^ {(i)} ], \tag {4.10} \\ \end{aligned}
$$

where $a_j$ are the rows and $\hat{a}_i$ are the columns of the matrix $A$. In order to solve this pair of problems using the smoothing approach, we need to find a reasonable prox-function for the simplex. Let us compare two possibilities.

# 1. Euclidean distance. Let us choose

$$
\begin{aligned} \| x \| _ {1} &= \left[ \sum_ {i = 1} ^ {n} (x ^ {(i)}) ^ {2} \right] ^ {1 / 2}, d _ {1} (x) = \frac {1}{2} \sum_ {i = 1} ^ {n} (x ^ {(i)} - \frac {1}{n}) ^ {2}, \\ \| u \| _ {2} &= \left[ \sum_ {j = 1} ^ {m} (u ^ {(j)}) ^ {2} \right] ^ {1 / 2}, d _ {2} (x) = \frac {1}{2} \sum_ {j = 1} ^ {m} (u ^ {(j)} - \frac {1}{m}) ^ {2}. \\ \end{aligned}
$$

Then $\sigma_{1} = \sigma_{2} = 1, D_{1} = 1 - \frac{1}{n} < 1, D_{2} = 1 - \frac{1}{m} < 1$ and

$$
\| A \| _ {1, 2} = \max _ {u} \{\| A x \| _ {2} ^ {*}: \| x \| _ {1} = 1 \} = \lambda_ {\max} ^ {1 / 2} (A ^ {T} A).
$$

Thus, in our case the estimate (4.3) for the result (4.2) can be specified as follows:

$$
0 \leq f (\hat {x}) - \phi (\hat {u}) \leq \frac {4 \lambda_ {\max} ^ {1 / 2} (A ^ {T} A)}{N + 1}. \tag {4.11}
$$

2. Entropy distance. Let us choose

$$
\| x \| _ {1} = \sum_ {i = 1} ^ {n} | x ^ {(i)} |, d _ {1} (x) = \ln n + \sum_ {i = 1} ^ {n} x ^ {(i)} \ln x ^ {(i)},
$$

$$
\| u \| _ {2} = \sum_ {j = 1} ^ {m} | u ^ {(j)} |, d _ {2} (u) = \ln m + \sum_ {j = 1} ^ {m} u ^ {(j)} \ln u ^ {(j)}.
$$

Lemma 3. Under the above choice of prox-functions we have

$$
\sigma_ {1} = \sigma_ {2} = 1, \quad D _ {1} = \ln n, \quad D _ {2} = \ln m.
$$

Proof. Note that $d_1(x)$ is two times continuously differentiable and $\langle d_1''(x)h, h \rangle = \sum_{i=1}^{n} \frac{(h^{(i)})^2}{x^{(i)}}$. It remains to use the following variant of Cauchy-Schwartz inequality

$$
\left(\sum_ {i = 1} ^ {n} | h ^ {(i)} |\right) ^ {2} \leq \left(\sum_ {i = 1} ^ {n} x ^ {(i)}\right) \cdot \left(\sum_ {i = 1} ^ {n} \frac {(h ^ {(i)}) ^ {2}}{x ^ {(i)}}\right),
$$

which is valid for all positive x. The reasoning for $d_{2}(u)$ is similar.

![](images/fdc59def7a094d39e307d1c5fcd021eaf9a9269348b6bc0bc7cd382e9ad317f2.jpg)

Note also, that now we get the following norm of the operator A:

$$
\| A \| _ {1, 2} = \max _ {x} \{\max _ {1 \leq j \leq m} | \langle a _ {j}, x \rangle |: \| x \| _ {1} = 1 \} = \max _ {i, j} | A ^ {(i, j)} |.
$$

Thus, if we apply the entropy distance, the estimate (4.3) can be written as follows:

$$
0 \leq f (\hat {x}) - \phi (\hat {u}) \leq \frac {4 \sqrt {\ln n \ln m}}{N + 1} \cdot \max _ {i, j} | A ^ {(i, j)} |. \tag {4.12}
$$

Note that typically the estimate (4.12) is much better than the Euclidean variant (4.11).

Let us write down explicitly the smooth approximation for the objective function in the first problem of $(4.10)$ using the entropy distance. By definition,

$$
\bar {f} _ {\mu} (x) = \langle c, x \rangle_ {1} + \max _ {u \in \Delta_ {m}} \left\{\sum_ {j = 1} ^ {m} u ^ {(j)} [ \langle a _ {j}, x \rangle + b ^ {(j)} ] - \mu \sum_ {j = 1} ^ {m} u ^ {(j)} \ln u ^ {(j)} - \mu \ln m \right\}.
$$

Let us apply the following result.

Lemma 4. The solution of the problem

$$
\text {Find} \phi_ {*} (s) = \max _ {u \in \Delta_ {m}} \left\{\sum_ {j = 1} ^ {m} u ^ {(j)} s ^ {(j)} - \mu \sum_ {j = 1} ^ {m} u ^ {(j)} \ln u ^ {(j)} \right\} \tag {4.13}
$$

is given by the vector $u_{\mu}(s) \in \Delta_m$ with the entries

$$
u _ {\mu} ^ {(j)} (s) = \frac {e ^ {s ^ {(j)} / \mu}}{\sum_ {l = 1} ^ {m} e ^ {s ^ {(l)} / \mu}}, \quad j = 1, \dots , m. \tag {4.14}
$$

Therefore $\phi_{*}(s) = \mu \ln \left(\sum_{l = 1}^{m}e^{s^{(l)} / \mu}\right)$.

Proof. Indeed, the first order necessary and sufficient optimality conditions for (4.13) look as follows:

$$
\begin{aligned} s ^ {(j)} - \mu (1 + \ln u ^ {(j)}) &= \lambda , j = 1, \dots , m, \\ \sum_ {j &= 1} ^ {m} u ^ {(j)} = 1. \\ \end{aligned}
$$

Clearly, they are satisfied by (4.14) with $\lambda = \mu \ln \left(\sum_{l=1}^{m} e^{s^{(l)} / \mu}\right) - \mu$.

![](images/5509faf3d436da4b69735db5535235f329a0673fa6dd97a7f377424baf45e4ef.jpg)

Using the result of Lemma 4, we conclude that in our case the problem (4.1) looks as follows:

$$
\bar {f} _ {\mu} (x) = \langle c, x \rangle_ {1} + \mu \ln \left(\frac {1}{m} \sum_ {j = 1} ^ {m} e ^ {[ \langle a _ {j}, x \rangle + b ^ {(j)} ] / \mu}\right) \quad \rightarrow \quad \min: x \in \Delta_ {n}.
$$

Note that the complexity of the oracle for this problem is basically the same as that for the initial problem (4.10).

# 4.2. Continuous location problem

Consider the following location problem. There are p “cities” with “population” $m_{j}$, which are located at points $c_{j} \in R^{n}, j = 1, \ldots, p$. We want to construct a service center at some position $x \in R^{n} \equiv E_{1}$, which minimizes the total social distance $f(x)$ to the center. On the other hand, this center must be constructed not too far from the origin.

Mathematically, the above problem can be posed as follows

$$
\text {Find} f ^ {*} = \min _ {x} \left\{f (x) = \sum_ {j = 1} ^ {p} m _ {j} \| x - c _ {j} \| _ {1}: \| x \| _ {1} \leq \bar {r} \right\}. \tag {4.15}
$$

In accordance to interpretation, it is natural to choose

$$
\| x \| _ {1} = \left[ \sum_ {i = 1} ^ {n} (x ^ {(i)}) ^ {2} \right] ^ {1 / 2}, \quad d _ {1} (x) = \frac {1}{2} \| x \| _ {1} ^ {2}.
$$

Then $\sigma_{1} = 1$ and $D_{1} = \frac{1}{2}\bar{r}^{2}$.

Further, the structure of the adjoint space $E_{2}$ is quite clear:

$$
E _ {2} = (E _ {1} ^ {*}) ^ {p}, \quad Q _ {2} = \left\{u = (u _ {1}, \dots , u _ {p}) \in E _ {2}: \| u _ {j} \| _ {1} ^ {*} \leq 1, j = 1, \dots , p \right\}.
$$

Let us choose

$$
\| u \| _ {2} = \left[ \sum_ {j = 1} ^ {p} m _ {j} (\| u _ {j} \| _ {1} ^ {*}) ^ {2} \right] ^ {1 / 2}, \quad d _ {2} (u) = \frac {1}{2} \| u \| _ {2} ^ {2}.
$$

Then $\sigma_{2} = 1$ and $D_{2} = \frac{1}{2} P$ with $P \equiv \sum_{j=1}^{p} m_{j}$. Note that the value $P$ can be seen as the total size of the population.

It remains to compute the norm of the operator A:

$$
\begin{aligned} \| A \| _ {1, 2} &= \max _ {x, u} \left\{\sum_ {j = 1} ^ {p} m _ {j} \langle u _ {j}, x \rangle_ {1}: \sum_ {j = 1} ^ {p} m _ {j} (\| u _ {j} \| _ {1} ^ {*}) ^ {2} = 1, \| x \| _ {1} = 1 \right\} \\ &= \max _ {r _ {j}} \left\{\sum_ {j = 1} ^ {p} m _ {j} r _ {j}: \sum_ {j = 1} ^ {p} m _ {j} r _ {j} ^ {2} = 1 \right\} = P ^ {1 / 2}. \\ \end{aligned}
$$

Putting the computed values in the estimate (4.3), we get the following rate of convergence:

$$
f (\hat {x}) - f ^ {*} \leq \frac {2 P \bar {r}}{N + 1}. \tag {4.16}
$$

Note that the value $\tilde{f}(x)=\frac{1}{P}f(x)$ corresponds to average individual expenses generated by the location x. Therefore,

$$
\tilde {f} (\hat {x}) - \tilde {f} ^ {*} \leq \frac {2 \bar {r}}{N + 1}.
$$

It is interesting that the right-hand side of this inequality is independent of any dimension. At the same time, it is clear that the reasonable accuracy for the approximate solution of the discussed problem should not be too high. Given a very low complexity of each iteration in the scheme (3.11), the total efficiency of the proposed technique looks quite promising.

To conclude with the location problem, let us write down explicitly a smooth approximation of the objective function.

$$
\begin{aligned} f _ {\mu} (x) &= \max _ {u} \left\{\sum_ {j = 1} ^ {p} m _ {j} \langle u _ {j}, x - c _ {j} \rangle_ {1} - \mu d _ {2} (u): u \in Q _ {2} \right\} \\ &= \max _ {u} \left\{\sum_ {j = 1} ^ {p} m _ {j} \left(\langle u _ {j}, x - c _ {j} \rangle_ {1} - \frac {1}{2} \mu (\| u _ {j} \| _ {1} ^ {*}) ^ {2}\right): \| u _ {j} \| _ {1} ^ {*} \leq 1, j = 1, \dots , p \right\} \\ &= \sum_ {j = 1} ^ {p} m _ {j} \psi_ {\mu} (\| x - c _ {j} \| _ {1}), \\ \end{aligned}
$$

where the function $\psi_{\mu}(\tau),\tau \geq 0$, is defined as follows:

$$
\psi_ {\mu} (\tau) = \max _ {\gamma \in [ 0, 1 ]} \{\gamma \tau - \frac {1}{2} \mu \gamma^ {2} \} = \left\{ \begin{array}{l l} \frac {\tau^ {2}}{2 \mu}, & 0 \leq \tau \leq \mu , \\ \tau - \frac {\mu}{2}, & \mu \leq \tau . \end{array} \right. \tag {4.17}
$$

# 4.3. Variational inequalities with linear operator

Consider a linear operator $B(w) = Bw + c \colon E \to E^*$, which is monotone:

$$
\langle B h, h \rangle \geq 0 \quad \forall h \in E _ {1}.
$$

Let $Q$ be a bounded closed convex set in $E$. Then we can pose the following variational inequality problem:

$$
\text {Find} w ^ {*} \in Q: \quad \langle B (w ^ {*}), w - w ^ {*} \rangle \geq 0 \quad \forall w \in Q. \tag {4.18}
$$

Note that we can always rewrite problem (4.18) as an optimization problem. Indeed, define

$$
\psi (w) = \max _ {v} \{\langle B (v), w - v \rangle : v \in Q \}.
$$

Clearly, $\psi(w)$ is a convex function. It is well known that the problem

$$
\min _ {w} \{\psi (w): w \in Q \} \tag {4.19}
$$

is equivalent to (4.18). For the sake of completeness let us provide this statement with a simple proof.

Lemma 5. A point $w^{*}$ is a solution to (4.19) if and only if it solves variational inequality (4.18). Moreover, for such $w^{*}$ we have $\psi(w^{*}) = 0$.

Proof. Indeed, at any $w \in Q$ the function $\psi$ is non-negative. If $w^*$ is a solution to (4.18), then for any $v \in Q$ we have

$$
\langle B (v), v - w ^ {*} \rangle \geq \langle B (w ^ {*}), v - w ^ {*} \rangle \geq 0.
$$

Hence, $\psi(w^{*}) = 0$ and $w^{*}\in \operatorname{Arg}\min_{w\in Q}\psi (w)$.

Now, consider some $w^{*} \in Q$ with $\psi(w^{*}) = 0$. Then for any $v \in Q$ we have

$$
\langle B (v), v - w ^ {*} \rangle \geq 0.
$$

Suppose there exists some $v_{1} \in Q$ such that $\langle B(w^{*}), v_{1} - w^{*} \rangle < 0$. Consider the points

$$
v _ {\alpha} = w ^ {*} + \alpha (v _ {1} - w ^ {*}), \quad \alpha \in [ 0, 1 ].
$$

Then

$$
\begin{aligned} 0 &\leq \langle B (v _ {\alpha}), v _ {\alpha} - w ^ {*} \rangle = \alpha \langle B (v _ {\alpha}), v _ {1} - w ^ {*} \rangle \\ &= \alpha \langle B (w ^ {*}), v _ {1} - w ^ {*} \rangle + \alpha^ {2} \langle B \cdot (v _ {1} - w ^ {*}), v _ {1} - w ^ {*} \rangle . \\ \end{aligned}
$$

Hence, for $\alpha$ small enough we get a contradiction.

Clearly, there are two possibilities for representing the problem (4.18), (4.19) in the form (2.1), (2.2).

1. Primal form. We take $E_1 = E_2 = E$, $Q_1 = Q_2 = Q$, $d_1(x) = d_2(x) = d(x)$, $A = B$ and

$$
\hat {f} (x) = \langle b, x \rangle_ {1}, \quad \hat {\phi} (u) = \langle b, u \rangle_ {1} + \langle B u, u \rangle_ {1}.
$$

Note that the quadratic function $\hat{\phi}(u)$ is convex. For computation of the function $f_{\mu}(x)$ we need to solve the following problem:

$$
\max _ {u} \{\langle B x, u \rangle_ {1} - \mu d (u) - \langle b, u \rangle_ {1} + \langle B u, u \rangle_ {1}: u \in Q \}. \tag {4.20}
$$

Since in our case M = 0, from Theorem 3 we get the following estimate for the complexity of problem (4.18):

$$
\frac {4 D _ {1} \| B \| _ {1 , 2}}{\sigma_ {1} \epsilon}. \tag {4.21}
$$

However, note that, because of the presence of the non-trivial quadratic function in (4.20), this computation can be quite complicated. We can avoid that in the dual variant of the problem.

2. Dual form. Consider the dual variant of the problem (4.19):

$$
\min _ {w \in Q} \max _ {v \in Q} \langle B (v), w - v \rangle = \max _ {v \in Q} \min _ {w \in Q} \langle B (v), w - v \rangle = - \min _ {v \in Q} \max _ {w \in Q} \langle B (v), v - w \rangle .
$$

Thus, we can take $E_{1} = E_{2} = E$, $Q_{1} = Q_{2} = Q$, $d_{1}(x) = d_{2}(x) = d(x)$, $A = B$ and

$$
\hat {f} (x) = \langle b, x \rangle_ {1} + \langle B x, x \rangle_ {1}, \quad \hat {\phi} (u) = \langle b, u \rangle_ {1}.
$$

Now the computation of function $f_{\mu}(x)$ becomes much simpler:

$$
f _ {\mu} (x) = \max _ {u} \{\langle B x, u \rangle_ {1} - \mu d (u) - \langle b, u \rangle_ {1}: u \in Q \}.
$$

It is interesting that we pay quite a moderate cost. Indeed, now $M$ becomes equal to $\| B \|_{1,2}$. Hence, the complexity estimate (4.21) increases up to the following level:

$$
\frac {4 D _ {1} \| B \| _ {1 , 2}}{\sigma_ {1} \epsilon} + \sqrt {\frac {D _ {1} \| B \| _ {1 , 2}}{\sigma_ {1} \epsilon}}.
$$

Note that in an important particular case of skew-symmetry of operator B, that is $B + B^{*} = 0$, the primal and dual variant have similar complexity.

# 4.4. Piece-wise linear optimization

1. Maximum of absolute values. Consider the following problem:

$$
\min _ {x} \left\{f (x) = \max _ {1 \leq j \leq m} | \langle a _ {j}, x \rangle_ {1} - b ^ {(j)} |: x \in Q _ {1} \right\}. \tag {4.22}
$$

For simplicity, let us choose

$$
\| x \| _ {1} = \left[ \sum_ {i = 1} ^ {n} (x ^ {(i)}) ^ {2} \right] ^ {1 / 2}, \quad d _ {1} (x) = \frac {1}{2} \| x \| ^ {2}.
$$

Denote by $A$ the matrix with rows $a_{j}, j = 1, \dots, m$. It is convenient to choose

$$
E _ {2} = R ^ {2 m}, \quad \| u \| _ {2} = \sum_ {j = 1} ^ {2 m} | u ^ {(j)} |, \quad d _ {2} (u) = \ln (2 m) + \sum_ {j = 1} ^ {2 m} u ^ {(j)} \ln u ^ {(j)}.
$$

Then

$$
f (x) = \max _ {u} \{\langle \hat {A} x, u \rangle_ {2} - \langle \hat {b}, u \rangle_ {2}: u \in \Delta_ {2 m} \},
$$

where $\hat{A} = \binom{A}{-A}$ and $\hat{b} = \binom{b}{-b}$. Thus, $\sigma_1 = \sigma_2 = 1$, $D_2 = \ln(2m)$, and

$$
D _ {1} = \frac {1}{2} \bar {r} ^ {2}, \quad \bar {r} = \max _ {x} \{\| x \| _ {1}: x \in Q _ {1} \}.
$$

It remains to compute the norm of the operator $\hat{A}$ :

$$
\begin{aligned} \| \hat {A} \| _ {1, 2} &= \max _ {x, u} \{\langle \hat {A} x, u \rangle_ {2}: \| x \| _ {1} = 1, \| u \| _ {2} = 1 \} \\ &= \max _ {x} \{\max _ {1 \leq j \leq m} | \langle a _ {j}, x \rangle_ {1} |: \| x \| _ {1} = 1 \} = \max _ {1 \leq j \leq m} \| a _ {j} \| _ {1} ^ {*} \\ \end{aligned}
$$

Putting all computed values in the estimate (4.4), we see that the problem (4.22) can be solved in

$$
2 \sqrt {2} \bar {r} \max _ {1 \leq j \leq m} \| a _ {j} \| _ {1} ^ {*} \sqrt {\ln (2 m)} \cdot \frac {1}{\epsilon}
$$

iterations of the scheme (3.11). The standard subgradient schemes in this situation can count only on an

$$
O \left(\left[ \bar {r} \max _ {1 \leq j \leq m} \| a _ {j} \| _ {1} ^ {*} \cdot \frac {1}{\epsilon} \right] ^ {2}\right)
$$

upper bound for the number of iterations.

Finally, the smooth version of the objective function in (4.22) looks as follows:

$$
\bar {f} _ {\mu} (x) = \mu \ln \left(\frac {1}{m} \sum_ {j = 1} ^ {m} \xi \left(\frac {1}{\mu} [ \langle a _ {j}, x \rangle + b ^ {(j)} ]\right)\right)
$$

with $\xi (\tau) = \frac{1}{2}[e^{\tau} + e^{-\tau}]$.

2. Sum of absolute values. Consider now the problem

$$
\min _ {x} \left\{f (x) = \sum_ {j = 1} ^ {m} | \langle a _ {j}, x \rangle_ {1} - b ^ {(j)} |: x \in Q _ {1} \right\}. \tag {4.23}
$$

The simplest representation of the function $f(x)$ looks as follows. Denote by $A$ the matrix with the rows $a_{j}$. Let us choose

$$
E _ {2} = R ^ {m}, \quad Q _ {2} = \{u \in R ^ {m}: | u ^ {(j)} | \leq 1, j = 1, \dots , m \},
$$

$$
d _ {2} (u) = \frac {1}{2} \| u \| _ {2} ^ {2} = \frac {1}{2} \sum_ {j = 1} ^ {m} \| a _ {j} \| _ {1} ^ {*} \cdot (u ^ {(j)}) ^ {2}.
$$

Then the smooth version of the objective function looks as follows:

$$
f _ {\mu} (x) = \max _ {u} \{\langle A x - b, u \rangle_ {2} - \mu d _ {2} (u): u \in Q _ {2} \} = \sum_ {j = 1} ^ {m} \| a _ {j} \| _ {1} ^ {*} \cdot \psi_ {\mu} \left(\frac {| \langle a _ {j} , x \rangle_ {1} - b ^ {(j)} |}{\| a _ {j} \| _ {1} ^ {*}}\right),
$$

where the function $\psi_{\mu}(\tau)$ is defined by (4.17). Note that

$$
\begin{aligned} \| A \| _ {1, 2} &= \max _ {x, u} \left\{\sum_ {j = 1} ^ {m} u ^ {(j)} \langle a _ {j}, x \rangle_ {1}: \| x \| _ {1} \leq 1, \| u \| _ {2} \leq 1 \right\} \\ &\leq \max _ {u} \left\{\sum_ {j = 1} ^ {m} \| a _ {j} \| _ {1} ^ {*} \cdot | u ^ {(j)} |: \sum_ {j = 1} ^ {m} \| a _ {j} \| _ {1} ^ {*} \cdot (u ^ {(j)}) ^ {2} \leq 1 \right\} \\ &= D ^ {1 / 2} \equiv \left[ \sum_ {j = 1} ^ {m} \| a _ {j} \| _ {1} ^ {*} \right] ^ {1 / 2}. \\ \end{aligned}
$$

On the other hand, $D_{2} = \frac{1}{2}D$ and $\sigma_{2} = 1$. Therefore from Theorem 3 we get the following complexity bound:

$$
\frac {2}{\epsilon} \cdot \sqrt {\frac {2 D _ {1}}{\sigma_ {1}}} \cdot \sum_ {j = 1} ^ {m} \| a _ {j} \| _ {1} ^ {*}.
$$

# 5. Implementation issues

# 5.1. Computational complexity

Let us discuss the computational complexity of the method (3.11) as applied to the function $\tilde{f}_{\mu}(x)$. The main computations are performed at the Steps 1-3 of the algorithm.

Step 1. Call of the oracle. At this step we need to compute the solution of the following maximization problem:

$$
\max _ {u} \{\langle A x, u \rangle_ {2} - \hat {\phi} (u) - \mu d _ {2} (u): u \in Q _ {2} \}.
$$

Note that from the origin of this problem we know, that this computation for $\mu = 0$ can be done in a closed form. Thus, we can expect that with properly chosen prox-function this computation is not too difficult for $\mu > 0$ also. In Section 4 we have seen three examples which confirm this belief.

Step 3. Computation of $z_{k}$. This computation consists in solving the following problem:

$$
\min _ {x} \{d _ {1} (x) + \langle s, x \rangle_ {1}: x \in Q _ {1} \}
$$

for some fixed $s \in E_1^*$. If the set $Q_1$ and the prox-function $d_1(x)$ are simple enough, this computation can be done in a closed form (see Section 4). For some sets we need to solve an auxiliary equation with one variable. The above problem arises also in the mirror descent scheme. A discussion of different possibilities can be found in [1].

Step 2. Computation of $T_{Q}(x)$. Again, the complexity of this step depends on the complexity of the set $Q_{1}$ and the norm $\| \cdot \|_1$. In the literature such a computation is usually implemented with a Euclidean norm. Therefore let us discuss the general case in more detail.

Sometimes the following statement helps.

Lemma 6. For any $g \in E^*$ and $h \in E$ we have

$$
\langle g, h \rangle_ {1} + \frac {1}{2} L \| h \| ^ {2} = \max _ {s} \left\{\langle s, h \rangle_ {1} - \frac {1}{2} L (\| s - g \| ^ {*}) ^ {2}: s \in E ^ {*} \right\}.
$$

Proof. Indeed,

$$
\begin{aligned} \langle g, h \rangle_ {1} + \frac {1}{2} L \| h \| ^ {2} &= \max _ {r \geq 0} \{\langle g, h \rangle_ {1} + r \| h \| _ {1} - \frac {1}{2 L} r ^ {2} \} \\ &= \max _ {r, s} \{\langle g, h \rangle_ {1} + \langle r s, h \rangle_ {1} - \frac {1}{2 L} r ^ {2}: r \geq 0, \| s \| ^ {*} = 1 \} \\ &= \max _ {s} \{\langle g + s, h \rangle_ {1} - \frac {1}{2 L} (\| s \| ^ {*}) ^ {2}: s \in E ^ {*} \} \\ &= \max _ {s} \left\{\langle s, h \rangle_ {1} - \frac {1}{2 L} (\| s - g \| ^ {*}) ^ {2}: s \in E ^ {*} \right\}. \\ \end{aligned}
$$

□

Let us check what is the complexity of computing $T_{Q}(x)$ in the situation discussed in Section 4.1. We need to find a solution to the problem

$$
\text {Find} \psi^ {*} = \min _ {x} \{\langle \bar {g}, x - \bar {x} \rangle + \frac {1}{2} L \| x - \bar {x} \| ^ {2}: x \in \Delta_ {n} \}, \tag {5.1}
$$

where $\| x\| = \sum_{i=1}^{n}|x^{(i)}|$ and $\bar{x}\in \Delta_n$. Therefore, without loss of generality we can assume that

$$
\min _ {1 \leq i \leq n} \bar {g} ^ {(i)} = 0. \tag {5.2}
$$

Using Lemma 6, we can rewrite the above problem as follows:

$$
\begin{aligned} \psi^ {*} &= \min _ {x \in \Delta_ {n}} \max _ {s} \left\{\langle s, x - \bar {x} \rangle - \frac {1}{2 L} (\| s - \bar {g} \| ^ {*}) ^ {2} \right\} \\ &= \min _ {x \geq 0} \max _ {s, \lambda} \left\{\langle s, x - \bar {x} \rangle - \frac {1}{2 L} (\| s - \bar {g} \| ^ {*}) ^ {2} + \lambda (1 - \langle e _ {n}, x \rangle) \right\} \\ &= \max _ {s, \lambda} \left\{- \langle s, \bar {x} \rangle - \frac {1}{2 L} (\| s - \bar {g} \| ^ {*}) ^ {2} + \lambda): s \geq \lambda e _ {n} \right\}. \\ \end{aligned}
$$

Note that in our case $\| s\|^{*} = \max_{1\leq i\leq n}|s^{(i)}|$. Therefore

$$
\left. - \psi^ {*} = \min _ {s, \lambda , \tau} \left\{\langle s, \bar {x} \rangle + \frac {\tau^ {2}}{2 L} - \lambda : s ^ {(i)} \geq \lambda , | s ^ {(i)} - \bar {g} ^ {(i)} | \leq \tau , i = 1, \dots , n \right\}. \right. \tag {5.3}
$$

In the latter problem we can easily find the optimal values of $s^{(i)}$ :

$$
s _ {*} ^ {(i)} = \max \{\lambda , \bar {g} ^ {(i)} - \tau \}, \quad i = 1, \dots , n.
$$

Moreover, the feasible set of this problem is non-empty if and only if

$$
\lambda \leq \bar {g} ^ {(i)} + \tau , \quad i = 1, \dots , n.
$$

In view of (5.2), this means $\lambda \leq \tau$. Thus,

$$
\begin{aligned} - \psi^ {*} &= \min _ {\tau \geq \lambda} \left\{\sum_ {i = 1} ^ {n} \bar {x} ^ {(i)} \max \{\lambda , \bar {g} ^ {(i)} - \tau \} + \frac {\tau^ {2}}{2 L} - \lambda \right\} \\ &= \min _ {\tau \geq \lambda} \left\{\sum_ {i = 1} ^ {n} \bar {x} ^ {(i)} (\bar {g} ^ {(i)} - \tau - \lambda) _ {+} + \frac {\tau^ {2}}{2 L} \right\}, \\ \end{aligned}
$$

where $(a)_+ = \max \{a, 0\}$. Since the objective function of the latter problem is decreasing in $\lambda$, we conclude that $\lambda^* = \tau$.

Finally, we come to the following representation:

$$
- \psi^ {*} = \min _ {\tau \geq 0} \left\{\sum_ {i = 1} ^ {n} \bar {x} ^ {(i)} (\bar {g} ^ {(i)} - 2 \tau) _ {+} + \frac {\tau^ {2}}{2 L} \right\}.
$$

Clearly, its solution can be found by ordering the components of the vector $\bar{g}^{(i)}$ and checking the derivative of the objective function at the points

$$
\tau_ {i} = \frac {1}{2} \bar {g} ^ {(i)}, \quad i = 1, \dots , n.
$$

The total complexity of this computation is of the order $O(n \ln n)$. We leave the reconstruction of primal solution $x^{*}$ of the problem (5.1) as an exercise for the reader.

# 5.2. Computational stability

Our approach is based on smoothing of non-differentiable functions. In accordance with (4.8) the value of the smoothness parameter $\mu$ must be of the order of $\epsilon$. This may cause some numerical troubles in computation of function $\tilde{f}_{\mu}(x)$ and its gradient. Among the examples of Section 4, only a smooth variant of the objective function in Section 4.2 does not involve dangerous operations; all others need a careful implementation.

In both Section 4.1 and Section 4.4 we need a stable technique for computation of the values and the derivatives of the function

$$
\eta (u) = \mu \ln \left(\sum_ {j = 1} ^ {m} e ^ {u ^ {(j)} / \mu}\right) \tag {5.4}
$$

with very small values of the parameter $\mu$. This can be done in the following way. Denote

$$
\bar {u} = \max _ {1 \leq j \leq m} u ^ {(j)}, \quad v ^ {(j)} = u ^ {(j)} - \bar {u}, j = 1, \dots , m.
$$

Then

$$
\eta (u) = \bar {u} + \eta (v)
$$

Note that all components of the vector $v$ are non-negative and one of them is zero. Therefore the value $\eta(v)$ can be computed with a small numerical error. The same technique can be used for computing the gradient of this function since $\nabla \eta(u) = \nabla \eta(v)$.

The computations presented in Section 6 confirm that the proposed smoothing technique works even for a quite high accuracy.

# 5.3. Modified method

As we have seen, at each iteration of the method (3.11) it is necessary to solve two auxiliary minimization problems of two different types. It appears that quite often the computation of the point $y_{k}$ is more complicated then that of $z_{k}$. Let us show how to modify the scheme (3.11) in order to have both auxiliary problems written in terms of the prox-function $d(x)$.

For simplicity assume that $d(x)$ is differentiable. Denote by

$$
\xi (z, x) = d (x) - d (z) - \langle \nabla d (z), x - z \rangle , \quad z, x \in Q,
$$

the Bregman distance between $z$ and $x$. Clearly,

$$
\xi (z, x) \geq \frac {1}{2} \sigma \| x - z \| ^ {2}.
$$

Define the following mapping:

$$
V _ {Q} (z, g) = \arg \min _ {x} \{\langle g, x - z \rangle + \xi (z, x): x \in Q \}.
$$

In what follows we use the notation of Section 3.

Lemma 7. Let sequence $\{\alpha_k\}_{k=0}^{\infty}$ satisfies condition (3.6). Suppose that condition $(\mathcal{R}_k)$ holds for some $k \geq 0$. Let us choose $\gamma_k = \frac{\sigma}{L} \alpha_{k+1}$. Define

$$
x _ {k + 1} = \tau_ {k} z _ {k} + (1 - \tau_ {k}) y _ {k},
$$

$$
\hat {x} _ {k + 1} = V _ {Q} (z _ {k}, \gamma_ {k} \nabla f (x _ {k + 1})),
$$

$$
y _ {k + 1} = \tau_ {k} \hat {x} _ {k + 1} + (1 - \tau_ {k}) y _ {k}. \tag {5.5}
$$

Then the relation $(\mathcal{R}_{k + 1})$ holds.

Proof. Denote $l_{k}(x) \equiv \beta_{k} + \langle l_{k}, x - z_{k} \rangle = \sum_{i=0}^{k} \alpha_{i}[f(x_{i}) + \langle \nabla f(x_{i}), x - x_{i} \rangle]$. Then

$$
\langle \frac {L}{\sigma} d' (z _ {k}) + l _ {k}, x - z _ {k} \rangle \geq 0 \quad \forall x \in Q.
$$

Hence, since $\psi_{k} = \frac{L}{\sigma} d(z_{k}) + \beta_{k}$, in view of inequality (3.8) we have the following:

$$
\begin{array}{l} \frac {L}{\sigma} d (x) + l _ {k} (x) + \alpha_ {k + 1} \langle \nabla f (x _ {k + 1}), x - x _ {k + 1} \rangle \\ = \frac {L}{\sigma} \xi (z _ {k}, x) + \frac {L}{\sigma} (d (z _ {k}) + \langle d' (z _ {k}), x - z _ {k} \rangle) \\ + \beta_ {k} + \langle l _ {k}, x - z _ {k} \rangle + \alpha_ {k + 1} \langle \nabla f (x _ {k + 1}), x - x _ {k + 1} \rangle \\ \geq \frac {L}{\sigma} \xi (z _ {k}, x) + \psi_ {k} + \alpha_ {k + 1} \langle \nabla f (x _ {k + 1}), x - x _ {k + 1} \rangle \\ \geq \frac {L}{\sigma} \xi (z _ {k}, x) + A _ {k + 1} f (x _ {k + 1}) + \alpha_ {k + 1} \lan + 1} \langle \nabla f (x _ {k + 1}), x - z _ {k} \rangle . \\ \end{array}
$$

Thus, using (3.6), we get the following

$$
\begin{array}{l} \psi_ {k + 1} \geq \min _ {x} \left\{\frac {L}{\sigma} \xi \left(z _ {k}, x\right) + A _ {k + 1} f \left(x _ {k + 1}\right) + \alpha_ {k + 1} \langle \nabla f \left(x _ {k + 1}\right), x - z _ {k} \rangle : x \in Q \right\} \\ = \frac {L}{\sigma} \xi (z _ {k}, \hat {x} _ {k + 1}) + A _ {k + 1} f (x _ {k + 1}) + \alpha_ {k + 1} \langle \nabla f (x _ {k + 1}), \hat {x} _ {k + 1} - z _ {k} \rangle \\ \geq \frac {1}{2} L \| \hat {x} _ {k + 1} - z _ {k} \| ^ {2} + A _ {k + 1} f (x _ {k + 1}) + \alpha_ {k + 1} \langle \nabla f (x _ {k + 1}), \hat {x} _ {k + 1} - z _ {k} \rangle \\ \geq A _ {k + 1} \left(\frac {1}{2} L \tau_ {k} ^ {2} \| \hat {x} _ {k + 1} - z _ {k} \| ^ {2} + f (x _ {k + 1}) + \tau_ {k} \langle \nabla f (x _ {k + 1}), \hat {x} _ {k + 1} - z _ {k} \rangle\right). \\ \end{array}
$$

It remains to use relation $y_{k+1}-x_{k+1}=\tau_{k}(\hat{x}_{k+1}-z_{k})$.

$\square$

Clearly, we can take

$$
y _ {0} = z _ {0} = \arg \min _ {x} \left\{\frac {L}{\sigma} d (x) + \alpha_ {0} [ f (x _ {0}) + \langle f' (x _ {0}), x - x _ {0} \rangle ]: x \in Q \right\}
$$

for any $\alpha_{0}\in(0,1]$. In particular, we can use the sequence suggested in Lemma 2. In this case we come to the following algorithmic scheme.

1. Choose $y_0 = \arg \min_x \left\{ \frac{L}{\sigma} d(x) + \frac{1}{2} [f(x_0) + \langle f'(x_0), x - x_0 \rangle] : x \in Q \right\}$.

2. For $k \geq 0$ iterate:

a) Find $z_k = \arg \min_x \left\{ \frac{L}{\sigma} d(x) + \sum_{i=0}^{k} \frac{i+1}{2} [f(x_i) + \langle \nabla f(x_i), x - x_i \rangle] : x \in Q \right\}$.

b) Set $\tau_{k} = \frac{2}{k + 3}$ and $x_{k + 1} = \tau_kz_k + (1 - \tau_k)y_k$.

c) Find $\hat{x}_{k + 1} = V_Q(z_k,\frac{\sigma}{L}\frac{k + 2}{2}\nabla f(x_{k + 1}))$ .

d) Set $y_{k+1} = \tau_k \hat{x}_{k+1} + (1 - \tau_k)y_k$. (5.6)

Of course, for this method the statement of Theorem 2 holds. As an example, let us present the form of the mapping $V_{Q}(z, g)$ for entropy distance:

$$
V _ {Q} ^ {(i)} (z, g) = z ^ {(i)} e ^ {- g ^ {(i)}} \cdot \left[ \sum_ {j = 1} ^ {n} z ^ {(j)} e ^ {- g ^ {(j)}} \right] ^ {- 1}, \quad i = 1, \dots , n. \tag {5.7}
$$

Clearly, this computation looks more attractive as compared with the strategy discussed in Section 5.1.

# 6. Preliminary computational results

We conclude this paper with the results of computational experiments on a random set of matrix game problems

$$
\min _ {x \in \Delta_ {n}} \max _ {u \in \Delta_ {m}} \langle A x, u \rangle_ {2}.
$$

The matrix $A$ is generated randomly. Each of its entries is uniformly distributed in the interval $[-1, 1]$.

The goal of this numerical study is twofold. Firstly, we want to be sure that the technique discussed in this paper is stable enough to be implemented on a computer with floating point arithmetic. Secondly, it is interesting to demonstrate that the complexity of finding an $\epsilon$-solution of the above problem indeed grows proportionally to $\frac{1}{\epsilon}$ with logarithmic factors dependent on n and m.

In order to achieve these goals we implemented the scheme (3.11) exactly as it is presented in the paper. We chose the parameters of the method in accordance with the recommendation (4.8). Note that for small $\epsilon$ these values become quite big. For example, if we take

$$
\| A \| _ {1, 2} = 1, \quad n = 10 ^ {4}, \quad m = 10 ^ {3}, \quad \epsilon = 10 ^ {- 3},
$$

then the values of parameters of the method (3.11) are as follows:

$$
\mu = 0. 72 \cdot 1 0 ^ {- 4}, \quad L _ {\mu} = 2 3 8 5 8. 5 4, \quad N = 3 1 9 0 6.
$$

Thus, it was not evident that the method with such parameters could be numerically stable.

We present three sets of results. They correspond to different values of accuracy $\epsilon$, namely to $10^{-2}$, $10^{-3}$ and $10^{-4}$. For the last value of $\epsilon$ we skip the problems of highest dimension since the general picture becomes already clear. At each step of the method we compute two matrix-vector products with matrix A. In order to check the stopping criterion, we compute the values of exact primal and dual functions at the current approximations $\hat{x}$ and $\hat{u}$ and check if

$$
f (\hat {x}) - \phi (\hat {u}) \leq \epsilon .
$$

This test is performed periodically, after one hundred (or one thousand) iterations. So, it does not increase significantly the computational time. For our computations we used a personal computer with processor Pentium 4 (2.6GHz) and frequency of RAM 1GHz. In the tables below for each problem instance we give the number of iterations, computational time in seconds and the percentage of the actual number of iterations with respect to the predicted complexity N.

Looking at all three tables, we can see that the complexity of the problem indeed grows linearly with respect to $\frac{1}{\epsilon}$. Moreover, the prediction of the necessary number of iterations is very accurate. The computational time, especially for the big problems, looks quite important. However, that is due to the fact that the matrix A is dense. In real-life problems we never meet big instances with such a level of density.

It seems that Tables 1 and 2 present quite encouraging results. This range of accuracy is already very high for the subgradient schemes with $O(\frac{1}{\epsilon^{2}})$ complexity estimates. Of course, we can solve our problem by a cutting plane scheme, which has a linear rate of convergence. However, usually such a method decreases the gap by a constant factor in n iterations. In this aspect the results shown in the last column of Table 2 are very promising: we get three digits of accuracy after n or 2n iterations. At the same time, the complexity of each step in the cutting plane schemes is at least $O(\frac{1}{3}n^{3})$. Therefore, even if we implement them in the smallest dimension (m), the arithmetical complexity of the computation shown in the most right-down corner of Table 3 would be equivalent to $180 \cdot 3 \cdot 2 = 1080$ iterations (since there n = 10m).

The level of accuracy in Table 3 is unreachable for the standard subgradient schemes. It is quite high for cutting plane schemes also. Again, the arithmetical complexity of the process presented in the cell (3,3) of this table is equivalent to $116 \cdot 3 \cdot 2 = 696$ iterations

Table 1. Computational results for $\epsilon = 0.01$.

<table><tr><td>m\n</td><td>100</td><td>300</td><td>1000</td><td>3000</td><td>10000</td></tr><tr><td>100</td><td>808 0&quot;,44%</td><td>1011 0&quot;,49%</td><td>1112 3&quot;,49%</td><td>1314 12&quot;,54%</td><td>1415 44&quot;,54%</td></tr><tr><td>300</td><td>910 0&quot;,44%</td><td>1112 2&quot;,49%</td><td>1415 10&quot;,56%</td><td>1617 35&quot;,60%</td><td>1819 135&quot;,63%</td></tr><tr><td>1000</td><td>1112 2&quot;,49%</td><td>1213 8&quot;,48%</td><td>1415 32&quot;,51%</td><td>1718 115&quot;,58%</td><td>2020 451&quot;,63%</td></tr></table>

Table 2. Computational results for $\epsilon = 0.001$.

<table><tr><td>m\n</td><td>100</td><td>300</td><td>1000</td><td>3000</td><td>10000</td></tr><tr><td>100</td><td>6970 2&quot;,38%</td><td>8586 8&quot;,42%</td><td>9394 29&quot;,42%</td><td>10000 91&quot;,41%</td><td>10908 349&quot;,42%</td></tr><tr><td>300</td><td>7778 8&quot;,38%</td><td>10101 27&quot;,44%</td><td>12424 97&quot;,49%</td><td>14242 313&quot;,53%</td><td>15656 1162&quot;,54%</td></tr><tr><td>1000</td><td>8788 30&quot;,39%</td><td>11010 105&quot;,44%</td><td>13030 339&quot;,47%</td><td>15757 1083&quot;,53%</td><td>18282 4085&quot;,57%</td></tr></table>

Table 3. Computational results for $\epsilon = 0.0001$.

<table><tr><td>m\n</td><td>100</td><td>300</td><td>1000</td><td>3000</td></tr><tr><td>100</td><td>67068 25&quot;,36%</td><td>72073 80&quot;,35%</td><td>74075 287&quot;,33%</td><td>80081 945&quot;,33%</td></tr><tr><td>300</td><td>85086 89&quot;,42%</td><td>92093 243&quot;,40%</td><td>101102 914&quot;,40%</td><td>112113 3302&quot;,41%</td></tr><tr><td>1000</td><td>97098 331&quot;,43%</td><td>100101 760&quot;,40%</td><td>116117 2936&quot;,42%</td><td>139140 11028&quot;,47%</td></tr></table>

of a cutting plane scheme in dimension $n = 1000$. That is indeed not too much for four digits of accuracy.

Acknowledgements. The author would like to thank Laurence Wolsey for useful comments on the text and the anonymous referees for their suggestions.

# References

1. Ben-Tal, A., Nemirovskii, A.: Lectures on Modern Convex Optimization: Analysis, Algorithms, and Engineering Applications. (SIAM, Philadelphia, 2001)  
2. Bertsekas, D.P.: Constrained optimization and Lagrange multiplier methods. (Academic Press, New York, 1982)  
3. Goffin, J.-L.: On the convergence rate of subgradient optimization methods. Mathematical Programming 13, 329–347 (1977)  
4. Hiriart-Urruty, J.-B., Lemarechal, C.: Convex Analysis and Minimization Algorithms. (Springer-Verlag, 1993)  
5. Polyak, B.: On Bertsekas' method for minimization of composite function. In: Bensoussan, A., Lions, J.L. (eds) Inter. Symp. Systems Opt. 1979, Analysis Springer, pp. 179–186  
6. Polyak, R.: Nonlinear rescaling vs. smoothing technique in convex optimization. Mathematical Programming Ser. A 92, 197–235 (2002)  
7. Polyak, B.: Introduction to Optimization. (Optimization Software, Inc., Publications Division, New York, 1987)  
8. Nemirovsky, A., Yudin, D.: Informational Complexity and Efficient Methods for Solution of Convex Extremal Problems. (J. Wiley & Sons, New York, 1983)  
9. Nesterov, Yu.: A method for unconstrained convex minimization problem with the rate of convergence $O(\frac{1}{k^2})$. Doklady AN SSSR (translated as Soviet Math. Docl.) 269, 543-547 (1983)  
10. Nesterov, Yu.: Introductory Lectures on Convex Optimization: Basic course. (Kluwer, Boston, 2003)  
11. Shor, N.: Minimization Methods for Non-Differentiable Functions. (Springer-Verlag, Berlin, 1985)
