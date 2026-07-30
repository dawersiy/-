# SPLITTING ALGORITHMS FOR THE SUM OF TWO NONLINEAR OPERATORS*

P. L. LIONS† AND B. MERCIER‡

Abstract. Splitting algorithms for the sum of two monotone operators.

We study two splitting algorithms for (stationary and evolution) problems involving the sum of two monotone operators. These algorithms are well known in the linear case and are here extended to the case of multivalued monotone operators. We prove the convergence of these algorithms, we give some applications to the obstacle problem and to minimization problems; and finally we present numerical computations comparing these algorithms to some other classical methods.

We consider the nonlinear multivalued evolution equation

$$
\frac {\partial u}{\partial t} + C (u) \ni 0, \tag {1}
$$

$$
u (0) = u ^ {0},
$$

and the associated stationary equation

$$
C (\bar {u}) \ni 0, \tag {2}
$$

where $C$ is a monotone operator on a Hilbert space $H$ , which is multivalued that is, for $u \in H$ , $C(u)$ is a (possibly empty) subset of $H$ .

We shall consider the case where $C = A + B$ and A and B are maximal monotone. We study the following algorithms:

$$
u ^ {n + 1} = (I + \lambda B) ^ {- 1} (I - \lambda A) (I + \lambda A) ^ {- 1} (I - \lambda B) u ^ {n}, \tag {3}
$$

which was introduced, in the case of linear operators, by Peaceman–Rachford [16], [18], and

$$
u ^ {n + 1} = (I + \lambda B) ^ {- 1} [ (I + \lambda A) ^ {- 1} (I - \lambda B) + \lambda B ] u ^ {n}, \tag {4}
$$

which was introduced by Douglas-Rachford [8].

In this paper, we show that these algorithms can be used to solve the evolution equation (1) by letting $\lambda \rightarrow 0$ , and $\lambda$ appears then as a time step. We show also that they have the interesting property that, for fixed $\lambda$ , $u^{n} \rightarrow u_{\infty}$ as $n \rightarrow \infty$ , where $u_{\infty}$ is a solution of the stationary problem (2).

Last, but not least, they are both unconditionally stable, i.e. $u^{n}$ remains bounded independently of n for any $\lambdaLast, but not least, they are both unconditionally stable, i.e. $u^{n}$ remains bounded independently of n for any $\lambda$.

This set of properties is remarkable if we compare them to that we get for more standard algorithms.

The first one is

$$
u ^ {n + 1} = (I + \lambda A) ^ {- 1} (I - \lambda B) u ^ {n}, \tag {5}
$$

which is not unconditionally stable, but converges to the solution of the stationary problem for $\lambda$ sufficiently small if $B$ is Lipschitz continuous (see Goldstein [12], Bruck [6]).

The second one is

$$
u ^ {n + 1} = (I + \lambda A) ^ {- 1} (I + \lambda B) ^ {- 1} u ^ {n}, \tag {6}
$$

which is unconditionally stable but does not converge to the solution of the stationary problem for any $\lambdawhich is unconditionally stable but does not converge to the solution of the stationary problem for any $\lambda$, except with some special modification (see Lions [14]). except with some special modification (see Lions [14]).

All these are called “splitting” algorithms since, up to the introduction of a fractionary step, they can be interpreted as the combination of a step for A and a step for B.

As an example, (5) can be written

$$
\begin{aligned} \frac {u ^ {n + 1 / 2} - u ^ {n}}{\lambda} + B u ^ {n} &= 0, \\ \frac {u ^ {n + 1} - u ^ {n + 1 / 2}}{\lambda} + A u ^ {n + 1} &= 0, \\ \end{aligned}
$$

which shows that (5) results from the combination of a forward step on $B$ and a backward step on $Awhich shows that (5) results from the combination of a forward step on $B$ and a backward step on $A$.

An outline of this paper is as follows: in § 1, we study the convergence of (3), (4), in the stationary case; in § 2, we study consistency of these algorithms and the convergence to the solution of the evolution equation (as $\lambda \to 0$ ); in § 3, we give some numerical results. Finally, § 4 contains some comments.

# 1. The stationary case.

# 1.1. Assumptions and notations

We shall assume that $A$ and $B$ are maximal monotone. We denote by $D(A)$ the domain of $AWe shall assume that $A$ and $B$ are maximal monotone. We denote by $D(A)$ the domain of $A$. We recall that $A$ monotone means We recall that $A$ monotone means

$$
(y - z, u - v) \geqq 0, \quad \forall u \in H, y \in A (u), v \in H, z \in A (v),
$$

where $(\cdot,\cdot)$ denotes the scalar product of H and $|\cdot|$ the associated norm; a maximal monotone is equivalent to saying the resolvent $J_{A}^{\lambda}=(I+\lambda A)^{-1}$ is a contraction defined on H. When A is single valued, we have the identity

$$
(I + \lambda A) J _ {A} ^ {\lambda} = I. \tag {7}
$$

In this section, we shall assume that the stationary problem (2) has at least one solution. Hence

$$
\text {there exists} u \in H, a \in A (u), b \in B (u) \quad \text {such that} a + b = 0. \tag {8}
$$

In the case here considered, where $A$ and $B$ are multivalued, we need make precise the definition of algorithms (3) and (4). For both, $u^0 \in D(B)$ is given, and we choose $b^0 \in B(u^0)$ and set $v^0 = u^0 + \lambda b^0$ in such a way that $u^0 = J_B^\lambda v^0In the case here considered, where $A$ and $B$ are multivalued, we need make precise the definition of algorithms (3) and (4). For both, $u^0 \in D(B)$ is given, and we choose $b^0 \in B(u^0)$ and set $v^0 = u^0 + \lambda b^0$ in such a way that $u^0 = J_B^\lambda v^0$. We then define by induction the sequence $v^n$ in the following way. We then define by induction the sequence $v^n$ in the following way.

ALGORITHM I.

$$
v ^ {n + 1} = (2 J _ {A} ^ {\lambda} - I) (2 J _ {B} ^ {\lambda} - I) v ^ {n}; \tag {9}
$$

ALGORITHM II.

$$
v ^ {n + 1} = J _ {A} ^ {\lambda} (2 J _ {B} ^ {\lambda} - I) v ^ {n} + (I - J _ {B} ^ {\lambda}) v ^ {n}. \tag {10}
$$

One can check that in the case where $A$ and $B$ are single valued, Algorithm I is equivalent to the Peaceman-Rachford algorithm (3) up to the change of variable $u^n = J_B^\lambda v^n$ (with the use of (7)). Likewise, Algorithm II equivalent to the Douglas-Rachford (4). But (9) and (10) have a meaning even for $A$ and $B$ multivalued.

Remark 1. Algorithm I has been considered by Brezis [4] and Lions [14], but with a severe restriction: $B$ is assumed to be coercive, that is $B - \alpha I$ monotone for some $\alpha > 0Remark 1. Algorithm I has been considered by Brezis [4] and Lions [14], but with a severe restriction: $B$ is assumed to be coercive, that is $B - \alpha I$ monotone for some $\alpha > 0$.

1.2. Convergence of Algorithm I. We shall use the following notation

$$
v = u + \lambda b, \quad w = u + \lambda a,
$$

$$
w ^ {n} = 2 u ^ {n} - v ^ {n}, \quad b ^ {n} = \frac {v ^ {n} - u ^ {n}}{\lambda}, \quad a ^ {n} = \frac {w ^ {n} - v ^ {n + 1}}{2 \lambda}.
$$

We prove the following result.

PROPOSITION 1. Under the assumption (8), the sequences $u^n, v^n, w^n, a^n, b^nPROPOSITION 1. Under the assumption (8), the sequences $u^n, v^n, w^n, a^n, b^n$, remain bounded. Moreover remain bounded. Moreover

$$
\lim _ {n \to + \infty} (b ^ {n} - b, u ^ {n} - u) = 0; \tag {11a}
$$

$$
\lim _ {n \to + \infty} \left(a ^ {n} - a, \frac {v ^ {n + 1} + w ^ {n}}{2} - u\right) = 0. \tag {11b}
$$

Proof. From the definition of $b^n$ , we have $v^n = u^n + \lambda b^n$ . As $u^n = J_B^\lambda v^n$ , we have $v^n \in u^n + \lambda Bu^n$ , hence $b^n \in Bu^n$ . From the monotonicity of $B$ , we get

$$
0 \leqq (b ^ {n} - b, u ^ {n} - u) = \frac {1}{4 \lambda} \left(| v ^ {n} - v | ^ {2} - | w ^ {n} - w | ^ {2}\right), \tag {12}
$$

where we have used

$$
u ^ {n} = \frac {v ^ {n} + w ^ {n}}{2}, \quad u = \frac {v + w}{2}, \quad b ^ {n} = \frac {v ^ {n} - w ^ {n}}{2 \lambda}, \quad b = \frac {v - w}{2 \lambda}.
$$

On the other hand, from (9), we get

$$
v ^ {n + 1} = (2 J _ {A} ^ {\lambda} - I) w ^ {n} \Rightarrow \frac {v ^ {n + 1} + w ^ {n}}{2} = J _ {A} ^ {\lambda} w ^ {n}.
$$

Hence

$$
w ^ {n} \in \frac {v ^ {n + 1} + w ^ {n}}{2} + \lambda A \left(\frac {v ^ {n + 1} + w ^ {n}}{2}\right),
$$

$$
a ^ {n} = \frac {w ^ {n} - v ^ {n + 1}}{2 \lambda} \in A \bigg (\frac {v ^ {n + 1} + w ^ {n}}{2} \bigg).
$$

From the monotonicity of $AFrom the monotonicity of $A$, we get we get

$$
0 \leqslant \left(a ^ {n} - a, \frac {v ^ {n + 1} + w ^ {n}}{2} - u\right) = \left(\frac {w ^ {n} - v ^ {n + 1}}{2 \lambda} - \frac {w - v}{2 \lambda}, \frac {v ^ {n + 1} + w ^ {n}}{2} - \frac {v + w}{2}\right) \tag {13}
$$

$$
= \frac {1}{4 \lambda} \left(\left| w ^ {n} - w \right| ^ {2} - \left| v ^ {n + 1} - v \right| ^ {2}\right),
$$

which shows, with (12), that

$$
\left| v ^ {n + 1} - v \right| ^ {2} \leq \left| w ^ {n} - w \right| ^ {2} \leq \left| v ^ {n} - v \right| ^ {2},
$$

and the sequences $v^n$ , $w^n$ are bounded, thus proving the first part. Finally, as $|v^n - v|^2 - |v^{n+1} - v|^2 \to 0$ as $n \to +\infty$ , (12), (13) imply (11) thereby completing the proof.

COROLLARY 1. If $B$ is single valued and satisfies the following property: (14) For all $x_{n}, x \in D(B)$ such that $Bx_{n}$ is bounded, $x_{n} \rightharpoonup \bar{x}$ weakly, and

$$
(B x _ {n} - B x, x _ {n} - x) \rightarrow 0
$$

as $n \to +\infty$ , then one has $x = \bar{x}$ ; then $u^n$ converges weakly to $u$ , solution of (2), which is unique.

Proof. Let us prove first the uniqueness. Let $u_{1}, u_{2}$ be two solutions of (2); we have

$$
0 \leq (B u _ {1} - B u _ {2}, u _ {1} - u _ {2}) = - (A u _ {1} - A u _ {2}, u _ {1} - u _ {2}) \leq 0,
$$

hence $(Bu_{1} - Bu_{2}, u_{1} - u_{2}) = 0$ which, together with property (14) implies $u_{1} = u_{2}hence $(Bu_{1} - Bu_{2}, u_{1} - u_{2}) = 0$ which, together with property (14) implies $u_{1} = u_{2}$.

Let $u_{n'}$ denote a subsequence of the bounded sequence $u_n$ converging weakly to $\bar{u}$ ; from (11a) and (14), one gets $u = \bar{u}$ , and the whole sequence $u_n$ converges weakly to $u$ .

Remark 2. We give some cases where property (14) is satisfied:

1. $B$ is coercive: there exists some $\alpha > 0$ such that $B - \alpha I$ is monotone. In this case, the sequence $u^n$ converges even strongly to $u1. $B$ is coercive: there exists some $\alpha > 0$ such that $B - \alpha I$ is monotone. In this case, the sequence $u^n$ converges even strongly to $u$.

2. $B^{-1}$ is coercive: there exists $\beta > 0$ such that

$$
(B u - B v, u - v) \geqq \beta | B u - B v | ^ {2}, \quad \forall u, v \in D (B);
$$

in such a case, (11a) implies that $Bu^n \to Bu$ strongly. Moreover, if $B^{-1}$ is univoque, (14) is satisfied since $Bx_n \to Bx$ ; as $x_n \rightharpoonup \bar{x}$ , $\bar{x} \in D(B)$ and $B\bar{x} = Bx$ ; thus $\bar{x} = x$ .

3. $B$ is strictly monotone and weakly closed: that is if $u, v \in D(B)$ and $(Bu - Bv, u - v) = 0$ , one has $u = v$ ; if $x_n \in D(B)$ , with $x_n \rightharpoonup \bar{x} \in H$ weakly and such that there exists $y_n \in Bx_n$ with $y_n \rightharpoonup y \in H$ , then $\bar{x} \in D(B)$ and $y = B\bar{x}$ .

Let us prove that in this case again (14) is satisfied. Indeed, let $x_{n}$ be as in (14) and $x_{n'}$ denote a subsequence such that $Bx_{n'} \to y$ weakly. From the weak closure of $B$ , we have $\bar{x} \in D(B)$ and $y \in B\bar{x}$ . The assumption on $x_{n}$ implies

$$
\begin{array}{l} \lim _ {n ^ {\prime} \to \infty} (B x _ {n ^ {\prime}}, x _ {n ^ {\prime}}) = \lim _ {n ^ {\prime} \to \infty} (B x, x _ {n ^ {\prime}} - x) + \lim _ {n ^ {\prime} \to \infty} (B x _ {n ^ {\prime}}, x) \\ = (B x, \bar {x} - x) + (B \bar {x}, x) \\ \leq (B \bar {x}, \bar {x}), \\ \end{array}
$$

where we have applied the monotonicity of $B$ . A result of Brezis [3, Prop. 2.5] proves then that the inequality is actually an equality, which implies $(Bx - B\bar{x}, x - \bar{x}) = 0$ ; then $x = \bar{x}$ , which proves that (14) holds.

Remark 3. If $B$ is linear, or if $J_B^\lambda$ is compact, then $B$ is weakly closed.

Remark 4. In Corollary 1, if we assume that $A$ instead of $B$ satisfies (14), then the sequence $(v^{n+1} + w^n)/2$ converges weakly to the unique solution of the stationary problem (2).

Remark 5. We can prove that, if a subsequence $(v^{n'})$ of $(v^n)$ is bounded, then the stationary problem (2) has one solution $u$ . Indeed, let $T = (2J_A^\lambda - I)(2J_B^\lambda - I)$ , we have $v^{n+1} = Tv^n$ . As $2J_A^\lambda - I$ and $2J_B^\lambda - I$ are nonexpansive, $T$ itself is nonexpansive. The boundedness of a subsequence $v^{n'}$ implies then that $T$ has a fixed point $v$ , with $Tv = v$ .

Let $u = J_{B}^{\lambda}vLet $u = J_{B}^{\lambda}v$, we have $u \in D(B)$ and we have $u \in D(B)$ and

$$
\begin{aligned} v &= (2 J _ {A} ^ {\lambda} - I) (2 u - v), \\ u &= J _ {A} ^ {\lambda} (2 u - v); \\ \end{aligned}
$$

hence $u \in D(A)hence $u \in D(A)$. Let $t \in B(u)$ satisfy $v = u + \lambda t$ ; we have Let $t \in B(u)$ satisfy $v = u + \lambda t$ ; we have

$$
u = J _ {A} ^ {\lambda} (u - \lambda t) \quad \Rightarrow \quad u - \lambda t \in u + \lambda A u,
$$

that is $-t \in A(u)that is $-t \in A(u)$, hence u is a solution of the stationary problem (2). hence u is a solution of the stationary problem (2).

Remark 6. A counter-example. Let $H = \mathbb{C}$ , $A = B = i : Az = iz$ . Note that $A$ is maximal monotone on $\mathbb{R}^2$ ; moreover, $A$ is linear compact and one to one; however, $2J_A^\lambda - I = (1 - \lambda i)/(1 + \lambda i)$ is a rotation and $v^n$ does not converge strongly to the solution of (2) which is 0.

1.3. Convergence of Algorithm II. We shall see that the convergence for Algorithm II occurs for more general operators $A$ and $B$ than those considered previously in Remark 2. Indeed, we shall prove the following result.

THEOREM 1. Under the assumption (8), the sequence $v^n$ generated by the algorithm (10), converges weakly to $v \in H$ , as $n \to \infty$ , such that $u = J_B^\lambda v$ is a solution of (2). Furthermore, let $u^n = J_B^\lambda v^n$ ,

(i) if $B$ is linear, $u^{n}$ converges weakly to a solution of (2);  
(ii) if $A$ and $B$ are odd, $u^n$ converges strongly to a solution of (2);  
(iii) If $A + B$ is maximal monotone, any subsequence of $(u^n)$ converges weakly to a solution of (2).

1.3.1. Preliminary results. We need first to recall a definition and a result.

DEFINITION. Let $K \subset H$ be a closed convex subset of $H$ . An operator $T: K \to K$ is said to be firmly nonexpansive if, for all $x, y \in K$ ,

$$
(T x - T y, x - y) \geq | T x - T y | ^ {2}.
$$

(Note that firmly nonexpansive $\Rightarrow$ nonexpansive).

RESULT (Browder [5]). If $T$ is firmly nonexpansive from $K$ into $K$ , and if $T$ has at least one fixed point $\xi \in K$ , then, for all $x \in K$ , $T^{n+1}x - T^n x \to 0$ strongly, as $n \to \infty$ , and $T^n x \to \bar{x} \in K$ weakly, where $\bar{x} = T\bar{x}$ is a fixed point of $T$ .

We shall prove the following result.

LEMMA 1. Let $T_{1}$ and $T_{2}$ be two firmly nonexpansive operators from $K$ into $KLEMMA 1. Let $T_{1}$ and $T_{2}$ be two firmly nonexpansive operators from $K$ into $K$, then $S = T_{1}(2T_{2} - I) + I - T_{2}$ is firmly nonexpansive. More precisely, one has then $S = T_{1}(2T_{2} - I) + I - T_{2}$ is firmly nonexpansive. More precisely, one has

$$
(S x - S y, x - y) \geq | S x - S y | ^ {2} + (T _ {2} x - T _ {2} y, (I - T _ {2}) x - (I - T _ {2}) y). \tag {15}
$$

Proof. We have

$$
\begin{aligned} \left| S x - S y \right| ^ {2} &= \left| T _ {1} (2 T _ {2} - I) x - T _ {1} (2 T _ {2} - I) y \right| ^ {2} + \left| (I - T _ {2}) x - (I - T _ {2}) y \right| ^ {2} \\ + 2 (T _ {1} (2 T _ {2} - I) x - T _ {1} (2 T _ {2} - I) y, (I - T _ {2}) x - (I - T _ {2}) y). \\ \end{aligned}
$$

As $T_{1}$ is firmly nonexpansive, we get

$$
\begin{aligned} \left| S x - S y \right| ^ {2} &\leq (T _ {1} (2 T _ {2} - I) x - T _ {1} (2 T _ {2} - I) y, x - y) + \left| (I - T _ {2}) x - (I - T _ {2}) y \right| ^ {2} \\ &= (S x - S y, x - y) - (T _ {2} x - T _ {2} y, (I - T _ {2}) x - (I - T _ {2}) y) \\ \end{aligned}
$$

which proves (15). The positivity of the last term results from the fact that $T_{2}$ is firmly nonexpansive.

1.3.2. Convergence. We shall apply this result to

$$
G (\lambda) = J _ {A} ^ {\lambda} (2 J _ {B} ^ {\lambda} - I) + I - J _ {B} ^ {\lambda}, \tag {16}
$$

and we note that the algorithm (10) can be written

$$
v ^ {n + 1} = G (\lambda) v ^ {n}.
$$

PROPOSITION 2. The operator $G(\lambda)$ defined in (16) is firmly nonexpansive and satisfies

$$
\begin{aligned} (G (\lambda) x - G (\lambda) y, x - y) &\geq | G (\lambda) x - G (\lambda) y | ^ {2} \tag {17} \\ + ((I - J _ {B} ^ {\lambda}) x - (I - J _ {B} ^ {\lambda}) y, J _ {B} ^ {\lambda} x - J _ {B} ^ {\lambda} y). \\ \end{aligned}
$$

Then, under the assumption (8), we have

$$
v ^ {n} \rightarrow v ~ \text {weakly, where} ~ v = G (\lambda) v, \tag {18}
$$

$$
u ^ {n} ~ \text {is bounded and} ~ u ^ {n + 1} - u ^ {n} \rightarrow 0.
$$

Let $b^n = (v^n - u^n) / \lambda$ ; $b^n$ is bounded, $b^{n+1} - b^n \to 0Let $b^n = (v^n - u^n) / \lambda$ ; $b^n$ is bounded, $b^{n+1} - b^n \to 0$, and and

$$
(b ^ {n} - b, u ^ {n} - u) \rightarrow 0, \quad \text {as } n \rightarrow \infty . \tag {19}
$$

Proof. As $J_B^\lambda$ is firmly nonexpansive, we may apply Lemma 1 to prove (17). From the "result" above, we have $v^{n+1} - v^n \to 0$ and $v^n \rightharpoonup v$ weakly, where $v$ is a fixed point of $G(\lambda)$ . As $u^n = J_B^\lambda v^n$ , (18) results from the nonexpansiveness of $J_B^\lambda$ . Finally, applying (17) with $x = v^n$ and $y = v$ , we get

$$
(v ^ {n + 1} - v, v ^ {n} - v) \geq | v ^ {n + 1} - v | ^ {2} + \lambda (b ^ {n} - b, u ^ {n} - u), \tag {20}
$$

which proves that $|v^{n}-v|^{2}$ decreases and (19). ☐

COROLLARY 2. Assume that $J_B^\lambda$ is weakly closed; then under the assumption (8), $u^n$ converges weakly to a solution $u = J_B^\lambda v$ of (2).

Proof. From Proposition 2, $v^n \to v$ and $u = J_B^\lambda v$ is a solution of (2). As the sequence $u^n$ is bounded, for any subsequence $u^{n'}$ converging weakly to some $\bar{u} \in H$ , we have $\bar{u} = J_B^\lambda v = u$ , hence the weak convergence of the whole sequence to $u$ .

COROLLARY 3. If 33$J_A^\lambda$ is compact, then $u^n \to u$ the solution of (2), strongly.

Proof. From (10), we have

$$
u ^ {n} = v ^ {n} - v ^ {n + 1} + J _ {A} ^ {\lambda} (2 u ^ {n} - v ^ {n}), \tag {21}
$$

which shows that the sequence $u^{n}$ remains in a compact set. But, for any convergent subsequence $u^{n'} \rightarrow u$ , as $J_{B}^{\lambda}$ is maximal monotone, $u = J_{B}^{\lambda} v$ . ☐

Remark 7. If $J_B^\lambda$ is compact, $J_B^\lambda$ is also weakly closed and Corollary 2 applies. However, the convergence is obviously strong.

Remark 8. If A and B are odd, then $v^{n}$ converges strongly to a fixed point of $G(\lambda)Remark 8. If A and B are odd, then $v^{n}$ converges strongly to a fixed point of $G(\lambda)$, and $u^{n}$ to a solution of (2). This results from a result by Baillon [1], for odd firmly nonexpansive operators, which $G(\lambda)$ is, in this case. and $u^{n}$ to a solution of (2). This results from a result by Baillon [1], for odd firmly nonexpansive operators, which $G(\lambda)$ is, in this case.

The following result gives some additional information about the convergence of the sequences $u^n$ and $v^nThe following result gives some additional information about the convergence of the sequences $u^n$ and $v^n$.

PROPOSITION 3. Under the assumption (8), there exists a sequence $\varepsilon^n$ such that

$$
\varepsilon^ {n} + a ^ {n} + b ^ {n} = 0 \quad \text {where}~ b ^ {n} = \frac {v ^ {n} - u ^ {n}}{\lambda}, a ^ {n} \in A (u ^ {n} + \lambda \varepsilon^ {n}) \quad \text {and} \quad \varepsilon^ {n} \to 0~ \text {strongly}. \tag {22}
$$

Furthermore

$$
(b ^ {n} - b, u ^ {n} - u) \rightarrow 0, \tag {23a}
$$

$$
(a ^ {n} - (- b), u ^ {n} + \lambda \varepsilon^ {n} - u) \rightarrow 0, \quad \text {as } n \rightarrow + \infty . \tag {23b}
$$

Proof. Let $a^n$ be the element of $A(u^n + v^{n+1} - v^n)$ such that (see (21))

$$
u ^ {n} + v ^ {n} - v ^ {n + 1} + \lambda a ^ {n} = 2 u ^ {n} - v ^ {n} = u ^ {n} - \lambda b ^ {n},
$$

which implies (22) with the choice $\varepsilon^n = (v^n - v^{n+1}) / \lambdawhich implies (22) with the choice $\varepsilon^n = (v^n - v^{n+1}) / \lambda$. To complete the proof, we notice that To complete the proof, we notice that

$$
\begin{aligned} (\varepsilon^ {n} + a ^ {n} + b ^ {n}, u ^ {n} - u) &= 0, \\ (\varepsilon^ {n}, u ^ {n} - u) + (a ^ {n} + b, u ^ {n} + \lambda \varepsilon^ {n} - u) + (b ^ {n} - b, u ^ {n} - u) &= \lambda (a ^ {n} + b, \varepsilon^ {n}). \\ \end{aligned}
$$

As $b^{n}$ is bounded (Proposition 2), (22) shows that $a^{n}$ is bounded. Hence,

$$
(a ^ {n} + b, u ^ {n} + \lambda \varepsilon^ {n} - u) + (b ^ {n} - b, u ^ {n} - u) \to 0.
$$

As each term is positive by monotonicity of A and B, we get (23). □

Remark 9. If A or B satisfies property (14), the sequence $u^{n}$ converges weakly to a solution u of the stationary problem (2). If A or B is coercive, the convergence is strong, and one has $u = J_{B}^{\lambda} vRemark 9. If A or B satisfies property (14), the sequence $u^{n}$ converges weakly to a solution u of the stationary problem (2). If A or B is coercive, the convergence is strong, and one has $u = J_{B}^{\lambda} v$. In any case, if $u^{n} \rightharpoonup u = J_{B}^{\lambda} v$ weakly, then $b^{n} = (v^{n} - u^{n}) / \lambda$ converges weakly to an element b satisfying (8). In any case, if $u^{n} \rightharpoonup u = J_{B}^{\lambda} v$ weakly, then $b^{n} = (v^{n} - u^{n}) / \lambda$ converges weakly to an element b satisfying (8).

1.3.3. Speed of convergence. We shall give an evaluation of the speed of convergence of Algorithm II, in the special case where B is both coercive and Lipschitz. Then, there exists $\alpha$ and M>0 such that

$$
| B x _ {1} - B x _ {2} | \leq M | x _ {1} - x _ {2} |, \tag {24a}
$$

$$
(B x _ {1} - B x _ {2}, x _ {1} - x _ {2}) \geqq \alpha \left| x _ {1} - x _ {2} \right| ^ {2}, \tag {24b}
$$

for all $x_{1}, x_{2} \in Hfor all $x_{1}, x_{2} \in H$.

PROPOSITION 4. Under the assumption (24), there exists a constant $C_1$ such that

$$
\left| v ^ {n} - v \right| \leq C _ {1} k ^ {n}; \quad \left| u ^ {n} - u \right| \leq C _ {1} k ^ {n},
$$

where $u = J_B^\lambda v$ is the unique solution of (2) and $k = (1 - 2\lambda \alpha / (1 + \lambda M)^2)^{1/2}where $u = J_B^\lambda v$ is the unique solution of (2) and $k = (1 - 2\lambda \alpha / (1 + \lambda M)^2)^{1/2}$.

Proof. In view of (20) and (24b), we have

$$
\left| v ^ {n + 1} - v \right| ^ {2} + 2 \lambda \alpha \left| u ^ {n} - u \right| ^ {2} \leq \left| v ^ {n} - v \right| ^ {2},
$$

where we have applied that $v^n = u^n + \lambda b^n$ , $v = u + \lambda b$ , $b^n \in Bu^n$ , $b \in Bu$ , which gives also with (24a)

$$
\left| v ^ {n} - v \right| ^ {2} \leq (1 + \lambda M) ^ {2} \left| u ^ {n} - u \right| ^ {2}.
$$

Hence

$$
\left| v ^ {n + 1} - v \right| ^ {2} \leq \left(1 - \frac {2 \lambda \alpha}{(1 + \lambda M) ^ {2}}\right) \left| v ^ {n} - v \right| ^ {2},
$$

which gives the first estimate. The second one results from the fact that $J_B^\lambda$ is a contraction.

Remark 10. In view of (12) and (13), we can derive a similar estimate for Algorithm I. Both estimates show that there is an optimal value for $\lambda$ , which is confirmed by the experiments. The best estimate for $k$ above corresponds to $\lambda = 1/M$ which gives $k = (1 - \alpha / (2M))^{1/2}$ . The experiments show that this estimate is rough. Notice that for the algorithm (5), one gets only $(1 - \alpha^2 / (M^2))^{1/2}$ .

1.3.4. The general case. Finally, in the general case, the algorithm is “almost convergent.”

PROPOSITION 5. Assume that $A+B$ is maximal monotone and $0\in R(A+B)$ , then $v^{n}\rightharpoonup v$ weakly and $u$ is solution of (3) with $u=J_{B}^{\lambda}u$ .

Proof. In view of (22), we deduce that, for any $x \in D(A + B)$ , $y \in Ax$ , $z \in Bx$ ,

$$
(a ^ {n} + b ^ {n} - (y + z), u ^ {n} - x) = (a ^ {n} - y, u ^ {n} + \lambda \varepsilon^ {n} - x) + (b ^ {n} - z, u ^ {n} - x) - \lambda (a ^ {n} - y, \varepsilon^ {n})
$$

$$
\geq - \lambda (a ^ {n} - y, \varepsilon^ {n}).
$$

Thus, if a subsequence $u^{n'}$ converges weakly to $\tilde{u}Thus, if a subsequence $u^{n'}$ converges weakly to $\tilde{u}$, we have we have

$$
(- (y + z), \tilde {u} - x) \geq 0 \quad \forall x \in D (A + B),
$$

hence $0 \in (A + B)\tilde{u}hence $0 \in (A + B)\tilde{u}$, since $A + B$ is maximal monotone. $\square$ since $A + B$ is maximal monotone. $\square$

Remark 11. In the special case where $A = B$ , we claim that the whole sequence $u^n$ converges weakly to $u \in A^{-1}(0)$ . Indeed, in this case, $u = J_A^\lambda u = v$ , hence $|u^n + \lambda b^n - u|^2 = |v^n - v|^2$ decreases. From (23a), $2\lambda(b^n, u^n - u)$ tends to zero, hence the sequence $|u^n - u|^2 + \lambda^2 |b^n|^2$ converges to a real number depending on $u$ , say $p(u)$ . Let us show that this implies the uniqueness of the weak limit of any convergent subsequence, hence the weak convergence of the whole sequence $u^n$ . Indeed, let $u^{n'} \to u_1 \in A^{-1}(0)$ and $u^{m'} \to u_2 \in A^{-1}(0)$ ; one has

$$
\left| b ^ {n} \right| ^ {2} + \left| u ^ {n} - u _ {1} \right| ^ {2} = \left| u ^ {n} - u _ {2} \right| ^ {2} + 2 (u ^ {n} - u _ {2}, u _ {2} - u _ {1}) + \left| u _ {2} - u _ {1} \right| ^ {2} + \left| b ^ {n} \right| ^ {2}.
$$

By taking the limit with respect to the subsequences $n'$ or $m'$ , we get $p(u_1) = p(u_2) \pm |u_2 - u_1|^2$ , hence $u_2 = u_1$ .

As a bibliographical comment, we would like to mention that Algorithm II has been studied by Lieutaud [13, Chap V, § 2] in the finite dimensional and univoque case.

For additional bibliography, we refer the interested reader to Varga [18] and Marchouk [15].

A generalization of Algorithm II to the sum of $n$ operators has been given by Douglas-Gunn [7]. However, the convergence seems difficult to prove in this general framework, even in the case of a sum of 3 operators. Varga [18, p. 240] suggests to combine the Peaceman-Rachford and the Douglas-Rachford algorithm in a single algorithm depending on a parameter $\omega$ , which gives Peaceman-Rachford for $\omega = 0$ and Douglas-Rachford for $\omega = 1$ .

Let $F(\lambda) = (2J_{A}^{\lambda} - I)(2J_{B}^{\lambda} - I)Let $F(\lambda) = (2J_{A}^{\lambda} - I)(2J_{B}^{\lambda} - I)$, the generalized algorithm suggested by Varga is nothing but the generalized algorithm suggested by Varga is nothing but

$$
v ^ {n + 1} = [ (1 - \omega) F (\lambda) + \omega G (\lambda) ] v ^ {n}
$$

that is a convex combination of Algorithms I and II.

As the Browder result above extends to the convex combination of a nonexpansive operator $(F(\lambda))$ and a firmly nonexpansive operator $(G(\lambda))$ , the new algorithm has the same properties as Algorithm II in the case $0 < \omega < 1$ .

1.4. Application to a class of optimization problems. We shall consider the following abstract optimization problem introduced by Rockafellar [17]: Find $\bar{x} \in X1.4. Application to a class of optimization problems. We shall consider the following abstract optimization problem introduced by Rockafellar [17]: Find $\bar{x} \in X$, solution of solution of

$$
\inf _ {x \in X} [ f (\Lambda x) + g (x) ], \tag {25}
$$

where $\Lambda: X \to Y$ is a continuous linear operator, with closed range, $X$ and $Y$ are two Hilbert spaces, $f: Y \to (-\infty, +\infty]$ and $g: Y \to (-\infty, +\infty]$ are two convex lower semi-continuous functions.

This problem occurs in many situations in mechanics and economics. We shall explain how the previous algorithms can be applied to solve this problem.

1.4.1. The case where $g$ is linear. Let $g(x) = \langle b, x \rangle$ where $b \in X'$ dual of $X$ , and $\langle \cdot, \cdot \rangle$ denote the duality pairing between $X$ and $X'$ . We call $\Lambda^* \colon Y' \to X'$ the adjoint of $\Lambda$ . As the range of $\Lambda$ is assumed to be closed, there exists $\beta \in Y'$ such that $\Lambda^*\beta = b$ .

Let $h(y) = f(y) + \langle \beta, y \rangleLet $h(y) = f(y) + \langle \beta, y \rangle$, one can check that (25) is equivalent to one can check that (25) is equivalent to

$$
\inf _ {y \in K} h (y), \tag {26}
$$

where $K = R(\Lambda)$ denotes the range of $\Lambdawhere $K = R(\Lambda)$ denotes the range of $\Lambda$.

We call $I_{K}$ the indicator $^{1}$ function of K; assuming that

$$
\partial (h + I _ {K}) = \partial h + \partial I _ {K}, \tag {27}
$$

which requires some qualification hypothesis on $h$ (see Ekeland-Temam [9]), we have a special case of the stationary problem (2) with $H = Y$ , $A = \partial I_K$ , and $B = \partial h$ .

The resolvent operator $J_{A}^{\lambda}$ is then the projection operator onto K, which is easy to compute since K is a linear subspace.

Algorithms I and II can be applied for solving (26). Indeed, II is equivalent to one of the penalty-duality algorithms considered in [10], [11], where many numerical results can be found.

The application of I and II is easy when $I + \lambda \partial h$ is easy to invert. That is easy in the following situation which covers most of the examples considered in [10] and [11]:

$$
X = H _ {0} ^ {1} (\Omega), \qquad Y = (L ^ {2} (\Omega)) ^ {n}, \qquad \Lambda = \mathrm{grad},
$$

where $\Omega$ is an open bounded set of $\mathbb{R}^nwhere $\Omega$ is an open bounded set of $\mathbb{R}^n$, and and

$$
h (y) = \int_ {\Omega} \psi (y (\xi)) d \xi ,
$$

where $\psi\colon\mathbb{R}^{n}\to\mathbb{R}$ is a convex lower semi-continuous function.

To solve $(I + \lambda \partial h)(y) \ni z$ is then equivalent to solving almost everywhere (on each element in the discrete case) the nonlinear equation in n variables

$$
(I + \lambda \partial \psi) y (\xi) \ni z (\xi). \tag {28}
$$

Note that I and II can also be applied to the dual

$$
\inf _ {p \in K ^ {*}} h ^ {*} (p), \tag {29}
$$

where $K^{*}$ is the kernel of $\Lambda^{*}$ (again a linear subspace) and $h^{*}$ is the conjugate of h.

1.4.2. The general case. In the general case where g is nonlinear, following an idea of J. P. Aubin, the problem (25) can be considered as a particular case of the stationary problem (2), but with $H = X \times Y1.4.2. The general case. In the general case where g is nonlinear, following an idea of J. P. Aubin, the problem (25) can be considered as a particular case of the stationary problem (2), but with $H = X \times Y$. Indeed, (25) is equivalent to Indeed, (25) is equivalent to

$$
\inf _ {v \in K} \phi (v), \tag {30}
$$

where $K = \{ \{x, y\} \in X \times Y : y - \Lambda x = 0 \}$ and $\phi(v) = f(y) + g(x)$ for $v = \{x, y\}$ . Provided that $\partial \phi + \partial I_K = \partial (\phi + I_K)$ , which requires again a qualification hypothesis, (25) is then a particular case of (2) with $A = \partial I_K$ and $B = \partial \phi = \begin{pmatrix} \partial g & 0 \\ 0 & \partial f \end{pmatrix}$ .

Again K is a linear subspace, hence $J_{A}^{\lambda}=P_{K}$ is easy to compute, which makes Algorithms I and II very attractive to solve (25). They can also be applied to the dual of (25) which has the same structure (cf. [9]).

# 2. Application of Algorithms I and II to the evolution equations.

# 2.1. Introduction. We recall the definition (16) of $G(\lambda)$ and write

$$
F (\lambda) = (2 J _ {A} ^ {\lambda} - I) (2 J _ {B} ^ {\lambda} - I). \tag {31}
$$

Let $u^{0} \in D(A) \cap D(B)$ and $b^{0} \in B(u^{0})$ be given; from now on we choose $\lambda = t/nLet $u^{0} \in D(A) \cap D(B)$ and $b^{0} \in B(u^{0})$ be given; from now on we choose $\lambda = t/n$, where $t > 0$ is given. We let $v_{n}^{0} = u^{0} + (t/n)b^{0}$ and where $t > 0$ is given. We let $v_{n}^{0} = u^{0} + (t/n)b^{0}$ and

ALGORITHM I.

$$
v ^ {n} = F \bigg (\frac {t}{n} \bigg) v _ {n} ^ {0}, \quad u ^ {n} = \bigg (I + \frac {t}{n} B \bigg) ^ {- 1} v ^ {n}.
$$

ALGORITHM II.

$$
v ^ {n} = G \bigg (\frac {t}{n} \bigg) v _ {n} ^ {0}, \quad u ^ {n} = \bigg (I + \frac {t}{n} B \bigg) ^ {- 1} v ^ {n}.
$$

In this section, we shall prove the sequence $(u^{n})In this section, we shall prove the sequence $(u^{n})$, generated by these algorithms, converges to the solution of the evolution equation (1) in the following sense: generated by these algorithms, converges to the solution of the evolution equation (1) in the following sense:

$$
u ^ {n} \rightarrow u (2 t), \quad \text {as} n \rightarrow + \infty , \quad \text {in case I}; \tag {32a}
$$

$$
u ^ {n} \to u (t), \quad \text { as } n \to \infty , \quad \text { in   case   II. } \tag {32b}
$$

We shall denote by $E^0$ the minimal section of an operator $E$ , such that $E^0 x$ is the projection of the origin on the set $Ex$ . Our main tool for this purpose is the following result of Brezis-Pazy (see e.g. Brezis [3]).

LEMMA 2. Let C be a maximal monotone operator and $u(t)$ denote the solution of the evolution equation (1). Let $T(\lambda)$ be a family of contractions from $\overline{D(C)}$ into $\overline{D(C)}$ such that for any $\rho > 0$

$$
\lim _ {\lambda \to 0} \left(I + \rho \left(\frac {I - T (\lambda)}{\lambda}\right)\right) ^ {- 1} x \to (I + \rho C) ^ {- 1} x \quad \text {for all} x \in D (C); \tag {33}
$$

then,

$$
T \Big (\frac {t}{n} \Big) ^ {n} u ^ {0} \to u (t),
$$

uniformly for $t$ in any compact set of $[0, +\infty)uniformly for $t$ in any compact set of $[0, +\infty)$.

# 2.2. Convergence. We shall prove the following result.

THEOREM 2. The families of nonexpansive operators $F(\lambda)$ and $G(\lambda)THEOREM 2. The families of nonexpansive operators $F(\lambda)$ and $G(\lambda)$, defined in (31) and (16), satisfy the consistency property (33). As a corollary, if $C = A + B$ is maximal monotone, the sequences $u^n$ generated by Algorithms I and II satisfy the convergence property (32) to the solution of the evolution equation (1). defined in (31) and (16), satisfy the consistency property (33). As a corollary, if $C = A + B$ is maximal monotone, the sequences $u^n$ generated by Algorithms I and II satisfy the convergence property (32) to the solution of the evolution equation (1).

The proof of this theorem relies on the following lemma, originally proved by Baillon-Mercier [2], of which we give a simpler proof.

LEMMA 3. Let $A$ be a maximal monotone operator on $H$ ; $u \in D(A)$ and $u_{\lambda} \in H$ satisfy $(u_{\lambda} - u)/\lambda \to y$ as $\lambda \to 0LEMMA 3. Let $A$ be a maximal monotone operator on $H$ ; $u \in D(A)$ and $u_{\lambda} \in H$ satisfy $(u_{\lambda} - u)/\lambda \to y$ as $\lambda \to 0$, then then

$$
\frac {u _ {\lambda} - J _ {A} ^ {\lambda} u _ {\lambda}}{\lambda} \rightarrow P _ {A u} (y) \quad \text{as} \lambda \to 0,
$$

where $P_{Au}(\cdot)$ denotes the projection operator onto Au.

Proof. Let $E$ denote the maximal monotone operator such that $Eu = Au - y$ for all $u \in D(A)$ ; we have

$$
J _ {E} ^ {\lambda} (u _ {\lambda} - \lambda y) = J _ {A} ^ {\lambda} u _ {\lambda}.
$$

Let $v_{\lambda} = u_{\lambda} - \lambda y$ ; we have

$$
\frac {1}{\lambda} \left(v _ {\lambda} - J _ {E} ^ {\lambda} v _ {\lambda}\right) = \frac {1}{\lambda} \left(v _ {\lambda} - u\right) + \frac {1}{\lambda} \left(u - J _ {E} ^ {\lambda} u\right) + \frac {1}{\lambda} \left(J _ {E} ^ {\lambda} u - J _ {E} ^ {\lambda} v _ {\lambda}\right);
$$

we notice that $\lim_{\lambda \to 0}(v_{\lambda} - u) / \lambda = 0we notice that $\lim_{\lambda \to 0}(v_{\lambda} - u) / \lambda = 0$, by assumption, that $(1 / \lambda)(u - J_E^{\lambda}u)\to E^{0}u = P_{Eu}(0)$ from a result of Brezis [3, p. 28]; finally, as $J_{E}^{\lambda}$ is a contraction, by assumption, that $(1 / \lambda)(u - J_E^{\lambda}u)\to E^{0}u = P_{Eu}(0)$ from a result of Brezis [3, p. 28]; finally, as $J_{E}^{\lambda}$ is a contraction,

$$
\left| \frac {1}{\lambda} \left(J _ {E} ^ {\lambda} u - J _ {E} ^ {\lambda} v _ {\lambda}\right) \right| \leqq \left| \frac {1}{\lambda} \left(u - v _ {\lambda}\right) \right| \to 0 \quad \text {as} \lambda \to 0,
$$

which proves that

$$
\frac {1}{\lambda} \left(v _ {\lambda} - J _ {E} ^ {\lambda} v _ {\lambda}\right)\rightarrow P _ {E u} (0),
$$

which is equivalent to the desired result. □

Proof of Theorem 2. For $b \in BxProof of Theorem 2. For $b \in Bx$, we define $x_{\lambda} = x + \lambda b$ and we notice that we define $x_{\lambda} = x + \lambda b$ and we notice that

$$
C ^ {0} x = b + P _ {A x} (- b).
$$

Let us consider

$$
\begin{aligned} \frac {1}{\lambda} \left(x _ {\lambda} - F (\lambda) x _ {\lambda}\right) &= \frac {1}{\lambda} \left(2 J _ {B} ^ {\lambda} x _ {\lambda} - 2 J _ {A} ^ {\lambda} \left(2 J _ {B} ^ {\lambda} x _ {\lambda} - x _ {\lambda}\right)\right) \\ &= \frac {1}{\lambda} \left(2 x - 2 J _ {A} ^ {\lambda} (x - \lambda b)\right) \\ &= 2 b + \frac {2}{\lambda} (u _ {\lambda} - J _ {A} ^ {\lambda} u _ {\lambda}), \\ \end{aligned}
$$

where we have introduced $u_{\lambda} = x - \lambda bwhere we have introduced $u_{\lambda} = x - \lambda b$. We can then apply Lemma 3 for $x = u$ and $y = -b$ which shows that We can then apply Lemma 3 for $x = u$ and $y = -b$ which shows that

$$
\lim _ {\lambda \to 0} \frac {1}{\lambda} (x _ {\lambda} - F (\lambda) x _ {\lambda}) = 2 (b + P _ {A u} (- b)) = 2 C ^ {0} u.
$$

In other words, $C_{\lambda} = (1 / \lambda)(I - F(\lambda))$ is such that there exists $y_{\lambda} \in C_{\lambda}x_{\lambda}$ with $y_{\lambda} \to 2C^{0}xIn other words, $C_{\lambda} = (1 / \lambda)(I - F(\lambda))$ is such that there exists $y_{\lambda} \in C_{\lambda}x_{\lambda}$ with $y_{\lambda} \to 2C^{0}x$. By a slight extension of a result of Brezis [3, Prop. 2.8, p. 29] this proves that By a slight extension of a result of Brezis [3, Prop. 2.8, p. 29] this proves that

$$
(I + \rho C _ {\lambda}) ^ {- 1} x \rightarrow (I + \rho 2 C) ^ {- 1} x \quad \text {for} x \in D (C) \text {and} \lambda \rightarrow 0.
$$

Then $F(\lambda)$ is consistent with 2C in the sense of (33); this shows, with Lemma 2, that $F(t / n)^n u^0 \to u(2t)$ . Finally, to show that $v^n$ , and therefore $u^n = (I + (t / n)B)^{-1}v^n \to u(2t)$ , we notice that

$$
\left| v ^ {n} - F \left(\frac {t}{n}\right) ^ {n} u ^ {0} \right| \leqslant \frac {t}{n} | b ^ {0} |
$$

since $F(\lambda)$ is a contraction. In the same way, we have, from (16),

$$
\begin{array}{l} \frac {1}{\lambda} \left(x _ {\lambda} - G (\lambda) x _ {\lambda}\right) = \frac {1}{\lambda} \left(J _ {B} ^ {\lambda} - J _ {A} ^ {\lambda} \left(2 J _ {B} ^ {\lambda} - I\right)\right) x _ {\lambda} \\ = \frac {1}{\lambda} \left(x - J _ {A} ^ {\lambda} (x - \lambda b)\right) \\ = b + \\frac{1}{\\lambda}(u_{\lambda} - J_A^{\lambda} u_{\lambda}), \\ \end{array}
$$

and we conclude, in the same way as for $F(\lambda)$ , that $G(\lambda)$ is consistent with $C$ , hence (32a).

Comments. In the linear case (A and B linear), it is well known that Algorithm I is of the second order, namely:

$$
\left| u ^ {n} - u (t) \right| = O (\Delta t) ^ {2} \quad \text {where} \Delta t = \frac {t}{n};
$$

on the contrary, Algorithm II is only $O(\Delta t)$ (see e.g. [15], [16], [18]).

However, the first part devoted to the stationary problem showed that II is somewhat more stable than I in view of the counter-example given at Remark 6, even though both are unconditionally stable.

# 3. Examples and numerical results.

3.1. The obstacle problem. Let $\Omega$ be a regular bounded open set of $\mathbb{R}^d$ and $f\in L^{2}(\Omega)$ be given. We let $H = L^{2}(\Omega)$ and

$$
B v = - \Delta v + f,
$$

where we specify $D(B) = H^{2}(\Omega) \cap H_{0}^{1}(\Omega)where we specify $D(B) = H^{2}(\Omega) \cap H_{0}^{1}(\Omega)$. From Poincaré-Friedrichs' inequality, we have the existence of $\alpha > 0$ such that From Poincaré-Friedrichs' inequality, we have the existence of $\alpha > 0$ such that

$$
(B u - B v, u - v) \geq \alpha | u - v | ^ {2};
$$

hence $B - \alpha I$ is monotone. We choose

$$
K = \{v \in L ^ {2} (\Omega): v (x) \geq 0 ~ \text {a.e.} ~ x \in \Omega \},
$$

and $A = \partial I_K$ so that $J_A^\lambda = P_K$ is the projection operator onto $K$ and consists then of a single truncation:

$$
(P _ {K} v) (x) = \max {(0, v (x))}, \quad \text {a.e.} x \in \Omega .
$$

At each step of Algorithms I and II, one has then only to make a truncation and then to compute the solution of a linear problem involving the Laplace operator. Note that, in this case, each step of the standard backward scheme

$$
u ^ {n + 1} = (I + \lambda C) ^ {- 1} u ^ {n}
$$

is as difficult to solve as the stationary problem itself. As for the algorithm (5), it is unstable for any $\lambda$ in this continuous framework.

3.2. Problem solved. We have chosen $d = 1, \Omega = ]0, 1[$ and $f(x) = -100$ for $x \leq \frac{1}{2}$ , $f(x) = +100$ for $x \geq \frac{1}{2}$ . The exact solution of the stationary problem is known analytically and consists of two pieces of parabola.

We have solved a finite difference approximation of the previous problem which corresponds to replace $H$ by $\mathbb{R}^NWe have solved a finite difference approximation of the previous problem which corresponds to replace $H$ by $\mathbb{R}^N$, and the Laplace operator by the matrix of the 3 point and the Laplace operator by the matrix of the 3 point

formula

$$
\frac {u _ {i - 1} - 2 u _ {i} + u _ {i + 1}}{h ^ {2}},
$$

where $h = 1/(N + 1)$ . This problem may seem very simple, but the condition number of this matrix is $0(h^{-2})$ . The stability condition for the forward scheme (5) is then $\lambda < Ch^{-2}$ . In the case where $h = \frac{1}{40}$ , we have been obliged to choose $\lambda \leq \lambda_{0}$ for the forward scheme with $\lambda_{0} = 3 \times 10^{-4}$ .

In Table 1, we give a comparison between the present algorithms for various $\lambda$ and the forward scheme (5) with $\lambda = \lambda_{0}$ . For values of $\lambda$ about 30 times bigger than $\lambda_{0}$ , the present algorithms give approximately the same results with a relative difference less than 1%.

TABLE 1
Values of the solution at x = 0.7 for various values of t and λ.

<table><tr><td></td><td colspan="3"> $\lambda = 3 \cdot 10^{-4}$ </td><td colspan="2"> $\lambda = 3 \cdot 10^{-3}$ </td><td colspan="2"> $\lambda = 6 \cdot 10^{-3}$ </td><td colspan="2"> $\lambda = 3 \cdot 10^{-2}$ </td></tr><tr><td>alg. $t$ </td><td>FWD*</td><td>I†</td><td>II‡</td><td>I</td><td>II</td><td>I</td><td>II</td><td>I</td><td>II</td></tr><tr><td>0.06</td><td>3.253</td><td>3.248</td><td>3.242</td><td>3.265</td><td>3.209</td><td>3.300</td><td>3.180</td><td>3.951</td><td>3.094</td></tr><tr><td>0.12</td><td>3.991</td><td>3.989</td><td>3.986</td><td>3.994</td><td>3.972</td><td>4.018</td><td>3.960</td><td>4.562</td><td>3.976</td></tr><tr><td>0.18</td><td>4.198</td><td>4.197</td><td>4.196</td><td>4.202</td><td>4.190</td><td>4.210</td><td>4.186</td><td>4.337</td><td>4.220</td></tr><tr><td>0.24</td><td>4.259</td><td>4.259</td><td>4.258</td><td>4.261</td><td>4.257</td><td>4.266</td><td>4.257</td><td>4.340</td><td>4.287</td></tr><tr><td>0.30</td><td>4.278</td><td>4.278</td><td>4.277</td><td>4.278</td><td>4.277</td><td>4.281</td><td>4.278</td><td>4.282</td><td>4.301</td></tr><tr><td>0.36</td><td>4.283</td><td>4.283</td><td>4.283</td><td>4.283</td><td>4.283</td><td>4.285</td><td>4.284</td><td>4.307</td><td>4.303</td></tr><tr><td>0.42</td><td>4.285</td><td>4.285</td><td>4.285</td><td>4.285</td><td>4.285</td><td>4.286</td><td>4.285</td><td>4.290</td><td>4.301</td></tr><tr><td>0.48</td><td>4.285</td><td>4.285</td><td>4.285</td><td>4.285</td><td>4.285</td><td>4.286</td><td>4.286</td><td>4.297</td><td>4.298</td></tr><tr><td>0.54</td><td>4.285</td><td>4.285</td><td>4.285</td><td>4.285</td><td>4.285</td><td>4.285</td><td>4.286</td><td>4.289</td><td>4.294</td></tr><tr><td>0.60</td><td>4.285</td><td>4.285</td><td>4.285</td><td>4.285</td><td>4.285</td><td>4.285</td><td>4.285</td><td>4.290</td><td>4.291</td></tr><tr><td>0.66</td><td>4.285</td><td>4.285</td><td>4.285</td><td>4.285</td><td>4.285</td><td>4.285</td><td>4.285</td><td>4.286</td><td>4.289</td></tr></table>

* FWD: forward scheme (5)  
† I: Algorithm I  
‡ II: Algorithm II

In Table 2, we give an idea of the efficiency of the present algorithms as a tool for solving the stationary problem. To get 4 exact digits, Algorithm II needs about 15 times less iterations than the forward scheme (5), and Algorithm I, 30 times less. A comparison with the case $h = \frac{1}{20}$ showed us that this difference increases as N increases.

Algorithm I seems twice as fast as Algorithm II, and this can be explained by the fact that the first gives, at the nth step, an approximation of the solution of the evolution problem at the time $2n\lambda$ versus $n\lambda$ for the second algorithm.

TABLE 2
Number of iterations necessary for Algorithms I and II to give a solution with n exact digits.

<table><tr><td></td><td colspan="2"> $\lambda = 3 \cdot 10^{-4}$ </td><td colspan="2"> $\lambda = 3 \cdot 10^{-3}$ </td><td colspan="2"> $\lambda = 6 \cdot 10^{-3}$ </td><td colspan="2"> $\lambda = 3 \cdot 10^{-2}$ </td></tr><tr><td>n</td><td>I</td><td>II/FWD</td><td>I</td><td>II</td><td>I</td><td>II</td><td>I</td><td>II</td></tr><tr><td>1</td><td>300</td><td>500</td><td>30</td><td>50</td><td>10</td><td>25</td><td>6</td><td>18</td></tr><tr><td>2</td><td>400</td><td>700</td><td>40</td><td>70</td><td>15</td><td>35</td><td>9</td><td>24</td></tr><tr><td>3</td><td>600</td><td>1100</td><td>60</td><td>110</td><td>25</td><td>55</td><td>14</td><td>36</td></tr><tr><td>4</td><td>700</td><td>1400</td><td>70</td><td>140</td><td>45</td><td>95</td><td>60</td><td>102</td></tr><tr><td>5</td><td>900</td><td>1900</td><td>90</td><td>190</td><td>70</td><td>140</td><td>100</td><td>186</td></tr></table>

3.3. An hyperbolic obstacle problem. We have also considered the same obstacle problem with $Bu = du / dx - f$ instead of $-d^2 u / dx^2 + f3.3. An hyperbolic obstacle problem. We have also considered the same obstacle problem with $Bu = du / dx - f$ instead of $-d^2 u / dx^2 + f$, and the specification and the specification

$$
D (B) = \{u \in H ^ {1} (0, 1), u (0) = 0 \}.
$$

We notice that B is monotone but not coercive:

$$
(B u, u) = \frac {1}{2} u ^ {2} (1) \geq 0.
$$

We chose $A = \partial I_K$ , where $K = \{v \in L^2(0,1): v \leq 0\}$ , $f(x) = +1$ for $x \leq \frac{1}{2}$ and $f(x) = -1$ for $x \geq \frac{1}{2}$ .

The exact solution of the stationary problem is

$$
u _ {\infty} (x) = \left\{ \begin{array}{c l} 0 & \text {for} x \leq \frac {1}{2}, \\ \frac {1}{2} - x & \text {for} x \geq \frac {1}{2}. \end{array} \right.
$$

The exact solution of the evolution problem can be evaluated by an integration along the characteristics.

For the discrete problem, $H$ is replaced by $\mathbb{R}^{N}For the discrete problem, $H$ is replaced by $\mathbb{R}^{N}$, and $du/dx$ by an $N\times N$ matrix such that and $du/dx$ by an $N\times N$ matrix such that

$$
(B u) _ {i} = \frac {u _ {i} - u _ {i - 1}}{h} - f _ {i},
$$

where $h = 1 / Nwhere $h = 1 / N$.

It happens, in this case, that for $\lambda = hIt happens, in this case, that for $\lambda = h$, the forward scheme (5) corresponds to an integration along the characteristics and gives then the exact solution of the evolution problem. the forward scheme (5) corresponds to an integration along the characteristics and gives then the exact solution of the evolution problem.

This is not the case however for $\lambda < h$ , and the stability condition for (5) is exactly $\lambda \leqslant h$ .

All the computations have been performed with $h = \frac{1}{100}All the computations have been performed with $h = \frac{1}{100}$.

We give a comparison of Algorithms I and II on this academic problem (see Tables 3, 4, 5 and 6). The results show that Algorithm I is more accurate than II, but II is more stable and not subject to the same oscillations as I for $\lambda$ five or ten times greater than h.

TABLE 3  
Values of the solution for x = 1, with respect to t, λ, and the type of the algorithm (hyperbolic case where $u^{0} = 0$ for t = 0).

<table><tr><td></td><td> $\lambda = 0.005$ </td><td colspan="3"> $\lambda = 0.01$ </td><td colspan="2"> $\lambda = 0.05$ </td><td colspan="2"> $\lambda = 0.1$ </td></tr><tr><td>t</td><td>FWD</td><td>FWD(exact)</td><td>I</td><td>II</td><td>I</td><td>II</td><td>I</td><td>II</td></tr><tr><td>0.2</td><td>-0.200</td><td>-0.200</td><td>-0.200</td><td>-0.200</td><td>-0.199</td><td>-0.199</td><td>-0.198</td><td>-0.194</td></tr><tr><td>0.4</td><td>-0.399</td><td>-0.400</td><td>-0.397</td><td>-0.393</td><td>-0.390</td><td>-0.373</td><td>-0.381</td><td>-0.353</td></tr><tr><td>0.6</td><td>-0.499</td><td>-0.500</td><td>-0.497</td><td>-0.490</td><td>-0.509</td><td>-0.468</td><td>-0.509</td><td>-0.446</td></tr><tr><td>0.8</td><td>-0.500</td><td>-0.500</td><td>-0.500</td><td>-0.499</td><td>-0.503</td><td>-0.495</td><td>-0.540</td><td>-0.485</td></tr><tr><td>1.0</td><td>-0.500</td><td>-0.500</td><td>-0.500</td><td>-0.500</td><td>-0.498</td><td>-0.499</td><td>-0.505</td><td>-0.496</td></tr><tr><td>1.2</td><td>-0.500</td><td>-0.500</td><td>-0.500</td><td>-0.500</td><td>-0.500</td><td>-0.500</td><td>-0.487</td><td>-0.499</td></tr><tr><td>1.4</td><td>-0.500</td><td>-0.500</td><td>-0.500</td><td>-0.500</td><td>-0.500</td><td>-0.500</td><td>-0.504</td><td>-0.500</td></tr><tr><td>1.6</td><td>-0.500</td><td>-0.500</td><td>-0.500</td><td>-0.500</td><td>-0.500</td><td>-0.500</td><td>-0.504</td><td>-0.500</td></tr></table>

TABLE 4
Number of iterations necessary for Algorithms I and II to give a solution with n exact digits.

<table><tr><td></td><td colspan="2"> $\lambda = 0.01$ </td><td colspan="2"> $\lambda = 0.05$ </td><td colspan="2"> $\lambda = 0.1$ </td></tr><tr><td>n</td><td>I</td><td>II</td><td>I</td><td>II</td><td>I</td><td>II</td></tr><tr><td>1</td><td>50</td><td>50</td><td>6</td><td>12</td><td>3</td><td>6</td></tr><tr><td>2</td><td>60</td><td>60</td><td>6</td><td>16</td><td>7</td><td>10</td></tr><tr><td>3</td><td>70</td><td>70</td><td>12</td><td>20</td><td>25</td><td>13</td></tr><tr><td>4</td><td>70</td><td>80</td><td>23</td><td>24</td><td>38</td><td>16</td></tr></table>

TABLE 5
Same as above but starting from $u^{0} = -x$ (for t = 0).

<table><tr><td></td><td colspan="3"> $\lambda = 0.01$ </td><td colspan="2"> $\lambda = 0.05$ </td></tr><tr><td>t</td><td>FWD(exact)</td><td>I</td><td>II</td><td>I</td><td>II</td></tr><tr><td>0.1</td><td>-1.000</td><td>-1.000</td><td>-1.000</td><td>-1.000</td><td>-0.999</td></tr><tr><td>0.2</td><td>-1.000</td><td>-1.000</td><td>-1.000</td><td>-0.999</td><td>-0.998</td></tr><tr><td>0.3</td><td>-1.000</td><td>-0.999</td><td>-0.999</td><td>-0.996</td><td>-0.985</td></tr><tr><td>0.4</td><td>-1.000</td><td>-0.995</td><td>-0.986</td><td>-0.981</td><td>-0.946</td></tr><tr><td>0.5</td><td>-1.000</td><td>-0.944</td><td>-0.920</td><td>-0.933</td><td>-0.872</td></tr><tr><td>0.6</td><td>-0.800</td><td>-0.796</td><td>-0.785</td><td>-0.828</td><td>-0.772</td></tr><tr><td>0.7</td><td>-0.600</td><td>-0.620</td><td>-0.635</td><td>-0.672</td><td>-0.672</td></tr><tr><td>0.8</td><td>-0.500</td><td>-0.520</td><td>-0.541</td><td>-0.526</td><td>-0.593</td></tr><tr><td>1.0</td><td>-0.500</td><td>-0.500</td><td>-0.501</td><td>-0.485</td><td>-0.518</td></tr><tr><td>1.2</td><td>-0.500</td><td>-0.500</td><td>-0.500</td><td>-0.513</td><td>-0.502</td></tr></table>

TABLE 6
Number of iterations necessary for Algorithms I and II to give a solution with n exact digits.

<table><tr><td></td><td colspan="2"> $\lambda = 0.01$ </td><td colspan="2"> $\lambda = 0.05$ </td></tr><tr><td>n</td><td>I</td><td>II</td><td>I</td><td>II</td></tr><tr><td>1</td><td>40</td><td>80</td><td>8</td><td>16</td></tr><tr><td>2</td><td>45</td><td>90</td><td>13</td><td>22</td></tr><tr><td>3</td><td>45</td><td>110</td><td>25</td><td>26</td></tr><tr><td>4</td><td>50</td><td>120</td><td>35</td><td>32</td></tr></table>

For given $t$ , the solution $u(x, t)$ given by Algorithms I and II is smoother than the exact solution: the same phenomenon occurs for the forward scheme (5) and $\lambda < h$ .

The results show that it is possible, in this case, to take $\lambda$ five times bigger than h with still fairly accurate results, which does not give a decisive superiority of Algorithms I and II over the standard forward scheme which requires clearly less computations in this special one dimensional case.

4. Conclusion. From the numerical results, it seems that the alternating direction Algorithms I and II are more interesting in parabolic problems where the stability

condition for the forward scheme is sharp; Algorithm I requires roughly half the computation of II.

For the hyperbolic problem considered in § 3.3, I seems to be more accurate than II, but II to be more stable than I. The comparison with a forward scheme is difficult, since the forward scheme gives an exact solution for $\lambda = h$ (integration along the characteristics).

The superiority of Algorithm II over the forward scheme (5) has been shown by [10], [11], for a wide class of problems of the type considered in § 1.4, where $J_A^\lambda$ is linear and $J_B^\lambda$ nonlinear but split in small nonlinear pieces. We conjecture that I should have some analogous properties in this case.

Acknowledgment. We would like to thank Jim Douglas and Todd Dupont for very helpful conversations, and the referee for his interesting remarks.

# REFERENCES

[1] J. B. BAILLON, Quelques propriétés de convergence asymptotique pour les contractions impaires, C.R. Acad. Sci. Paris, Série A, 283 (1976), pp. 587–590.  
[2] J. B. BAILLON AND B. MERCIER, Internal Report, Ecole Polytechnique, 1977.  
[3] H. BREZIS, Opérateurs maximaux monotones et semigroupes de contraction dans les espaces de Hilbert, Lecture Notes no. 5, North-Holland, Amsterdam, 1973.  
[4] ——, to appear. (Lecture Notes, Ecole Polytechnique, Unpublished.)  
[5] F. E. BROWDER AND W. V. PETRYSHYN, Construction of fixed points of nonlinear mappings in Hilbert spaces, J. Math. Anal. Appl., 20 (1967), pp. 197-228.  
[6] R. E. BRUCK, An iterative solution of a variational inequality for certain monotone operators in Hilbert spaces, Bull. Amer. Math. Soc., 81 (1975), pp. 890-892.  
[7] J. DOUGLAS AND J. E. GUNN, A general formulation of alternating direction methods, Numer. Math., 6 (1964), pp. 428–453.  
[8] J. DOUGLAS AND H. H. RACHFORD, On the numerical solution of the heat conduction problem in 2 and 3 space variables, Trans. Amer. Math. Soc., 82 (1956), pp. 421-439.  
[9] I. EKELAND AND R. TEMAM, Convex Analysis and Variational Problems, Springer-Verlag, New York, 1977.  
[10] D. GABAY AND B. MERCIER, A dual algorithm for the solution of nonlinear variational problems via finite element approximation, Computer Math. Appl., 2 (1976), pp. 17-40.  
[11] R. GLOWINSKI AND A. MAROCCO, Approximation par éléments finis d'ordre un et résolution par pénalisation-dualité d'une classe de problèmes non linéaires, R.A.I.R.O., R2 (1975), pp. 41–76.  
[12] A. A. GOLDSTEIN, Convex programming in Hilbert spaces, Bull. Amer. Math. Soc., 70 (1964), pp. 709–710.  
[13] J. LIEUTAUD, Approximation par des méthodes de décomposition, Doctoral Dissertation, Paris, 1971.  
[14] P. L. LIONS, Une méthode itérative de résolution d'inéquations variationnelles, to appear.  
[15] G. I. MARCHOUK, Methods of Numerical Mathematics, Springer-Verlag, New York, 1975.  
[16] D. W. PEACEMAN AND H. H. RACHFORD, The numerical solution of parabolic and elliptic differential equations, J. Soc. Indust. Appl. Math., 3 (1955), pp. 28–41.  
[17] R. T. ROCKAFELLAR, Convex Analysis, Princeton University Press, Princeton, NJ, 1970.  
[18] R. S. VARGA, Matrix iterative analysis, Prentice-Hall, Englewood Cliffs, NJ, 1966.

Note added in proof. Our references would be incomplete without the excellent paper by R. B. Kellogg, Nonlinear alternating direction algorithms, Math. Comp. 23 (1969), pp. 23–28 which deals with Algorithm I in the case of single valued monotone operators.
