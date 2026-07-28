# Robustness of the Hybrid Extragradient-Proximal Point Algorithm*†

R. S. Burachik

Universidade Federal do Rio de Janeiro,
Engenharia de Sistemas e Computação, Rio de Janeiro, Brazil

S. Scheimberg

Universidade Federal do Rio de Janeiro,
Instituto de Matemática, Rio de Janeiro, Brazil

B.F. Svaiter

Instituto de Matemática Pura e Aplicada,
Rio de Janeiro, Brazil.

# Abstract

The hybrid extragradient proximal point method recently proposed by Solodov and Svaiter has the distinctive feature of allowing a relative error tolerance. We extend the error tolerance of this method, proving that it converges even if a summable error is added to the relative error. Furthermore, the extragradient step may be performed inexactly, with a summable error. We present a convergence analysis, which encompasses other well-known variations of the proximal point method, previously unrelated. We establish weak global convergence under mild assumptions.

*The first author was partially supported by PRONEX-Optimization. The second author was partially supported by CNPq Grant 302393/85-4(RN). The third author was partially supported by CNPq Grant 301200/93-9(RN) and by PRONEX-Optimization.

$^{\dagger}$ We thank the anonymous referees, whose corrections and suggestions improved the original version of this work.

Key Words. Maximal monotone operators, proximal point algorithm, extragradient method, enlargement of a maximal monotone operator.

# 1 Introduction

Let $H$ be a Hilbert space with inner product $\langle\cdot,\cdot\rangle$. Call $\mathcal{P}(H)$ the family of subsets of $H$. A multifunction $T\colon H\to\mathcal{P}(H)$ is said to be a monotone operator if

$$
\langle z - z', w - w' \rangle \geq 0 \quad \mathrm{whenever} \quad w \in T (z), w' \in T (z').
$$

It is said to be maximal monotone if, in addition, the graph

$$
G (T) := \{(z, w) \in H \times H \mid w \in T (z) \},
$$

is not properly contained in the graph of any other monotone operator $T' \colon H \to \mathcal{P}(H)$. We recall also the definition of the domain of T:

$$
D (T) := \{x \in H: T (x) \neq \emptyset \}.
$$

Given a maximal monotone operator $T: H \to \mathcal{P}(H)$, we consider the following problem:

$$
\text {find} x \in H \text {such that} 0 \in T (x). \tag {1}
$$

There is an extensive literature concerning this classical problem (see for example Refs. 1–3). Moreover, it can be regarded as a unified formulation of several important problems. For an appropriate choice of the operator T, Problem (P) covers a wide range of mathematical applications, like variational inequalities, complementarity problems and nonsmooth convex optimization. Problem (P) has applications in physics, economics and in several areas of engineering.

One of the most important methods for finding zeros of a maximal monotone operator is the proximal point algorithm (Refs. 4–12, see Ref. 13 for a survey). This method generates for any starting point $x^{0} \in H$ a sequence $\{x^{k}\}$ by the approximation rule

$$
x ^ {k} \approx (c _ {k} T + I) ^ {- 1} (x ^ {k - 1}). \tag {2}
$$

Here $c_k$ is a sequence of positive real numbers. From a practical point of view, it is essential to work with approximations of $(c_k T + I)^{-1}(x^{k-1})$ in order to obtain implementable methods. The classical proximal point method (Ref. 11) employs a summable error tolerance in steps (2). Another example of summable error criterion comes from optimization. It is well-known that minimizing a convex function $f$ is equivalent to solving $0 \in \partial f(x)$. Let $\partial_{\varepsilon}f(x)$ be the $\varepsilon$ -subdifferential of $f$ at $x$ (Ref. 14). Lemaire (Ref. 15) studied the proximal point method applied to $\partial f$ with the following approximated scheme:

$$
x ^ {k} \in (c _ {k} \partial_ {\varepsilon_ {k}} f + I) ^ {- 1} (x ^ {k - 1}), \quad \sum c _ {k} \varepsilon_ {k} <   \infty , \tag {3}
$$

and $c_{k} \geq \hat{c} > 0$. For $\varepsilon \geq 0$, $\partial f(x) \subseteq \partial_{\varepsilon} f(x)$, and equality holds for $\varepsilon = 0$. In (3), $x^{k}$ is the exact solution of a proximal iteration involving a perturbation or enlargement of the operator $\partial f$. Following Ref. 15, we call this method perturbed proximal point method for optimization.

Note that convergence of the perturbed proximal point method for optimization cannot be deduced from the approximation scheme of Ref. 11. From (3), it follows (see the remark in Ref. 16)

$$
\| x ^ {k} - (c _ {k} \partial f + I) ^ {- 1} (x ^ {k - 1}) \| \leq \sqrt {c _ {k} \varepsilon_ {k}}.
$$

This estimate is not important by itself, but it is important that this estimate is exact with respect to the order $\sqrt{\varepsilon_k}$. Thus the summable error tolerance used in Ref. 11 for (2) may not hold. For this reason, a different kind of analysis is required for (3). In Ref. 17 Burachik, Iusem and Svaiter extended the inexact scheme (3) to maximal monotone operators in finite dimensional spaces. For this purpose, they introduced the $\varepsilon$ -enlargement of an arbitrary maximal monotone operator $T$. Using the notation $T^{\varepsilon}$ for such an enlargement of $T$ (we will describe it in Section 2), we again have $T(x) \subseteq T^{\varepsilon}(x)$ for $\varepsilon \geq 0$ and equality when $\varepsilon = 0$ (i.e., $T^0 = T$ ). One of the perturbed proximal point methods analyzed in Ref. 17 was

$$
x ^ {k} \in (c _ {k} T ^ {\varepsilon_ {k}} + I) ^ {- 1} (x ^ {k - 1}), \quad \sum \varepsilon_ {k} <   \infty , \tag {4}
$$

and $\bar{c} > c_k \geq \hat{c} > 0$. In this setting, $\sum c_k \varepsilon_k < \infty$ is equivalent to $\sum \varepsilon_k < \infty$. In Ref. 17, generalized proximal point methods with Bregman functions (Ref. 18) were considered. For the particular case in which the Bregman function is $(1/2)\| \cdot \|^2$, iteration (4) is recovered. The $\varepsilon$ -enlargement was extended for maximal monotone operators on infinite dimensional spaces in Refs. 19 - 20.

Up to now, summability of errors has been the standard for ensuring convergence of inexact proximal and proximal-like methods. From the point of view of numerical analysis, relative errors are easier to estimate and analyze. Very recently, Solodov and Svaiter proposed in Ref. 21 an inexact hybrid extragradient-proximal point algorithm for problem (P) using a relative error tolerance as we will explain later on. We point out that the traditional inexact proximal point method may not converge under the relative error tolerance proposed on Ref. 21 (an example is supplied in that paper, Section 3). As for the implementability of the hybrid extragradient proximal point method, we mention (Ref. 21, Section 5.2) a globally convergent Newton-type method for solving problem (P) when T is smooth and H is a finite dimensional space. In this example, a single Newton iteration is applied to the regularized system at each proximal extragradient step. The hybrid extragradient proximal point method also allows the use of elements in the enlargement $T^{\varepsilon}$. The $\varepsilon$ -enlarged operator appears naturally in the context of variational inequality problems (Ref. 22). We refer the reader to this work for a connection between the error measure used by the hybrid extragradient proximal point method (which is based on $T^{\varepsilon}$ ) and the regularized gap function, introduced independently by Auchmuty (Ref. 23) and Fukushima (Ref. 24). Still in Ref. 22, it is proved that this error measure is convex and an application of the hybrid method in this context is presented.

Regarding other possible uses of the enlargement $T^{\varepsilon}$, in Ref. 25, a bundle-like proximal method for solving (P) was proposed. This method used elements in $T^{\varepsilon}$, generated by a “transportation formula” (Refs. 19 – 20). This formula allows to compute elements in $T^{\varepsilon}$ using convex combinations of pairs $(x_{i}, v_{i} \in T(x_{i}))$ (i.e., $(x_{i}, v_{i}) \in G(T)$ ).

There are two partially open questions regarding the hybrid extragradient proximal point method. First: Does the hybrid extragradient proximal method converge under a “summable error” criterion? This is a natural question because the “summable error” criterion has been the standard for convergence analysis of proximal and proximal-like methods. Each iteration of the hybrid extragradient proximal point method consists on solving approximately a proximal subproblem and performing an extragradient step. The second question is: This method converges when small errors are present in the extragradient steps? This is also a natural question because each extragradient step relies on the exact evaluation of some $v \in T^{\varepsilon}(x)$. As we mentioned before, an element in $T^{\varepsilon}$ can be obtained as a convex combination of elements in the image of T at possibly different points. So, small errors

may be done while performing these sums (which always happens in digital computers using floating point arithmetic). Even in the smooth case, when H is a finite dimensional space and a closed formula is available for T, in the computer implementation of the method, truncations and rounding errors may appear in evaluating $v = T(x)$.

These issues were partially addressed in Ref. 21 by suggesting how a summable error could replace the relative error tolerance in the method (we will explain this later on). The aim of our paper is to prove robustness of the hybrid extragradient proximal point method in the following sense: it is convergent even if a summable error tolerance is added to the relative error tolerance and the extragradient steps are performed with a summable error tolerance. We also show that our scheme provides a unified framework for several proximal point-like methods.

We explain briefly the hybrid extragradient proximal point method Ref. 21, because it is new and our aim is to show its robustness. The exact proximal point iteration generates $x^{k}$ by the rule:

$$
x ^ {k} = (c _ {k} T + I) ^ {- 1} (x ^ {k - 1}), \tag {5}
$$

where $c_k > 0$. If we define $v^k = (1 / c_k)(x^{k-1} - x^k)$, then the pair $v^k, x^k$ solves the system in $v, x$ :

$$
v \in T (x), \tag {6a}
$$

$$
c _ {k} v + x - x ^ {k - 1} = 0. \tag {6b}
$$

Conversely, if $v^k, x^k$ solves the above system, then $x^k$ satisfies (5), and $v^k = (1 / c_k)(x^{k-1} - x^k)$. We point out that $x^k$ may also be expressed as:

$$
x ^ {k} = x ^ {k - 1} - c _ {k} v ^ {k}.
$$

So, the exact proximal point method can be interpreted as an extragradient method (Ref. 26). In Solodov and Svaiter's hybrid extragradient method an approximate solution of system (6), $\tilde{v}^{k}, \tilde{x}^{k}$ is obtained. This pair shall satisfy, for some “small” $\varepsilon_{k} > 0$ :

$$
\tilde {v} ^ {k} \in T ^ {\varepsilon_ {k}} (\tilde {x} ^ {k}), \tag {7a}
$$

$$
c _ {k} \tilde {v} ^ {k} + \tilde {x} ^ {k} - x ^ {k - 1} \approx 0. \tag {7b}
$$

Observe that, in system (7) we have an approximated inclusion (controlled by $\varepsilon_{k}$ ), and an approximated equality. The approximation criterion proposed in Ref. 21 is

$$
\| c _ {k} \tilde {v} ^ {k} + \tilde {x} ^ {k} - x ^ {k - 1} \| ^ {2} + 2 c _ {k} \varepsilon_ {k} \leq \sigma^ {2} \| \tilde {x} ^ {k} - x ^ {k - 1} \| ^ {2}, \tag {8}
$$

where $\sigma$ is some fixed number on [0,1). Having an approximate solution of (7), i.e., a pair $\tilde{x}^{k}$, $\tilde{v}^{k}$ satisfying condition (8), one may be tempted to take $\tilde{x}^{k}$ as the next iterate:

$$
x ^ {k} := \tilde {x} ^ {k}. \tag {9}
$$

Solodov and Svaiter presented in Ref. 21 an example in two dimensions where this strategy generates a divergent sequence, even taking $\tilde{v}^{k} \in T(x^{k})$. Therefore, strategy (9) does not work with approximate solutions satisfying error criterion (8). So, instead of taking $\tilde{x}^{k}$ as the next iterate, these authors proposed an extragradient step, i.e., $x^{k}$ is generated as

$$
x ^ {k} = x ^ {k - 1} - c _ {k} \tilde {v} ^ {k}.
$$

Observe that (8) can be interpreted as a fixed relative error tolerance. To make this clear, let us discuss the case $\varepsilon_{k}=0$. An approximate solution of (6) is a pair v, y such that

$$
v \in T (y),
$$

$$
c _ {k} v + y - x ^ {k - 1} = r \approx 0.
$$

The sum of the two terms, $c_{k}v$ and $y - x^{k-1}$ would ideally be zero. Instead of zero, we may get r at an approximate solution. To estimate the relative error in the relation

$$
c _ {k} v + y - x ^ {k - 1} = r \approx 0,
$$

one has to look at the ratios between $\| r \|$ (the error) and $\| c_k v \|$, $\| r \|$ and $\| y - x^{k-1} \|$, i.e., the quantities

$$
\frac {\| r \|}{\| c _ {k} v \|}, \quad \frac {\| r \|}{\| y - x ^ {k - 1} \|}.
$$

In this sense, (8) may be interpreted as a relative error tolerance, even taking $\varepsilon_{k}=0$.

Still in Ref. 21, it was observed (without a convergence analysis) that a summable error could also be used at the right hand side of inequality (8) (see Ref. 21, Eq. (4.3)):

$$
\| c _ {k} \tilde {v} ^ {k} + \tilde {x} ^ {k} - x ^ {k - 1} \| ^ {2} + 2 c _ {k} \varepsilon_ {k} \leq \delta_ {k}, \quad \sum \delta_ {k} <   + \infty .
$$

Let us survey the convergence results for the above-mentioned methods. The classical proximal point method converges weakly to a solution and diverges if the solution set is empty (Ref. 11). An example of weak convergence

without strong convergence was given in Ref. 6. Regarding the perturbed proximal point method for optimization, besides weak convergence of the iterates (when the solution set is nonempty), the functional values of the iterates converges to the infimum of the function, even if the solution set is empty [Ref. 15, Section 5]. The perturbed proximal point method was studied in Ref. 17 in finite dimensional spaces and convergence to a solution was proved. The case of an empty solution set was not studied in this work. The hybrid extragradient proximal point method was proposed in Ref. 21 in Hilbert spaces. Weak convergence to a solution and divergence in the case of empty solution set were proved.

We propose an extension of the approximation criterion for the hybrid extragradient proximal point method. First, we combine both criteria (summable error and relative error) for approximate solutions of the proximal system (6). Second, the extragradient step is relaxed to

$$
x ^ {k} \approx x ^ {k - 1} - c _ {k} \tilde {v} ^ {k}. \tag {10}
$$

In some applications, instead of $\tilde{v}^{k}$, what is available is $\hat{v}^{k}$, an approximation of $\tilde{v}^{k}$. In this case, an exact extragradient step cannot be performed. Since $\hat{v}^{k} \approx \tilde{v}^{k}$, we have

$$
x ^ {k - 1} - c _ {k} \hat {v} ^ {k} \approx x ^ {k - 1} - c _ {k} \tilde {v} ^ {k}.
$$

So, taking $x^{k} = x^{k-1} - c_{k}\hat{v}^{k}$, we get an approximated extragradient step as described in (10). The proposed algorithm also provides a unified framework for convergence analysis of the classical proximal point method, the perturbed proximal point method for optimization (Ref. 15), the perturbed proximal point method (Ref. 17), and the hybrid extragradient proximal method.

The paper is organized as follows. In Section 2 we define the algorithm and analyze its connection with the algorithms cited above. In Section 3, under mild assumptions we establish weak convergence of each sequence generated by the algorithm to a solution of the original Problem (P). Finally, we prove unboundedness of the sequence in the case of empty solution set.

# 2 Algorithm

From now on $H$ will be a real Hilbert space. In order to present the method we recall Burachik, Iusem and Svaiter's definition of enlargement of a maximal monotone operator (Refs. 17, 19, 20).

Definition 1 Let $\varepsilon \geq 0$, the operator $T^{\varepsilon} \colon H \to \mathcal{P}(H)$ is defined as

$$
T ^ {\varepsilon} (x) = \{v \in H \mid \langle w - v, z - x \rangle \geq - \varepsilon \text {for all} (z, w) \in G (T) \}.
$$

It follows that $T^0 = T$ and for each $x \in H$

$$
T ^ {\varepsilon_ {1}} (x) \subseteq T ^ {\varepsilon_ {2}} (x) \quad \text {if} \quad 0 \leq \varepsilon_ {1} \leq \varepsilon_ {2}.
$$

In particular it holds that

$$
T (x) \subseteq T ^ {\varepsilon} (x) \quad \text {for all} \quad \varepsilon \geq 0.
$$

So, $T^{\varepsilon}$ is indeed an enlargement of T, in a similar way in which the $\varepsilon$-subdifferential is an enlargement of the subdifferential.

Remark 1 Let $f:H\to\mathbb{R}\cup\{+\infty\}$ be a proper closed convex function. Then $\partial f:H\to\mathcal{P}(H)$ is maximal monotone and for $T=\partial f$, it holds that

$$
\partial_ {\varepsilon} f (x) \subseteq T ^ {\varepsilon} (x) = (\partial f) ^ {\varepsilon} (x)
$$

for any $x \in H$, $\varepsilon \geq 0$. The inclusion is proper in the general case (see Ref. 17 for an example).

# Algorithm 2.1 Inexact Hybrid Extragradient-Proximal Algorithm

(i) Initialization. Take $x^0 \in H$, $k = 0$.

(ii) Iterative step. Given $x^{k - 1} \in H$, and $c_k > 0$, take

$$
x ^ {k} \approx x ^ {k - 1} - c _ {k} \tilde {v} ^ {k}
$$

where for some $\tilde{y}^{k}$, the pair $\tilde{y}^{k}$, $\tilde{v}^{k}$ is an approximate solution of the system

$$
v \in T (y)
$$

$$
c _ {k} v + y - x ^ {k - 1} = 0,
$$

in the following sense: for some $\varepsilon_{k} \geq 0$,

$$
\tilde {v} ^ {k} \in T ^ {\varepsilon_ {k}} (\tilde {y} ^ {k}), \tag {11a}
$$

$$
\| c _ {k} \tilde {v} ^ {k} + \tilde {y} ^ {k} - x ^ {k - 1} \| ^ {2} + 2 c _ {k} \varepsilon_ {k} \leq \delta_ {k} + \sigma_ {k} ^ {2} \| \tilde {y} ^ {k} - x ^ {k - 1} \| ^ {2}, \tag {11b}
$$

$$
\| x ^ {k} - (x ^ {k - 1} - c _ {k} \tilde {v} ^ {k}) \| \leq \alpha_ {k}, \tag {11c}
$$

where $\{c_k\}$, $\{\delta_k\}$, $\{\sigma_k\}$ and $\{\alpha_k\}$ are nonnegative and

$$
\sum \delta_ {k} <   + \infty , \quad \sum \alpha_ {k} <   + \infty . \tag {12a}
$$

$$
0 <   \sigma_ {k} \leq \sigma <   1, \quad c _ {k} \geq c > 0, \tag {12b}
$$

for all k. The assumption on $\{c_{k}\}$ is a standard assumption in the setting of proximal point methods. We will prove convergence of the algorithm under the above approximation criteria. We point out that $\varepsilon_{k}$, $\tilde{y}^{k}$ and $\tilde{v}^{k}$ do not need to be explicitly computed. More precisely, if a sequence $\{x^{k}\}$ is generated by the classical proximal point method (Ref. 11), then there exist sequences $\{\tilde{y}^{k}\}$, $\{\tilde{v}^{k}\}$, $\{\varepsilon_{k}\}$ satisfying, together with $\{x^{k}\}$, conditions (11) - (12). This will be stated formally and proved in (A) below.

Observe that the errors allowed are bounded by the terms $\alpha_{k}$, $\delta_{k}$ and $\sigma_{k}$. For instance, if $\delta_{k} = \sigma_{k} = 0$, then $\varepsilon_{k}$ needs to be zero. In this case, $\tilde{v}^{k} \in T(\tilde{y}^{k})$ and $\tilde{y}^{k} = x^{k-1} - c_{k}\tilde{v}^{k}$ is the exact solution of the proximal problem $0 \in c_{k}T(x) + x - x^{k-1}$. If we also have that $\alpha_{k} = 0$, then we retrieve an exact proximal iteration.

Some more words concerning tolerances in (11). Assume that T is a point-to-point operator given by a closed formula and that we are not using its enlargement. The summable error tolerance $\delta_{k}$ and the relative error tolerance $\sigma_{k}$ allows for solving inexactly the proximal subproblem, which is connected to evaluating

$$
(c _ {k} T + I) ^ {- 1} (x ^ {k - 1}).
$$

In a computational implementation, due to truncation, roundings, etc, given x, the calculation of

$$
v = T (x),
$$

(even by a closed formula) may produce some small errors. To deal with these errors, we have the error tolerance $\alpha_{k}$ in the extragradient step. It is natural to expect that, in principle, the errors on evaluating $T(\cdot)$ are considerably smaller than those in evaluating $(c_{k}T + I)^{-1} (\cdot)$. So, our approach is to consider a summable error tolerance for the extragradient step. It would be better if the extragradient step error tolerance were relative, rather than absolute. Unfortunately, our convergence analysis does not apply when there are relative errors in the extragradient step.

We claim that Algorithm 2.1, together with approximation criteria (11)-(12) generalizes the classical proximal method, the perturbed proximal point method and the hybrid extragradient-proximal method. We claim also that the convergence analysis of Algorithm 2.1 is applicable to the perturbed proximal point method for optimization. Let us verify the first claim.

(A) Classical Proximal Method:

In this method, the sequence $\{x^{k}\}$ satisfies

$$
\| x ^ {k} - P _ {k} (x ^ {k - 1}) \| \leq \alpha_ {k}, \quad \sum \alpha_ {k} <   \infty ,
$$

where

$$
P _ {k} := (c _ {k} T + I) ^ {- 1},
$$

and $c_{k}\geq c > 0$.Defining

$$
\tilde {y} ^ {k} := P _ {k} (x ^ {k - 1}), \tilde {v} ^ {k} := (1 / c _ {k}) (x ^ {k - 1} - \tilde {y} ^ {k}),
$$

we have

$$
\tilde {v} ^ {k} \in T (\tilde {y} ^ {k}), \tag {13a}
$$

$$
\| c _ {k} \tilde {v} ^ {k} + \tilde {y} ^ {k} - x ^ {k - 1} \| = 0. \tag {13b}
$$

and

$$
\| x ^ {k} - (x ^ {k - 1} - c _ {k} \tilde {v} ^ {k}) \| = \| x ^ {k} - P _ {k} (x ^ {k - 1}) \| \leq \alpha_ {k}.
$$

Recall that $T^{0}=T$. Therefore, setting $\varepsilon_{k}=\delta_{k}=\sigma_{k}=0$ for all k, we have a valid sequence for Algorithm 2.1, with approximation criteria (11)-(12).

(B) Perturbed Proximal Point Method.

Consider the sequence $\{x^{k}\}$ generated by the rule

$$
0 \in c _ {k} T ^ {\varepsilon_ {k}} (x ^ {k}) + x ^ {k} - x ^ {k - 1}, \quad \sum c _ {k} \varepsilon_ {k} <   \infty , \tag {14}
$$

with $0 < \hat{c} \leq c_k$.

Let us prove that (14) is a particular instance of Algorithm 2.1. Indeed, consider in Algorithm 2.1 the same choice of $\varepsilon_{k}$ as in (14), $\sigma_{k} = \alpha_{k} = 0$, $\delta_{k} = 2c_{k}\varepsilon_{k}$ for all $k \in N$. Take also $\tilde{y}^{k} = x^{k}$ and $\tilde{v}^{k} = (1/c_{k})(x^{k-1} - x^{k})$. Then, algorithm (14) coincides with a particular instance of Algorithm 2.1 with approximation criteria (11)-(12).

(C) Hybrid Extragradient Proximal Point Method.

In this method, the new iterate is given by

$$
x ^ {k} = x ^ {k - 1} - c _ {k} \tilde {v} ^ {k},
$$

where $\tilde{v}^k\in T^{\varepsilon_k}(\tilde{y}^k)$ and

$$
\| c _ {k} \tilde {v} ^ {k} + \tilde {y} ^ {k} - x ^ {k - 1} \| ^ {2} + 2 c _ {k} \varepsilon_ {k} \leq \sigma_ {k} ^ {2} \| \tilde {y} ^ {k} - x ^ {k - 1} \| ^ {2},
$$

with $0 < \sigma_{k} \leq \sigma < 1$ and $0 < \hat{c} \leq c_{k}$. Taking $\delta_{k} = \alpha_{k} = 0$, we have a valid sequence for Algorithm 2.1, with approximation criteria (11)-(12).

For verifying the second claim, regarding the perturbed proximal point method for optimization, let $\{x^{k}\}$ be a sequence satisfying (3). Take $T = \partial f$. Using Remark 2.1, $\partial_{\varepsilon_{k}} f(x^{k}) \subset T^{\varepsilon_{k}}(x^{k})$ and

$$
(c _ {k} \partial_ {\varepsilon_ {k}} f + I) ^ {- 1} (x ^ {k - 1}) \subseteq (c _ {k} T ^ {\varepsilon_ {k}} + I) ^ {- 1} (x ^ {k - 1}).
$$

Therefore, such sequence $\{x^{k}\}$ satisfies also (14). As the perturbed proximal point method (B) is a particular case of Algorithm 2.1, the second claim follows.

As we have seen, Algorithm 2.1 provides a unified framework for studying many variations of the proximal point method, previously unrelated. For this reason, the convergence proof is somewhat involved. Even though, the convergence result of this method is the same as the one that holds for the classical proximal point method: weak convergence to a solution when the solution set is not empty, and divergence otherwise.

# 3 Convergence Analysis

From now on, $\{x^{k}\}$, $\{\tilde{y}^{k}\}$ and $\{\tilde{v}^{k}\}$ are sequences generated by Algorithm 2.1, with parameters $\{\varepsilon_{k}\}$, $\{c_{k}\}$, $\{\delta_{k}\}$, and $\{\sigma_{k}\}$ satisfying (11)-(12). The main result we shall prove is the following:

Theorem 3.1 If the solution set of problem (P) is not empty, then $\{x^{k}\}$ converges weakly to a solution. If the solution set of problem (P) is empty, then $\{x^{k}\}$ is unbounded.

To prove this theorem, we will need some intermediate results. Define an auxiliary sequence

$$
z ^ {k} := x ^ {k - 1} - c _ {k} \tilde {v} ^ {k}. \tag {15}
$$

Observe that $z^{k}$ corresponds to the “exact” extragradient step.

We begin with a technical lemma used to deduce some key properties of the sequences generated by Algorithm 2.1.

Lemma 3.1 Let $x^{*} \in H$ be a solution of problem (P). Then, for all $k$,

$$
| | x ^ {*} - x ^ {k - 1} | | ^ {2} - | | x ^ {*} - z ^ {k} | | ^ {2} \geq (1 - \sigma_ {k} ^ {2}) | | \tilde {y} ^ {k} - x ^ {k - 1} | | ^ {2} - \delta_ {k},
$$

Proof. By definition of norm in a Hilbert space we obtain

$$
\begin{aligned} | | x ^ {*} - x ^ {k - 1} | | ^ {2} - | | x ^ {*} - z ^ {k} | | ^ {2} &= | | x ^ {*} - \tilde {y} ^ {k} + (\tilde {y} ^ {k} - x ^ {k - 1}) | | ^ {2} \\ - | | x ^ {*} - \tilde {y} ^ {k} + (\tilde {y} ^ {k} - z ^ {k}) | | ^ {2} \\ &= 2 \langle z ^ {k} - x ^ {k - 1}, x ^ {*} - \tilde {y} ^ {k} \rangle + | | \tilde {y} ^ {k} - x ^ {k - 1} | | ^ {2} \\ - | | \tilde {y} ^ {k} - z ^ {k} | | ^ {2}. \\ \end{aligned}
$$

On the other hand, as $0 \in T(x^{*})$ and $\tilde{v}^k \in T^{\varepsilon_k}(\tilde{y}^k)$, we have by definition of $T^{\varepsilon_k}$ :

$$
c _ {k} \left\langle 0 - \tilde {v} ^ {k}, x ^ {*} - \tilde {y} ^ {k} \right\rangle \geq - c _ {k} \varepsilon_ {k}.
$$

Combining the expression above with (15), we get

$$
\langle z ^ {k} - x ^ {k - 1}, x ^ {*} - \tilde {y} ^ {k} \rangle \geq - c _ {k} \varepsilon_ {k}.
$$

Thus we have

$$
| | x ^ {*} - x ^ {k - 1} | | ^ {2} - | | x ^ {*} - z ^ {k} | | ^ {2} \geq | | \tilde {y} ^ {k} - x ^ {k - 1} | | ^ {2} - | | \tilde {y} ^ {k} - z ^ {k} | | ^ {2} - 2 c _ {k} \varepsilon_ {k}.
$$

Now, the desired result follows from (11). In fact, we have that

$$
| | \tilde {y} ^ {k} - z ^ {k} | | ^ {2} + 2 c _ {k} \varepsilon_ {k} = | | \tilde {y} ^ {k} - x ^ {k - 1} + c _ {k} \tilde {v} ^ {k} | | ^ {2} + 2 c _ {k} \varepsilon_ {k} \leq \delta_ {k} + \sigma_ {k} ^ {2} | | \tilde {y} ^ {k} - x ^ {k - 1} | | ^ {2}.
$$

Using the last two inequalities, we gather

$$
\begin{aligned} | | x ^ {*} - x ^ {k - 1} | | ^ {2} - | | x ^ {*} - z ^ {k} | | ^ {2} &\geq | | \tilde {y} ^ {k} - x ^ {k - 1} | | ^ {2} - (| | \tilde {y} ^ {k} - z ^ {k} | | ^ {2} + 2 c _ {k} \varepsilon_ {k}) \\ &\geq \left. \left| \left| \tilde {y} ^ {k} - x ^ {k - 1} \right| \right| ^ {2} - \left(\delta_ {k} + \sigma_ {k} ^ {2} \right| \left| \tilde {y} ^ {k} - x ^ {k - 1} \right| \right| ^ {2}) \\ &= (1 - \sigma_ {k} ^ {2}) | | \tilde {y} ^ {k} - x ^ {k - 1} | | ^ {2} - \delta_ {k}. \\ \end{aligned}
$$

The proof is complete.

Now we are able to give the first estimative on the behavior of the distance of the iterates $x^{k}$ to the solution set.

Corollary 3.1 Let $x^{*} \in H$ be a solution of Problem (P). Then, for all $k$

$$
\| x ^ {k} - x ^ {*} \| \leq \alpha_ {k} + \sqrt {\| x ^ {k - 1} - x ^ {*} \| ^ {2} + \delta_ {k}}. \tag {16}
$$

Proof. Using the triangle inequality, (15) and the second condition in (11) we get:

$$
\begin{aligned} \| x ^ {k} - x ^ {*} \| &\leq \| x ^ {k} - z ^ {k} \| + \| z ^ {k} - x ^ {*} \| \\ &\leq \alpha_ {k} + \| z ^ {k} - x ^ {*} \|. \\ \end{aligned}
$$

By Lemma 3.1

$$
\begin{aligned} \| z ^ {k} - x ^ {*} \| &\leq \sqrt {\| x ^ {k - 1} - x ^ {*} \| ^ {2} + \delta_ {k} - (1 - \sigma_ {k} ^ {2}) \| \tilde {y} ^ {k} - x ^ {k - 1} \| ^ {2}} \\ &\leq \sqrt {\| x ^ {k - 1} - x ^ {*} \| ^ {2} + \delta_ {k}}, \\ \end{aligned}
$$

and the desired result follows.

The next lemma, which can be found in Ref. 27, Lemma 2.2.2, will be the basic tool for deriving the first convergence result.

Lemma 3.2 Let $\{\alpha_k\}$, $\{\delta_k\}$ and $\{\gamma_k\}$ be sequences of nonnegative scalars such that the following conditions are satisfied:

(i) $\sum_{k=0}^{\infty} \delta_k < \infty$ and $\sum_{k=0}^{\infty} \alpha_k < \infty$,  
(ii) $\gamma_{k + 1}\leq \alpha_{k} + \sqrt{\gamma_{k}^{2} + \delta_{k}}$ for all $k\in N$

Then $\{\gamma_k\}$ converges to some $L\in \mathbb{R}_{+}$.

Corollary 3.2 For any $x^*$, solution of (P), the sequence $\{ \| x^k - x^* \| \}$ converges to some $L \in \mathbb{R}_+$.

Proof. Take $\gamma_{k} := \|x^{k-1} - x^{*}\|$. By Corollary 3.1 and (12), Lemma 3.2 applies. Hence, the conclusion holds.

The next result gives tools that allow us to derive the convergence theorem.

Corollary 3.3 Suppose that problem (P) has solutions. Then it holds that

(i) The sequence $\{x^k\}$ is bounded.  
(ii) $\lim_{k\to \infty}\| x^{k - 1} - \tilde{y}^k\| = 0.$  
(iii) $\lim_{k\to \infty}\varepsilon_k = 0.$  
(iv) $\lim_{k\to \infty}\| \tilde{v}^k\| = 0,\lim_{k\to \infty}\| c_k\tilde{v}^k\| = 0.$

Proof. Take $x^{*}$ a solution of problem (P). From Corollary 3.2, it follows that

$$
\lim _ {k \to \infty} \| x ^ {k} - x ^ {*} \| = L \in \mathbb {R} _ {+}. \tag {17}
$$

Hence, item (i) holds. We proceed to prove (ii). By Lemma 3.1 and the fact that $\sigma_{k} \leq \sigma < 1$, we have that

$$
(1 - \sigma^ {2}) \| \tilde {y} ^ {k} - x ^ {k - 1} \| ^ {2} \leq \| x ^ {k - 1} - x ^ {*} \| ^ {2} - \| z ^ {k} - x ^ {*} \| ^ {2} + \delta_ {k}. \tag {18}
$$

Now, as $\lim_{k\to \infty}\| x^k -z^k\| \leq \lim_{k\to \infty}\alpha_k = 0$, and using also (17) it follows that

$$
\lim _ {k \to \infty} \| z ^ {k} - x ^ {*} \| = L. \tag {19}
$$

Combining (17), (18), (19), and taking into account that $\lim_{k\to \infty}\delta_k = 0$, we conclude that item (ii) holds.

Recall that, according to (11),

$$
\| c _ {k} \tilde {v} ^ {k} + \tilde {y} ^ {k} - x ^ {k - 1} \| ^ {2} + 2 c _ {k} \varepsilon_ {k} \leq \delta_ {k} + \sigma_ {k} ^ {2} \| \tilde {y} ^ {k} - x ^ {k - 1} \| ^ {2}.
$$

Since $\sigma_{k}$ is bounded, using also item (ii) and the nonnegativity of $c_{k}$, we conclude that

$$
\lim _ {k \to \infty} \| c _ {k} \tilde {v} ^ {k} + \tilde {y} ^ {k} - x ^ {k - 1} \| = \lim _ {k \to \infty} c _ {k} \varepsilon_ {k} = 0 \tag {20}
$$

Since $c_k$ is bounded away from zero, we conclude that item (iii) holds. To prove item (iv), observe that

$$
\| c _ {k} \tilde {v} ^ {k} \| \leq \| c _ {k} \tilde {v} ^ {k} + \tilde {y} ^ {k} - x ^ {k - 1} \| + \| \tilde {y} ^ {k} - x ^ {k - 1} \|.
$$

Combining this with item (ii) and (20), we obtain that $\lim_{k\to\infty}\|c_{k}\tilde{v}^{k}\|=0$. Using again that $c_{k}$ is bounded away from zero, the first claim of item (iv) follows.

Lemma 3.3 If the solution set of problem (P) is not empty, then $\{x^{k}\}$ converges weakly to a solution.

Proof. First we claim that any weak cluster point of $\{x^{k}\}$ is a solution of problem (P). Indeed, let $\bar{x}$ be a weak cluster point of $\{x^{k}\}$. By Corollary 3.3(ii), $\bar{x}$ is also a weak cluster point of $\{\tilde{y}^{k}\}$. Hence, there exists a subsequence $\{\tilde{y}^{k_{j}}\}$ converging weakly to $\bar{x}$ :

$$
\tilde {y} ^ {k _ {j}} \xrightarrow {w} \bar {x}.
$$

Observe also that, from Corollary 3.3(iii)-(iv):

$$
\begin{array}{l} \tilde {v} ^ {k _ {j}} \stackrel {{\| \cdot \|}} {{\longrightarrow}} 0, \\ \varepsilon_ {k _ {j}} \rightarrow 0. \\ \end{array}
$$

Since $\tilde{v}^{k_j} \in T^{\varepsilon_{k_j}}(\tilde{y}^{k_j})$, and $T^\varepsilon$ has a demiclosed graph (Ref. 19), it follows that $0 \in T(\bar{x})$. In other words, $\bar{x}$ is a solution of (P).

By Corollary 3.3(i), $\{x^k\}$ is bounded. So, it has some weak cluster point, say $\bar{x}$, which by the first part of the proof, is a solution of (P). Now we shall prove that the whole sequence converges weakly to $\bar{x}$. Since $\{x^k\}$ is bounded, it is enough to prove that $\bar{x}$ is the unique weak cluster point. Suppose there exists another weak cluster point $\bar{z} \neq \bar{x}$ of $\{x^k\}$. By the first part of the proof, $\bar{z}$ is a solution of (P). Let $\{x^{k_j}\}$ and $\{x^{k_i}\}$ be two subsequences of $\{x^k\}$ converging weakly to $\bar{x}$ and $\bar{z}$, respectively:

$$
x ^ {k _ {j}} \stackrel {w} {\longrightarrow} \bar {x}, \quad x ^ {k _ {i}} \stackrel {w} {\longrightarrow} \bar {z}.
$$

Using the Opial lemma (Ref. 28) we get

$$
\begin{aligned} \operatorname * {l i m i n f} _ {j} \| x ^ {k _ {j}} - \bar {z} \| &> \operatorname * {l i m i n f} _ {j} \| x ^ {k _ {j}} - \bar {x} \|, \\ \operatorname * {l i m i n f} _ {i} \| x ^ {k _ {i}} - \bar {x} \| &> \operatorname * {l i m i n f} _ {i} \| x ^ {k _ {i}} - \bar {z} \|. \\ \end{aligned}
$$

Using also Corollary 3.2, we conclude that

$$
\begin{aligned} \lim _ {k} \| x ^ {k} - \bar {z} \| &> \lim _ {k} \| x ^ {k} - \bar {x} \|, \\ \lim _ {k} \| x ^ {k} - \bar {x} \| &> \lim _ {k} \| x ^ {k} - \bar {z} \|, \\ \end{aligned}
$$

which is a contradiction.

![](images/fe4a1e88379f5dd73452f818421784c07209c3f90ee714b912198be6c59059cb.jpg)

We note that the main part of the proof of the following lemma is similar to the proof of Theorem 1 in Ref. 11.

For $A \subset H$ , we denote by $A^{\circ}$ the interior of A. Given a closed and convex set C, we recall that $N_{C}$ , the normality operator associated to the convex set C, is $N_{C}(z) := \{w \in H \mid \langle w, z - u \rangle \geq 0 \quad \forall u \in C\}$ if $z \in C$ , and $\emptyset$ otherwise.

Lemma 3.4 If the solution set of problem (P) is empty, then $x^{k}$ is unbounded.

Proof. Suppose, for purposes of contradiction, that $T^{-1}(0)=\emptyset$, and that $\{x^{k}\}$ is bounded. Now we claim that $\{\tilde{y}^{k}\}$ is also bounded. Observe that $\|x^{k}-z^{k}\|\leq\alpha_{k}$, and hence, $\{z^{k}\}$ is also bounded. Since $z^{k}=x^{k}-c_{k}\tilde{v}^{k}$, it follows also that $\{c_{k}\tilde{v}^{k}\}$ is bounded. Recall that, according to (11),

$$
\| c _ {k} \tilde {v} ^ {k} + \tilde {y} ^ {k} - x ^ {k - 1} \| ^ {2} + 2 c _ {k} \varepsilon_ {k} \leq \delta_ {k} + \sigma_ {k} ^ {2} \| \tilde {y} ^ {k} - x ^ {k - 1} \| ^ {2}.
$$

Define $t_{k} := \|\tilde{y}^{k} - x^{k-1}\|$. Expanding the square in the left hand side of the above inequality, and using Cauchy-Schwartz inequality,

$$
\| c _ {k} \tilde {v} ^ {k} \| ^ {2} - 2 \| c _ {k} \tilde {v} ^ {k} \| t _ {k} + t _ {k} ^ {2} + 2 c _ {k} \varepsilon_ {k} \leq \delta_ {k} + \sigma_ {k} ^ {2} t _ {k} ^ {2}.
$$

Since $c_{k}\varepsilon_{k}\geq 0$ and $\sigma_{k}\leq \sigma$, we obtain

$$
\| c _ {k} \tilde {v} ^ {k} \| ^ {2} - 2 \| c _ {k} \tilde {v} ^ {k} \| t _ {k} + t _ {k} ^ {2} \leq \delta_ {k} + \sigma^ {2} t _ {k} ^ {2}.
$$

Rearranging the expression above, we get

$$
(1 - \sigma^ {2}) t _ {k} ^ {2} - 2 \| c _ {k} \tilde {v} ^ {k} \| t _ {k} + \| c _ {k} \tilde {v} ^ {k} \| ^ {2} - \delta_ {k} \leq 0.
$$

Since $\{\|c_k\tilde{v}^k\|\}$ and $\{\delta_k\}$ converge to zero, take $d \geq \max_k \|c_k\tilde{v}^k\|$ and $\delta \geq \max_k \delta_k$. Then,

$$
(1 - \sigma^ {2}) t _ {k} ^ {2} - 2 d t _ {k} \leq \delta .
$$

Therefore, $\{t_k\}$ is bounded. So $\{\tilde{y}^k\}$ is also bounded.

Our aim now is to define a related operator, say U, such that $U^{-1}(0) \neq \emptyset$, and the sequences $\{x^{k}\}$, $\{\tilde{y}^{k}\}$, $\{\tilde{v}^{k}\}$, and $\{z^{k}\}$ satisfy conditions (11)-(12) of Algorithm 2.1 applied to find a zero of U. In order to define such an operator, take $z_{0}$ in the domain of T, and some M > 0 such that

$$
\begin{array}{l} \| z _ {0} \| <   M, \\ \| x ^ {k} \| <   M, \| \tilde {y} ^ {k} \| <   M, \quad \forall k. \\ \end{array}
$$

Let $S$ be the closed ball with radius $2M$ and center 0,

$$
S := \{x \in H \mid \| x \| \leq 2 M \}.
$$

Define

$$
U := T + N _ {S},
$$

where $N_{S}$ stands for the normality operator associated to S. Observe that $z_{0} \in D(T) \cap S^{\circ}$. Therefore, from Ref. 29, Theorem 1, it follows that U is

maximal monotone. Furthermore, U has a bounded domain and hence is onto (see Ref. 30). In particular,

$$
U ^ {- 1} (0) \neq \emptyset .
$$

Observe that for proving that the mentioned sequences satisfy conditions (11)-(12) for finding a zero of $U$, it is enough to check the approximated inclusion $\tilde{v}^k \in U^{\varepsilon_k}(\tilde{y}^k)$ for all $k$. In other words, we must show that $\forall (w,z) \in G(U)$,

$$
\langle w - \tilde {v} ^ {k}, z - \tilde {y} ^ {k} \rangle \geq - \varepsilon^ {k}.
$$

Take $(w,z)\in G(U)$. By definition of $U$,

$$
w = u + \eta ,
$$

for some $u \in T(z)$ and $\eta \in N_S(z)$. Note that $\tilde{v}^k \in T^{\varepsilon_k}(\tilde{y}^k)$ and $\tilde{y}^k \in S^\circ$. Therefore by the definition of normal cone and Definition 1 it follows that

$$
\langle u - \tilde {v} ^ {k}, z - \tilde {y} ^ {k} \rangle \geq - \varepsilon^ {k},
$$

and

$$
\langle \eta , z - \tilde {y} ^ {k} \rangle \geq 0,
$$

for all $k \in N$. Hence by summing this two inequalities we get

$$
\langle w - \tilde {v} ^ {k}, z - \tilde {y} ^ {k} \rangle \geq - \varepsilon^ {k},
$$

for all $k \in N$. Since $(z, w)$ is an arbitrary point of the graph of $U$ we conclude that

$$
\tilde {v} ^ {k} \in U ^ {\varepsilon_ {k}} (\tilde {y} ^ {k}),
$$

for each $k\in N$

Now we can apply Lemma 3.3 to the operator U and we get that the sequence $\{x^{k}\}$ is weakly convergent to an element $\bar{x}$ in $U^{-1}(0)$. In other words, $0 \in T(\bar{x}) + N_{S}(\bar{x})$. Since $||x^{k}|| < M$ for all $k \in N$, it holds that $||\bar{x}|| \leq M$. Hence, $\bar{x} \in S^{\circ}$, so it must be $N_{S}(\bar{x}) = \{0\}$. Therefore $0 \in T(\bar{x})$, which is in contradiction with our assumptions. Thus the sequence $\{x^{k}\}$ is unbounded.

Clearly, the last two lemmas imply Theorem 3.1.

# References

1. ROCKAFELLAR, R. T. and WETS, R. J.-B., Variational analysis, Springer-Verlag, Berlin, 1998.  
2. ROBINSON, S. M., Generalized equations and their solutions. I. Basic theory, Mathematical Programming Study, No. 10, pp. 128–141, 1979.  
3. ZEIDLER, E., Nonlinear functional analysis and its applications. II/B, Nonlinear monotone operators, Springer-Verlag, New York, 1990.  
4. ECKSTEIN, J. and BERTSEKAS, D. P., On the Douglas-Rachford splitting method and the proximal point algorithm for maximal monotone operators, Mathematical Programming, Vol. 55, pp. 293-318, 1992.  
5. FERRIS, M. C., Finite termination of the proximal point algorithm, Mathematical Programming, Vol. 50, No. 3, (Ser. A), pp. 359–366, 1991.  
6. GÜLER, O., New proximal point algorithms for convex minimization, Society for Industrial and Applied Mathematics. Journal on Optimization, Vol. 2, No. 4, pp. 649–664, 1992.  
7. LUQUE, F. J., Asymptotic convergence analysis of the proximal point algorithm, Society for Industrial and Applied Mathematics. Journal on Control and Optimization, Vol. 22, No. 2, pp. 277–293, 1984.  
8. MARTINET, B., Régularisation d'inéquations variationnelles par approximations successives, Revue Française d'Informatique et Recherche Opérationnelle, Vol. 4, pp. 154–158, 1970.  
9. MARTINET, B., Algorithms pour la résolution de problèmes d'optimisation et minimax, Université de Grenoble, PhD Thesis, 1972.  
10. MOREAU, J. J., Proximité et dualité dans un espace Hilbertien, Bulletin de la Société Mathematique de France, Vol. 93, pp. 273–299, 1965.  
11. ROCKAFELLAR, R. T., Monotone operators and the proximal point algorithm, Society for Industrial and Applied Mathematics. Journal on Control and Optimization, Vol. 14, No. 5, pp. 877–898, 1976.  
12. ROCKAFELLAR, R. T., Augmented Lagrangians and applications of the proximal point, Mathematics of Operations Research, Vol. 1, No. 2, pp. 97–116, 1976.  
13. LEMAIRE, B., The proximal algorithm, New methods in optimization and their industrial uses (Pau/Paris, 1987), Birkhäuser, Basel, pp. 73-87, 1989.  
14. BR∅NDSTED, A. and ROCKAFELLAR, R. T., On the subdifferentiability of convex functions, Proceedings of the American Mathematical Society, Vol. 16, pp. 605–611, 1965.  
15. LEMAIRE, B., About the convergence of the proximal method, Advances in optimization, Lecture Notes in Economics and Mathematical Systems, Springer-Verlag, Berlin, Germany, Vol 382, pp. 39–51, 1992.  
16. AUSLENDER, A., Numerical methods for nondifferentiable convex optimization, Mathematical Programming Studies, No. 30, pp. 102–126, 1987.  
17. BURACHIK, R. S., IUSEM, A. N. and SVAITER, B. F., Enlargement of monotone operators with applications to variational inequalities, Set-Valued Analysis, Vol. 5, No. 2, pp. 159–180, 1997.  
18. BREGMAN, L. M., The projection method for solving systems of linear inequalities, Akademiya Nauk SSSR. Sibirskoe Otdelenie. Sibirskii Matematicheskii Zhurnal, Vol. 29, No. 4, pp. 23–30, 1988.  
19. BURACHIK, R. S., SAGASTIZÁBAL, C. A. and SVAITER, B. F., ε-enlargements of maximal monotone operators: theory and applications, Reformulation: nonsmooth, piecewise smooth, semismooth and smoothing methods (Lausanne, 1997), Kluwer Academic Publishers, Dordrecht, pp. 25–43, 1999.  
20. BURACHIK, R. S. and SVAITER, B. F., $\epsilon$-enlargements of maximal monotone operators in Banach spaces, Set-Valued Analysis, Vol. 7, No. 2, pp. 117–132, 1999.  
21. SOLODOV, M. V. and SVAITER, B. F., A hybrid approximate extragradient-proximal point algorithm using the enlargement of a maximal monotone operator, Set-Valued Analysis, Vol. 7, No. 4, pp. 323–345, 1999.  
22. SOLODOV, M.V. and SVAITER, B.F., Error Bounds for Proximal Point Subproblems and Associated Inexact Proximal Point Algorithms, Mathematical Programming, Vol. 88, No. 2, pp. 371–389, 2000.  
23. AUCHMUTY, G., Variational principles for variational inequalities, Numerical Functional Analysis and Optimization, Vol. 10, No. 9–10, pp. 863–874, 1989.  
24. FUKUSHIMA, M., Equivalent differentiable optimization problems and descent methods for asymmetric variational inequality problems, Mathematical Programming, Vol. 53, No. 1, (Ser. A), pp. 99–110, 1992.  
25. BURACHIK, R. S., SAGASTIZÁBAL, C. and Svaiter, B. F., Bundle methods for maximal monotone operators, Ill-posed variational problems and regularization techniques (Trier, 1998), Springer-Verlag, Berlin, pp. 49–64, 1999.  
26. KORPELEVICH, G.M., The Extragradient Method for Finding Saddle Points end other Problems, Matecon, Vol. 12, pp. 747–756, 1976.  
27. Polyak, B. T., Introduction to optimization, Optimization Software Inc., Publications Division, New York, New York, 1987.  
28. OPIAL, Z., Weak convergence of the sequence of successive approximations for nonexpansive mappings, Bulletin of the American Mathematical Society, Vol. 73, pp. 591–597, 1967.  
29. ROCKAFELLAR, R. T., On the maximality of sums of nonlinear monotone operators, Translations of the American Mathematical Society, Vol. 149, pp. 75–88, 1970.  
30. BRÉZIS, H., Opérateurs maximaux monotones et semi-groupes de contractions dans les espaces de Hilbert, Mathematical Studies, North-Holland, Amsterdam, The Netherlands, Vol. 5, 1973.
