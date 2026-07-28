# PROXIMAL POINT ALGORITHM CONTROLLED BY A SLOWLY VANISHING TERM: APPLICATIONS TO HIERARCHICAL MINIMIZATION*

ALEXANDRE CABOT $^{\dagger}$

Abstract. Let $\Phi_{0}: R^{n} \to R \cup \{+\infty\}$ be a closed convex function and $\Phi_{1}: R^{n} \to R$ be a finite convex function that are bounded from below. Our goal is to build an algorithm which first minimizes the map $\Phi_{0}$ and secondly the map $\Phi_{1}$ over the set $S_{0} := argmin\Phi_{0}$. For that purpose, we define the following proximal-type algorithm:

$$
- (x _ {n + 1} - x _ {n}) / \lambda_ {n} \in \partial_ {\eta_ {n}} (\Phi_ {0} + \varepsilon_ {n} \Phi_ {1}) (x _ {n + 1}), \tag {$\mathcal{A$} _ {1}}
$$

where $(\lambda_{n})$ is a positive step sequence, $(\eta_{n})$ is a summable error sequence, and $(\varepsilon_{n})$ is a control sequence tending toward 0; $\partial_{\eta}$ denotes the $\eta$ -approximate subdifferential. When $(\varepsilon_{n})$ is a slow control, i.e., $\sum_{n=0}^{+\infty} = \varepsilon_{n} + \infty$, we prove that, under adequate conditions, the sequence $(x_{n})$ defined by $(\mathcal{A}_{1})$ tends toward an element of $S_{1} := \arg\min_{S_{0}} \Phi_{1}$.

More generally, given finite convex functions $\Phi_2, \ldots, \Phi_N: \mathbb{R}^n \to \mathbb{R}$, let us define the sets $(S_i)_{i \in \{1, \ldots, N\}}$ by the recursive relation $S_i := \operatorname{argmin}_{S_{i-1}} \Phi_i$. We introduce an extension of algorithm $(\mathcal{A}_1)$ to minimize hierarchically each function $\Phi_i$ on the set $S_{i-1}$, for $i \in \{1, \ldots, N\}$.

Key words. steepest descent system, proximal point method, hierarchical optimization, convex minimization, slow control

AMS subject classifications. 37N40, 49M30, 65K10

DOI. 10.1137/S105262340343467X

1. Introduction. Let $\Phi_{1}: R^{n} \to R$ be a smooth convex function that we wish to minimize over the convex set $S_{0}$. A powerful method consists in following the orbits of a discrete or continuous dynamical system, hopefully converging toward some element of $\arg\min_{S_{0}} \Phi_{1}$. It is classical to apply the steepest descent system to the function $\Phi_{1} + \delta_{S_{0}}$ ( $\delta_{S_{0}}$ is the indicator function of $S_{0}$ ), thus leading to

$$
\dot {x} (t) + \nabla \Phi_ {1} (x (t)) \in - N _ {S _ {0}} (x (t)), \qquad t \geq 0,
$$

where $N_{S_{0}}(x(t))$ is the normal cone to $S_{0}$ at the point $x(t)$. It can be shown that this differential inclusion falls into the framework of gradient-projection methods (see Brézis [12]). Antipin [3] has initiated another continuous gradient-projection system, where the constraint $S_{0}$ is integrated through the projection operator $P_{S_{0}}$. In another direction, Cabot [13] has considered in a recent paper the following continuous dynamical system:

$$
\dot {x} (t) + \nabla \Phi_ {0} (x (t)) + \varepsilon (t)   \nabla \Phi_ {1} (x (t)) = 0, \qquad t \geq 0, \tag {SDC}
$$

where $\Phi_0: \mathbb{R}^n \to \mathbb{R}$ is a smooth convex function satisfying $\operatorname{argmin} \Phi_0 = S_0$ and $\varepsilon: \mathbb{R}_+ \to \mathbb{R}_+$ is a control parameter tending to 0 when $t \to +\infty$. In the (SDC) system, the information on the constraint $S_0$ is contained in the function $\Phi_0$. The main difference from the previous methods lies in the fact that we do not have to handle nonsmooth operators, like the normal cone $N_{S_0}$ or the projection $P_{S_0}$. However, the

difficulty comes from the choice of the control parameter $\varepsilon$. If the map $\varepsilon$ tends to 0 too quickly, the potential $\Phi_{1}$ cannot sufficiently influence the trajectory $x(.)$, so that the minimization of $\Phi_{1}$ may not occur. We feel the interest of a “slow control,” and it is shown in [13] that the adequate condition on $\varepsilon$ is $\int_{0}^{+\infty}\varepsilon(t)dt=+\infty$. The notion of slow control has already been pointed out by several authors, essentially for continuous dynamical systems. See, for example, Cominetti [16] and Attouch and Cominetti [5], where the slow control is aimed at stabilizing a continuous gradient-like system toward a peculiar equilibrium. In the same direction, Attouch and Czarnecki [6], Cabot and Czarnecki [15], and Cabot [14] apply the notion of slow control to stabilize second-order-in-time systems.

Coming back to the (SDC) system and keeping in mind numerical applications, it is natural to deal with a discretized version of (SDC). In this paper, we will be especially interested in the following implicit discretization of (SDC):

$$
- (x _ {n + 1} - x _ {n}) / \lambda_ {n} = \nabla (\Phi_ {0} + \varepsilon_ {n} \Phi_ {1}) (x _ {n + 1}), \qquad n \in \mathbb {N},
$$

where $\lambda_{n}$ is the step length at iteration n and $\varepsilon_{n}$ is the value of $\varepsilon(.)$ at time $t_{n} := \sum_{k=0}^{n-1} \lambda_{k}$. If the closed convex functions $\Phi_{0}$ and $\Phi_{1}$ take their values in $R \cup \{+\infty\}$ without regularity assumptions, one can easily adapt the previous algorithm as follows:

$$
- (x _ {n + 1} - x _ {n}) / \lambda_ {n} \in \partial (\Phi_ {0} + \varepsilon_ {n} \Phi_ {1}) (x _ {n + 1}),
$$

where $\partial$ denotes the subdifferential in the sense of convex analysis. Notice that this algorithm falls into the field of proximal point methods proposed in [24, 25] and inspired by [26]. Such methods have been intensively studied over the last few decades, and there is a significant amount of results concerning this type of algorithm, ranging from abstract convergence theorems to applications in nonlinear programming (see, for example, [1, 2, 7, 8, 10, 17, 19, 20, 21, 22, 23, 27, 28, 29, 31]). In the previous algorithm, the iterate $x_{n+1}$ is uniquely determined by $x_{n+1} = J_{\lambda_n}^{A_n}(x_n)$, where $A_n$ is the maximal monotone operator $\partial(\Phi_0 + \varepsilon_n \Phi_1)$ and $J_\lambda^A := (I + \lambda A)^{-1} : \mathbb{R}^n \to \mathbb{R}^n$ is the resolvent of A of parameter $\lambda$. In order to deal with numerical applications, it is convenient to authorize at each iteration n an error $\eta_n$ in the evaluation of the subdifferential. More precisely, denoting by $\partial_\eta$ the $\eta$ -approximate subdifferential, we are led to the following algorithm:

$$
- (x _ {n + 1} - x _ {n}) / \lambda_ {n} \in \partial_ {\eta_ {n}} (\Phi_ {0} + \varepsilon_ {n} \Phi_ {1}) (x _ {n + 1}). \tag {$\mathcal{A$} _ {1}}
$$

The sequence $(\eta_{n})$ of errors is assumed to be summable so as to remain close to the exact subdifferential. We show that, under the slow control criterion, i.e., $\sum_{n=0}^{+\infty} \varepsilon_n = +\infty$, each sequence generated by $(\mathcal{A}_1)$ tends to minimize $\Phi_1$ over $\arg\min \Phi_0$ in a sense that will be made precise throughout the paper.

The next stage consists in building an algorithm which is able to minimize hierarchically several functions over their successive argmin sets. More precisely, consider finite convex functions $\Phi_{2},\ldots,\Phi_{N}$ (with $N\geq2$ ) and define their successive argmin sets by $S_{0}:=argmin\Phi_{0}$ and $S_{i}:=argmin_{S_{i-1}}\Phi_{i}$ for $i\in\{1,\ldots,N\}$. We introduce in the paper the algorithm $(\mathcal{A}_{N})$, given by

$$
(\mathcal {A} _ {N}) \qquad - (x _ {n + 1} - x _ {n}) / \lambda_ {n} \in \partial_ {\eta_ {n}} \Big (\Phi_ {0} + \varepsilon_ {n} \Phi_ {1} + \varepsilon_ {n} ^ {(2)} \Phi_ {2} + \dots + \varepsilon_ {n} ^ {(N)} \Phi_ {N} \Big) (x _ {n + 1}),
$$

where the choice of the sequences $(\varepsilon_{n}^{(2)}),\ldots,(\varepsilon_{n}^{(N)})$ depends on the functions $\Phi_{0},\ldots,\Phi_{N}$. We prove that, under adequate conditions, the algorithm $(\mathcal{A}_{N})$ tends to minimize

hierarchically each function $\Phi_{i}$ on the set $S_{i-1}$, for $i \in \{1, \ldots, N\}$. The introduction of the algorithms $(\mathcal{A}_{i})_{i \in \{1, \ldots, N\}}$ seems to be a new and promising tool in hierarchical minimization problems.

The paper is organized as follows. In section 2, we recall general features about proximal algorithms. We also study the case of a fast parametrization $(\varepsilon_{n})$ and we obtain the weak convergence of the algorithm $(\mathcal{A}_{1})$ toward some element of $S_{0}=\arg\min\Phi_{0}$. Section 3 is devoted to the case of a slow control. In the finite-dimensional setting, we prove that the distance of the iterate $x_{n}$ to the set $S_{1}=\arg\min_{S_{0}}\Phi_{1}$ tends toward 0. We give sufficient conditions ensuring that the sequence $(x_{n})$ converges toward some element of $S_{1}$. Finally, in section 4, we generalize the previous results by considering the algorithm $(\mathcal{A}_{N})$, which is shown to minimize hierarchically the respective functions $\Phi_{1},\ldots,\Phi_{N}$ over the respective sets $S_{0},\ldots,S_{N-1}$. For pedagogical reasons, the first paragraph of section 4 starts with the case N=2.

2. General results. Case of a fastly vanishing term. In this section, we consider a Hilbert space $H$ endowed with scalar product and corresponding norm, respectively, denoted by $\langle .,.\rangle$ and $|.|$. Let $\Phi_0:H\to \mathbb{R}\cup \{+\infty \}$ be a closed convex function and $\Phi_1:H\to \mathbb{R}$ a finite convex function that are bounded from below. We are also given nonnegative sequences $(\varepsilon_n)$, $(\lambda_n)$, and $(\eta_n)$. Denoting by $\partial_{\eta}$ the $\eta$ -approximate subdifferential, we consider the following algorithm:

$$
(\mathcal {A} _ {1}) \quad - \frac {x _ {n + 1} - x _ {n}}{\lambda_ {n}} \in \partial_ {\eta_ {n}} (\Phi_ {0} + \varepsilon_ {n} \Phi_ {1}) (x _ {n + 1}).
$$

Setting

$$
\Psi_ {n} := \Phi_ {0} - \inf \Phi_ {0} + \varepsilon_ {n} (\Phi_ {1} - \inf \Phi_ {1}) \geq 0, \tag {2.1}
$$

algorithm $(\mathcal{A}_{1})$ can be rewritten as the following diagonal proximal iteration:

$$
- \frac {x _ {n + 1} - x _ {n}}{\lambda_ {n}} \in \partial_ {\eta_ {n}} \Psi_ {n} (x _ {n + 1}), \tag {DProx}
$$

where the sequence $(\Psi_{n})$ converges pointwise to $\Phi_{0}$ as soon as $\lim_{n\to+\infty}\varepsilon_{n}=0$. In the context of convex programming, this idea of coupling the proximal method with an approximate scheme has been used by Auslender, Crouzeix, and Fedit [8], Kaplan [19], Mouallif [27], and Mouallif and Tossings [28]. Later, a more systematic study of diagonal proximal methods was developed by Alart and Lemaire [1], Bahraoui and Lemaire [10], Cominetti [17], and Lemaire [20, 21, 22, 23]. In the literature, we may find other inexact diagonal processes, such as

$$
(\mathrm{DProx} ^ {*}) \quad x _ {n + 1} \in \eta_ {n} \text {-argmin} \left(\frac {| \cdot - x _ {n} | ^ {2}}{2 \lambda_ {n}} + \Psi_ {n}\right),
$$

where $\eta$ -argmin denotes the $\eta$ -approximate set of optimal minimizers. The approximate algorithm (DProx*) has been introduced by Auslender [7] in the case $\Psi_{n} \equiv \Psi$ and the relations with (DProx) are explained in [7, Proof of Theorem 1.1].

Throughout this paper, we will assume the following hypotheses on the sequences $(\varepsilon_{n}), (\lambda_{n}), (\eta_{n})$ :

$(\mathcal{H}_{\varepsilon})$ The sequence $(\varepsilon_{n})$ is nonincreasing and $\lim_{n\to +\infty}\varepsilon_n = 0$.  
$(\mathcal{H}_{\lambda})$ There exist $\underline{\lambda} >0$ and $\overline{\lambda} >0$ such that $\underline{\lambda}\leq \lambda_n\leq \overline{\lambda}$ for every $n\in \mathbb{N}$.  
$(\mathcal{H}_{\eta})$ The sequence $(\eta_{n})$ is summable, i.e., $\sum_{n=0}^{+\infty}\eta_n < +\infty$.

The summability condition $(\mathcal{H}_{\eta})$ means that the authorized error $\eta_{n}$ in the computation of the subdifferential is small enough so as to remain close to the exact subdifferential. The following proposition states the main general features about the algorithm $(\mathcal{A}_{1})$.

PROPOSITION 2.1. Let $H$ be a Hilbert space endowed with the norm $|.|$, $\Phi_0: H \to \mathbb{R} \cup \{+\infty\}$ a closed convex function, and $\Phi_1: H \to \mathbb{R}$ a finite convex function. Assume that the functions $\Phi_0$ and $\Phi_1$ are bounded from below. We are given nonnegative sequences $(\varepsilon_n)$, $(\lambda_n)$, $(\eta_n)$ satisfying, respectively, $(\mathcal{H}_\varepsilon)$, $(\mathcal{H}_\lambda)$, $(\mathcal{H}_\eta)$. Any sequence $(x_n)$ generated by the algorithm $(\mathcal{A}_1)$ satisfies (i) $\lim_{n \to +\infty} \Phi_0(x_n) = \inf \Phi_0$. (ii) If the set $\operatorname{argmin} \Phi_0$ is nonempty and if $x_{n_k} \rightharpoonup \bar{x}$ weakly in $H$, then $\bar{x} \in \operatorname{argmin} \Phi_0$.

This result is an immediate consequence of [23, Proposition 3.2] in view of the monotonicity of the sequence $(\Psi_n)$ defined by (2.1). Proposition 2.1 is also closely related to [1, Theorem 3.1] and [21, Corollary 3.1].

Our purpose is now to specify the convergence properties of $(x_{n})$. When $\varepsilon_{n}=0$ for every $n\geq0$, the $(\mathcal{A}_{1})$ algorithm reduces to the standard proximal point method applied to $\Phi_{0}$. The sequence $(x_{n})$ generated by $(\mathcal{A}_{1})$ is then known to weakly converge toward a minimum of $\Phi_{0}$ : the arguments of the proof rely on the Opial lemma [30]. This result can be generalized when the sequence $(\varepsilon_{n})$ tends to zero fast enough. The key condition is $\sum_{n=0}^{+\infty}\varepsilon_{n}<+\infty$, and any sequence $(\varepsilon_{n})$ satisfying such a criterion will be referred to as a fast control (or sequence). Let us now state the following proposition.

PROPOSITION 2.2. Under the hypotheses of Proposition 2.1, assume moreover that $\arg\min \Phi_0 \neq \emptyset$ and that $\sum_{n=0}^{+\infty} \varepsilon_n < +\infty$. Then any sequence $(x_n)$ defined by the algorithm $(\mathcal{A}_1)$ weakly converges toward some $x_\infty \in \arg\min \Phi_0$.

We will let the reader check that this result is implied by [23, Corollary 4.2]. Weak convergence of the sequences generated by (DProx) or (DProx*) has been established with varying degrees of generality in [1, 8, 17, 23, 27, 28]. A common characteristic of these results is that the approximate functions $\Psi_{n}$ are expected to converge to their limit sufficiently fast.

It is also interesting to notice the analogy between the discrete case and the continuous one. In the continuous case, it has been proved in [13] that the trajectories of (SDC) weakly converge toward a minimum of $\Phi_0$ under the condition $\int_0^{+\infty}\varepsilon (t)dt < +\infty$. This result is exactly the continuous version of Proposition 2.2. Conversely, it is shown in [13] that the assumption $\int_0^{+\infty}\varepsilon (t)dt = +\infty$ allows us to rescale the (SDC) system conveniently, then giving rise to the minimization of $\Phi_{1}$ over the set argmin $\Phi_0$. The same phenomenon occurs in the discrete case, as will be shown by Theorem 3.1.

3. Slow control: Minimization of $\Phi_{1}$ over argmin $\Phi_{0}$. From now on, H is a finite-dimensional Hilbert space, i.e., $H = R^{n}$.

3.1. Convergence of the distance to the set $\arg\min_{S_{0}}\Phi_{1}$. When $(\varepsilon_{n})$ is a fast control, Proposition 2.2 shows the convergence of the algorithm, but the limit does not depend explicitly on $\Phi_{1}$. The potential $\Phi_{1}$ plays no crucial role because the sequence $(\varepsilon_{n})$ vanishes too quickly, from which comes the idea of introducing a slow control satisfying $\sum_{n=0}^{+\infty}\varepsilon_{n}=+\infty$. Assuming that $\Phi_{1}=|.|^{2}/2$, the algorithm $(\mathcal{A}_{1})$ combines the proximal point method and the Tikhonov regularization [33]. Convergence under slow parametrization has been proved in this case by Moudafi [29], and the limit equals the element of minimal norm of $S_{0}=arg\min\Phi_{0}$. This result presents interesting similarities with the corresponding results of Attouch and Cominetti [5] and Attouch and Czarnecki [6] in the continuous case. Coming back to the general

case, Cominetti [17] has established the convergence of $(\mathcal{A}_{1})$ under slow parametrization when $\Phi_{0} + \varepsilon\Phi_{1}$ is strongly convex for every $\varepsilon > 0$ (in fact, the results of [17] concern a more general approximation scheme). Our approach here is different and does not rely on the existence of an optimal path $(x(\varepsilon))_{\varepsilon > 0}$. The following theorem states that, under the condition $\sum_{n=0}^{+\infty}\varepsilon_{n} = +\infty$, the algorithm $(\mathcal{A}_{1})$ tends to minimize $\Phi_{1}$ over the set argmin $\Phi_{0}$, without strong convexity assumptions on $\Phi_{0}$ and $\Phi_{1}$.

THEOREM 3.1. Let $\Phi_0: \mathbb{R}^n \to \mathbb{R} \cup \{+\infty\}$ be a closed convex function and $\Phi_1: \mathbb{R}^n \to \mathbb{R}$ be a finite convex function. Assume that the functions $\Phi_0$ and $\Phi_1$ are bounded from below, that the set $S_0 := \arg\min \Phi_0$ is nonempty, and that the set $S_1 := \arg\min_{S_0} \Phi_1$ is nonempty and bounded. We consider a sequence $(\varepsilon_n)$ satisfying $(\mathcal{H}_{\varepsilon})$ and $\sum_{n=0}^{+\infty} \varepsilon_n = +\infty$. We are also given nonnegative sequences $(\lambda_n), (\eta_n)$ verifying, respectively, $(\mathcal{H}_{\lambda})$ and $(\mathcal{H}_{\eta})$. Then any sequence $(x_n)$ generated by the algorithm $(\mathcal{A}_1)$ satisfies:

(i) $\lim_{n\to+\infty}d(x_n,S_1)=0,$

(ii) $\lim_{n\to +\infty}(\Phi_0(x_n),\Phi_1(x_n)) = (\min \Phi_0,\min_{S_0}\Phi_1)$, where $d(.,S_1)$ stands for the distance function to the set $S_{1}$.

Proof. (i) The proof relies on the study of the sequence $(h_n)$ defined by

$$
h _ {n} = \frac {1}{2} d (x _ {n}, S _ {1}) ^ {2}.
$$

Denoting by $P_{S_{1}}$ the projection operator onto the convex set $S_{1}$, we have

$$
\begin{array}{l} h _ {k} = \frac {1}{2} | x _ {k} - P _ {S _ {1}} (x _ {k}) | ^ {2} \\ = \frac {1}{2} | x _ {k} - P _ {S _ {1}} (x _ {k}) - (x _ {k + 1} - P _ {S _ {1}} (x _ {k + 1})) | ^ {2} + \frac {1}{2} | x _ {k + 1} - P _ {S _ {1}} (x _ {k + 1}) | ^ {2} \\ + \langle x _ {k} - P _ {S _ {1}} (x _ {k}) - (x _ {k + 1} - P _ {S _ {1}} (x _ {k + 1})), x _ {k + 1} - P _ {S _ {1}} (x _ {k + 1}) \rangle \\ \geq h _ {k + 1} + \left\langle x _ {k} - x _ {k + 1}, x _ {k + 1} - P _ {S _ {1}} (x _ {k + 1}) \right\rangle \\ + \langle P _ {S _ {1}} (x _ {k + 1}) - P _ {S _ {1}} (x _ {k}), x _ {k + 1} - P _ {S _ {1}} (x _ {k + 1}) \rangle . \\ \end{array}
$$

Since $P_{S_1}(x_k) \in S_1$, we classically have $\langle P_{S_1}(x_{k+1}) - P_{S_1}(x_k), x_{k+1} - P_{S_1}(x_{k+1}) \rangle \geq 0$ and finally

$$
h _ {k + 1} - h _ {k} \leq \langle x _ {k + 1} - x _ {k}, x _ {k + 1} - P _ {S _ {1}} (x _ {k + 1}) \rangle . \tag {3.1}
$$

From the fact that $-(x_{k + 1} - x_k) / \lambda_k\in \partial_{\eta_k}(\Phi_0 + \varepsilon_k\Phi_1)(x_{k + 1})$, we infer

$$
\langle - (x _ {k + 1} - x _ {k}) / \lambda_ {k}, x _ {k + 1} - P _ {S _ {1}} (x _ {k + 1}) \rangle
$$

$$
\geq \Phi_ {0} (x _ {k + 1}) - \min \Phi_ {0} + \varepsilon_ {k} \left(\Phi_ {1} (x _ {k + 1}) - \min _ {S _ {0}} \Phi_ {1}\right) - \eta_ {k}. \tag {3.2}
$$

By combining (3.1) and (3.2), we are led to

$$
h _ {k + 1} - h _ {k} + \lambda_ {k} \left(\Phi_ {0} (x _ {k + 1}) - \min \Phi_ {0} + \varepsilon_ {k} (\Phi_ {1} (x _ {k + 1}) - \min _ {S _ {0}} \Phi_ {1})\right) \leq \overline {{\lambda}}   \eta_ {k}
$$

and therefore

$$
h _ {k + 1} - h _ {k} + \lambda_ {k} \varepsilon_ {k} (\Phi_ {1} (x _ {k + 1}) - \min _ {S _ {0}} \Phi_ {1}) \leq \overline {{\lambda}} \eta_ {k}. \tag {3.3}
$$

We now distinguish the following cases:

(a) There exists $n_0 \in \mathbb{N}$ such that for all $n \geq n_0$, $\Phi_1(x_n) > \min_{S_0} \Phi_1$.  
(b) For all $n_0 \in \mathbb{N}$, there exists $n \geq n_0$, $\Phi_1(x_n) \leq \min_{S_0} \Phi_1$.

Case (a). We assume that there exists $n_0 \in \mathbb{N}$ such that, for every $n \geq n_0$, $\Phi_1(x_n) > \min_{S_0} \Phi_1$. From (3.3), we deduce that, for every $k \geq n_0$, $h_{k+1} - h_k \leq \overline{\lambda} \eta_k$. Therefore, we have $(h_{k+1} - h_k)^+ \leq \overline{\lambda} \eta_k$, which in view of the following lemma implies that

$$
\lim _ {n \to + \infty} h _ {n} \quad \text {exists.} \tag {3.4}
$$

LEMMA 3.2. Let $(h_n)$ be a sequence of nonnegative reals satisfying $\sum_{k=0}^{+\infty}(h_{k+1}-h_k)^{+}<+\infty$, where $[t]^+:= \max\{t,0\}$ denotes the positive part of $t$. Then $\lim_{n\to+\infty}h_n$ exists.

The proof of Lemma 3.2 is elementary and left to the reader. Coming back to the proof of Theorem 3.1, we infer that the sequence $(d(x_{n}, S_{1}))_{n \in \mathbb{N}}$ is bounded, and since $S_{1}$ is bounded, we conclude that $(x_{n})$ is bounded too. The end of the proof consists in showing that this limit equals zero. Let us add inequalities (3.3) from $k = n_{0}$ to n - 1; we find

$$
h _ {n} - h _ {n _ {0}} + \underline {{\lambda}} \sum_ {k = n _ {0}} ^ {n - 1} \varepsilon_ {k} \left(\Phi_ {1} (x _ {k + 1}) - \min _ {S _ {0}} \Phi_ {1}\right) \leq \overline {{\lambda}} \sum_ {k = n _ {0}} ^ {n - 1} \eta_ {k}.
$$

Since $h_n \geq 0$ and $\sum_{k=n_0}^{+\infty} \eta_k < +\infty$, we deduce that

$$
\sum_ {k = n _ {0}} ^ {+ \infty} \varepsilon_ {k} \left(\Phi_ {1} (x _ {k + 1}) - \min _ {S _ {0}} \Phi_ {1}\right) <   + \infty . \tag {3.5}
$$

From (3.5), it is immediate that $\liminf_{n\to +\infty}\Phi_1(x_n) = \min_{S_0}\Phi_1$ (indeed, the assumption $\liminf_{n\to +\infty}\Phi_1(x_n) > \min_{S_0}\Phi_1$ would lead to a contradiction with the fact that $\sum_{k=0}^{+\infty}\varepsilon_k = +\infty$ ). Consider a subsequence of $(x_n)$, still denoted $(x_n)$ such that $\lim_{n\to +\infty}\Phi_1(x_n) = \min_{S_0}\Phi_1$. Since the sequence $(x_n)$ is bounded, we can extract a converging subsequence $(x_{n_k})$ of $(x_n)$ : there exists $\bar{x} \in \mathbb{R}^n$ such that $\lim_{k\to +\infty}x_{n_k} = \bar{x}$. In view of Proposition 2.1(ii), we have $\bar{x} \in \arg\min\Phi_0 = S_0$. The continuity of the finite convex function $\Phi_1$ implies that

$$
\Phi_ {1} (\bar {x}) = \lim _ {k \to + \infty} \Phi_ {1} (x _ {n _ {k}}) = \lim _ {n \to + \infty} \Phi_ {1} (x _ {n}) = \min _ {S _ {0}} \Phi_ {1},
$$

and hence $\bar{x} \in argmin_{S_{0}}\Phi_{1} = S_{1}$. On the other hand, we have

$$
\lim _ {k \to + \infty} h _ {n _ {k}} = \lim _ {k \to + \infty} \frac {1}{2} d (x _ {n _ {k}}, S _ {1}) ^ {2} = \frac {1}{2} d (\bar {x}, S _ {1}) ^ {2} = 0,
$$

which means that 0 is a limit point of $(h_n)$. Since the sequence $(h_n)$ is convergent, we conclude that $\lim_{n\to +\infty}h_n = 0$. (Notice that our arguments are no more valid in infinite-dimensional spaces. The strong convergence of the sequence $(x_{n_k})$ toward $\bar{x}$ would be replaced by the weak convergence. Since the distance function $x\mapsto d(x,S_1)^2$ is lower semicontinuous for the weak topology, we obtain that $\liminf_{k\to +\infty}\frac{1}{2} d(x_{n_k},S_1)^2$ $\geq \frac{1}{2} d(\bar{x},S_1)^2 = 0$, but this inequality is insufficient to conclude.)

Case (b). We assume that for every $n_0 \in \mathbb{N}$, there exists $n \geq n_0$ such that $\Phi_1(x_n) \leq \min_{S_0} \Phi_1$. Let us consider the sequence $(\tau_n)$ defined by

$$
\tau_ {n} = \max \{k \in \mathbb {N}, \quad k \leq n \quad \text {and} \quad \Phi_ {1} (x _ {k}) \leq \min _ {S _ {0}} \Phi_ {1} \}.
$$

From the above assumption, it is immediate that $(\tau_{n})$ is defined for $n$ large enough and that $\lim_{n\to +\infty}\tau_n = +\infty$. Suppose now that $\tau_{n}\leq n - 1$. From the definition of $\tau_{n}$ and formula (3.3), we have

$$
\forall k \in \{\tau_ {n}, n - 1 \}, \quad h _ {k + 1} - h _ {k} \leq \overline {{\lambda}} \eta_ {k}.
$$

By adding these $(n - \tau_{n})$ inequalities, we obtain

$$
h _ {n} - h _ {\tau_ {n}} \leq \overline {{\lambda}} \sum_ {k = \tau_ {n}} ^ {n - 1} \eta_ {k}
$$

and therefore

$$
h _ {n} \leq h _ {\tau_ {n}} + \overline {{\lambda}} \sum_ {k = \tau_ {n}} ^ {+ \infty} \eta_ {k}. \tag {3.6}
$$

Notice that, if $\tau_{n} = n$, then we have $h_{\tau_n} = h_n$ so that relation (3.6) is always true. If we are able to prove that $\lim_{n\to +\infty}h_{\tau_n} = 0$, then inequality (3.6) combined with the fact that $\lim_{n\to +\infty}\sum_{k = \tau_n}^{+\infty}\eta_k = 0$, will immediately imply that $\lim_{n\to +\infty}h_n = 0$.

Let us first prove that the sequence $(h_{\tau_{n}})$ is bounded. From Proposition 2.1(i), there exists $M_{0} \in R$ such that, for every $n \in N$, $\Phi_{0}(x_{n}) \leq M_{0}$, i.e.,

$$
\{x _ {n}, n \in \mathbb {N} \} \subset [ \Phi_ {0} \leq M _ {0} ].
$$

From the definition of $\tau_{n}$, the point $x_{\tau_n}$ belongs to $[\Phi_1 \leq \min_{S_0} \Phi_1]$ so that

$$
x _ {\tau_ {n}} \in [ \Phi_ {0} \leq M _ {0} ] \cap [ \Phi_ {1} \leq \min _ {S _ {0}} \Phi_ {1} ],
$$

as soon as $x_{\tau_n}$ is defined. In view of the following lemma, the set $[\Phi_0 \leq M_0] \cap [\Phi_1 \leq \min_{S_0} \Phi_1]$ is bounded, which implies that the sequence $(h_{\tau_n})$ is bounded.

LEMMA 3.3. Assume that the functions $\Phi_0$ and $\Phi_1$ satisfy the assumptions of Theorem 3.1. Then, for every $(M_0, M_1) \in \mathbb{R}^2$, the set $[\Phi_0 \leq M_0] \cap [\Phi_1 \leq M_1]$ is bounded. The proof of Lemma 3.3 is postponed to the appendix.

Let us now show that $\lim_{n\to +\infty}h_{\tau_n} = 0$. Consider a convergent subsequence of the bounded sequence $(x_{\tau_n})$, still denoted by $(x_{\tau_n})$ : there exists $\bar{x}\in \mathbb{R}^n$ such that $\lim_{n\to +\infty}x_{\tau_n} = \bar{x}$. The set $[\Phi_1\leq \min_{S_0}\Phi_1]$ is closed as a sublevel set of the continuous function $\Phi_1$. From the definition of $\tau_{n}$, we have $x_{\tau_n}\in [\Phi_1\leq \min_{S_0}\Phi_1]$ for every $n\in \mathbb{N}$, thus implying $\bar{x}\in [\Phi_1\leq \min_{S_0}\Phi_1]$. On the other hand, from Proposition 2.1(ii), we have $\bar{x}\in S_0 = \arg \min \Phi_0$. We immediately deduce that $\bar{x}\in S_1 = \arg \min_{S_0}\Phi_1$, which means that every limit point of the sequence $(x_{\tau_n})$ belongs to $S_{1}$. It is then clear that 0 is the unique limit point of the bounded sequence $(d(x_{\tau_n},S_1))$. We easily conclude that $\lim_{n\to +\infty}h_{\tau_n} = \lim_{n\to +\infty}\frac{1}{2} d(x_{\tau_n},S_1)^2 = 0$.

(ii) Since $\lim_{n\to +\infty}\Phi_0(x_n) = \min \Phi_0$ from Proposition 2.1(i), we just have to prove that $\lim_{n\to +\infty}\Phi_1(x_n) = \min_{S_0}\Phi_1$. The sequence $(\Phi_1(x_n))$ is the image of the bounded sequence $(x_n)$ by the continuous function $\Phi_1$, and hence $(\Phi_1(x_n))$ is bounded. Let $(\Phi_1(x_{n_k}))$ be a converging subsequence of $(\Phi_1(x_n))$. Since $(x_{n_k})$ is bounded, there is a subsequence of $(x_{n_k})$, still denoted by $(x_{n_k})$, which converges to $\bar{x} \in \mathbb{R}^n$. From (i), we have $\lim_{k\to +\infty}d(x_{n_k}, S_1) = 0$, and hence $\bar{x} \in S_1$. From the continuity of $\Phi_1$, we deduce that $\lim_{k\to +\infty}\Phi_1(x_{n_k}) = \min_{S_0}\Phi_1$. Since $\min_{S_0}\Phi_1$ is the limit of every converging subsequence of $(\Phi_1(x_n))$, we conclude that $\lim_{n\to +\infty}\Phi_1(x_n) = \min_{S_0}\Phi_1$ .

Remark 3.1. The main idea of the proof of Theorem 3.1 consists in the study of the sequence $(d(x_{n}, S_{1})^{2})_{n}$ by the distinction of cases (a) and (b). In the context of control and stabilization of nonlinear oscillators, this type of proof has been initiated by Attouch and Czarnecki [6]. It has been used in [13] to derive convergence properties of the (SDC) system (see the introduction). In fact, Theorem 3.1 can also be recovered $^{1}$ by a repeated application of [2, Theorem 3]. This last result is itself a discrete version of a former result due to Baillon and Cominetti [11, Theorem 2.1].

Remark 3.2. We point out that, in Theorem 3.1, the involved spaces are finite dimensional. Removing this restriction would extend the applicability of the approach to algorithms coming from the discretization of PDE models. It is out of the scope of the paper but this certainly indicates a matter for future research.

3.2. Convergence of the sequence $(x_{n})$. From Theorem 3.1, the distance of the sequence $(x_{n})$ (generated by $(\mathcal{A}_{1})$ ) to the set $S_{1}$ tends to 0. In particular, if $S_{1}$ is reduced to a singleton, then the sequence $(x_{n})$ converges. However, in the slow case we do not have any general result of convergence for $(x_{n})$ like Proposition 2.2 in the fast case. The convergence of the sequence $(x_{n})$ can be obtained by strengthening the assumptions on $(\varepsilon_{n})$. Before stating the result, let us introduce the sequence $(\omega_{n})$ defined by

$$
\omega_ {n} := \inf _ {x \in \mathbb {R} ^ {n}} [ \Phi_ {0} (x) - \min \Phi_ {0} + \varepsilon_ {n} (\Phi_ {1} (x) - \min _ {S _ {0}} \Phi_ {1}) ]. \tag {3.7}
$$

The sequence $(\omega_{n})$ is minorized by

$$
\omega_ {n} \geq - \varepsilon_ {n} \left(\min _ {S _ {0}} \Phi_ {1} - \inf \Phi_ {1}\right).
$$

The following proposition establishes that the negative part of the sequence $(\omega_{n})$ is negligible with respect to $\varepsilon_{n}$ when $n\to +\infty$.

PROPOSITION 3.4. Assume that $\Phi_0: \mathbb{R}^n \to \mathbb{R} \cup \{+\infty\}$ and $\Phi_1: \mathbb{R}^n \to \mathbb{R}$ satisfy the hypotheses of Theorem 3.1. Consider a sequence $(\varepsilon_n)$ such that $\lim_{n \to +\infty} \varepsilon_n = 0$. Then the sequence $(\omega_n)$ defined by (3.7) satisfies $\lim_{n \to +\infty} \omega_n^- / \varepsilon_n = 0$.

Proof. Let us argue by contradiction and assume that $\liminf_{n\to +\infty}\omega_n / \varepsilon_n < 0$. Then there exist $\eta >0$ and a sequence $(n_k)$ tending toward $+\infty$ such that

$$
\forall k \in \mathbb {N}, \quad \inf _ {x \in \mathbb {R} ^ {n}} \left[ \Phi_ {0} (x) - \min \Phi_ {0} + \varepsilon_ {n _ {k}} \left(\Phi_ {1} (x) - \min _ {S _ {0}} \Phi_ {1}\right) \right] \leq - \eta \varepsilon_ {n _ {k}}.
$$

Therefore, there exists a sequence $(x_{n_{k}})$ in $R^{n}$ such that

$$
\forall k \in \mathbb {N}, \quad \Phi_ {0} (x _ {n _ {k}}) - \min \Phi_ {0} + \varepsilon_ {n _ {k}} \left(\Phi_ {1} (x _ {n _ {k}}) - \min _ {S _ {0}} \Phi_ {1}\right) \leq - \frac {\eta}{2} \varepsilon_ {n _ {k}}. \tag {3.8}
$$

Noticing that $\Phi_{1}(x_{n_{k}})\geq\inf\Phi_{1}$ and taking the upper limit when $k\to+\infty$, we find

$$
\operatorname * {l i m s u p} _ {k \to + \infty} \Phi_ {0} (x _ {n _ {k}}) \leq \min \Phi_ {0}. \tag {3.9}
$$

Since, on the other hand, $\Phi_0(x_{n_k})\geq \min \Phi_0$, we infer from (3.8) that

$$
\operatorname * {l i m s u p} _ {k \to + \infty} \Phi_ {1} (x _ {n _ {k}}) \leq \min _ {S _ {0}} \Phi_ {1} - \frac {\eta}{2}. \tag {3.10}
$$

From (3.9) and (3.10), it is clear that for every $M_0 > \min \Phi_0$, we have

$$
x _ {n _ {k}} \in [ \Phi_ {0} \leq M _ {0} ] \cap [ \Phi_ {1} \leq \min _ {S _ {0}} \Phi_ {1} ]
$$

for $k$ large enough. Since the set $S_{1}$ is bounded, we conclude in view of Lemma 3.3 that the sequence $(x_{n_k})$ is bounded. Therefore, there exist $\bar{x} \in \mathbb{R}^n$ and a subsequence of $(x_{n_k})$, still denoted by $(x_{n_k})$, such that $\lim_{k \to +\infty} x_{n_k} = \bar{x}$. From the closedness of $\Phi_0$ and inequality (3.9), we deduce that

$$
\Phi_ {0} (\bar {x}) \leq \operatorname * {l i m i n f} _ {k \to + \infty} \Phi_ {0} (x _ {n _ {k}}) \leq \operatorname * {l i m s u p} _ {k \to + \infty} \Phi_ {0} (x _ {n _ {k}}) \leq \min \Phi_ {0},
$$

i.e., $\bar{x} \in S_{0}$. Similarly, the continuity of $\Phi_{1}$ combined with inequality (3.10) yields

$$
\Phi_ {1} (\bar {x}) = \lim _ {k \to + \infty} \Phi_ {1} (x _ {n _ {k}}) \leq \min _ {S _ {0}} \Phi_ {1} - \frac {\eta}{2},
$$

a contradiction with $\bar{x} \in S_0$.

Let us now give examples for which it is possible to compute explicitly the sequence $(\omega_{n})$ (or at least a lower bound for $(\omega_{n})$ ).

PROPOSITION 3.5. Assume that $\Phi_0: \mathbb{R}^n \to \mathbb{R} \cup \{+\infty\}$ and $\Phi_1: \mathbb{R}^n \to \mathbb{R}$ satisfy the hypotheses of Theorem 3.1.

(i) If $\arg\min \Phi_0 \cap \arg\min \Phi_1 \neq \emptyset$, then $\omega_n \geq 0$ for every $n \in \mathbb{N}$.  
(ii) Assume that there exist $a > 0$, $b > 0$, and $p \geq 1$ such that

(a) $\Phi_0 - \min \Phi_0 \geq a d(., S_0)^p$,  
(b) $\Phi_1 - \min_{S_0}\Phi_1\geq -bd(.,[\Phi_1\geq \min_{S_0}\Phi_1])$

Then there exist $\alpha \geq 0$ and $q > 1$ such that $\omega_{n} \geq -\alpha \varepsilon_{n}^{q}$ for $n$ large enough (when $p > 1$ the exponent $q$ is the conjugate of $p$, i.e., $q = 1 / (1 - 1 / p)$ ).

Proof. (i) Notice that the assumption $\arg\min\Phi_{0}\cap\arg\min\Phi_{1}\neq\emptyset$ implies that $\arg\min_{S_{0}}\Phi_{1}=\arg\min\Phi_{0}\cap\arg\min\Phi_{1}$ and $\min_{S_{0}}\Phi_{1}=\min\Phi_{1}$. As a consequence,

$$
\Phi_ {0} - \min \Phi_ {0} + \varepsilon_ {n} \left(\Phi_ {1} - \min _ {S _ {0}} \Phi_ {1}\right) = \Phi_ {0} - \min \Phi_ {0} + \varepsilon_ {n} \left(\Phi_ {1} - \min \Phi_ {1}\right) \geq 0
$$

and $\omega_{n}\geq 0$ for every $n\in \mathbb{N}$.

(ii) Since the set $S_0$ is included in the set $[\Phi_1 \geq \min_{S_0} \Phi_1]$, we have $d(., S_0) \geq d(., [\Phi_1 \geq \min_{S_0} \Phi_1])$, which combined with the assumption on $\Phi_1$, implies

$$
\Phi_ {1} - \min _ {S _ {0}} \Phi_ {1} \geq - b   d (., S _ {0}).
$$

Taking into account assumption (a), we deduce from the previous inequality that, for every $x \in R^{n}$,

$$
\Phi_ {0} (x) - \min \Phi_ {0} + \varepsilon_ {n} \left(\Phi_ {1} (x) - \min _ {S _ {0}} \Phi_ {1}\right) \geq a d (x, S _ {0}) ^ {p} - b \varepsilon_ {n} d (x, S _ {0}).
$$

First assume that $p = 1$. It is then immediate that we have, for $n$ large enough,

$$
\Phi_ {0} (x) - \min \Phi_ {0} + \varepsilon_ {n} \left(\Phi_ {1} (x) - \min _ {S _ {0}} \Phi_ {1}\right) \geq 0,
$$

so that $\omega_{n} \geq 0$. Now assume that $p > 1$. An elementary computation then shows that

$$
a d (x, S _ {0}) ^ {p} - b \varepsilon_ {n} d (x, S _ {0}) \geq - b \left(\frac {b}{p a}\right) ^ {\frac {1}{p - 1}} \left(\frac {p - 1}{p}\right) \varepsilon_ {n} ^ {\frac {p}{p - 1}},
$$

so that the expected inequality holds with $\alpha = b\left(\frac{b}{p a}\right)^{\frac{1}{p - 1}}\left(\frac{p - 1}{p}\right)$ and $q = \frac{p}{p - 1}$.

Remark 3.3. Given a convex set $S_0$ and a convex function $\Phi_1: \mathbb{R}^n \to \mathbb{R}$, let us consider the following constrained minimization problem:

$$
(\mathcal {P}) \qquad \min \{\Phi_ {1} (x), \quad x \in S _ {0} \}.
$$

As recalled in the introduction, we associate with $(\mathcal{P})$ the algorithm $(\mathcal{A}_{1})$ via the choice of a function $\Phi_{0}: R^{n} \to R$ satisfying $\arg\min\Phi_{0} = S_{0}$. For theoretical purposes, it is convenient to choose $\Phi_{0} := d(., S_{0})$ or $\Phi_{0} := d(., S_{0})^{2}$. For these functions, condition (a) of Proposition 3.5 trivially holds.

Remark 3.4. The Lipschitz-type condition (b) on $\Phi_{1}$ is verified in many situations. Indeed, let us denote by $M$ the quantity

$$
M := \sup \big \{| \xi |: \xi \in \partial \Phi_ {1} (x),   \Phi_ {1} (x) = \min _ {S _ {0}} \Phi_ {1} \big \}.
$$

Supposing that $M < +\infty$, then for any $x \in [\Phi_{1} \leq \min_{S_{0}} \Phi_{1}]$, one has

$$
\Phi_ {1} (x) - \min _ {S _ {0}} \Phi_ {1} \geq \langle \partial \Phi_ {1} (y), x - y \rangle \geq - M d (x, [ \Phi_ {1} \geq \min _ {S _ {0}} \Phi_ {1} ]),
$$

where $y$ is the projection of $x$ on $[\Phi_1 = \min_{S_0}\Phi_1]$.

Let us come back to the convergence of the sequence $(x_{n})$ associated with the algorithm $(\mathcal{A}_{1})$. Proposition 3.4 shows the existence of a gap between the sequences $(\varepsilon_{n})$ and $(\omega_{n}^{-})$. The next proposition shows how to exploit this property to obtain the convergence of the sequence $(x_{n})$ generated by $(\mathcal{A}_{1})$.

PROPOSITION 3.6. Under the hypotheses of Theorem 3.1, let us consider the sequence $(\omega_{n})$ defined by (3.7). We assume that $\sum_{n=0}^{+\infty} \varepsilon_{n} = +\infty$ and $\sum_{n=0}^{+\infty} \omega_{n}^{-} < +\infty$. Then, any sequence $(x_{n})$ generated by the algorithm $(\mathcal{A}_{1})$ converges to some $\bar{x} \in S_{1}$.

Proof. Given any $z \in S_1$, let us define the sequence $(g_n)$ by

$$
g _ {n} = \frac {1}{2} | x _ {n} - z | ^ {2}.
$$

Decomposing $x_{k} - z$ as $x_{k} - z = x_{k} - x_{k + 1} + x_{k + 1} - z$, we obtain for every $k\in \mathbb{N}$

$$
g _ {k} = \frac {1}{2} | x _ {k} - x _ {k + 1} | ^ {2} + g _ {k + 1} + \langle x _ {k} - x _ {k + 1}, x _ {k + 1} - z \rangle ,
$$

and hence

$$
\begin{aligned} g _ {k + 1} &= g _ {k} - \frac {1}{2} | x _ {k + 1} - x _ {k} | ^ {2} + \langle x _ {k + 1} - x _ {k}, x _ {k + 1} - z \rangle \\ &\leq g _ {k} - \lambda_ {k} \left\langle - (x _ {k + 1} - x _ {k}) / \lambda_ {k}, x _ {k + 1} - z \right\rangle . \\ \end{aligned}
$$

Since $-(x_{k + 1} - x_k) / \lambda_k\in \partial_{\eta_k}(\Phi_0 + \varepsilon_k\Phi_1)(x_{k + 1})$, the previous inequality gives

$$
g _ {k + 1} \leq g _ {k} - \lambda_ {k} \left(\Phi_ {0} (x _ {k + 1}) + \varepsilon_ {k} \Phi_ {1} (x _ {k + 1}) - \Phi_ {0} (z) - \varepsilon_ {k} \Phi_ {1} (z) - \eta_ {k}\right).
$$

As a consequence, we have

$$
g _ {k + 1} - g _ {k} + \lambda_ {k} \left(\Phi_ {0} (x _ {k + 1}) - \min \Phi_ {0} + \varepsilon_ {k} \left(\Phi_ {1} (x _ {k + 1}) - \min _ {S _ {0}} \Phi_ {1}\right)\right) \leq \overline {{\lambda}} \eta_ {k},
$$

and hence

$$
g _ {k + 1} - g _ {k} - \lambda_ {k} \omega_ {k} ^ {-} \leq g _ {k + 1} - g _ {k} + \lambda_ {k} \omega_ {k} \leq \overline {{\lambda}} \eta_ {k}.
$$

This implies that

$$
(g _ {k + 1} - g _ {k}) ^ {+} \leq \overline {{\lambda}} (\eta_ {k} + \omega_ {k} ^ {-}).
$$

By using the fact that $\sum_{k=0}^{+\infty}\eta_k < +\infty$ and $\sum_{k=0}^{+\infty}\omega_k^- < +\infty$, we obtain in view of Lemma 3.2 that $\lim_{n\to +\infty}g_n$ exists, and hence

$$
\lim _ {n \to + \infty} | x _ {n} - z | \quad \text {exists for any} z \in S _ {1}. \tag {3.11}
$$

Since the sequence $(x_{n})$ is bounded, we can extract a converging subsequence: there exist $\bar{x} \in \mathbb{R}^{n}$ and $(x_{n_k})$ such that $\lim_{k \to +\infty} x_{n_k} = \bar{x}$. From Theorem 3.1, we have $\bar{x} \in S_1$. Taking $z = \bar{x}$ in (3.11), we deduce that $\lim_{n \to +\infty} |x_n - \bar{x}|$ exists, which combined with $\lim_{k \to +\infty} |x_{n_k} - \bar{x}| = 0$, finally yields $\lim_{n \to +\infty} |x_n - \bar{x}| = 0$.

Let us denote by $l^1$ the set of nonnegative sequences $(a_n)$ satisfying $\sum_{n=0}^{+\infty} a_n < +\infty$. The assumptions of Proposition 3.6 can be rewritten as $(\varepsilon_n) \notin l^1$ and $(\omega_n^-) \in l^1$. The question of the convergence is open when $(\omega_n^-) \notin l^1$, which corresponds to the "very slow case." If $\omega_n \geq 0$ for every $n \in \mathbb{N}$, the required condition reduces to $(\varepsilon_n) \notin l^1$.

# 4. Generalization: Toward hierarchical minimization.

4.1. Algorithm $(\mathcal{A}_{2})$ : Minimization of $\Phi_{2}$ over $\arg\min_{S_{0}}\Phi_{1}$. Given three convex functions $\Phi_{0}, \Phi_{1}$, and $\Phi_{2}$, it is natural in view of Theorem 3.1 to try to minimize $\Phi_{2}$ over the set $\arg\min_{S_{0}}\Phi_{1}$. For that purpose, we define the algorithm $(\mathcal{A}_{2})$ :

$$
(\mathcal {A} _ {2}) \quad - \frac {x _ {n + 1} - x _ {n}}{\lambda_ {n}} \in \partial_ {\eta_ {n}} \Big (\Phi_ {0} + \varepsilon_ {n} \Phi_ {1} + \varepsilon_ {n} ^ {(2)} \Phi_ {2} \Big) (x _ {n + 1}),
$$

where the choice of the sequence $(\varepsilon_n^{(2)})$ is specified in the next theorem.

THEOREM 4.1. Let $\Phi_0: \mathbb{R}^n \to \mathbb{R} \cup \{+\infty\}$ be a closed convex function and $\Phi_1, \Phi_2: \mathbb{R}^n \to \mathbb{R}$ finite convex functions. Assume that the functions $\Phi_0, \Phi_1, \Phi_2$ are bounded from below, that the set $S_0 := \arg\min \Phi_0$ is nonempty, and that the sets $S_1 := \arg\min_{S_0} \Phi_1, S_2 := \arg\min_{S_1} \Phi_2$ are nonempty and bounded. We are given a sequence $(\varepsilon_n)$ satisfying $(\mathcal{H}_\varepsilon)$ and a sequence $(\varepsilon_n^{(2)})$ such that

$$
\lim _ {n \to + \infty} \varepsilon_ {n} ^ {(2)} / \varepsilon_ {n} = 0 \quad a n d \quad \lim _ {n \to + \infty} \omega_ {n} ^ {-} / \varepsilon_ {n} ^ {(2)} = 0, \tag {4.1}
$$

where the sequence $(\omega_{n})$ is defined by (3.7). We assume moreover that $\sum_{n=0}^{+\infty}\varepsilon_n^{(2)} = +\infty$. We are also given nonnegative sequences $(\lambda_n)$, $(\eta_n)$ verifying, respectively, $(\mathcal{H}_{\lambda})$ and $(\mathcal{H}_{\eta})$. Any sequence $(x_{n})$ generated by the algorithm $(\mathcal{A}_2)$ satisfies

(i) $\lim_{n\to +\infty}d(x_n,S_2) = 0,$

(ii) $\lim_{n\to +\infty}(\Phi_0(x_n),\Phi_1(x_n),\Phi_2(x_n)) = (\min \Phi_0,\min_{S_0}\Phi_1,\min_{S_1}\Phi_2)$.

Proof. The reader is referred to the proof of Theorem 4.4, which is a generalization of Theorem 4.1 to the case $N \geq 2$. $\square$

As for the algorithm $(\mathcal{A}_{1})$, we now study the convergence of the sequence $(x_{n})$ generated by $(\mathcal{A}_{2})$. Let us introduce the sequence $(\omega_{n}^{(2)})$ defined by

$$
\omega_ {n} ^ {(2)} := \inf _ {x \in \mathbb {R} ^ {n}} [ \Phi_ {0} (x) - \min \Phi_ {0} + \varepsilon_ {n} \left(\Phi_ {1} (x) - \min _ {S _ {0}} \Phi_ {1}\right) + \varepsilon_ {n} ^ {(2)} \left(\Phi_ {2} (x) - \min _ {S _ {1}} \Phi_ {2}\right) ]. \tag {4.2}
$$

The sequence $(\omega_n^{(2)})$ is minorized by

$$
\omega_ {n} ^ {(2)} \geq - \varepsilon_ {n} \left(\min _ {S _ {0}} \Phi_ {1} - \inf \Phi_ {1}\right) - \varepsilon_ {n} ^ {(2)} \left(\min _ {S _ {1}} \Phi_ {2} - \inf \Phi_ {2}\right).
$$

Let us notice that if $\arg\min \Phi_0 \cap \arg\min \Phi_1 \cap \arg\min \Phi_2 \neq \emptyset$, then we have $\omega_n \geq 0$ for every $n \in \mathbb{N}$. Moreover, for every choice of $(\varepsilon_n^{(2)})$, we also have $\omega_n^{(2)} \geq 0$ for every $n \in \mathbb{N}$. The following proposition provides us with another example for which the sequence $(\omega_n^{(2)})$ can be explicitly evaluated.

PROPOSITION 4.2. Assume that $\Phi_0: \mathbb{R}^n \to \mathbb{R} \cup \{+\infty\}$, $\Phi_1, \Phi_2: \mathbb{R}^n \to \mathbb{R}$ satisfy the hypotheses of Theorem 4.1. Assume that there exist $a_0, a_1, b_1, b_2, c \in \mathbb{R}_+^*$ and $p_0, p_1 \in [1, +\infty[$ such that

$$
\left\{ \begin{array}{l l} \text {(i)} & \Phi_ {0} - \min \Phi_ {0} \geq a _ {0} d (., S _ {0}) ^ {p _ {0}}, \\ \text {(ii)} & \Phi_ {1} - \min _ {S _ {0}} \Phi_ {1} \geq a _ {1} d (., [ \Phi_ {1} \leq \min _ {S _ {0}} \Phi_ {1} ]) ^ {p _ {1}} - b _ {1} d (., [ \Phi_ {1} \geq \min _ {S _ {0}} \Phi_ {1} ]), \\ \text {(iii)} & \Phi_ {2} - \min _ {S _ {1}} \Phi_ {2} \geq - b _ {2} d (., [ \Phi_ {2} \geq \min _ {S _ {1}} \Phi_ {2} ]), \\ \text {(iv)} & d (., S _ {1}) \leq c (d (., [ \Phi_ {1} \leq \min _ {S _ {0}} \Phi_ {1} ]) + d (., S _ {0})). \end{array} \right.
$$

Then the following assertions hold:

(a) There exist $m \geq 0$ and $q_0 > 1$ such that $\omega_n \geq -m\varepsilon_n^{q_0}$ for $n$ large enough.  
(b) Take $\varepsilon_n^{(2)} = \varepsilon_n^r$ for some $r\in ]1,q_0[$. Then there exist $M\geq 0$ and $q_{1} > r$ such that $\omega_{n}^{(2)}\geq -M\varepsilon_{n}^{q_{1}}$ for $n$ large enough.

Proof. (a) Let us first minorize the quantity

$$
A _ {\varepsilon_ {n}} (x) := \Phi_ {0} (x) - \min \Phi_ {0} + \varepsilon_ {n} \left(\Phi_ {1} (x) - \min _ {S _ {0}} \Phi_ {1}\right).
$$

Since $S_0 \subset [\Phi_1 \geq \min_{S_0} \Phi_1]$, we have $d(., S_0) \geq d(., [\Phi_1 \geq \min_{S_0} \Phi_1])$, which, combined with (ii), implies

$$
\Phi_ {1} (x) - \min _ {S _ {0}} \Phi_ {1} \geq a _ {1}   d (x, [ \Phi_ {1} \leq \min _ {S _ {0}} \Phi_ {1} ]) ^ {p _ {1}} - b _ {1}   d (x, S _ {0}). \tag {4.3}
$$

In view of (i), we deduce that $A_{\varepsilon_{n}}(x) \geq a_{0} d(x, S_{0})^{p_{0}} - b_{1} \varepsilon_{n} d(x, S_{0})$. The same computation as in the proof of Proposition 3.5 (ii) shows that there exist $m \geq 0$ and $q_{0} > 1$ such that, for n large enough,

$$
a _ {0}   d (x, S _ {0}) ^ {p _ {0}} - b _ {1}   \varepsilon_ {n}   d (x, S _ {0}) \geq - m   \varepsilon_ {n} ^ {q _ {0}}.
$$

More precisely, if $p_0 > 1$ one can take $q_0 = p_0 / (p_0 - 1)$ and if $p_0 = 1$, the previous inequality is satisfied with $m = 0$. We have established that $A_{\varepsilon_n}(x) \geq -m\varepsilon_n^{q_0}$, which ends the proof of (a).

(b) Let us now find a lower bound for the quantity

$$
B _ {\varepsilon_ {n}} (x) := \Phi_ {0} (x) - \min \Phi_ {0} + \varepsilon_ {n} \left(\Phi_ {1} (x) - \min _ {S _ {0}} \Phi_ {1}\right) + \varepsilon_ {n} ^ {r} \left(\Phi_ {2} (x) - \min _ {S _ {1}} \Phi_ {2}\right).
$$

The inclusion $S_1 \subset [\Phi_2 \geq \min_{S_1} \Phi_2]$ implies $d(., S_1) \geq d(., [\Phi_2 \geq \min_{S_1} \Phi_2])$, and hence in view of (iii) and (iv),

$$
\Phi_ {2} (x) - \min _ {S _ {1}} \Phi_ {2} \geq - b _ {2}   c   (d (x, [ \Phi_ {1} \leq \min _ {S _ {0}} \Phi_ {1} ]) + d (x, S _ {0})). \tag {4.4}
$$

Combining (i), (4.3), and (4.4), we obtain

$$
\begin{aligned} B _ {\varepsilon_ {n}} (x) &\geq a _ {0} d (x, S _ {0}) ^ {p _ {0}} - b _ {1} \varepsilon_ {n} d (x, S _ {0}) - b _ {2} c \varepsilon_ {n} ^ {r} d (x, S _ {0}) \tag {4.5} \\ + a _ {1} \varepsilon_ {n} d (x, [ \Phi_ {1} &\leq \min _ {S _ {0}} \Phi_ {1} ]) ^ {p _ {1}} - b _ {2} c \varepsilon_ {n} ^ {r} d (x, [ \Phi_ {1} \leq \min _ {S _ {0}} \Phi_ {1} ]). \\ \end{aligned}
$$

Since the quantity $\varepsilon_n^r$ is negligible with respect to $\varepsilon_{n}$ when $n\to +\infty$, the same arguments as above show that there exists $m_2\geq 0$ such that

$$
a _ {0}   d (x, S _ {0}) ^ {p _ {0}} - b _ {1}   \varepsilon_ {n}   d (x, S _ {0}) - b _ {2}   c   \varepsilon_ {n} ^ {r}   d (x, S _ {0}) \geq - m _ {2}   \varepsilon_ {n} ^ {q _ {0}}. \tag {4.6}
$$

In the same way, we let the reader check that there exist $m_3 \geq 0$ and $q_1 > r$ such that

$$
a _ {1} \varepsilon_ {n} d (x, [ \Phi_ {1} \leq \min _ {S _ {0}} \Phi_ {1} ]) ^ {p _ {1}} - b _ {2} c \varepsilon_ {n} ^ {r} d (x, [ \Phi_ {1} \leq \min _ {S _ {0}} \Phi_ {1} ]) \geq - m _ {3} \varepsilon_ {n} ^ {q _ {1}}. \tag {4.7}
$$

(If $p_1 > 1$, then one can take $q_1 = (r - 1)\left(\frac{p_1}{p_1 - 1}\right) + 1$ and if $p_1 = 1$, then inequality (4.7) is satisfied with $m_3 = 0$.) In view of (4.5), (4.6), and (4.7), we deduce that

$$
B _ {\varepsilon_ {n}} (x) \geq - m _ {2} \varepsilon_ {n} ^ {q _ {0}} - m _ {3} \varepsilon_ {n} ^ {q _ {1}}.
$$

Since $\min\{q_{0}, q_{1}\} > r$, the conclusion immediately follows. ☐

Let us now comment on items (ii) and (iv) of Proposition 4.2 by means of the following remarks.

Remark 4.1. Assumption (ii) of Proposition 4.2 may be decomposed into two parts: the first one is

$$
\forall x \in [ \Phi_ {1} \geq \min _ {S _ {0}} \Phi_ {1} ], \quad \Phi_ {1} (x) - \min _ {S _ {0}} \Phi_ {1} \geq a _ {1}   d (x, [ \Phi_ {1} \leq \min _ {S _ {0}} \Phi_ {1} ]) ^ {p _ {1}}, \tag {4.8}
$$

while the second one is

$$
\forall x \in [ \Phi_ {1} \leq \min _ {S _ {0}} \Phi_ {1} ], \quad \Phi_ {1} (x) - \min _ {S _ {0}} \Phi_ {1} \geq - b _ {1}   d (x, [ \Phi_ {1} \geq \min _ {S _ {0}} \Phi_ {1} ]). \tag {4.9}
$$

First assume that $\min_{S_0}\Phi_1 = \min \Phi_1$. In such a case, (4.8) reduces to

$$
\forall x \in \mathbb {R} ^ {n}, \quad \Phi_ {1} (x) - \min \Phi_ {1} \geq a _ {1} d (x, \operatorname{argmin} \Phi_ {1}) ^ {p _ {1}},
$$

which is a classical assumption on $\Phi_1$. Conversely, assume that $\min_{S_0} \Phi_1 > \min \Phi_1$ : we then have $0 \notin \partial \Phi_1(x)$ for every $x \in [\Phi_1 = \min_{S_0} \Phi_1]$. Let us denote by $m$ the quantity

$$
m := \inf \left\{\left| \xi \right|: \xi \in \partial \Phi_ {1} (x), \Phi_ {1} (x) = \min _ {S _ {0}} \Phi_ {1} \right\}.
$$

The theory of error bounds for closed convex functions (see, for example, [9]) shows that for every $x \in [\Phi_{1} \geq \min_{S_{0}} \Phi_{1}]$,

$$
\Phi_ {1} (x) - \min _ {S _ {0}} \Phi_ {1} \geq m d (x, [ \Phi_ {1} \leq \min _ {S _ {0}} \Phi_ {1} ]),
$$

so that (4.8) holds with $p_{1} := 1$ and $a_{1} := m$ as soon as m > 0. For comments relative to the second part of (4.9), we refer the reader to Remark 3.4.

Remark 4.2. Let us recall that the set $S_{1}$ equals the intersection $S_{0} \cap [\Phi_{1} \leq \min_{S_{0}} \Phi_{1}]$. Assumption (iv) of Proposition 4.2 means that the intersecting sets $S_{0}$ and $[\Phi_{1} \leq \min_{S_{0}} \Phi_{1}]$ are not tangent at the points of $S_{1}$ which belong to the boundary of $S_{0} \cup [\Phi_{1} \leq \min_{S_{0}} \Phi_{1}]$. In other words, the (possibly) inward corners of the set $S_{0} \cup \min_{S_{0}} \Phi_{1}$.

$[\Phi_{1} \leq \min_{S_{0}} \Phi_{1}]$ must not be inward cusps. We let the reader check that assumption (iv) can be replaced by the following less stringent one: there exist $p_{2}, p_{3} \in]0,1]$ such that

$$
(i v - b i s) \qquad d (., S _ {1}) \leq c \left(d (., [ \Phi_ {1} \leq \min _ {S _ {0}} \Phi_ {1} ]) ^ {p _ {2}} + d (., S _ {0}) ^ {p _ {3}}\right).
$$

This last assumption allows a wider class of intersecting sets $S_{0}$ and $[\Phi_{1} \leq \min_{S_{0}} \Phi_{1}]$.

Let us come back to the problem of the convergence of the algorithm $(\mathcal{A}_{2})$. By using arguments which are similar to those of Proposition 3.4, it is easy to show that the quantity $[\omega_{n}^{(2)}]^{-}$ is negligible with respect to $\varepsilon_{n}^{(2)}$ when $n \to +\infty$. The following proposition shows how to exploit this property to deduce the convergence of the algorithm $(\mathcal{A}_{2})$.

PROPOSITION 4.3. Under the hypotheses of Theorem 4.1, let us consider the sequence $(\omega_n^{(2)})$ defined by (4.2). We assume that $\sum_{n=0}^{+\infty} \varepsilon_n^{(2)} = +\infty$ and $\sum_{n=0}^{+\infty} [\omega_n^{(2)}]^- < +\infty$. Then, any sequence $(x_n)$ generated by the algorithm $(\mathcal{A}_2)$ converges to some $\bar{x} \in S_2$.

Proof. The arguments are similar to the ones of Proposition 3.6. The reader is also referred to the proof of Proposition 4.5, which is a generalization of Proposition 4.3 to the case $N \geq 2$.

4.2. Algorithm $(\mathcal{A}_N)$ and hierarchical minimization. Let $\Phi_0: \mathbb{R}^n \to \mathbb{R} \cup \{+\infty\}$ be a closed convex function and $\Phi_1, \ldots, \Phi_N: \mathbb{R}^n \to \mathbb{R}$ finite convex functions ( $N \geq 1$ ). Assume that $\Phi_0, \Phi_1, \ldots, \Phi_N$ are bounded from below and define the sets $(S_i)_{-1 \leq i \leq N}$ as follows: $S_{-1} := \mathbb{R}^n$ and for $i \in \{0, \ldots, N\}$, $S_i := \arg\min_{S_{i-1}} \Phi_i$. A challenging task consists in minimizing each function $\Phi_i$ on the set $S_{i-1}$ for $i \in \{0, \ldots, N\}$. This question of hierarchical minimization has been addressed by many authors (see, for example, Attouch [4], Cominetti and Courdurier [18]).

According to the previous results of the paper, the algorithm $(\mathcal{A}_{1})$ (resp., $(\mathcal{A}_{2})$ ) allows us to generate a sequence $(x_{n})$ which minimizes the function $\Phi_{1}$ (resp., $\Phi_{2}$ ) over the set $S_{0}$ (resp., $S_{1}$ ). It is then natural to define the algorithm $(\mathcal{A}_{N})$ by

$$
(\mathcal {A} _ {N}) \qquad - \frac {x _ {n + 1} - x _ {n}}{\lambda_ {n}} \in \partial_ {\eta_ {n}} \Big (\Phi_ {0} + \varepsilon_ {n} ^ {(1)} \Phi_ {1} + \varepsilon_ {n} ^ {(2)} \Phi_ {2} + \dots + \varepsilon_ {n} ^ {(N)} \Phi_ {N} \Big) (x _ {n + 1}),
$$

where the sequences $(\varepsilon_n^{(1)},\ldots ,(\varepsilon_n^{(N)})$ satisfy the construction suggested in the previous paragraph for $N = 2$. To unify the presentation, let us define the sequence $(\varepsilon_n^{(0)})$ by $\varepsilon_n^{(0)} = 1$ for every $n\in \mathbb{N}$. Assume that we have built the family of sequences $(\varepsilon_n^{(j)})_{1\leq j\leq i}$ for some $i\in \{2,\dots ,N\}$. For every $j\in \{1,\dots ,i\}$, let us introduce the sequence $(\omega_n^{(j)})$ defined by

$$
\omega_ {n} ^ {(j)} := \inf _ {x \in \mathbb {R} ^ {n}} \left[ \sum_ {l = 0} ^ {j} \varepsilon_ {n} ^ {(l)} (\Phi_ {l} (x) - \min _ {S _ {l - 1}} \Phi_ {l}) \right]. \tag {4.10}
$$

Suppose that the family of sequences $(\varepsilon_{n}^{(j)})_{1\leq j\leq i}$ satisfies the following property:

$$
\forall j \in \{2, \dots , i \}, \qquad \lim _ {n \to + \infty} \varepsilon_ {n} ^ {(j)} / \varepsilon_ {n} ^ {(j - 1)} = 0 \quad \text {and} \quad \lim _ {n \to + \infty} [ \omega_ {n} ^ {(j - 1)} ] ^ {-} / \varepsilon_ {n} ^ {(j)} = 0.
$$

By imitating the proof of Proposition 3.4, we can easily show that the sequence $(\omega_n^{(i)})$ defined by (4.10) satisfies $\lim_{n\to +\infty}[\omega_n^{(i)}]^- / \varepsilon_n^{(i)} = 0$. The next step consists in choosing

a sequence $(\varepsilon_{n}^{(i + 1)})$ satisfying

$$
\lim _ {n \to + \infty} \varepsilon_ {n} ^ {(i + 1)} / \varepsilon_ {n} ^ {(i)} = 0 \quad \text {and} \quad \lim _ {n \to + \infty} [ \omega_ {n} ^ {(i)} ] ^ {-} / \varepsilon_ {n} ^ {(i + 1)} = 0.
$$

By iterating the previous arguments, we obtain the existence of a family of sequences $(\varepsilon_{n}^{(i)})_{1\leq i\leq N}$ fulfilling

$$
\forall i \in \{2, \dots , N \}, \quad \lim _ {n \rightarrow + \infty} \varepsilon_ {n} ^ {(i)} / \varepsilon_ {n} ^ {(i - 1)} = 0 \quad \text {and} \quad \lim _ {n \rightarrow + \infty} [ \omega_ {n} ^ {(i - 1)} ] ^ {-} / \varepsilon_ {n} ^ {(i)} = 0.
$$

Once the existence of such a family is established, the main result relative to the algorithm $(\mathcal{A}_N)$ is the following.

THEOREM 4.4. Let $\Phi_0: \mathbb{R}^n \to \mathbb{R} \cup \{+\infty\}$ be a closed convex function and $\Phi_1, \ldots, \Phi_N: \mathbb{R}^n \to \mathbb{R}$ finite convex functions. Assume that $\Phi_0, \Phi_1, \ldots, \Phi_N$ are bounded from below and that the sets $(S_i)_{1 \leq i \leq N}$ defined as above are nonempty and bounded. We are given a sequence $(\varepsilon_n^{(1)})$ satisfying $(\mathcal{H}_{\varepsilon})$ and a family of sequences $(\varepsilon_n^{(2)}, \ldots, (\varepsilon_n^{(N)})$ satisfying

$$
\forall i \in \{2, \dots , N \}, \qquad \lim _ {n \to + \infty} \varepsilon_ {n} ^ {(i)} / \varepsilon_ {n} ^ {(i - 1)} = 0 \quad a n d \quad \lim _ {n \to + \infty} [ \omega_ {n} ^ {(i - 1)} ] ^ {-} / \varepsilon_ {n} ^ {(i)} = 0,
$$

where the sequences $(\omega_{n}^{(i)})_{1\leq i\leq N}$ are defined by relation (4.10). The sequence $(\varepsilon_{n}^{(N)})$ is supposed to verify $\sum_{n=0}^{+\infty}\varepsilon_{n}^{(N)}=+\infty$. We are also given nonnegative sequences $(\lambda_{n})$, $(\eta_{n})$ verifying, respectively, $(\mathcal{H}_{\lambda})$ and $(\mathcal{H}_{\eta})$. Any sequence $(x_{n})$ generated by the algorithm $(\mathcal{A}_{N})$ fulfills:

(i) $\lim_{n\to +\infty}d(x_n,S_N) = 0,$  
(ii) for all $i \in \{0, \dots, N\}$, $\lim_{n \to +\infty} \Phi_i(x_n) = \min_{S_{i-1}} \Phi_i$.

Proof. (i) The results of Proposition 2.1 for $(\mathcal{A}_{1})$ can be immediately extended to $(\mathcal{A}_{N})$. We then obtain that every limit point of the sequence $(x_{n})$ belongs to $\arg\min\Phi_{0}$. Let us argue by recurrence and let us denote by $(\mathcal{R}_{i})$ the following recurrence assumption:

$$
(\mathcal {R} _ {i}) \quad \lim _ {n \to + \infty} d (x _ {n}, S _ {i}) = 0.
$$

We let the reader check that $(\mathcal{R}_{1})$ is true. Let us prove the implication $(\mathcal{R}_{i-1}) \implies (\mathcal{R}_{i})$ for every $i \in \{2, \ldots, N\}$. For that purpose, we define the sequence $h_{n}^{(i)}$ by

$$
h _ {n} ^ {(i)} = \frac {1}{2} d (x _ {n}, S _ {i}) ^ {2}.
$$

We let the reader check that

$$
h _ {k + 1} ^ {(i)} - h _ {k} ^ {(i)} + \lambda_ {k} \sum_ {j = 0} ^ {N} \varepsilon_ {k} ^ {(j)} (\Phi_ {j} (x _ {k + 1}) - \Phi_ {j} (P _ {S _ {i}} (x _ {k + 1}))) \leq \overline {{\lambda}} \eta_ {k}.
$$

Notice that, since $P_{S_i}(x_{k + 1})\in S_i$, we have

$$
\forall j \in \{0, \dots , i \}, \quad \Phi_ {j} (P _ {S _ {i}} (x _ {k + 1})) = \min _ {S _ {j - 1}} \Phi_ {j},
$$

so that the previous inequality can be rewritten as

$$
\begin{aligned} h _ {k + 1} ^ {(i)} - h _ {k} ^ {(i)} + \lambda_ {k} \sum_ {j &= 0} ^ {i} \varepsilon_ {k} ^ {(j)} (\Phi_ {j} (x _ {k + 1}) - \min _ {S _ {j - 1}} \Phi_ {j}) + \lambda_ {k} \sum_ {j = i + 1} ^ {N} \varepsilon_ {k} ^ {(j)} (\Phi_ {j} (x _ {k + 1}) \\ - \Phi_ {j} (P _ {S _ {i}} (x _ {k + 1}))) &\leq \overline {{\lambda}} \eta_ {k}. \tag {4.11} \\ \end{aligned}
$$

Each function $\Phi_{j}$ is minorized by $\inf\Phi_{j}$ on $R^{n}$ and majorized by $\sup_{S_{i}}\Phi_{j}$ on the compact set $S_{i}$. Setting $m_{j} := \sup_{S_{i}}\Phi_{j} - \inf\Phi_{j} \geq 0$, we deduce that, for every $k \geq 0$,

$$
\Phi_ {j} (x _ {k + 1}) - \Phi_ {j} (P _ {S _ {i}} (x _ {k + 1})) \geq - m _ {j}.
$$

Since $\lim_{n\to +\infty}\varepsilon_n^{(j)} / \varepsilon_n^{(j - 1)} = 0$ when $n\to +\infty$ for every $j\in \{2,\dots ,N\}$, there exists $M\in \mathbb{R}_+$ such that for $k$ large enough,

$$
\sum_ {j = i + 1} ^ {N} \varepsilon_ {k} ^ {(j)} (\Phi_ {j} (x _ {k + 1}) - \Phi_ {j} (P _ {S _ {i}} (x _ {k + 1}))) \geq - M   \varepsilon_ {k} ^ {(i + 1)}. \tag {4.12}
$$

On the other hand, from the definition of the sequence $(\omega_{n}^{(i-1)})$, we have

$$
\sum_ {j = 0} ^ {i - 1} \varepsilon_ {k} ^ {(j)} (\Phi_ {j} (x _ {k + 1}) - \min _ {S _ {j - 1}} \Phi_ {j}) \geq \omega_ {k} ^ {(i - 1)} \geq - [ \omega_ {k} ^ {(i - 1)} ] ^ {-}. \tag {4.13}
$$

By combining (4.11), (4.12), and (4.13), we deduce

$$
h _ {k + 1} ^ {(i)} - h _ {k} ^ {(i)} + \lambda_ {k} \varepsilon_ {k} ^ {(i)} \Big (\Phi_ {i} (x _ {k + 1}) - \min _ {S _ {i - 1}} \Phi_ {i} - M \varepsilon_ {k} ^ {(i + 1)} / \varepsilon_ {k} ^ {(i)} - [ \omega_ {k} ^ {(i - 1)} ] ^ {-} / \varepsilon_ {k} ^ {(i)} \Big) \leq \overline {{\lambda}} \eta_ {k}.
$$

The rest of the proof consists in distinguishing the following cases:

$(\mathrm{a}_i)$ There exists $n_0 \in \mathbb{N}$ such that for all $n \geq n_0, \Phi_i(x_{n+1}) > \min_{S_{i-1}} \Phi_i + M \varepsilon_n^{(i+1)} / \varepsilon_n^{(i)} + [\omega_n^{(i-1)}]^- / \varepsilon_n^{(i)}$.

$(\mathrm{b}_i)$ For all $n_0 \in \mathbb{N}$, there exists $n \geq n_0$, $\Phi_i(x_{n+1}) \leq \min_{S_{i-1}} \Phi_i + M \varepsilon_n^{(i+1)} / \varepsilon_n^{(i)} + [\omega_n^{(i-1)}] / \varepsilon_n^{(i)}$.

The arguments of the proof of Theorem 3.1(i) still apply here insofar as the quantities $\varepsilon_n^{(i + 1)} / \varepsilon_n^{(i)}$ and $[\omega_n^{(i - 1)}]^{-} / \varepsilon_n^{(i)}$ tend to 0 when $n\to +\infty$. As a consequence, we obtain that $\lim_{n\to +\infty}h_n^{(i)} = \lim_{n\to +\infty}\frac{1}{2} d(x_n,S_i)^2 = 0$ and $(\mathcal{R}_i)$ is satisfied. The details are left to the reader.

(ii) is an immediate consequence of (i). For further details, we refer the reader to the proof of Theorem 3.1(ii). $\square$

Under the hypotheses of Theorem 4.4, it is easy to verify that the negative part of the sequence $(\omega_{n}^{(N)})$ is negligible with respect to $\varepsilon_{n}^{(N)}$ when $n \to +\infty$. The next proposition shows how to exploit this property to obtain the convergence of the sequence $(x_{n})$ generated by $(\mathcal{A}_{N})$.

PROPOSITION 4.5. Under the hypotheses of Theorem 4.4, assume that $\sum_{n=0}^{+\infty} \varepsilon_n^{(N)} = +\infty$ and $\sum_{n=0}^{+\infty} [\omega_n^{(N)}]^- < +\infty$. Then, any sequence $(x_n)$ generated by the algorithm $(\mathcal{A}_N)$ converges to some $\bar{x} \in S_N$.

Proof. Given any $z \in S_N$, let us define the sequence $(g_n)$ by $g_n = \frac{1}{2} |x_n - z|^2$. An elementary computation shows that

$$
g _ {k + 1} - g _ {k} + \lambda_ {k} \sum_ {j = 0} ^ {N} \varepsilon_ {k} ^ {(j)} (\Phi_ {j} (x _ {k + 1}) - \min _ {S _ {j - 1}} \Phi_ {j}) \leq \overline {{\lambda}}   \eta_ {k}.
$$

From the definition of $(\omega_n^{(N)})$, we deduce

$$
g _ {k + 1} - g _ {k} - \lambda_ {k} \left[ \omega_ {k} ^ {(N)} \right] ^ {-} \leq g _ {k + 1} - g _ {k} + \lambda_ {k} \omega_ {k} ^ {(N)} \leq \overline {{\lambda}} \eta_ {k},
$$

and hence

$$
(g _ {k + 1} - g _ {k}) ^ {+} \leq \overline {{\lambda}} (\eta_ {k} + [ \omega_ {k} ^ {(N)} ] ^ {-}).
$$

The sequel of the proof is similar to the one of Proposition 3.6, and the reader is referred to it. $\square$

5. Appendix: Proof of Lemma 3.3. Without loss of generality, we can assume that $M_0 \geq \min \Phi_0$ and $M_1 \geq \min_{S_0} \Phi_1$. We then have

$$
S _ {1} \subset [ \Phi_ {0} \leq M _ {0} ] \cap [ \Phi_ {1} \leq M _ {1} ],
$$

so that the set $[\Phi_{0} \leq M_{0}] \cap [\Phi_{1} \leq M_{1}]$ is nonempty. It is then well known (see, for example, [32]) that the closed convex sets $[\Phi_{0} \leq M_{0}]$ and $[\Phi_{1} \leq M_{1}]$ satisfy the following equality:

$$
\big ([ \Phi_ {0} \leq M _ {0} ] \cap [ \Phi_ {1} \leq M _ {1} ]) ^ {\infty} = [ \Phi_ {0} \leq M _ {0} ] ^ {\infty} \cap [ \Phi_ {1} \leq M _ {1} ] ^ {\infty},
$$

where $C^\infty$ is the horizon cone of $C$. Denoting by $f^\infty$ the horizon function of $f$, we have $[\Phi_0 \leq M_0]^{\infty} = [\Phi_0^{\infty} \leq 0]$ and $[\Phi_1 \leq M_1]^{\infty} = [\Phi_1^{\infty} \leq 0]$. As a consequence, the following equivalences hold:

$$
\begin{aligned} \left[ \Phi_ {0} &\leq M _ {0} \right] \cap \left[ \Phi_ {1} \leq M _ {1} \right] \quad \text {bounded} \quad \Longleftrightarrow \quad \left(\left[ \Phi_ {0} \leq M _ {0} \right] \cap \left[ \Phi_ {1} \leq M _ {1} \right]\right) ^ {\infty} = \{0 \} \\ \Longleftrightarrow \quad [ \Phi_ {0} ^ {\infty} &\leq 0 ] \cap [ \Phi_ {1} ^ {\infty} \leq 0 ] = \{0 \}. \\ \end{aligned}
$$

It is then clear that the boundedness of the set $[\Phi_{0} \leq M_{0}] \cap [\Phi_{1} \leq M_{1}]$ does not depend on the values $M_{0}$ and $M_{1}$. Taking $M_{0} = \min\Phi_{0}$ and $M_{1} = \min_{S_{0}}\Phi_{1}$, the previous set reduces to $S_{1}$ which is bounded by assumption. We conclude that the set $[\Phi_{0} \leq M_{0}] \cap [\Phi_{1} \leq M_{1}]$ is bounded for any value of $M_{0}$ and $M_{1}$.

Acknowledgments. The author thanks Professor Cominetti for pertinent remarks and fruitful discussions about the paper. The author also expresses his gratitude to the referees for their careful reading of the paper. Their valuable suggestions and critical comments made numerous improvements throughout.

# REFERENCES

[1] P. ALART AND B. LEMAIRE, Penalization in nonclassical convex programming via variational convergence, Math. Programming, 51 (1991), pp. 307-331.  
[2] F. ALVAREZ AND R. COMINETTI, Primal and dual convergence of a proximal point exponential penalty method for linear programming, Math. Programming, 93 (2002), pp. 87-96.  
[3] A. S. ANTIPIN, Minimization of convex functions on convex sets by means of differential equations, Differential Equations, 30 (1994), pp. 1365-1375.  
[4] H. ATTOUCH, Viscosity solutions of minimization problems, SIAM J. Optim., 6 (1996), pp. 769–806.  
[5] H. ATTOUCH AND R. COMINETTI, A dynamical approach to convex minimization coupling approximation with the steepest descent method, J. Differential Equations, 128 (1996), pp. 519–540.  
[6] H. ATTOUCH AND M.-O. CZARNECKI, Asymptotic control and stabilization of nonlinear oscillators with non isolated equilibria, J. Differential Equations, 179 (2002), pp. 278–310.  
[7] A. AUSLENDER, Numerical methods for nondifferentiable convex optimization, Math. Programming Stud., 30 (1987), pp. 102-126.  
[8] A. AUSLENDER, J.-P. CROUZEIX, AND P. FEDIT, Penalty-proximal methods in convex programming, J. Optim. Theory Appl., 55 (1987), pp. 1–21.  
[9] D. AZÉ AND J. N. CORVELLEC, Characterizations of error bounds for lower semicontinuous functions on metric spaces, ESAIM Control Optim. Calc. Var., 10 (2004), pp. 409–425.  
[10] M. A. BAHRAOUI AND B. LEMAIRE, Convergence of diagonally stationary sequences in convex optimization, Set-Valued Anal., 2 (1994), pp. 49–61.  
[11] J.-B. BAILLON AND R. COMINETTI, A convergence result for non-autonomous subgradient evolution equations and its application to the steepest descent exponential penalty trajectory in linear programming, J. Funct. Anal., 187 (2001), pp. 263-273.  
[12] H. BRÉZIS, Opérateurs maximaux monotones et semi-groupes de contractions dans les espaces de Hilbert, North Holland Math. Stud. 5, North–Holland, Amsterdam, 1973.  
[13] A. CABOT, The steepest descent dynamical system with control. Applications to constrained minimization, ESAIM Control Optim. Calc. Var., 10 (2004), pp. 243–258.  
[14] A. CABOT, Inertial gradient-like dynamical system controlled by a stabilizing term, J. Optim. Theory Appl., 120 (2004), pp. 275–303.  
[15] A. CABOT AND M.-O. CZARNECKI, Asymptotic control of pairs of oscillators coupled by a repulsion, with nonisolated equilibria I: The regular case, SIAM J. Control Optim., 41 (2002), pp. 1254–1280.  
[16] R. COMINETTI, Asymptotic convergence of the steepest descent method for the exponential penalty in linear programming, J. Convex Anal., 2 (1995), pp. 145–152.  
[17] R. COMINETTI, Coupling the proximal point algorithm with approximation methods, J. Optim. Theory Appl., 95 (1997), pp. 581–600.  
[18] R. COMINETTI AND M. COURDURIER, Coupling general penalty schemes for convex programming with the steepest descent and the proximal point algorithm, SIAM J. Optim., 13 (2002), pp. 745-765.  
[19] A. KAPLAN, A convex programming method with internal regularization, Dokl. Akad. Nauk, 241 (1978), pp. 22-25.  
[20] B. LEMAIRE, Coupling optimization methods and variational convergence, in Trends in Mathematical Optimization, International Ser. Numer. Math. 84, Birkhäuser, Basel, 1988, pp. 163–179.  
[21] B. LEMAIRE, About the convergence of the proximal method, in Advances in Optimization, Lecture Notes in Econom. and Math. Systems 382, Springer, Berlin, 1992, pp. 39–51.  
[22] B. LEMAIRE, Bounded diagonally stationary sequences in convex optimization, J. Convex Anal., 1 (1994), pp. 75–86.  
[23] B. LEMAIRE, On the convergence of some iterative methods for convex minimization, in Recent Developments in Optimization, Lecture Notes in Econom. and Math. Systems 429, Springer, Berlin, 1995, pp. 252–268.  
[24] B. MARTINET, Régularisation d'inéquations variationnelles par approximations successives, Rev. Française Informat. Recherche Opérationnelle, 4 (1970), pp. 154–159.  
[25] B. MARTINET, Détermination approchée d'un point fixe d'une application pseudo-contractante, C. R. Acad. Sci. Paris Ser. A-B, 274 (1972), pp. 163–165.  
[26] J. J. MOREAU, Proximité et dualité dans un espace hilbertien, Bull. Soc. Math. France, 93 (1965), pp. 273–299.  
[27] K. MOUALLIF, Sur la convergence d'une méthode associant pénalisation et régularisation, Bull. Soc. Roy. Sci. Liège, 56 (1987), pp. 175–180.  
[28] K. MOUALLIF AND P. TOSSINGS, Une méthode de pénalisation exponentielle associée à une régularisation proximale, Bull. Soc. Roy. Sci. Liège, 56 (1987), pp. 181–192.  
[29] A. MOUDAFI, Coupling proximal algorithm and Tikhonov method, Nonlinear Times Digest, 1 (1994), pp. 203-209.  
[30] Z. OPIAL, Weak convergence of the sequence of successive approximations for nonexpansive mappings, Bull. Amer. Math. Soc., 73 (1967), pp. 591-597.  
[31] R. T. ROCKAFELLAR, Monotone operators and the proximal point algorithm, SIAM J. Control Optim., 14 (1976), pp. 877–898.  
[32] R. T. ROCKAFELLAR AND R. WETS, Variational Analysis, Springer, Berlin, 1998.  
[33] A. N. Tikhonov AND V. Y. ARSENINE, Méthodes de résolution de problèmes mal posés, MIR, Moscow, 1976.
