# A Variable Metric Proximal Point Algorithm for Monotone Operators

J.V. Burke $^{*}$ Maijian Qian $^{\dagger}$

Submitted to SIAM Journal on Control and Optimization in August, 1992.

Revision submitted in September, 1997

# Abstract

The Proximal Point Algorithm (PPA) is a method for solving inclusions of the form $0 \in T(z)$ where $T$ is a monotone operator on a Hilbert space. The algorithm is one of the most powerful and versatile solution techniques for solving variational inequalities, convex programs, and convex-concave mini-max problems. It possesses a robust convergence theory for very general problem classes and is the basis for a wide variety of decomposition methods called splitting methods. Yet, the classical PPA typically exhibits slow convergence in many applications. For this reason, acceleration methods for the PPA algorithm are of great practical importance. In this paper we propose a variable metric implementation of the proximal point algorithm. In essence, the method is a Newton-like scheme applied to the Moreau-Yosida resolvent of the operator $T$. In this article, we establish the global and linear convergence of the proposed method. In addition, we characterize the super-linear convergence of the method. In a companion work, we establish the super-linear convergence of the method when implemented with Broyden updating (the non-symmetric case) and BFGS updating (the symmetric case).

Keywords: maximal monotone operator, proximal point methods, variable metric, global convergence, convergence rates.

Abbreviated title: Variable Metric PPA: Convergence.

AMS(MOS) subject classifications (1991): primary 90C25; secondary 49J45, 47H05, 49M45.

# 1 Introduction

The Proximal Point Algorithm (PPA) is one of the most powerful and versatile solution techniques for problems of convex programming and mini-max convex-concave programming. It possesses a robust convergence theory for very general problem classes in finite-and infinite-dimensions (e.g. see [11, 16, 21, 22, 23, 28, 32, 41, 40]), and is the basis for a wide variety of decomposition methods called splitting methods (e.g. see [4, 9, 12, 43, 44]). Yet, the classical PPA typically exhibits slow convergence in many applications. For this reason, acceleration methods for the PPA are of great practical importance. In this paper we propose a variable metric implementation of the proximal point algorithm. Our approach extends and refines results that originally appeared in [38] and is in the spirit of several recent articles [3, 7, 10, 18, 20, 24, 25, 36]. However, there is a fundamental difference between the method presented here and those studied in [3, 7, 10, 18, 20, 24, 25, 36]. This difference has a profound impact on the methodology applied in this article. All previous work on this topic (except [38]) applies exclusively to monotone operators that arise as the subdifferential of a finite-valued, finite-dimensional convex function. The results of this article apply to general monotone operators on a Hilbert space. The resulting difference in methodology roughly corresponding to the difference between methods for function minimization and methods for solving systems of equations.

There are both advantages and disadvantages to the more general approach. The advantages are that the method applies to a much broader class of problems. This is so not only because the theory is developed in the Hilbert space setting, but, more importantly, because many monotone operators cannot be represented as the subdifferential of a finite-valued, finite-dimensional convex function. General monotone operators do not possess many of the rich structural properties associated with the subdifferential of a convex function (e.g., subdifferentials of convex functions are the only maximal cyclically monotone operators [33]). In addition, in the case where the operator is the subdifferential of a convex function, we do not require the usual assumption that the underlying function be finite-valued.

The disadvantages of our general approach arise from the fact that the method cannot make use of the additional structure present when the operator is the subdifferential of a convex function. This complicates both the structure of the method and its analysis. Of particular note in this regard is the complexity of our global convergence result. If the operator is the subdifferential of a convex function, then solving the inclusion $0 \in T(x)$ is equivalent to minimizing the underlying convex function. The global convergence of a method is then typically driven by a line-search routine (e.g., see [3, 7, 10, 18, 20, 24, 25, 36]). In the general setting we do not have direct recourse to this strategy. This complicates both the structure of the algorithm and its convergence theory. Nonetheless, the proof technique developed in this paper can be refined in the convex programming setting, thereby significantly simplifying both the global and local convergence results [5, 6].

Notwithstanding these differences in methodology, our approach is still nicely motivated by recalling the behavior of the PPA in the context of convex programming:

$$
\min _ {z \in \mathcal {H}} f (z), \tag {1}
$$

where $\mathcal{H}$ is a Hilbert space and $f\colon\mathcal{H}\mapsto\mathbb{R}\cup\{+\infty\}$ is a lower semi-continuous convex function that is not identically $+\infty$. Define the Moreau-Yosida regularization of $f$ to be the function $f_{\lambda}\colon\mathcal{H}\mapsto\mathbb{R}$ given by

$$
f _ {\lambda} (\bar {z}) := \min _ {z \in \mathcal {H}} \{\lambda f (z) + \frac {1}{2} \| z - \bar {z} \| ^ {2} \}.
$$

The set of solutions to (1) corresponds precisely to the set of points at which $f_{\lambda}$ attains its minimum value. The function $f_{\lambda}$ is continuously Fréchet differentiable [28, Proposition 7.d]. The PPA applied to (1) is approximately the steepest descent algorithm applied to $f_{\lambda}$ [11]. This analogy immediately suggests that a variable metric approach could be applied to the function $f_{\lambda}$ to accelerate the method. This idea was first studied in [38] and is the basis of the acceleration techniques described in [3, 7, 10, 18, 20, 24, 25, 36].

In [3], Bonnans, Gilbert, Lemaréchal, and Sagastizábal develop methods along an algorithmic pattern originally suggested by Qian in [38]. This pattern circumvents many of the difficulties associated with a variable metric approach applied directly to the function $f_{\lambda}$. The key is to employ a matrix secant update based on the function $f$ instead of $f_{\lambda}$. The local convergence results in [3, Section 3] require some smoothness assumptions. In particular, linear convergence is established when the function $f$ is differentiable with Lipschitz continuous derivative, and super-linear convergence is established when $f$ is twice strictly Fréchet differentiable at a unique solution $\bar{z}$ where the second derivative is positive definite (we only speak of quotient or q-rate of convergence).

In [18, 20, 24, 25], the authors apply the bundle concept for nonsmooth convex minimization [17] to approximate the Moreau–Yosida regularization $f_{\lambda}$ and its derivative. Variable metric updates, in particular, quasi–Newton updates, are then applied using these approximate values. The super-linear convergence results in the papers [18, 20, 24] either require strong smoothness assumptions on the function $f$ (such as the Lipschitz continuity of $\nabla f$ ) or that the regularization parameter $\lambda$ diverges to $+\infty$. In [20], Lemaréchal, and Sagastizábal propose a clever reversal quasi–Newton formula which uses the value of the gradient of $f_{\lambda}$ at a variety of points other than those strictly obtained by the iterates. This promising idea deserves further theoretical and numerical study.

In [10] and [36], the authors develop an approach based on Newton's method for semi-smooth functions as developed in [30, 31, 37, 34]. Properly speaking, these methods are neither an adaptation of the PPA algorithm nor a variable metric method. Nonetheless, the flavor of both these methodologies are present. In order to obtain super-linear convergence, smoothness hypotheses are again required, however, these hypotheses are of a somewhat more technical nature. Specifically, it is required that

(a) the function $f$ be semi-smooth at a unique solution to (1) [37],  
(b) every element of the set-valued mapping

$$
\partial_ {B} ^ {2} f (z) := \{\lim _ {y _ {k} \to z} \nabla^ {2} f _ {\lambda} (y _ {k}): y _ {k} \to z, \nabla f (y _ {k}) \text {exists for all} k = 1, 2, \ldots \}
$$

is nonsingular at the unique solution $\bar{z}$, and

(c) the sequence of Hessian approximates $\{V_k\}$ used to generate the iterates $\{z_k\}$ must satisfy

$$
\lim _ {k \to \infty} \mathrm{dist} \left(V _ {k}, \partial_ {B} ^ {2} f (z _ {k})\right) = 0 . \tag {2}
$$

One can show that the semi-smoothness hypotheses is satisfied in many cases of interest when $f$ is finite-valued. Moreover, by Rademacher's theorem on the differentiability of Lipschitz continuous functions, it follows that the set-valued mapping $\partial_B^2 f(z)$ is always well-defined and compact-valued in the finite dimensional, finite-valued case with the non-singularity property being closely tied to the usual hypothesis of strong convexity. Although the limiting hypotheses on the $V_k$ 's is a bit strong, it is not entirely unreasonable in the absence of differentiability. In [36], Chen and Qi propose a very nice preconditioning technique wherein an exact value for the gradient of a shifted Moreau-Yosida regularization can be computed from inexact values for the gradient of $f_\lambda$. This technique is similar in spirit to the reversal quasi-Newton formula found in [20]. Both of these techniques should prove useful in numerical implementations.

The algorithm presented in this paper is most closely related to the methods proposed by Chen and Fukushima [7] and Mifflin, Sun, and Qi [25]. However, there are several fundamental distinctions. The foremost of which is that the methods in [7, 25] are restricted to finite dimensional finite-valued convex programming problems. Within this framework, these authors use bundle strategies to approximate $f_{\lambda}$ and its gradient and establish the global convergence of their methods with the aid of a line search routine. Chen and Fukushima establish global and linear convergence results along with a generalization of the Dennis-Moré characterization theorem for super-linear convergence [14]. One of the most important features of the Chen-Fukushima algorithm is that the line search is based on the function $f$ rather than approximations to the function $f_{\lambda}$. This is very important in practise since obtaining sufficiently accurate approximations to the function $f_{\lambda}$ is usually quite time consuming. Their linear and super-linear convergence results blend bundle techniques with the theory of nonsmooth equations. Consequently, the convergence hypotheses are reminiscent of those employed in [10] and [36], in particular, they require semi-smoothness, CD-regularity, and the strong approximation property (2). In [6], the methods of this paper are applied to the Chen-Fukushima algorithm to obtain the super-linear convergence of the method when BFGS matrix secant updating is employed.

In [25], Mifflin, Sun, and Qi obtain the first super-linear convergence result for a variable metric proximal point algorithm using the BFGS matrix secant update in the setting of finite dimensional finite-valued convex programming. Their proposed algorithm uses a line search based on approximations to the function $f_{\lambda}$ and requires that the function $f_{\lambda}$ is strongly convex with $\nabla f_{\lambda}$ Fréchet differentiable at the unique global solution to the convex program. In addition it is assumed that the iterates satisfy a certain approximation property involving the gradient $\nabla f_{\lambda}$. In Section 4 of this paper, we discuss how these hypotheses are related to those that are also required in our convergence analysis.

In this paper, we provide a general theory for a variable metric proximal point algorithm (VMPPA) applied to maximal monotone operators from a Hilbert space to itself. In the important special case of convex programming, where $T$ is taken to be the subdifferential of the function $f$, we do not assume that $f$ is finite-valued or differentiable on the whole space.

However, to obtain super-linear convergence, we do require certain smoothness hypotheses at a unique global solution $\bar{z}$. These smoothness hypotheses differ from those assumed in [3, 18, 20, 24] since they are imposed on the operator $T^{-1}$ rather than $T$. In this regard, they are reminiscent of the hypotheses employed in [25]. The choice of smoothness hypotheses has deep significance in the context of convex programming. Differentiability hypotheses on $T = \partial f$ imply the second-order differentiability of $f$, whereas differentiability hypotheses on $T^{-1} = (\partial f)^{-1}$ are related to the standard strong second-order sufficiency conditions of convex programming [40, Proposition 2] and thus reduce to the standard hypotheses used in local analysis of convergence. In particular, the differentiability of $(\partial f)^{-1}$ does not imply that $\partial f$ is single-valued or differentiable nor does it imply that $f$ is finite-valued.

Our smoothness hypotheses also differ from those that appear in [7, 10, 36]. These methods rely on the theory of nonsmooth equations and require hypotheses such as semi-smoothness and non-singularity of the elements of $\partial_B^2 f$. In addition, the proof theory for these methods specifically requires that the underlying convex function be finite-valued in a neighborhood of the unique solution to (1) (again, these methods assume that the function is finite-valued on all of $\mathbb{R}^n$ ). This limits direct application to constrained problems since in the constrained case solutions typically lie on the boundary of the constraint region (i.e., on the boundary of the domain of the essential objective function).

Throughout the paper we illustrate many of the ideas and results by applying them to the case of convex programming. Our purpose here is not only to show how the results can be applied, but also to ground them in the familiar surroundings of this concrete application. Further details on the application of these results to the case of convex programming can be found in $[5]$.

The paper is structured as follows. We begin with a review of the classic proximal point algorithm in §2. The VMPPA is introduced in §3. This section contains the approximation criteria that must be satisfied at each iteration. Two criteria are presented. The first is required to obtain global convergence and the second is required to accelerate the local convergence of the method. This division into global and local criteria is one of the recurring themes of the paper. On the global level the method behaves like a steepest descent method while at the local level it becomes more Newton like. This feature is common to most general purpose methods in nonlinear programming such as the non-monotone descent methods, the dogleg method, and trust-region methods. In §4 we discuss the smoothness hypotheses required for the local analysis. We also extend some of the differentiability results appearing in [19, 35] to maximal monotone operators. In §5, we study the operators $\mathcal{N}_k$ associated with the Newton-like iteration proposed in §3. The focus of this section is to provide conditions under which the operators $\mathcal{N}_k$ are non-expansive at a solution to the inclusion $0 \in T(z)$. A global convergence result paralleling Rockafellar's 1976 result [41] is given in §6. In §7 we study local convergence rates. Linear convergence is established under a Lipschitz continuity assumption on $T^{-1}$, and a characterization of super-linear convergence for the VMPPA is also given. This characterization is modeled on the landmark characterization of super-linear convergence of variable metric methods in nonlinear programming due to Dennis and Moré [14]. In [6], we use this characterization result to establish the super-linear convergence of the method when the derivatives are approximated using the BFGS and Broyden updating strategies.

A word about our notation is in order. We denote the closed unit ball in the Hilbert space $\mathcal{H}$ by $\mathbb{B}$ . Then the ball with center $a$ and radius $r$ is denoted by $a + r\mathbb{B}$ . Given a set $Z \subset \mathcal{H}$ and an element $z \in \mathcal{H}$ , the distance of $z$ to $Z$ is $\text{dist}(z, Z) = \inf\{\|z - z'\| : z' \in Z\}$ .

Let $\mathcal{H}_1$ and $\mathcal{H}_2$ be two Hilbert spaces. Given a multi-function (also referred to as a mapping or an operator depending on the context) $T: \mathcal{H}_1 \rightrightarrows \mathcal{H}_2$, the $graph$ of $T$, $\mathrm{gph} T$ , is the subset of the product space $\mathcal{H}_1 \times \mathcal{H}_2$ defined by $\mathrm{gph} T = \{(z, w) \in \mathcal{H}_1 \times \mathcal{H}_2 | w \in T(z)\}$. The $domain$ of $T$ is the set $\mathrm{dom} T := \{z \in \mathcal{H}_1 | T(z) \neq \emptyset\}$. The identity mapping will be denoted by $I$. The $inverse$ of an operator $T$ is defined by $T^{-1}(w) := \{z \in \mathcal{H}_1 | (z, w) \in \mathrm{gph} T\}$.

Given a lower semi-continuous convex function $f: \mathcal{H} \to \mathbb{R} \cup \{+\infty\}$, the conjugate of $f$ is defined by $f^{*}(z^{*}) = \sup_{z \in \mathcal{H}} \{\langle z^{*}, z \rangle - f(z)\}$.

# 2 Monotone Operators and the Classic Algorithm

Given a real Hilbert space $\mathcal{H}$ with inner product $\langle\cdot,\cdot\rangle$, we say that the multi-function $T:\mathcal{H}\rightrightarrows\mathcal{H}$ is monotone if for every $z$ and $z'$ in $\operatorname{dom} T$, and $w\in T(z)$ and $w'\in T(z')$, we have $\langle z-z',w-w'\rangle\geq\kappa\|z-z'\|^2$ for some $\kappa\geq0$. If $\kappa>0$, then $T$ is said to be strongly monotone with modulus $\kappa$. The monotone operator $T$ is said to be maximal if its graph is not properly contained in the graph of any other monotone operator. An important example of a monotone operator is the subgradient of a convex function (see Minty [27] and Moreau [28]).

We are concerned with solving inclusions of the form

$$
0 \in T (z) \tag {3}
$$

where $T$ is a maximal monotone operator. In the case of the convex programming problem (1), the operator $T$ is the subdifferential of the convex function $f$ and the inclusion (3) characterizes the points $z$ at which $f$ attains its minimum value. A wide variety of other problems can be cast in this framework, e.g. variational inequalities, complementary problems, and mini-max problems. Existence results for inclusion (3) can be found in [41].

In 1962, Minty [27] showed that, when the operator T is maximal monotone, the Moreau-Yosida Resolvent of T,

$$
P _ {\lambda} = (I + \lambda T) ^ {- 1} \text {with} \lambda > 0,
$$

is single-valued and non-expansive on $\mathcal{H}$. This result suggests that a solution to the inclusion $0 \in T(z)$ can be iteratively approximated by the recursion $z^{k+1} = P_{\lambda}(z^k)$. One can modify this scheme by varying the scalar $\lambda$ and by choosing the iterates $z^{k+1}$ to be an approximate solution to the equation $(I + \lambda_k T)(z) = z^k$. The proximal point algorithm applies precisely these ideas. The algorithm, starting from any point $z^0$, generates a sequence $\{z^k\}$ in $\mathcal{H}$ by the approximation rule

$$
z ^ {k + 1} \approx (I + c _ {k} T) ^ {- 1} \left(z ^ {k}\right). \tag {4}
$$

The principle difficulty in applying the proximal point algorithm lies in executing the operators $P_{k} = (I + c_{k}T)^{-1}$. In the case of convex programming, the iteration (4) reduces

to the iteration

$$
z ^ {k + 1} \approx \arg \min _ {z \in \mathcal {H}} \{c _ {k} f (z) + \frac {1}{2} \| z - z ^ {k} \| ^ {2} \}.
$$

Notice that executing the algorithm exactly (i.e., with “=” instead of “≈” in the above algorithm) can be as difficult as solving the original problem directly. Hence it is critical that the convergence results are obtained under the assumption of approximation.

In [22] and [23], Martinet proved the convergence of the exact proximal point algorithm for certain cases of the operator T with fixed $c_{k} \equiv c$. The first theorem on the convergence of the general proximal point algorithm was proved by Rockafellar [41] in 1976. His theorem not only insures the global convergence under an approximating rule, but also describes the global behavior when the inclusion $0 \in T(z)$ has no solution.

The convergence rate of the proximal point algorithm depends on properties of the operator $T$, the choice of the sequence $\{c_k\}$, and the accuracy of the approximation in (4). The first rate of convergence results were also obtained by Rockafellar [41] in 1976, under the assumption that the solution set is a singleton $\{\bar{z}\}$. He proved that if the sequence $\{c_k\}$ is bounded away from 0, and $T^{-1}(w)$ is bounded by a linear function of $\| w \|$ when $w$ is near 0, then the rate of convergence is at least linear. Luque [21] extended Rockafellar's theorem to the case where $T^{-1}(0)$ is not required to be a singleton, and showed that such an estimate of the convergence rate is tight.

# 3 The Algorithm and Approximation Criteria

The algorithm proposed in this section is a Newton-like iteration for solving the resolvent equation $z = P_{\lambda}(z)$. In the context of the convex programming problem, the iteration takes the form

$$
z ^ {k + 1} = z ^ {k} - H _ {k} \nabla f _ {\lambda} (z ^ {k}),
$$

where the operator $H_{k}$ is used to approximate second-order properties of the function $f_{\lambda}$. If $f_{\lambda}$ is twice differentiable with $[\nabla^2 f_\lambda (z^k)]^{-1}$ bounded, then for Newton's method one sets $H_{k} = [\nabla^{2}f_{\lambda}(z^{k})]^{-1}$. However, in general, $f_{\lambda}$ is only known to be differentiable with Lipschitz continuous gradient [28]. Thus, in the finite dimensional case, the Hessian $\nabla^2 f_{\lambda}(x)$ is only guaranteed to exist on a dense subset by Rademacher's Theorem. Further results on the second-order properties of $f_{\lambda}$ can be found in [19, 35, 42].

It is well known that the negative gradient $-\nabla f_{\lambda}(z^{k})$ is the unique element $w^{k}$ solving the problem

$$
\min _ {w \in \mathcal {H}} \{\lambda f (z ^ {k} + w) + \frac {1}{2} \| w \| ^ {2} \},
$$

or equivalently, satisfying the inclusion

$$
0 \in \lambda \partial f (z ^ {k} + w ^ {k}) + w ^ {k}. \tag {5}
$$

The proximal point algorithm for a general maximal monotone operator T can be formally derived from equation (5) by replacing $\lambda$, $z^{k}$, and $\partial f$ by $c_{k}$, $z^{k}$, and T respectively, to obtain

$$
0 \in c _ {k} T (z ^ {k} + w ^ {k}) + w ^ {k},
$$

or equivalently,

$$
w ^ {k} = [ (I + c _ {k} T) ^ {- 1} - I ] (z ^ {k}) ,
$$

where equality follows from the fact that $w^k$ is unique. This motivates us to define the operator

$$
D _ {k} := (I + c _ {k} T) ^ {- 1} - I. \tag {6}
$$

This operator provides the analog of the direction of steepest descent in the operator setting.

The algorithm we propose for solving the inclusion $0 \in T(z)$ can be succinctly stated as follows:

# The Variable Metric Proximal Point Algorithm:

Let $z^0 \in \mathcal{H}$ and $c_0 \geq 1$ be given. Having $z^k$, set

$$
z ^ {k + 1} := z ^ {k} + H _ {k} w ^ {k} \quad \text {where} \quad w ^ {k} \approx D _ {k} (z ^ {k})
$$

and choose $c_{k + 1}\geq 1$

As mentioned in the previous section, it is critical that the convergence results are obtained under the assumption that $D_{k}(z^{k})$ can only be approximated. We use the following approximation criteria:

$$
(\mathcal {G}) \qquad \| w ^ {k} - D _ {k} (z ^ {k}) \| \leq \min \{1, \frac {1}{\| H _ {k} \|} \} \epsilon_ {k} \text {with} \sum_ {k = 0} ^ {\infty} \epsilon_ {k} <   \infty
$$

and

$$
(\mathcal {L}) \quad \| w ^ {k} - D _ {k} (z ^ {k}) \| \leq \delta_ {k} \| w ^ {k} \| \text {with} \lim _ {k \to \infty} \delta_ {k} = 0.
$$

The approximation criteria $(\mathcal{G})$ is used to establish global convergence properties, while criteria $(\mathcal{L})$ is used to obtain local rates of convergence.

Although these criteria are used in the proof of convergence, they are impractical from the perspective of implementation. In their stead, we provide criteria that are implementable. To obtain these criteria we recall the following result from Rockafellar [41].

Proposition 1 [41, Proposition 3] Let $S_{k}(w) := T(z^{k} + w) + \frac{1}{c_{k}} w$. Then $0 \in S_{k}(w^{k}) \Leftrightarrow w^{k} = D_{k}(z^{k})$. Moreover, for all $w \in \mathcal{H}$ we have the bound

$$
\| w - D _ {k} (z ^ {k}) \| \leq c _ {k} \mathrm{dist} (0, S _ {k} (w)). \tag {7}
$$

Proposition 1 yields the following alternative approximation criteria for the $w^k$ 's. Since this result is an immediate consequence of Proposition 1, its proof is omitted.

Proposition 2 Consider the following acceptance criteria for the $w^k$ 's:

$$
\begin{array}{l} (\mathcal {G} ^ {\prime}) \quad \operatorname{dist} \left(0, S _ {k} (w ^ {k})\right) \leq \min \left\{1, \frac {1}{\| H _ {k} \|} \right\} \frac {\epsilon_ {k}}{c _ {k}} \quad \text {with} \quad \sum_ {k = 0} ^ {\infty} \epsilon_ {k} <   \infty \quad \text {and} \\ (\mathcal {L} ^ {\prime}) \quad \operatorname{dist} \left(0, S _ {k} \left(w ^ {k}\right)\right) \leq \frac {\delta_ {k}}{c _ {k}} \| w ^ {k} \| \quad \text {with} \quad \lim _ {k \rightarrow \infty} \delta_ {k} = 0. \\ \end{array}
$$

We have $(\mathcal{G}')$ implies $(\mathcal{G})$ and $(\mathcal{L}')$ implies $(\mathcal{L})$ .

Remark Note that to satisfy either $(\mathcal{G}')$ or $(\mathcal{L}')$ it is not necessary to find an element of $S_{k}(w^{k})$ of least norm.

Before leaving this section we recall from [41] a few properties of the operators $D_{k}$ and $P_{k} := D_{k} + I$ that are essential in the analysis to follow.

Proposition 3 [41, Proposition 1]

a) The operator $D_{k}$ can be expressed as

$$
D _ {k} = - (I + T ^ {- 1} \frac {1}{c _ {k}}) ^ {- 1} \tag {8}
$$

and for any $z \in \mathcal{H}$, $-\frac{1}{c_k} D_k(z) \in T(P_k(z))$.

b) For any $z, z' \in \mathcal{H}$, $\langle P_k(z) - P_k(z'), D_k(z) - D_k(z') \rangle \leq 0$.  
c) For any $z, z' \in \mathcal{H}$, $\| P_k(z) - P_k(z')\|^2 + \| D_k(z) - D_k(z')\|^2 \leq \| z - z'\|^2$.

Remark An important consequence of Part c) above is that the operators $P_{k}$ and $D_{k}$ are Lipschitz continuous with Lipschitz constant 1, that is, they are non-expansive. Henceforth, we make free use of this fact.

# 4 On the Differentiability of $T^{-1}$ and $D_{k}$

Just as Newton's method for minimization locates roots of the gradient, one can view the variable metric proximal point algorithm as a Newton-like method for locating roots of the operator $D_{k}$. This perspective motivates our approach to the local convergence analysis. For this analysis, we require that the operator $T^{-1}$ possesses certain smoothness properties. These properties in turn imply the smoothness of the operators $D_{k}$. Smoothness hypotheses are used in the convergence analysis in much the same way as they are used in the convergence analysis for Newton's method. For example, recall that to ensure the quadratic convergence of Newton's method one requires the derivative at a solution to be both locally Lipschitz and non-singular. Non-singularity insures that the iterates are well defined and can be bounded, while the Lipschitzian hypothesis guarantees that the error in the linearization is quadratically bounded (see [29, 3.2.12 and 10.2.2]). We make use of similar properties in our analysis.

In order to discuss the smoothness of $T^{-1}$ and $D_{k}$, we recall various notions of differentiability for multi-valued functions from the literature. For a more thorough treatment of these ideas in the context of monotone operators, we refer the reader to [1, 19, 26, 35, 42].

Definition 4 We say that an operator $\Psi : \mathcal{H} \rightrightarrows \mathcal{H}$ is Lipschitz continuous at a point $\bar{w}$ (with modulus $\alpha \geq 0$ ) if the set $\Psi(\bar{w})$ is nonempty and there is a $\tau > 0$ such that

$$
\Psi (w) \subset \Psi (\bar {w}) + \alpha \| w - \bar {w} \| \mathbb {B} \quad \text {whenever} \| w - \bar {w} \| \leq \tau .
$$

We say that $\Psi$ is differentiable at a point $\bar{w}$ if $\Psi (\bar{w})$ consists of a single element $\bar{z}$ and there is a continuous linear transformation $J:\mathcal{H}\to \mathcal{H}$ such that for some $\delta >0$,

$$
\emptyset \neq \Psi (w) - \bar {z} - J (w - \bar {w}) \subset o (\| w - \bar {w} \|) \mathbb {B} \quad \text {whenever} \| w - \bar {w} \| \leq \delta .
$$

We then write $J = \nabla \Psi(\bar{w})$.

Remarks 1) These definitions of Lipschitz continuity and differentiability for multifunction are taken from [41, pages 885 and 887] (also see [2, page 41]). Note that these notions of Lipschitz continuity and differentiability correspond to the usual notions when $\Psi$ is single-valued.

2) Rockafellar [41, Theorem 2] was the first to use Lipschitz continuity to establish rates of convergence for the proximal point algorithm.  
3) When the set $\Psi(\bar{w})$ is restricted to be a singleton $\{\bar{z}\}$, the differentiability of $\Psi$ at $\bar{w}$ implies the Lipschitz continuity of $\Psi$ at $\bar{w}$. Moreover, one can take $\alpha(\tau) \to \|J\|$ as $\tau \to 0$. This observation is verified in [41, Proposition 4].  
4) It follows from the definition of monotonicity that if $T$ is a maximal monotone operator, then the operator $\nabla T(x)$ is positive semi-definite whenever it exists.

We now give a result that relates the differentiability of a multi-valued function to the differentiability of its inverse. The proof is omitted since it parallels the proof of a similar result for single-valued functions.

Lemma 5 Assume that $\Psi : \mathcal{H} \rightrightarrows \mathcal{H}$ is differentiable at $\bar{z}$ with $\Psi(\bar{z}) = \{\bar{w}\}$ and $\nabla\Psi(\bar{z}) = J$ with $J^{-1}$ bounded. Also assume that $\Psi^{-1}$ is Lipschitz continuous at $\bar{w}$ with $\Psi^{-1}(\bar{w}) = \{\bar{z}\}$. Then $\Psi^{-1}$ is differentiable at $\bar{w}$ with $\nabla\Psi^{-1}(\bar{w}) = J^{-1}$.

In the two examples that follow, we examine the concepts introduced in Definition 4 when the operator in question is the subdifferential of a convex function. The first example illustrates that $\partial f^{-1}$ can be Lipschitz continuous but not differentiable at the origin, while in the second example $\partial f^{-1}$ is differentiable at the origin but $\partial f$ is not differentiable on $(\partial f)^{-1}(0)$.

Example 6 Let

$$
f (z) := \left\{ \begin{array}{l l} 0 & \text {if } z <   0 \\ z & \text {if } z \geq 0 \end{array} \right. \quad \text {and} \quad T (z) := \partial f (z) = \left\{ \begin{array}{l l} 0 & \text {if } z <   0 \\ [ 0, 1 ] & \text {if } z = 0 \\ 1 & \text {if } z > 0 \end{array} \right..
$$

$$
\text {Then} \quad T ^ {- 1} (y) = \left\{ \begin{array}{l l} \emptyset & \text {if y <   0 or y > 1} \\ (- \infty , 0 ] & \text {if y = 0} \\ \{0 \} & \text {if y\in(0,1)} \\ [ 0, \infty) & \text {if y = 1 .} \end{array} \right.
$$

$T^{-1}$ is Lipschitz continuous at 0 but is not differentiable at 0.

Example 7 Let

$$
\begin{array}{l} f (z) := \left\{ \begin{array}{l l} - z & \text {if } z <   0 \\ z ^ {5 / 3} & \text {if } z \geq 0 \end{array} \right. \quad \text {and} \quad T (z) := \partial f (z) = \left\{ \begin{array}{l l} - 1 & \text {if } z <   0 \\ [ - 1, 0 ] & \text {if } z = 0 \\ \frac {5}{3} z ^ {2 / 3} & \text {if } z > 0 \end{array} \right.. \\ \text {Then} \quad T ^ {- 1} (y) = \left\{ \begin{array}{l l} \emptyset & \text {if } y <   - 1} \\ (- \infty , 0 ] & \text {if } y = -1} \\ \{0 \} & \text {if } y\in(-1,0)} \\ \left(\frac {3}{5} y\right) ^ {3 / 2} & \text {if } y\geq 0}. \end{array} \ri
$$

$T^{-1}$ is differentiable at 0 with $J = 0$ but $T$ is not differentiable on $T^{-1}(0)$.

The super-linear convergence result of §7 requires the assumption that the operator $T^{-1}$ be differentiable at the origin. Although this is a severe restriction on the applicability of these results, it turns out that in the case of convex programming it is a consequence of the standard second-order sufficiency conditions for constrained mathematical programs. This and related results were established by Rockafellar in [40, Proposition 2]. In this context, it is important to note that the second-order sufficiency condition is the standard hypothesis used in the mathematical programming literature to insure the rapid local convergence of numerical methods. So, at least in the context of constrained convex programming, such a differentiability hypothesis is not as severe an assumption as one might at first suspect. To the contrary, it is a bit weaker than the standard hypothesis employed for such results. For the sake of completeness, we recall a portion of Rockafellar's result below.

Theorem 8 Consider the convex programming problem (1) where $f: \mathbb{R}^n \to \mathbb{R} \cup \{\infty\}$ is given by

$$
f (z) = \left\{ \begin{array}{l l} f _ {0} (z) & \text {if} f _ {i} (z) \leq 0 \text {for} i = 1, 2, \dots , m \\ + \infty & \text {otherwise}, \end{array} \right.
$$

with $f_{i} : \mathbb{R}^{n} \to \mathbb{R}$ convex for $i = 0,1,\dots,m$. Suppose that the following conditions are satisfied:

(i) The functions $f_{i}$ for $i = 0,1,\ldots ,m$ are $k\geq 2$ times continuously differentiable in a neighborhood of a point $\bar{z}\in \mathbb{R}^n$.  
(ii) There is a Kuhn-Tucker vector $\bar{y} \in \mathbb{R}^m$ for $\bar{z}$ such that $\bar{y}_i > 0$ for $i \in I(\bar{z}) = \{i : f_i(\bar{z}) = 0, i = 1,2,\dots,m\}$.  
(iii) The gradients $\{\nabla f_i(\bar{z}):i\in I(\bar{z})\}$ are linearly independent.  
(iv) The matrix $H = \nabla^2 f_0(\bar{z}) + \sum_{i=1}^{m} \bar{y}_i \nabla^2 f_i(\bar{z})$ satisfies $u^T Hu > 0$ for every non-zero $u \in \mathbb{R}^n$ such that $\nabla f_0(\bar{z})^T u = 0$, and $\nabla f_i(\bar{z})^T u = 0$ for $i \in I(\bar{z})$.

Then the operator $\partial f^{-1}$ is $(k - 1)$ times continuously differentiable in a neighborhood of the origin.

Remark Theorem 8 follows by applying the implicit function theorem to the Kuhn-Tucker conditions for the parameterized problems $\min \{f(z) - \langle w,z\rangle \}$ in a neighborhood of $w = 0$. The relationship to $\partial f^{-1}$ comes from the fact that $\partial f^{-1}(w) = \arg \min \{f(z) - \langle w,z\rangle \}$. Rockafellar only establishes the result for $k = 2$. The extension to $k > 2$ follows trivially from the implicit function theorem.

We now examine the differentiability properties of the mapping $D_{k}$. Two results in this direction are given. The first uses equation (8) to relate the differentiability of the operators $T^{-1}$ and $D_{k}$, while the second uses the definition of $D_{k}$ given in (6) to relate the differentiability of the operators T and $D_{k}$.

Proposition 9 Let $T:\mathcal{H}\Rightarrow \mathcal{H}$ be maximal monotone and $\lambda >0$. Define

$$
D (z) = - (I + T ^ {- 1} \frac {1}{\lambda}) ^ {- 1} (z). \tag {9}
$$

Let $\bar{z} \in \mathcal{H}$ and set $\bar{w} = D(\bar{z})$ and $\bar{y} = -\frac{1}{\lambda}\bar{w}$. The operator $T^{-1}$ is differentiable at $\bar{y}$ with $[I + \frac{1}{\lambda}\nabla (T^{-1})(\bar{y})]^{-1}$ bounded if and only if the operator $D$ is differentiable at $\bar{z}$ with $(\nabla D(\bar{z}))^{-1}$ bounded. In either case, we have

$$
\nabla D (\bar {z}) = - \left[ I + \frac {1}{\lambda} \nabla \left(T ^ {- 1}\right) (\bar {y}) \right] ^ {- 1}. \tag {10}
$$

Proof First assume that $T^{-1}$ is differentiable at $\bar{y}$ with $\nabla(T^{-1})(\bar{y})$ bounded. The differentiability of $T^{-1}$ at $\bar{y}$ clearly implies that of $D^{-1}$ at $\bar{w}$ with

$$
\nabla [ D ^ {- 1} ] (\bar {w}) = - \big (I + \frac {1}{\lambda} \nabla [ T ^ {- 1} ] (\bar {y}) \big) .
$$

Since $D$ is Lipschitzian with $D(\bar{z}) = \bar{w}$, Lemma 5 implies that $D$ is differentiable at $\bar{z}$ with derivative given by (10). Since $\nabla[D^{-1}](\bar{w}) = (\nabla D(\bar{z}))^{-1}$, we conclude that the latter is bounded.

Conversely, assume that $D$ is differentiable at $\bar{z}$ with $(\nabla D(\bar{z}))^{-1}$ bounded. We show that $D^{-1}$ is single-valued and Lipschitzian at $\bar{w}$. The result will then follow from Lemma 5.

Let $\delta > 0$ be as in Definition 4 for $\nabla D(\bar{z})$. Since $D$ is single-valued and $\nabla D(\bar{z})$ surjective (it is invertible), we may apply a standard open mapping result from functional analysis (e.g. [8, Theorem 15.5]) to obtain the existence of a $\rho > 0$ and a $0 < \hat{\delta} < \delta$ such that

$$
\bar {w} + \rho \mathbb {B} \subset D (\bar {z} + \hat {\delta} \mathbb {B}). \tag {11}
$$

Hence for each $w \in \bar{w} + \rho IB$ and $z \in D^{-1}(w) \cap (\bar{z} + \hat{\delta} IB) \neq \emptyset$ we have

$$
w = \bar {w} + \nabla D (\bar {z}) (z - \bar {z}) + o (\| z - \bar {z} \|). \tag {12}
$$

Since $(\nabla D(\bar{z}))^{-1}$ is bounded, there is a $\kappa > 0$ such that

$$
\| w - \bar {w} \| + o (\| z - \bar {z} \|) = \| \nabla D (\bar {z}) (z - \bar {z}) \| \geq \kappa \| z - \bar {z} \|\mathrm{.}
$$

Hence, by reducing $\rho$ and $\hat{\delta}$ if necessary, we may assume that

$$
\| w - \bar {w} \| \geq \frac {\kappa}{2} \| z - \bar {z} \| \geq \frac {\kappa}{2} \| w - \bar {w} \|
$$

for $w \in \bar{w} + \rho IB$, where the second inequality follows since D is non-expansive. Therefore, we can assume that $o(\|z - \bar{z}\|) = o(\|w - \bar{w}\|)$ for all $w \in \bar{w} + \rho IB$ and $z \in D^{-1}(w) \cap (\bar{z} + \hat{\delta} IB)$. By substituting this into (12) and re-arranging, we obtain

$$
z = \bar {z} + (\nabla D (\bar {z})) ^ {- 1} (w - \bar {w}) + o (\| w - \bar {w} \|), \forall w \in \bar {w} + \rho \mathbb {B} \text {and} z \in D ^ {- 1} (w) \cap (\bar {z} + \hat {\delta} \mathbb {B}). (13)
$$

We now show that (13) implies the existence of an $\epsilon > 0$ such that $D^{-1}(\bar{w} + \epsilon IB) \subset \bar{z} + \hat{\delta} IB$. Indeed, if there were not the case, then there would exist sequences $\{w_i\}$ and $\{z_i\}$ such that $z_i \in D^{-1}(w_i)$, $\|z_i - \bar{z}\| > \hat{\delta}$, and $w_i \to \bar{w}$. Since $D^{-1}$ is itself maximal monotone, its images are convex, hence, by (11), there exists a sequence $\{\hat{z}_i\}$ with $\hat{z}_i \in D^{-1}(w_i)$ and $\|\hat{z}_i - \bar{z}\| = \hat{\delta}$ for all $i = 1,2,\ldots$. But then (13) implies that

$$
\hat {z} _ {i} = \bar {z} + (\nabla D (\bar {z})) ^ {- 1} (w _ {i} - \bar {w}) + o (\| w _ {i} - \bar {w} \|)
$$

for all $i = 1,2,\ldots$. This contradicts the fact that $w_{i} \to \bar{w}$ and $\| \hat{z}_i - \bar{z} \| = \hat{\delta}$ for all $i = 1,2,\ldots$, and so such an $\epsilon > 0$ must exist. This fact combined with (13) implies that $D^{-1}$ is Lipschitzian at $\bar{w}$ with $D^{-1}(\bar{w}) = \{\bar{z}\}$. Lemma 5 now applies to yield the result.

Proposition 10 Let $D$ be defined as in (9). Let $\bar{z} \in \mathcal{H}$ and set $\bar{y} = (I + D)(\bar{z})$. The operator $T$ is differentiable at $\bar{y}$ with $[I + \lambda \nabla T(\bar{y})]^{-1}$ bounded if and only if the operator $D$ is differentiable at $\bar{z}$ with $[I + \nabla D(\bar{z})]^{-1}$ bounded. In either case we have the formula

$$
\nabla D (\bar {z}) = [ I + \lambda \nabla T (\bar {y}) ] ^ {- 1} - I.
$$

Proof Replace $D$ by $P := I + D = (I + \lambda T)^{-1}$ and observe that $D$ is differentiable at $\bar{z}$ with $[I + \nabla D(\bar{z})]^{-1}$ bounded if and only if $P$ is differentiable at $\bar{z}$ with $[\nabla P(\bar{z})]^{-1}$ bounded. The proof now follows the same argument as in the proof of Proposition 9 with $D$ replaced by $P$, $T^{-1}$ replaced by $T$ and $\bar{w}$ replaced by $\bar{y}$.

Propositions 9 and 10 say quite different things about the differentiability of $D_{k}$. To illustrate this difference, observe that in Example 7, the operator $T$ is not differentiable at 0, while $T^{-1}$ and $D$ are differentiable at 0. On the other hand, if we take $T = \partial f$ with $f(x) = |x|^3$, then $T^{-1}$ is not differentiable at 0, while $T$ and $D$ are differentiable at 0. It is also important to note that even if neither $T$ nor $T^{-1}$ is differentiable, $D$ may be differentiable. But, in this case, we know from Propositions 9 and 10, that if $D$ is differentiable and neither $T$ nor $T^{-1}$ is differentiable, then both $\nabla D(\bar{z})$ and $\nabla P(\bar{z})$ have to be singular or have unbounded inverses. For a further discussion of these issues in the context of finite dimensional convex programming see [35].

When $T$ is assumed to be the subdifferential of a convex function $f$, Propositions 9 and 10 can be refined by making use of the relation $\partial f^{-1} = \partial f^{*}$ where $f^{*}$ is the convex conjugate

of $f$ [39, Corollary 12A]. This allows us to extend [35, Theorem 1] and [35, Theorem 2] to the Hilbert space setting (also see [19, Theorem 3.1]). However, some caution in terminology is required since $f^{*}$ is not necessarily twice differentiable in the classical sense at points where $\partial f^{*}$ is differentiable in the sense of Definition 4. Indeed, $\partial f^{*}$ may be multi-valued arbitrarily close to a point of differentiability. The best way to interpret this result is through Alexandrov's Theorem [1] which states that at almost every point $\bar{z}$ in the interior of the domain of a convex function $f\colon \mathbb{R}^n\mapsto \mathbb{R}\cup \{\infty \}$ there is a quadratic function $q_{\bar{z}}$ such that $f(x) = q_{\bar{z}}(x) + o(\| x - \bar{z}\| ^2)$. In [19] and [35], the matrix $\nabla^2 q_{\bar{z}}$ is called a generalized Hessian and is denoted $Hf(x)$. Note that the existence of a generalized Hessian at the point $\bar{z}$ guarantees that $f$ is strictly differentiable at $\bar{z}$. Moreover, if $\partial f(x)$ is single-valued in a neighborhood of a point $\bar{z}$ at which $Hf(\bar{z})$ exists, then $\nabla^2 f(\bar{z})$ exists and equals $Hf(\bar{z})$. We extend this terminology to the Hilbert space setting with the following definition.

Definition 11 Let $\phi: \mathcal{H} \mapsto \mathbb{R} \cup \{\infty\}$ be a function on the Hilbert space $\mathcal{H}$. We say that $\phi$ is twice differentiable in the generalized sense at a point $\bar{z} \in \mathcal{H}$ if there is a continuous quadratic functional $q_{\bar{z}}$ such that $\phi(x) = q_{\bar{z}}(x) + o(\|x - \bar{z}\|^2)$. The operator $\nabla^2 q_{\bar{z}}$ is called a generalized Hessian of $\phi$ at $\bar{z}$ and is denoted by $H\phi(\bar{z})$.

With this terminology in hand, we apply Propositions 9 and 10 to the case of convex programming. The proofs of these results are not required since they are a direct translation of Propositions 9 and 10 into the terminology of convex programming.

Corollary 12 Let $f:\mathcal{H}\to\mathbb{R}\cup\{+\infty\}$ be lower semi-continuous and convex. Let $\bar{z}\in\mathcal{H}$ and set $\bar{w}=\nabla f_{\lambda}(\bar{z})$ and $\bar{y}=\frac{1}{\lambda}\bar{w}$. Then $f_{\lambda}$ is twice (Fréchet) differentiable at $\bar{z}$ with $[\nabla^{2}f_{\lambda}(\bar{z})]^{-1}$ bounded if and only if $f^{*}$ has a generalized Hessian at $\bar{y}$ with $[I+\frac{1}{\lambda}Hf^{*}(\bar{y})]^{-1}$ bounded. In either case we have

$$
\nabla^ {2} f _ {\lambda} (\bar {z}) = [ I + \frac {1}{\lambda} H f ^ {*} (\bar {y}) ] ^ {- 1}.
$$

Corollary 13 Let $f:\mathcal{H}\to\mathbb{R}\cup\{+\infty\}$ be lower semi-continuous and convex. Let $\bar{z}\in\mathcal{H}$ and set $\bar{y}=\bar{z}-\nabla f_{\lambda}(\bar{z})$. Then $f_{\lambda}$ is twice (Fréchet) differentiable at $\bar{z}$ with $[I+\nabla^{2}f_{\lambda}(\bar{z})]^{-1}$ bounded if and only if $f$ is twice differentiable in the generalized sense at $\bar{y}$ with $[I+\lambda Hf(\bar{y})]^{-1}$ bounded. In either case we have

$$
\nabla^ {2} f _ {\lambda} (\bar {z}) = I - [ I + \lambda H f (\bar {y}) ] ^ {- 1}.
$$

Remark As observed earlier, the generalized Hessian is necessarily positive semi-definite. This observation can be used to further refine the statement of Corollaries 12 and 13.

# 5 Newton Operators

In this section we study the operators associated with the variable metric proximal point iteration:

$$
\mathcal {N} _ {k} := I + H _ {k} D _ {k} = P _ {k} + \left(H _ {k} - I\right) D _ {k}. \tag {14}
$$

This notation emphasizes the fact that these operators produce Newton-like iterates. Just as in the case of the classical Newton's method for equation solving [29, §12.6], one of the keys to the convergence analysis is to show that these operators are contractive with respect to the solution set $T^{-1}(0)$. Clearly the operators $\mathcal{N}_k$ are single-valued. Moreover, fixed points of the operators $\mathcal{N}_k$ are solutions to the inclusion $0 \in T(z)$ since

$$
0 \in T (z) \Leftrightarrow P _ {k} (z) = z \Leftrightarrow D _ {k} (z) = 0 \Leftrightarrow \mathcal {N} _ {k} (z) = z.
$$

Thus, conditions that ensure that the operators $N_{k}$ are non-expansive with respect to $T^{-1}(0)$ are important for the global analysis of the variable metric proximal point iteration. To obtain this property, we impose the following conditions on the linear transformations $\{H_{k}\}$.

(H1) Each $H_{k}$ is a continuous linear transformation with continuous inverse.  
(H2) There is a nonempty closed bounded subset $\Gamma$ of $T^{-1}(0)$ such that

$$
\| (H _ {k} - I) D _ {k} (z ^ {k}) \| \leq \gamma_ {k} \| D _ {k} (z ^ {k}) \| \quad \text {for all} k,
$$

where

$$
\gamma_ {k} := \frac {\| D _ {k} (z ^ {k}) \|}{2 \sigma_ {k} + 3 \| D _ {k} (z ^ {k}) \|} \mathrm{with} \sigma_ {k} = \sup \{\| z ^ {k} - z \|: z \in \Gamma \}.
$$

Remark The set $\Gamma$ in (H2) is used to guarantee the boundedness of the sequence $\{z^k\}$. By taking $\Gamma = \{\bar{z}\}$, one can show that every weak cluster point of the sequence $\{z^k\}$ is an element of $T^{-1}(0)$. It was observed by Iusem [13] that if $T^{-1}(0)$ is bounded and one takes $\Gamma = T^{-1}(0)$, then the sequence $\{z^k\}$ has a weak limit $z^\infty \in T^{-1}(0)$ (see Theorem 17 and [41, Theorem 1]).

Hypothesis (H1) is standard and is automatically satisfied in the finite dimensional case. On the other hand, hypothesis (H2) is quite technical and requires careful examination. This hypothesis is problematic since it specifies that the matrices $H_{k}$ satisfy a condition that depends on the unknown values $\sigma_{k}$ and $\|D_{k}(z^{k})\|$. We will show that in certain cases it is possible to satisfy (H2) without direct knowledge of these unknown values. This is done in two steps. First it is shown in Lemma 14 that if $T^{-1}$ is Lipschitz continuous or differentiable at the origin, then $\gamma_{k}$ is bounded below by a positive constant (which can be taken to be 1/6 as $\|D_{k}(z^{k})\|$ approaches zero). Then, in Lemma 15, it is shown that (H2) is satisfied if a related condition in terms of $H_{k}$ and $w^{k}$ is satisfied. Taken together, these results imply that at least locally (H2) can be satisfied by checking a condition based on known quantities.

Further insight into hypothesis (H2) can be gained by considering the case in which $T^{-1}$ is differentiable at the origin. In this case $H_{k}$ is intended to approximate $-(\nabla D_k(0))^{-1} = (I + c_k^{-1}J)$ where $J = \nabla (T^{-1})(0)$ (by Proposition 9). Hence, if $H_{k}\approx -(\nabla D_{k}(0))^{-1}$, then $(H_{k} - I)\approx c_{k}^{-1}J$. Therefore, one can guarantee that (H2) is satisfied by choosing $c_{k}$ sufficiently large and $H_{k}\approx I$. This fact is used in [6] to establish the super-linear convergence of the method when the $H_{k}$ 's are obtained via matrix secant updating techniques.

The purpose of hypothesis (H2) is to globalize what is essentially a local algorithm (Newton's method). In the context of convex programming, one commonly obtains global convergence properties with the aid of a line search routine applied to the objective function $f$, or its regularization $f_{\lambda}$. However, in the operator setting there is no natural underlying objective function to which a line search can be applied. This is a key difference between the approach taken in this paper and those in [3, 7, 10, 18, 20, 24, 36]. In the convex programming setting, the global convergence of the VMPPA is driven by a line search routine applied to the objective function $f$ (or its regularization $f_{\lambda}$ ). In the operator setting, hypothesis (H2) replaces the line search and the associated hypotheses needed to make the line search strategy effective (such as the finite-valuedness of the objective function $f$ and the boundedness of the sequence $\{H_k\}$ ). On the other hand, when it is known that the operator $T$ is the subdifferential of a finite-valued finite dimensional convex function, then the algorithm of this paper can be modified to include the line search routine of Chen and Fukushima [7] thereby avoiding the need for hypothesis (H2) [6].

We now show three cases where the $\gamma_{k}$ 's are bounded away from zero.

Lemma 14 Suppose $T^{-1}(0)$ is nonempty.

(i) If the operator $T$ is strongly monotone with modulus $\kappa$, then $T^{-1}(0) = \{\bar{z}\}$,

$$
\| z ^ {k} - \bar {z} \| \leq (1 + \frac {1}{\kappa c _ {k}}) \| D _ {k} (z ^ {k}) \| ,
$$

and $\gamma_{k}\geq \frac{1}{5 + \frac{2}{\kappa c_{k}}}\geq \frac{1}{5 + 2 / \kappa}$ for all $k$

(ii) If the operator $T^{-1}$ is Lipschitz continuous at the origin with modulus $\alpha$, then

$$
\operatorname{dist} \left(z ^ {k}, T ^ {- 1} (0)\right) \leq \left(1 + \frac {\alpha}{c _ {k}}\right) \| D _ {k} \left(z ^ {k}\right) \|, \tag {15}
$$

for all $k$ such that $\| D_k(z^k)\| \leq \tau$ where $\tau$ is given in Definition 4. Moreover, if $T^{-1}(0) = \{\bar{z}\}$, then $\gamma_k \geq \frac{1}{5 + 2\alpha / c_k} \geq \frac{1}{5 + 2\alpha}$ for all $k$ such that $\| D_k(z^k)\| \leq \tau$.

(iii) If $T^{-1}$ is differentiable at the origin with derivative $J$, then $T^{-1}(0) = \{\bar{z}\}$, there is a $\delta > 0$ such that for all $k$ with $\| D_k(z^k)\| \leq \tau$ we have

$$
\| z ^ {k} - \bar {z} \| \leq (1 + \frac {\| J \|}{c _ {k}} + \sigma (\| D _ {k} (z ^ {k}) \|)) \| D _ {k} (z ^ {k}) \| ,
$$

and $\gamma_{k}\geq \frac{1}{5 + 2\frac{\|J\|}{c_k} + \sigma(||D_k(z^k)||)}$ for all $k$, where $\sigma (\tau)\to 0$ as $\tau \to 0$.

Proof (i) If $T$ is strongly monotone with modulus $\kappa$, then $\|z - z'\| \leq \frac{1}{\kappa}\|w - w'\|$ for any $z, z', w, w'$ such that $w \in T(z)$ and $w' \in T(z')$. That is, $T^{-1}$ is single-valued and Lipschitz continuous. Let $z = P_k(z^k)$ and $z' = \bar{z}$ where $\{\bar{z}\} = T^{-1}(0)$. By Proposition 3 (a) we have $-\frac{1}{c_k} D_k(z^k) \in T(P_k(z^k))$. Hence

$$
\| z ^ {k} - \bar {z} \| \leq \| z ^ {k} - P _ {k} (z ^ {k}) \| + \| P _ {k} (z ^ {k}) - \bar {z} \| \leq (1 + \frac {1}{\kappa c _ {k}}) \| D _ {k} (z ^ {k}) \|,
$$

since $D_{k} = P_{k} - I$. By the definition of $\gamma_{k}$,

$$
\gamma_ {k} = \frac {\| D _ {k} (z ^ {k}) \|}{2 \| z ^ {k} - \bar {z} \| + 3 \| D _ {k} (z ^ {k}) \|} \geq \frac {\| D _ {k} (z ^ {k}) \|}{2 (1 + \frac {1}{\kappa c _ {k}}) \| D _ {k} (z ^ {k}) \| + 3 \| D _ {k} (z ^ {k}) \|} \geq \frac {\kappa c _ {k}}{5 \kappa c _ {k} + 2}.
$$

This establishes the result since $c_k \geq 1$ for all $k$.

(ii) If $\| D_k(z^k)\| \leq \tau$, Definition 4 implies that

$$
T ^ {- 1} (- \frac {1}{c _ {k}} D _ {k} (z ^ {k})) \subset T ^ {- 1} (0) + \alpha \| \frac {1}{c _ {k}} D _ {k} (z ^ {k}) \| \mathbb {B} = T ^ {- 1} (0) + \frac {\alpha}{c _ {k}} \| D _ {k} (z ^ {k}) \| \mathbb {B},
$$

or

$$
(I + T ^ {- 1} \frac {1}{c _ {k}}) (- D _ {k} (z ^ {k})) + D _ {k} (z ^ {k}) \subset T ^ {- 1} (0) + \frac {\alpha}{c _ {k}} \| D _ {k} (z ^ {k}) \| \mathbb {B}.
$$

Since $D_{k}(z^{k}) = -(I + T^{-1}\frac{1}{c_{k}})^{-1}(z^{k})$, we have $z^{k}\in (I + T^{-1}\frac{1}{c_{k}})(-D_{k}(z^{k}))$, and so

$$
z ^ {k} \in T ^ {- 1} (0) - D _ {k} (z ^ {k}) + \frac {\alpha}{c _ {k}} \| D _ {k} (z ^ {k}) \| \mathbb {B},
$$

hence (15) holds. If $T^{-1}(0) = \{\bar{z}\}$, then the lower bound on $\gamma_k$ follows as in Part (i). (iii) This result follows as in Part (ii) using the second remark after Definition 4.

$\square$

When $w^{k} \approx D_{k}(z^{k})$, one can establish the inequality in hypothesis (H2) from a related condition on the vectors $w^{k}$. A specific technique for accomplishing this is given in the following lemma.

Lemma 15 Let $\xi, \hat{\gamma}_k, \delta_k \in \mathbb{R}_+$ be such that

$$
0 \leq \xi <   1, \delta_ {k} \leq \min \left\{1, \| H _ {k} \| ^ {- 1} \right\} \frac {3}{7} (1 - \xi) \hat {\gamma} _ {k}, \quad \text {and} \quad \hat {\gamma} _ {k} \leq 1 / 3, \tag {16}
$$

and let $H_{k}$ be a continuous linear transformation from $\mathcal{H}$ to itself. If $z^{k}, w^{k} \in \mathcal{H}$ satisfy

$$
\| \left(I - H _ {k}\right) w ^ {k} \| \leq \xi \hat {\gamma} _ {k} \| w ^ {k} \| \quad \text {and} \quad \| w ^ {k} - D _ {k} \left(z ^ {k}\right) \| \leq \delta_ {k} \| w ^ {k} \|, \tag {17}
$$

then $\| (I - H_k)D_k(z^k)\| \leq \hat{\gamma}_k\| D_k(z^k)\|$. Therefore, if (H1) and criterion ( $\mathcal{L}$ ) are satisfied, and if $\xi$ and the sequence $\{(\hat{\gamma}_k,\delta_k)\} \subset \mathbb{R}^2$ satisfy (16), with $\hat{\gamma}_k\leq \gamma_k$ for all $k$ (where $\gamma_{k}$ is defined in (H2)), then hypothesis (H2) is satisfied.

Proof Now from (16) and (17), we have

$$
\| w ^ {k} \| \leq \| D _ {k} (z ^ {k}) \| + \| w ^ {k} - D _ {k} (z ^ {k}) \| \leq \| D _ {k} (z ^ {k}) \| + \frac {3}{7} (1 - \xi) \hat {\gamma} _ {k} \| w ^ {k} \|,
$$

hence

$$
\| w ^ {k} \| \leq \frac {1}{1 - \frac {3}{7} (1 - \xi) \hat {\gamma} _ {k}} \| D _ {k} (z ^ {k}) \|\mathrm{.}
$$

Again by (17),

$$
\begin{aligned} \| (I - H _ {k}) D _ {k} (z ^ {k}) \| &\leq \| (I - H _ {k}) w ^ {k} \| + \| H _ {k} \| \| w ^ {k} - D _ {k} (z ^ {k}) \| + \| w ^ {k} - D _ {k} (z ^ {k}) \| \\ &\leq \xi \hat {\gamma} _ {k} \| w ^ {k} \| + (\| H _ {k} \| + 1) \delta_ {k} \| w ^ {k} \| \leq \left(\xi + \frac {6}{7} (1 - \xi)\right) \hat {\gamma} _ {k} \| w ^ {k} \| \leq \frac {\xi + \frac {6}{7} (1 - \xi)}{1 - \frac {3}{7} (1 - \xi) \hat {\gamma} _ {k}} \hat {\gamma} _ {k} \| D _ {k} \left(z ^ {k}\right) \| \\ &\leq \hat {\gamma} _ {k} \| D _ {k} (z ^ {k}) \|, \\ \end{aligned}
$$

since the inequality $\hat{\gamma}_k\leq 1 / 3$ implies that $\frac{\xi + \frac{6}{7} (1 - \xi)}{1 - \frac{3}{7}(1 - \xi)\hat{\gamma}_k} = \frac{6 + \xi}{7 - 3(1 - \xi)\hat{\gamma}_k}\leq 1.$

$\square$

We conclude this section by showing that the operators $N_{k}$ are non-expansive with respect to the set $T^{-1}(0)$.

Proposition 16 Assume $T^{-1}(0)$ is nonempty. If the linear transformations $\{H_k\}$ satisfies hypotheses (H1) and (H2), then for all $k$ we have $\| H_k D_k(z^k)\| \leq \frac{3}{2}\| D_k(z^k)\|$ and

$$
\| \mathcal {N} _ {k} (z ^ {k}) - \bar {z} \| ^ {2} + \frac {\gamma_ {k} ^ {2}}{4} \| D _ {k} (z ^ {k}) \| ^ {2} \leq \| z ^ {k} - \bar {z} \| ^ {2} \quad \text {for all} \bar {z} \in \Gamma . \tag {18}
$$

Proof Let $\bar{z} \in \Gamma$. From the definitions of $P_k$ and $\mathcal{N}_k$, we have

$$
\| P _ {k} \left(z ^ {k}\right) - \bar {z} \| = \| \mathcal {N} _ {k} \left(z ^ {k}\right) - \left(H _ {k} - I\right) D _ {k} \left(z ^ {k}\right) - \bar {z} \| \geq | \| \mathcal {N} _ {k} \left(z ^ {k}\right) - \bar {z} \| - \| \left(H _ {k} - I\right) D _ {k} \left(z ^ {k}\right) \| |, \tag {19}
$$

hence

$$
\| P _ {k} (z ^ {k}) - \bar {z} \| ^ {2} \geq \| \mathcal {N} _ {k} (z ^ {k}) - \bar {z} \| ^ {2} + \| (H _ {k} - I) D _ {k} (z ^ {k}) \| ^ {2} - 2 \| (H _ {k} - I) D _ {k} (z ^ {k}) \| \| \mathcal {N} _ {k} (z ^ {k}) - \bar {z} \|. \tag {20}
$$

From hypothesis (H2), we have

$$
\| H _ {k} D _ {k} (z ^ {k}) \| \leq \| D _ {k} (z ^ {k}) \| + \| (H _ {k} - I) D _ {k} (z ^ {k}) \| \leq (1 + \gamma_ {k}) \| D _ {k} (z ^ {k}) \| \leq \frac {3}{2} \| D _ {k} (z ^ {k}) \|\enspace .
$$

Hence

$$
\| \mathcal {N} _ {k} (z ^ {k}) - \bar {z} \| \leq \| z ^ {k} - \bar {z} \| + \| H _ {k} D _ {k} (z ^ {k}) \| \leq \sigma_ {k} + \frac {3}{2} \| D _ {k} (z ^ {k}) \|\enspace .
$$

Then, again by hypothesis (H2),

$$
\| \left(H _ {k} - I\right) D _ {k} \left(z ^ {k}\right) \| \leq \gamma_ {k} \| D _ {k} \left(z ^ {k}\right) \| = \frac {\left\| D _ {k} \left(z ^ {k}\right) \right\| ^ {2}}{2 \sigma_ {k} + 3 \| D _ {k} \left(z ^ {k}\right) \|} \leq \frac {\left\| D _ {k} \left(z ^ {k}\right) \right\| ^ {2}}{2 \left\| \mathcal {N} _ {k} \left(z ^ {k}\right) - \bar {z} \right\|}. \tag {21}
$$

Thus, from (20) and (21),

$$
\| P _ {k} (z ^ {k}) - \bar {z} \| ^ {2} \geq \| \mathcal {N} _ {k} (z ^ {k}) - \bar {z} \| ^ {2} + \| (H _ {k} - I) D _ {k} (z ^ {k}) \| ^ {2} - \| D _ {k} (z ^ {k}) \| ^ {2}. \tag {22}
$$

Letting $z = z^{k}$ and $z' = \bar{z}$ in Proposition 3 Part (c) yields

$$
\| P _ {k} (z ^ {k}) - \bar {z} \| ^ {2} + \| D _ {k} (z ^ {k}) \| ^ {2} \leq \| z ^ {k} - \bar {z} \| ^ {2}. \tag {23}
$$

From (22) and (23) we have

$$
\| \mathcal {N} _ {k} (z ^ {k}) - \bar {z} \| ^ {2} + \| (H _ {k} - I) D _ {k} (z ^ {k}) \| ^ {2} \leq \| z ^ {k} - \bar {z} \| ^ {2}. \tag {24}
$$

We now consider $\alpha_{k} = \frac{\|(H_{k} - I)D_{k}(z^{k})\|}{\|D_{k}(z^{k})\|}$. If $\alpha_{k} \geq \frac{\gamma_{k}}{2}$, then (18) holds by (24). Suppose that $\alpha_{k} < \frac{\gamma_{k}}{2}$. From (19), we have

$$
\| P _ {k} (z ^ {k}) - \bar {z} \| \geq \| \mathcal {N} _ {k} (z ^ {k}) - \bar {z} \| - \frac {\gamma_ {k}}{2} \| D _ {k} (z ^ {k}) \|\mathrm{.}
$$

Therefore, by (23),

$$
\| \mathcal {N} _ {k} (z ^ {k}) - \bar {z} \| \leq \sqrt {\| z ^ {k} - \bar {z} \| ^ {2} - \| D _ {k} (z ^ {k}) \| ^ {2}} + \frac {\gamma_ {k}}{2} \| D _ {k} (z ^ {k}) \|\mathrm{.}
$$

Using the inequality $\sqrt{a^2 - b^2} \leq a - \frac{b^2}{2a}$ for $a > b > 0$,

$$
\| \mathcal {N} _ {k} (z ^ {k}) - \bar {z} \| \leq \| z ^ {k} - \bar {z} \| - \frac {\| D _ {k} (z ^ {k}) \| ^ {2}}{2 \| z ^ {k} - \bar {z} \|} + \frac {\gamma_ {k}}{2} \| D _ {k} (z ^ {k}) \|\mathrm{.}
$$

But $\frac{\|D_k(z^k)\|}{2\|z^k - \bar{z}\|} \geq \gamma_k$, thus

$$
\| \mathcal {N} _ {k} (z ^ {k}) - \bar {z} \| \leq \| z ^ {k} - \bar {z} \| - \frac {\gamma_ {k}}{2} \| D _ {k} (z ^ {k}) \| , \quad \mathrm{or}
$$

$$
\left\| \mathcal {N} _ {k} \left(z ^ {k}\right) - \bar {z} \right\| + \frac {\gamma_ {k}}{2} \left\| D _ {k} \left(z ^ {k}\right) \right\| \leq \left\| z ^ {k} - \bar {z} \right\|. \tag {25}
$$

From (25) we again obtain (18).

$\square$

# 6 Global Convergence

The statement and proof of the global convergence result given below parallels the development given by Rockafellar in [41, Theorem 1] for the classical proximal point algorithm.

Theorem 17 Let $\{z^k\}$ be any sequence generated by the variable metric proximal point algorithm under criterion $(\mathcal{G})$ (or $(\mathcal{G}')$ ). Suppose that the solution set $T^{-1}(0)$ is nonempty and the sequence of linear transformations $\{H_k\}$ satisfies the hypotheses (H1) and (H2). Then the sequence $\{z^k\}$ is bounded, each weak cluster point of this sequence is an element of $T^{-1}(0)$, and $\lim_k D_k(z^k) = 0$. If it is also assumed that $T^{-1}(0)$ is bounded and $\Gamma = T^{-1}(0)$ in (H2), then there is a $\bar{z} \in T^{-1}(0)$ such that $\{z^k\}$ converges weakly to $\bar{z}$.

In order to establish this result we require the following technical lemma whose proof is straightforward and so is omitted.

Lemma 18 Suppose the nonnegative sequences $\{\epsilon_k\}$ satisfies $\sum_{k=0}^{\infty} \epsilon_k < +\infty$. If $\{u_k\}$ is a nonnegative sequence satisfying $u_{k+1} \leq \epsilon_k + u_k$, then $\{u_k\}$ is a Cauchy sequence.

Proof of Theorem 17 We begin by showing that the limit $\lim_{k}\|z^{k}-\bar{z}\|=\mu(\bar{z})$ exists for every $\bar{z}\in\Gamma$. To this end let $\bar{z}\in\Gamma$ and observe that the definition of $N_{k}$ and Proposition 16 imply that

$$
\begin{aligned} \| z ^ {k + 1} - \bar {z} \| &= \| z ^ {k + 1} - \mathcal {N} _ {k} (z ^ {k}) + \mathcal {N} _ {k} (z ^ {k}) - \bar {z} \| \leq \| z ^ {k + 1} - \mathcal {N} _ {k} (z ^ {k}) \| + \| \mathcal {N} _ {k} (z ^ {k}) - \bar {z} \| \\ &\leq \| H _ {k} \| \| w ^ {k} - D _ {k} (z ^ {k}) \| + \| z ^ {k} - \bar {z} \| \leq \epsilon_ {k} + \| z ^ {k} - \bar {z} \|\ . \\ \end{aligned}
$$

Therefore, Lemma 18 implies that the sequence $\{\| z^k -\bar{z}\|\}$ is Cauchy and so $\mu (\bar{z})$ exists for every $\bar{z}\in \Gamma$. An immediate consequence of the existence of these limits is the boundedness of the sequences $\{z^k\}$ and $\sigma_{k}$.

We now show that the sequence $\{D_k(z^k)\}$ converges strongly to the origin. Indeed, if this is not the case, then there is a subsequence $J \subset \{1, 2, \ldots\}$ such that $\inf_J \| D_k(z^k) \| = \beta_1 > 0$. This in turn implies that $\inf_J \gamma_k = \beta_2 > 0$ since otherwise $\lim_J \| D_k(z^k) \| = 0$ due to the boundedness of the sequence $\{\sigma_k\}$. Let $\bar{z} \in \Gamma$. By Proposition 16,

$$
\begin{array}{l} \frac {\gamma_ {k} ^ {2}}{4} \| D _ {k} (z ^ {k}) \| ^ {2} - \| z ^ {k} - \bar {z} \| ^ {2} + \| z ^ {k + 1} - \bar {z} \| ^ {2} \leq \| z ^ {k + 1} - \bar {z} \| ^ {2} - \| \mathcal {N} _ {k} (z ^ {k}) - \bar {z} \| ^ {2} \\ = \langle z ^ {k + 1} - \mathcal {N} _ {k} (z ^ {k}), z ^ {k + 1} - \bar {z} + \mathcal {N} _ {k} (z ^ {k}) - \bar {z} \rangle \\ \leq \| z ^ {k + 1} - \mathcal {N} _ {k} (z ^ {k}) \| (\| z ^ {k + 1} - \bar {z} \| + \| \mathcal {N} _ {k} (z ^ {k}) - \bar {z} \|) \\ \leq \| H _ {k} \| \| w ^ {k} - D _ {k} (z ^ {k}) \| (\| z ^ {k + 1} - \bar {z} \| + \| z ^ {k} - \bar {z} \|) \leq \epsilon_ {k} (\| z ^ {k + 1} \| + 2 \| \bar {z} \| + \| z ^ {k} \|) = \epsilon_ {k} C _ {k}, \\ \end{array}
$$

with $\{C_{k}\}$ bounded, where the final inequality follows from criterion (G). Hence

$$
\frac {\gamma_ {k} ^ {2}}{4} \| D _ {k} (z ^ {k}) \| ^ {2} \leq \| z ^ {k} - \bar {z} \| ^ {2} - \| z ^ {k + 1} - \bar {z} \| ^ {2} + \epsilon_ {k} C _ {k}
$$

whereby we obtain the contradiction

$$
0 <   \frac{\beta_{1}^{2}\beta_{2}^{2}}{4}\leq \limsup_{J}\frac{\gamma_{k}^{2}}{4}\| D_{k}(z^{k})\|^{2}\leq \lim_{J}(\| z^{k} - \bar{z}\|^{2} - \| z^{k + 1} - \bar{z}\|^{2} + \epsilon_{k}C_{k}) = \mu (\bar{z}) - \mu (\bar{z}) + 0 = 0  .
$$

Therefore, $\lim_k \| D_k(z^k)\| = 0$.

Next let $J \subset \{1,2,\ldots\}$ be such that the subsequence $\{z^k\}_J$ converges weakly to $z^\infty$, i.e. $z^\infty$ is a weak cluster point of the sequence $\{z^k\}$. We show that $z^\infty$ must be an element of $T^{-1}(0)$. From Proposition 3 (a), we have that $-\frac{1}{c_k} D_k(z^k) \in T(P_k(z^k))$ for all $k$, hence $0 \leq \langle z - P_k(z^k), w + \frac{1}{c_k} D_k(z^k) \rangle$, or equivalently, $\langle z - z^k - D_k(z^k), w + \frac{1}{c_k} D_k(z^k) \rangle \geq 0$, for all $k$ and $z, w$ with $w \in T(z)$. Taking the limit over $J$ yields the inequality $\langle z - z^\infty, w \rangle \geq 0$ for all $z, w$ with $w \in T(z)$. Since $T$ is maximal monotone, we get $0 \in T(z^\infty)$.

Under the assumption that $\Gamma = T^{-1}(0)$, the argument showing that there is no more than one weak cluster point of $\{z^{k}\}$ is identical to the one given by Rockafellar in ([41] Theorem 1).

$\square$

Remark To ensure the strong convergence of the sequence $\{z^k\}$, one again requires a growth condition on the inverse mapping $T^{-1}$ in a neighborhood of the origin. Rockafellar has shown that Lipschitz continuity of $T^{-1}$ at the origin suffices for this purpose [41, Theorem 2]. Other conditions can be found in the work of Luque [21, Proposition 1.2]. The results of Rockafellar and Luque are easily extended to the variable metric proximal point algorithm.

# 7 Convergence Rates

# 7.1 Linear Convergence

Just as in Rockafellar [41, Theorem 2], we require that the operator $T^{-1}$ is Lipschitz continuous at the origin in order to establish that the convergence rate is at least linear.

Theorem 19 Let $\{z^k\}$ be any sequence generated by the variable metric proximal point algorithm satisfying both criterion $(\mathcal{G})$ and $(\mathcal{L})$ for all $k$. Assume that $T^{-1}$ is Lipschitz continuous at the origin with modulus $\alpha$ and the solution set $T^{-1}(0)$ is a singleton $\{\bar{z}\}$. If the sequence $\{H_k\}$ satisfies the hypotheses (H1) and (H2) with $\delta_k \| H_k \| \to 0$, then the sequence $\{z^k\}$ strongly converges to the solution and there is an index $\bar{k}$ such that

$$
\| z ^ {k + 1} - \bar {z} \| \leq \sigma_ {k} \| z ^ {k} - \bar {z} \| \quad \forall k \geq \bar {k},
$$

where $\sigma_{k}$ satisfies $\limsup_{k\to \infty}\sigma_k < 1$. That is, the convergence rate is linear.

Proof By Theorem 17, we have $\| D_k(z^k)\| \to 0$. Hence, Part (ii) of Lemma 14 implies that $\{z^k\}$ converges strongly to $\bar{z}$. We now establish the linear rate.

Let $\tau > 0$ be as in Definition 4 and let $\tilde{k}$ be such that $\| \frac{1}{c_k} D_k(z^k) \| \leq \tau \quad \forall k \geq \tilde{k}$. By Proposition 3 (a) and the Lipschitz continuity of $T^{-1}$ at 0, we have

$$
\| P _ {k} (z ^ {k}) - \bar {z} \| \leq \frac {\alpha}{c _ {k}} \| D _ {k} (z ^ {k}) \|. \tag {26}
$$

Hence relation (14) and hypothesis (H2) yield

$$
\begin{aligned} \| \mathcal {N} _ {k} (z ^ {k}) - \bar {z} \| &= \| P _ {k} (z ^ {k}) + (H _ {k} - I) D _ {k} (z ^ {k}) - \bar {z} \| \\ &\leq \left\| P _ {k} \left(z ^ {k}\right) - \bar {z} \right\| + \gamma_ {k} \left\| D _ {k} \left(z ^ {k}\right) \right\|. \tag {27} \\ \end{aligned}
$$

Let $a_{k}:=\frac{\alpha}{c_{k}}+\gamma_{k}$. Using (26) and (27),

$$
\| \mathcal {N} _ {k} (z ^ {k}) - \bar {z} \| \leq (\frac {\alpha}{c _ {k}} + \gamma_ {k}) \| D _ {k} (z ^ {k}) \| = a _ {k} \| D _ {k} (z ^ {k}) \|. \tag {28}
$$

Let $\gamma := \frac{1}{2(5 + 2\alpha)}$. By Proposition 16 and Lemma 14 we have, for $k \geq \tilde{k}$, that

$$
\left\| \mathcal {N} _ {k} \left(z ^ {k}\right) - \bar {z} \right\| ^ {2} + \gamma^ {2} \left\| D _ {k} \left(z ^ {k}\right) \right\| ^ {2} \leq \left\| z ^ {k} - \bar {z} \right\| ^ {2}. \tag {29}
$$

By (28) and (29), when $k \geq \tilde{k}$

$$
\| \mathcal {N} _ {k} \left(z ^ {k}\right) - \bar {z} \| ^ {2} \leq a _ {k} ^ {2} \| D _ {k} \left(z ^ {k}\right) \| ^ {2} \leq \frac {a _ {k} {} ^ {2}}{\gamma^ {2}} \| z ^ {k} - \bar {z} \| ^ {2} - \frac {a _ {k} {} ^ {2}}{\gamma^ {2}} \| \mathcal {N} _ {k} \left(z ^ {k}\right) - \bar {z} \| ^ {2}. \tag {30}
$$

Let $\mu_{k}:=\frac{a_{k}}{\sqrt{a_{k}^{2}+\gamma^{2}}}.$ From (30) we have

$$
\left\| \mathcal {N} _ {k} \left(z ^ {k}\right) - \bar {z} \right\| \leq \mu_ {k} \left\| z ^ {k} - \bar {z} \right\|. \tag {31}
$$

By (31), criterion $(\mathcal{L})$ (or $(\mathcal{L}'))$ , and Proposition 3 (c),

$$
\begin{aligned} \| z ^ {k + 1} - \bar {z} \| &\leq \| z ^ {k + 1} - \mathcal {N} _ {k} (z ^ {k}) \| + \| \mathcal {N} _ {k} (z ^ {k}) - \bar {z} \| \\ &\leq \delta_ {k} \| H _ {k} \| \| w ^ {k} \| + \mu_ {k} \| z ^ {k} - \bar {z} \| \leq \frac {\delta_ {k} \| H _ {k} \|}{1 - \delta_ {k}} \| D _ {k} (z ^ {k}) \| + \mu_ {k} \| z ^ {k} - \bar {z} \| \\ &\leq \left(\frac {\delta_ {k} \| H _ {k} \|}{1 - \delta_ {k}} + \mu_ {k}\right) \| z ^ {k} - \bar {z} \| = \sigma_ {k} \| z ^ {k} - \bar {z} \|, \\ \end{aligned}
$$

where $\sigma_{k} := \frac{\delta_{k}||H_{k}||}{1 - \delta_{k}} + \mu_{k}$. Since there is a $\tilde{\delta} > 0$ such that $\mu_{k} < 1 - \tilde{\delta}$ for any $k$, and $\delta_{k}||H_{k}|| \to 0$, we have $\sigma_{k} < 1$ for $k$ sufficiently large. Moreover, we have $\limsup_{k \to \infty} \sigma_{k} = \limsup_{k \to \infty} \mu_{k} \leq 1 - \tilde{\delta}$.

# 7.2 Super-linear Convergence

We now give an analog of Dennis and Moré's [14] characterization theorem for the super-linear convergence of variable metric methods in nonlinear programming that applies to the VMPPA. This result is used in [6] to establish the super-linear convergence of the variable metric proximal point algorithm when the Broyden (non-symmetric case) or the BFGS (symmetric case) updating formulas are used to generate the matrices $H_{k}$.

Theorem 20 Let $\{z^k\}$ be any sequence generated by the variable metric proximal point algorithm satisfying criterion (L) for all $k$. Suppose that the operator $T^{-1}$ is differentiable at the origin with $T^{-1}(0) = \{\bar{z}\}$ and $\nabla T^{-1}(0) = J$. If $\lim_k \| D_k(z^k)\| = 0$, then $\{z^k\}$ converges to the solution $\bar{z}$ super-linearly if and only if

$$
\frac {\left[ I - \left(I + \frac {1}{c _ {k}} J\right) H _ {k} ^ {- 1} \right]\left(z ^ {k + 1} - z ^ {k}\right)}{\left\| z ^ {k + 1} - z ^ {k} \right\|} \rightarrow 0 \quad \text {as } k \rightarrow \infty . \tag {32}
$$

Remark By Proposition 9 we have $\nabla D(\bar{z}) = -(I + \frac{1}{c} J)^{-1}$. Consequently, condition (32) can be recast in the more familiar form given in [15, Theorem 8.2.4]. Note that the assumption in (32) on the sequence $\{H_k\}$ is much weaker than assuming that this sequence converges. Specific choices of the linear transformations $H_{k}$ satisfying (32) are discussed in [6].

The proof of Theorem 20 requires the following lemma.

Lemma 21 Under the conditions in Theorem 20 we have

$(a)$ $T^{-1}(\frac{-1}{c_k} D_k(z^k)) - \bar{z} -J(\frac{-1}{c_k} D_k(z^k))\subset o(\| z^k -\bar{z}\|)\mathbb{B},$ and  
$(b)$ $(I + \frac{1}{c_k} J)H_k^{-1}(z^{k + 1} - \mathcal{N}_k(z^k))\in o(\| z^k -\bar{z}\|)\mathbb{B},$

for all $k$ sufficiently large.

Proof For part (a), let $\delta > 0$ be such that

$$
T ^ {- 1} (w) - J w - \bar {z} \subset o (\| w \|) \mathbb {B} \tag {33}
$$

whenever $\|w\| < \delta$. Let $\bar{k}_{1}$ be such that whenever $k > \bar{k}_{1}$, $\|D_{k}(z^{k})\| \leq \delta$. Then, by (33) and Proposition 3 (c), when $k > \bar{k}_{1}$,

$$
T ^ {- 1} (\frac {- 1}{c _ {k}} D _ {k} (z ^ {k})) - \bar {z} - J (\frac {- 1}{c _ {k}} D _ {k} (z ^ {k})) \subset o (\| D _ {k} (z ^ {k}) \|) \mathbb {B} \subset o (\| z ^ {k} - \bar {z} \|) \mathbb {B}.
$$

We now prove (b). Note that $\mathcal{N}_k(z^k) = (I + H_kD_k)(z^k)$, hence by criterion ( $\mathcal{L}$ )

$$
\begin{array}{l} \| \left(I + \frac {1}{c _ {k}} J\right) H _ {k} ^ {- 1} \left(z ^ {k + 1} - \mathcal {N} _ {k} \left(z ^ {k}\right)\right) \| = \left\| \left(I + \frac {1}{c _ {k}} J\right) \left(w ^ {k} - D _ {k} \left(z ^ {k}\right)\right) \right\| \\ \leq (1 + \| J \|) \| w ^ {k} - D _ {k} \left(z ^ {k}\right) \| \leq \delta_ {k} (1 + \| J \|) \| w ^ {k} \| \\ \leq \frac {\delta_ {k} (1 + \| J \|)}{1 - \delta_ {k}} \| D _ {k} \left(z ^ {k}\right) \|. \tag {34} \\ \end{array}
$$

Therefore by (34) and Proposition 3 (c),

$$
(I + \frac {1}{c _ {k}} J) H _ {k} ^ {- 1} (z ^ {k + 1} - \mathcal {N} _ {k} (z ^ {k})) \in o (\| D _ {k} (z ^ {k}) \|) \mathbb {B} \subset o (\| z ^ {k} - \bar {z} \|) \mathbb {B}.
$$

$\square$

Proof of Theorem 20: Let $\tilde{z}^{k + 1} := \mathcal{N}_k(z^k) = (I + H_k D_k)(z^k)$. By Proposition 3 (a) we have $\tilde{z}^{k + 1} = z^k - H_k(I + T^{-1}\frac{1}{c_k})^{-1}(z^k)$. Hence

$$
\begin{aligned} z ^ {k} &\in (I + T ^ {- 1} \frac {1}{c _ {k}}) [ H _ {k} ^ {- 1} (z ^ {k} - \tilde {z} ^ {k + 1}) ] \\ { &= } { H _ { k } ^ { - 1 } ( z ^ { k } - \tilde { z } ^ { k + 1 } ) + T ^ { - 1 } [ \frac { 1 } { c _ { k } } H _ { k } ^ { - 1 } ( z ^ { k } - \tilde { z } ^ { k + 1 } ) ] , } \\ \end{aligned}
$$

or equivalently,

$$
\begin{array}{l} z ^ {k + 1} - \bar {z} = z ^ {k} - \bar {z} + (z ^ {k + 1} - z ^ {k}) \\ \in [ T ^ {- 1} (\frac {1}{c _ {k}} H _ {k} ^ {- 1} (z ^ {k} - \tilde {z} ^ {k + 1})) - \bar {z} + (z ^ {k + 1} - z ^ {k}) + H _ {k} ^ {- 1} (z ^ {k} - \tilde {z} ^ {k + 1}) \\ = \left[ T ^ {- 1} (\frac {1}{c _ {k}} H _ {k} ^ {- 1} (z ^ {k} - \tilde {z} ^ {k + 1})) - \bar {z} - J (\frac {1}{c _ {k}} H _ {k} ^ {- 1} (z ^ {k} - \tilde {z} ^ {k + 1})) \right] \\ + [ I - (I + \frac {1}{c _ {k}} J) H _ {k} ^ {- 1} ] (z ^ {k + 1} - z ^ {k}) \\ + (I + \frac {1}{c _ {k}} J) H _ {k} ^ {- 1} (z ^ {k + 1} - \tilde {z} ^ {k + 1}) \\ = \left[ T ^ {- 1} (\frac {- 1}{c _ {k}} D _ {k} (z ^ {k})) - \bar {z} - J (\frac {- 1}{c _ {k}} D _ {k} (z ^ {k})) \right] \\ + [ I - (I + \frac {1}{c _ {k}} J) H _ {k} ^ {- 1} ] (z ^ {k + 1} - z ^ {k}) \\ + \left(I + \frac {1}{c _ {k}} J\right) H _ {k} ^ {- 1} \left(z ^ {k + 1} - \tilde {z} ^ {k + 1}\right). \tag {35} \\ \end{array}
$$

By Lemma 21 the first and third of the three terms appearing on the right hand side of this inclusion can be bounded by an expression of the form $o(\|z^k - \bar{z}\|)\mathbb{B}$. If (32) holds, then $[I - (I + \frac{1}{c_k} J)H_k^{-1}](z^{k+1} - z^k) \in o(\|z^{k+1} - z^k\|)\mathbb{B}$. Therefore there are positive sequences $\{\alpha_{1k}\}$ and $\{\alpha_{2k}\}$ each converging to zero such that, for $k > \bar{k}_1$,

$$
\begin{aligned} {\| z ^ {k + 1} - \bar {z} \|} &\leq {\alpha_ {1 k} \| z ^ {k + 1} - z ^ {k} \| + \alpha_ {2 k} \| z ^ {k} - \bar {z} \|} \\ &\leq \alpha_ {1 k} (\| z ^ {k} - \bar {z} \| + \| z ^ {k + 1} - \bar {z} \|) + \alpha_ {2 k} \| z ^ {k} - \bar {z} \| \\ { &= } { \alpha _ { 1 k } \| z ^ { k + 1 } - \bar { z } \| + ( \alpha _ { 1 k } + \alpha _ { 2 k } ) \| z ^ { k } - \bar { z } \| . } \\ \end{aligned}
$$

Let $\bar{k}_2 > \bar{k}_1$ be such that $\alpha_{1k} < \frac{1}{2}$ for all $k > \bar{k}_2$. Then, denoting $\frac{\alpha_{1k} + \alpha_{2k}}{1 - \alpha_{1k}}$ by $\tau_k$,

$$
\| z ^ {k + 1} - \bar {z} \| \leq \frac {\alpha_ {1 k} + \alpha_ {2 k}}{1 - \alpha_ {1 k}} \| z ^ {k} - \bar {z} \| = \tau_ {k} \| z ^ {k} - \bar {z} \|
$$

whenever $k > \bar{k}_2$, and $\tau_k \to 0$ as $k \to \infty$. Therefore $\{z^k\}$ converges to $\bar{z}$ super-linearly.

Conversely, suppose that

$$
\lim _ {k \rightarrow \infty} \frac {\left\| z ^ {k + 1} - \bar {z} \right\|}{\left\| z ^ {k} - \bar {z} \right\|} = 0. \tag {36}
$$

Divide (35) by $\| z^k -\bar{z}\|$ and let $k\to \infty$. From (36) and Lemma 21 we obtain

$$
\frac {[ I - (I + \frac {1}{c _ {k}} J) H _ {k} ^ {- 1} ] (z ^ {k + 1} - z ^ {k})}{\| z ^ {k} - \bar {z} \|} \to 0 \quad \mathrm{as} k \to \infty .
$$

However, from (36) we have

$$
\frac {\| z ^ {k} - \bar {z} \|}{\| z ^ {k + 1} - z ^ {k} \|} \leq \frac {\| z ^ {k} - \bar {z} \|}{\| z ^ {k} - \bar {z} \| - \| z ^ {k + 1} - \bar {z} \|} = \frac {1}{1 - \frac {\| z ^ {k + 1} - \bar {z} \|}{\| z ^ {k} - \bar {z} \|}} \to 1
$$

as $k\to \infty$. Hence (32) holds.

![](images/4534b902e67a98aac6ec0d65a9dc2e31847fad2eba09fe375589044f123961b1.jpg)

# 8 Concluding Remarks

In this paper, we introduced a new proximal point algorithm for solving the inclusion $0 \in T(x)$ where T is an arbitrary maximal monotone operator. The global convergence of the algorithm is demonstrated with an inexact solution at each step. This is important in practice, since solving for the exact solution at each step is impractical, and may in fact be almost as difficult as solving the original problem. If it is assumed that $T^{-1}$ is Lipschitz continuous at the origin, then the method is shown to be linearly convergent. If it is further assume that $T^{-1}$ is differentiable at the origin, then the classical characterization of super-linear convergence due to Dennis and Moré also holds for the VMPPA. In [6], this characterization of super-linear convergence is applied to establish the super-linear convergence of the method when certain matrix secant updating strategies are employed to generate the matrices $H_{k}$. In [5], we give some of the implementation details in the case of convex programming. We show how to apply the method to solve the associated primal,

dual, and Lagrangian saddle point problems. In particular, it is shown how the bundle technique [17] can be applied to satisfy the approximation criteria $(\mathcal{L})$ and $(\mathcal{G})$ in both the primal and saddle point solution techniques. Preliminary numerical results comparing these three approaches are also presented.

Acknowledgments The authors would like to thank the reviewers for their thorough work. Their comments and suggestions have greatly contributed to our exposition. In particular, we would like to thank Professor Alfredo Iusem of observing an error in an earlier version of Theorem 17 and for his suggested revision of this result when the set $T^{-1}(0)$ is assumed to be bounded.

# References

[1] A.D. Alexandrov. The existence almost everywhere of the second differential of a convex function and some associated properties of convex surfaces. Ucenye Zapiski Leningr. Gos. Univ. Ser. Mat. (in Russian), 37:3—35, 1939.  
[2] J. P. Aubin and H. Frankowska. Set-Valued Analysis. Birkhäuser, Boston, 1990.  
[3] J.F. Bonnans, J.C. Gilbert, C. Lemaréchal, and C. Sagastizábal. A family of variable metric proximal point methods. Mathematical Programming, 68:15—47, 1995.  
[4] L.M. Bregman. The method of successive projection for finding a common point of convex sets. Soviet Mathematics Doklady, 162:487—490, 1965.  
[5] J.V. Burke and M. Qian. Application of a variable metric proximal point algorithm to convex programming. Preprint, Mathematics, University of Washington, Seattle, WA, 1996.  
[6] J.V. Burke and M. Qian. On the super-linear convergence of the variable metric proximal point algorithm using Broyden and BFGS matrix secant updating. Preprint, Mathematics, University of Washington, Seattle, WA, 1996.  
[7] X. Chen and M. Fukushima. Proximal quasi-Newton methods for nondifferentiable convex optimization. Technical Report AMR 95/32, Dept. of Applied Math., University of New South Wales, Sydney, South Wales, Australia, 1995.  
[8] K. Deimling. Nonlinear Functional Analysis. Springer-Verlag, New York, 1980.  
[9] J. Eckstein. Splitting Methods for Monotone Operators with Application tp Parallel Optimization. Ph.d., Massachusetts Institute of Technology, Cambridge, MA 02139, 1989.  
[10] M. Fukushima and L. Qi. A globally and superlinearly convergent algorithm for nonsmooth convex minimization. SIAM J. Optim., 30:1106—1120, 1996.  
[11] O. Güler. New proximal point algorithms for convex minimization. SIAM J. Optimization, 2:649—664, 1992.  
[12] S. Han. A decomposition method and its application to convex programming. Mathematics of Operations Research, 14:237—248, 1989.  
[13] A. Iusem. Personal communication, October, 1996.  
[14] Jr. J.E. Dennis and J.J. Moré. A characterization of superlinear convergence and its application to quasi-Newton methods. Math. Comp., 28:549—560, 1974.  
[15] Jr. J.E. Dennis and R.B. Schnabel. Numerical Methods for Unconstrained Optimization and Nonlinear Equations. Prentice Hall, New Jersey, 1983.  
[16] G. Kassay. The proximal points algorithm for reflexive Banach spaces. Studia Univ. Babes Bolyai Math., 30:9—17, 1930.  
[17] C. Lemaréchal. Bundle methods in nonsmooth optimization. In C. Lemaréchal and R. Mifflin, editors, Nonsmooth Optimization. Pergamon Press, Oxford, 1978.  
[18] C. Lemaréchal and C. Sagastizábal. An approach to variable metric bundle methods. In J. Henry and J.P. Yuan, editors, IFIP Proceedings, Syatems Modeling and Optimization, pages 144—162. Springer, Berlin, 1994.  
[19] C. Lemaréchal and C. Sagastizábal. Practical aspects of the Moreau-Yosida regularization i: Theoretical preliminaries. SIAM J. Optim., 7:367—385, 1997.  
[20] C. Lemaréchal and C. Sagastizábal. Variable metric bundle methods: from conceptual to implementable forms. Mathematical Programming, 76:393-410, 1997.  
[21] F.J. Luque. Asymptotic convergence analysis of the proximal point algorithm. SIAM J. Control and Optimization, 22:277—293, 1984.  
[22] B. Martinet. Regularisation d'inequations variationelles par approximations successive. Revue Française d'Informatique et de Recherche Opérationelle, 4:154—158, 1970.  
[23] B. Martinet. Determination approachée d'un point fixe d'une application pseudo-contractante. cas de l'application prox. Comptes Rendus de l'Académie des Sciences, Paris, Série A, 274:163—165, 1972.  
[24] R. Mifflin. A quasi-second-order proximal bundle algorithm. Mathematical Programming, 73:51—72, 1996.  
[25] R. Mifflin, D. Sun, and L. Qi. Quasi-Newton bundle-type methods for nondifferentiable convex optimization. Technical Report AMR 96/21, Dept. of Applied Math., University of New South Wales, Sydney, South Wales, Australia, 1996.  
[26] F. Mignot. Control dan les inequations variationelles elliptiques. J. Funtional Anal., 22:130—185, 1976.  
[27] G.J. Minty. Monotone (nonlinear) operators in Hilbert space. Duke Math. J., 29:341—346, 1962.  
[28] J.J. Moreau. Proximité et dualité dans un espace Hilbertien. Bull. Soc. Math. France, 93:273—299, 1965.  
[29] J.M. Ortega and W.G. Rheinboldt. Iterative Solution of Nonlinear Equations in Several Variables. Academic Press, New York, 1970.  
[30] J.-S. Pang and L. Qi. Nonsmooth equations: Motivation and algorithms. SIAM J. on Optimization, 3:443-465, 1993.  
[31] J.-S. Pang and L. Qi. A globally convergent Newton method for SC $^{1}$ problems. to appear in Journal of Optimization Theory and Applications, 1996.  
[32] G.B. Passty. Weak convergence theorems for nonexpansive mappings in Banach spaces. J. Math. Anal. Appl., 67:274—276, 1979.  
[33] Robert R. Phelps. Convex Functions, Monotone Operators, and Differentiability. Lecture Notes in Mathematics, Springer-Verlag, New York, 1989.  
[34] L. Qi. Convergence analysis of some algorithms for solving nonsmooth equations. Math. of Operations Research, 18:227—244, 1993.  
[35] L. Qi. Second-order analysis of the Moreau-Yosida regularization of a convex function. Technical Report AMR 94/20, Dept. of Applied Math., University of New South Wales, Sydney, South Wales, Australia, 1994.  
[36] L. Qi and X. Chen. A preconditioning proximal Newton method for nondifferentiable convex optimization. Mathematical Programming, 76:411—430, 1995.  
[37] L. Qi and J. Sun. A nonsmooth version of Newton's method. Math. Programming, 66:25—43, 1994.  
[38] M. Qian. The Variable Metric Proximal Point Algorithm: Theory and Application. Ph.d., University of Washington, Seattle, WA, 1992.  
[39] R.T. Rockafellar. Conjugate Duality and Optimization. Society for Industrial and Applied Mathematics, Philadelphia, 1974.  
[40] R.T. Rockafellar. Augmented Lagrangians and applications of the proximal point algorithm in convex programming. Math. of Operations Research, 1:97—116, 1976.  
[41] R.T. Rockafellar. Monotone operators and the proximal point algorithm. SIAM J. Control and Optimization, 14:877—898, 1976.  
[42] R.T. Rockafellar. Maximal monotone relations and the second derivatives of nonsmooth functions. Ann. Inst. H. Poincaré Analyse Non Linéare, 2:167—184, 1985.  
[43] J.E. Spingarn. Partial inverse of a monotone operator. Appl. Math. Optim., 10:247—265, 1983.  
[44] J.E. Spingarn. Applications of the methods of partial inverses to convex programming: Decomposition. Math. Programming, 32:199—223, 1985.
