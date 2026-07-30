# A family of variable metric proximal methods

J.F. Bonnans, J.Ch. Gilbert, C. Lemaréchal, C.A. Sagastizábal

INRIA, Rocquencourt, B.P. 105, 78153 Le Chesnay Cedex, France

Received 18 February 1993; revised manuscript received 23 May 1994

# Abstract

We consider conceptual optimization methods combining two ideas: the Moreau–Yosida regularization in convex analysis, and quasi-Newton approximations of smooth functions. We outline several approaches based on this combination, and establish their global convergence. Then we study theoretically the local convergence properties of one of these approaches, which uses quasi-Newton updates of the objective function itself. Also, we obtain a globally and superlinearly convergent BFGS proximal method. At each step of our study, we single out the assumptions that are useful to derive the result concerned.

AMS Subject Classification: Primary: 65K05; Secondary: 90C30, 52A41, 90C25

Keywords: Bundle methods; Convex optimization; Global and superlinear convergence; Mathematical programming; Proximal point; Quasi-Newton algorithms; Variable metric

# 1. Introduction

We consider in this paper algorithms to solve

$$
\min \{f (x) \colon x \in \mathbb {R} ^ {N} \}, \tag {1.1}
$$

where $f$ is always assumed closed proper convex (we follow the terminology of [30]: $f$ takes its values in $\mathbb{R} \cup \{+\infty\}$ but is not identically $+\infty$ ; closedness means lower semi-continuity). Additional assumptions on $f$ will also be made, when studying rates of convergence.

Our algorithms are based on the use of the proximal mapping: given $x \in \mathbb{R}^{N}$ and a symmetric positive definite $N \times N$ matrix M, f is perturbed to the strongly convex function

$$
\varphi_ {M} (z) := f (z) + \frac {1}{2} \left\langle M (z - x), z - x \right\rangle ; \tag {1.2}
$$

$\langle u, v \rangle := u^{\mathrm{T}}v$ is the usual dot product in $\mathbb{R}^{N}$ and $|\cdot|$ the associated norm. Note that $\varphi_{M}$ has a unique minimizer. The image of $x$ under the proximal mapping is

$$
p _ {M} (x) := \arg \min \{\varphi_ {M} (z): z \in \mathbb {R} ^ {N} \}. \tag {1.3}
$$

Throughout, we will find it convenient to use the notation

$$
x ^ {p} := p _ {M} (x)  .
$$

A traditional way of solving problem (1.1) via the proximal mapping (1.3) is the proximal point algorithm (see [19,31]). This method generates a minimizing sequence $\{x_{n}\}$ by the recurrence formula

$$
x _ {n + 1} := x _ {n} ^ {p} = p _ {M} (x _ {n}), \tag {1.4}
$$

with a possibly varying matrix $M$ of the form $M = c_{n}I, c_{n} > 0$. In view of the optimality condition for (1.3),

$$
x ^ {p} = x - M ^ {- 1} g ^ {p}, \quad \text { for   some } g ^ {p} \in \partial f (x ^ {p}),
$$

the proximal point algorithm can be seen as a 'preconditioned implicit gradient method' to minimize $f$. The method is implicit since the subgradient used in the formula is evaluated at $x^p$, not at $x$, and the preconditioning is realized by the matrix $M$.

Another motivation for this approach is the Moreau–Yosida regularization of $f$ (see [21,31]). This is the function $f^{p}$ whose value at $x\in\mathbb{R}^{N}$ is

$$
f ^ {p} (x) := \varphi_ {M} (x ^ {p}) = \min \left\{f (z) + \frac {1}{2} \langle M (z - x), z - x \rangle : z \in \mathbb {R} ^ {N} \right\}. \tag {1.5}
$$

Indeed, the minima of $f$ coincide with those of $f^p$ and this latter function is convex, finite everywhere, and fairly smooth: with no additional assumption, $f^p$ has a Lipschitz continuous gradient given by the formula

$$
\nabla f ^ {p} (x) = M (x - x ^ {p}) = g ^ {p}. \tag {1.6}
$$

Then the proximal point algorithm written in the form

$$
x _ {n + 1} := x _ {n} ^ {p} = x _ {n} - M ^ {- 1} M (x _ {n} - x _ {n} ^ {p}) = x _ {n} - M ^ {- 1} \nabla f ^ {p} (x _ {n})
$$

can also be viewed as a preconditioned 'explicit' gradient method to minimize $f^p$.

Thus, the Moreau–Yosida regularization provides a link between classical and non-smooth optimization: a natural and attractive idea is to minimize $f^{p}$ by a variable metric method of the type

$$
x _ {n + 1} := x _ {n} - t _ {n} M _ {n} ^ {- 1} \nabla f ^ {p} (x _ {n}) = x _ {n} - t _ {n} M _ {n} ^ {- 1} M (x _ {n} - x _ {n} ^ {p}). \tag {1.7}
$$

The stepsize $t_n > 0$ can be computed as usual, and the matrix $M_n$ can be generated according to a quasi-Newton formula [8], $M_{n+1} := qN(M_n, y_n, s_n)$, using

$$
s _ {n} := x _ {n + 1} - x _ {n}, \quad y _ {n} := \nabla f ^ {p} (x _ {n + 1}) - \nabla f ^ {p} (x _ {n}) = M (x _ {n + 1} - x _ {n + 1} ^ {p} - x _ {n} + x _ {n} ^ {p}) \tag {1.8}
$$

(other choices for $s_n$ and $y_{n}$ are possible, see [18]).

For example, the BFGS formula can be used; because its convergence just requires Lipschitz continuity of the gradient [25], the resulting method will converge always globally, and superlinearly in the 'good' cases when $f^p$ has a Lipschitz continuous Hessian. Now come implementation issues: how can we compute $x_n^p$ ? and how will its computation - or rather its approximation - affect convergence properties? As pointed out in [9,1], bundle methods are a possible proposal. Given $x = x_n$, they provide a way of constructing a sequence $\{p^k\}$ tending to $p_M(x)$ when $k \to \infty$ ; more importantly, they also provide an efficient stopping criterion to apply a recurrence formula such as (1.4), the proximal point being replaced by its approximation $p^k$. We refer to [15,5] for an accurate account of bundle methods from this point of view.

Starting from these ideas, we distinguish three possibilities.

# Algorithmic Pattern 1 (AP1)

Step 0. The symmetric positive definite matrix $M$ is fixed throughout, say $M = I$. Start with an initial $x_{1}$ and some matrix $M_{1}$. Set the iteration counter $n = 1$.

Step 1. Given $x_{n}$ , generate a sequence $p_n^k \to p_M(x_n)$ , for example by a bundling algorithm, until the associated stopping criterion is satisfied.

Step 2. Compute a stepsize $t_n > 0$ to obtain

$$
x _ {n + 1} := x _ {n} - t _ {n} M _ {n} ^ {- 1} M (x _ {n} - p _ {n} ^ {k}) .
$$

Step 3. Update $M_{n}$ by a quasi-Newton formula using (1.8). Increase $n$ by 1 and loop to Step 1.

Unfortunately, bundle methods, which produce the estimate $p_n^k$ in Step 1, rely heavily on the update formula $x_{n+1} = p_n^k$. The reason is that Step 1 is stopped when $f(p_n^k)$ is sufficiently smaller than $f(x_n)$ ; but this decrease does not seem to allow $f(x_{n+1}) < f(x_n)$ in Step 2. We refer to [20] for first steps into the analysis of the above strategy.

Remark 1.1. Incidentally, a second question is the choice of M: after all, the best matrix for (1.1)-(1.3) should be $\mathbf{M} = 0$, in which case no update of $x_{n}$ would be needed. Among other things, $M$ should somewhat take into account the scaling of the problem.

A way round this difficulty is to take in (1.5) a varying matrix $M$ yielding $x_{n+1} = x_n^p$. This results in the following variant:

# Algorithmic Pattern 2 (AP2)

Step 0. Start with some initial point $x_{1}$ and matrix $M_{1}$. Set $n = 1$.

Step 1. Given $x_{n}$ and $M_{n}$, generate a sequence $p_{n}^{k} \to p_{M_{n}}(x_{n})$, for example by a bundling algorithm, until the associated stopping criterion is satisfied.

Step 2. Take

$$
x _ {n + 1} := p _ {n} ^ {k}.
$$

Step 3. Update $M_{n}$ by a quasi-Newton formula using (1.8). Increase $n$ by 1 and loop to Step 1.

The need for an artificial $M$ is thus eliminated (barring the initial $M_1$ ), and the spirit of bundle methods is preserved; but now, the difficulty is in the quasi-Newton field: we no longer have a fixed Moreau-Yosida regularization $f^p$, whose Hessian is going to be approximated by $\{M_n\}$ : we rather have a varying function $f^p$ which depends on $M_n$, giving birth to a sort of vicious circle.

Remark 1.2. Exploratory experiments with this latter algorithm indicate that some eigenvalues of $M_{n}$ may have a tendency to approach 0; in view of Remark 1.1 this is not bad ( $f^{p}$ becomes closer to the true objective $f$ ), but will certainly result in delicate analysis and numerical implementation. On the other hand, preliminary experiments also indicate that this pattern deserves study: the algorithm behaves quite well on a benchmark of test problems for non-smooth optimization [32].

In this paper, we concentrate on a third alternative, based on an idea of [28]:

# Algorithmic Pattern 3 (AP3)

Take (AP2) but, instead of (1.8), let the quasi-Newton update use more simply

$$
s _ {n} = x _ {n + 1} - x _ {n}, \quad y _ {n} = \nabla f (x _ {n + 1}) - \nabla f (x _ {n}). \tag {1.9}
$$

Then the algorithm is just that of (AP2) with the following last step:

Step 3. Update $M_{n}$ by a quasi-Newton formula using (1.9). Increase $n$ by 1 and loop to Step 1.

Naturally this has little meaning in the framework of non-smooth optimization: (1.9) requires differentiability from $f$. Furthermore, we will pay little attention to implementability issues, i.e., on the actual computation of each proximal point $x_{n}^{p}$. Our ambition here is limited to exploring preliminary results to combine methods for non-smooth optimization and classical quasi-Newton methods.

The paper is organized as follows. In the next section we state an abstract algorithmic pattern which accommodates any of the above strategies (AP1–3), and we give conditions guaranteeing global convergence. This section does not rely on the actual computation of proximal points $x_{n}^{p}$, neither on specific formulae generating the matrices $M_{n}$. We obtain in Section 2 our global results without any additional assumption on f. In the following sections, when we consider the local analysis of specific quasi-Newton formulae, we require $\nabla f$ to be locally Lipschitzian, we assume also that it admits directional derivatives at $\bar{x}$. In Section 3, we adapt to our case the criterion of [6] for superlinear convergence. Then we give superlinear convergence results for a wide class of quasi-Newton methods, including PSB and DFP, assuming that f has at $\bar{x}$ a Hessian, in a ‘strong’ sense. Under the same assumptions, we concentrate in Section 4 on both global and superlinear convergence of a conceptual algorithm using the BFGS update. Finally Section 5 gives some concluding remarks.

# 2. Global convergence

In this section we prove the global convergence of the algorithms described abstractly by the General Algorithmic Pattern (GAP) below. Let $(x_{n},M_{n})$ be the current iterate with

$M_{n}$ symmetric positive definite. Then, according to (1.4) and (1.5), the corresponding proximal point will be:

$$
x _ {n} ^ {p} := p _ {M _ {n}} (x _ {n}) = \arg \min \{f (z) + \frac {1}{2} \left\langle M _ {n} (z - x _ {n}), z - x _ {n} \right\rangle : z \in \mathbb {R} ^ {N} \}. \tag {2.1}
$$

We set

$$
W _ {n} := M _ {n} ^ {- 1}.
$$

Lemma 2.1. With the notation and assumptions of Section 1, the following holds:

(i) The proximal point $x_{n}^{p}$ is well defined and given by

$$
x _ {n} ^ {p} = x _ {n} - W _ {n} g _ {n} ^ {p}, \tag {2.2}
$$

with

$$
g _ {n} ^ {p} \in \partial f (x _ {n} ^ {p}). \tag {2.3}
$$

(ii)

$$
f (x _ {n} ^ {p}) \leqslant f (x _ {n}) - \left\langle W _ {n} g _ {n} ^ {p}, g _ {n} ^ {p} \right\rangle . \tag {2.4}
$$

(iii) $x_{n}$ minimizes $f \Leftrightarrow x_{n} = x_{n}^{p} \Leftrightarrow g_{n}^{p} = 0$.

(iv) For all $y$ with $f(y) \leqslant f(x_n^p)$, there holds

$$
\langle M _ {n} (y - x _ {n} ^ {p}), y - x _ {n} ^ {p} \rangle \leqslant \langle M _ {n} (y - x _ {n}), y - x _ {n} \rangle . \tag {2.5}
$$

Proof. The minimand in (2.1) is lower semi-continuous and strongly convex; moreover, for any $z \in \mathrm{dom}(\partial f)$ it has the subdifferential $\partial f(z) + M_n(z - x_n)$. Existence and uniqueness of its minimum (that is the proximal point) is therefore clear, as well as the optimality conditions (2.2), (2.3). To obtain (2.4), multiply (2.2) by $g_n^p$ and use (2.3). The equivalences in (iii) follow easily from (i) and (ii). As for (iv), take $y$ with $f(y) \leqslant f(x_n^p)$. Using (2.3),

$$
f (x _ {n} ^ {p}) \geqslant f (y) \geqslant f (x _ {n} ^ {p}) + \left\langle g _ {n} ^ {p}, y - x _ {n} ^ {p} \right\rangle ,
$$

so that, with (2.2),

$$
\langle M _ {n} (x _ {n} - x _ {n} ^ {p}), y - x _ {n} ^ {p} \rangle \leqslant 0.
$$

Then develop the relation $|M_n^{1/2}(x_n - y)|^2 = |M_n^{1/2}(x_n - x_n^p + x_n^p - y)|^2$ to obtain (2.5). □

Thus, the decrease of $f$ from $x_{n}$ to $x_{n}^{p}$ is at least $\langle g_{n}^{p}, W_{n}g_{n}^{p} \rangle$, a positive number unless $x_{n}$ is optimal. The Moreau-Yosida regularization takes the value

$$
f ^ {p} (x _ {n}) = f (x _ {n} ^ {p}) + \frac {1}{2} \left\langle x _ {n} ^ {p} - x _ {n}, M _ {n} (x _ {n} ^ {p} - x _ {n}) \right\rangle \tag {2.6}
$$

and, using (2.2) we set

$$
\delta_ {n} := f (x _ {n}) - f ^ {p} (x _ {n}) = f (x _ {n}) - f (x _ {n} ^ {p}) - \frac {1}{2} \left\langle g _ {n} ^ {p}, W _ {n} g _ {n} ^ {p} \right\rangle . \tag {2.7}
$$

Observe that, in view of (2.4),

$$
\frac {1}{2} \left\langle g _ {n} ^ {p}, W _ {n} g _ {n} ^ {p} \right\rangle \leqslant \delta_ {n} \leqslant f (x _ {n}) - f (x _ {n} ^ {p}). \tag {2.8}
$$

We consider in this section a very general pattern, in which $f$ is simply required to decrease at each iteration by at least a fixed fraction $m$ of $\delta_n$, interpreted as a 'nominal decrease'.

# General Algorithmic Pattern (GAP)

Step 0. Start with some initial point $x_{1}$ and matrix $M_{1}$ ; choose some descent parameter $m \in ]0,1[$ ; set $n = 1$.

Step 1. With $\delta_{n}$ given by (2.7), compute $x_{n + 1}$ satisfying

$$
f (x _ {n + 1}) \leqslant f (x _ {n}) - m \delta_ {n} \tag {2.9}
$$

(note: for this, Proposition 2.2 below is helpful).

Step 2. Update $M_{n}$, increase $n$ by 1 and loop to Step 1.

For a nominal decrease, the use of the value $f(x_{n}) - f(x_{n}^{p})$ in (2.9) may seem more natural than our $\delta_{n}$. A substantial advantage of (2.7), however, is that implementable methods are known to guarantee (2.9) without computing any proximal point. In fact, if f is replaced by some smaller function $\psi$ in the proximal problem (2.1), we get a smaller optimal value, which can be used to overestimate the nominal decrease.

Proposition 2.2. With the notation above, let $\psi$ be a closed convex function on $\mathbb{R}^N$ satisfying $\psi \leqslant f$ and set

$$
\pi := \arg \min \{\psi (z) + \frac {1}{2} \left\langle M _ {n} (z - x _ {n}), z - x _ {n} \right\rangle : z \in \mathbb {R} ^ {N} \}. \tag {2.10}
$$

(i) If

$$
f (\pi) \leqslant f (x _ {n}) - m [ f (x _ {n}) - \psi (\pi) ], \tag {2.11}
$$

then (2.9) is satisfied by $x_{n+1} = \pi$.

(ii) If $x_{n}$ does not minimize $f$, there exists $\epsilon_{n} > 0$ such that $f(\pi) - \psi(\pi) \leqslant \epsilon_{n}$ implies

$$
f (\pi) - \psi (\pi) \leqslant (1 - m) [ f (x _ {n}) - \psi (\pi) ], \tag {2.12}
$$

which is equivalent to (2.11).

Proof. In the inequality

$$
\psi (\pi) - f (x _ {n}) \leqslant \psi (\pi) + \frac {1}{2} \left\langle M _ {n} (\pi - x _ {n}), \pi - x _ {n} \right\rangle - f (x _ {n}),
$$

over-estimate the right-hand side by replacing successively $\pi$ by $x_{n}^{p}$ and $\psi$ by $f$. Using (2.2), (2.7) we obtain

$$
\psi (\pi) - f (x _ {n}) \leqslant f (x _ {n} ^ {p}) + \frac {1}{2} \left\langle W _ {n} g _ {n} ^ {p}, g _ {n} ^ {p} \right\rangle - f (x _ {n}) = - \delta_ {n}; \tag {2.13}
$$

because $m > 0$, (i) is clearly proved.

Now the equivalence between (2.12) and (2.11) is straightforward. If $x_{n}$ does not minimize $f$, then $x_{n}^{p} \neq x_{n}$ and $g_{n}^{p} \neq 0$. In view of (2.13), we see that (2.12) = (2.11) is satisfied whenever, for example,

$$
f (\pi) - \psi (\pi) \leqslant (1 - m) \delta_ {n} =: \epsilon_ {n} > 0  . \quad \square
$$

The idea underlying (2.11) is classical in line-searches and trust region algorithms, if we interpret $\psi$ as a model for f, whose value at the trial iterate $\pi$ is a target for $f(x_{n+1})$. Proposition 2.2 only says that our descent test (2.9) is passed whenever the model is accurate enough at $\pi$. Bundle methods, precisely, construct such a model which is piecewise affine, resulting in a quadratic program for the proximal program (2.1); see for example [5].

In the convergence result below, $\lambda_{\mathrm{min}}(W)$ denotes the smallest eigenvalue of a symmetric matrix $W$ ; (2.14) is natural to rule out perturbed functions $\varphi_M$ of (1.2) departing too much from $f$.

Theorem 2.3. Assume that the closed convex function $f$ has a nonempty bounded set of minima, and let $\{x_{n}\}$ be a sequence generated by (GAP). Then $\{x_{n}\}$ is bounded, and if

$$
\sum_ {n = 1} ^ {\infty} \lambda_ {\min} (W _ {n}) = \infty , \tag {2.14}
$$

any accumulation point of $\{x_{n}\}$ minimizes $f$. The same properties hold for the sequence of proximal points $\{x_{n}^{p}\}$ and it also holds $\liminf |g_{n}^{p}| = 0$.

Proof. Our starting assumption implies that the level sets of $f$ are bounded (see [30], Theorems 8.4 and 8.7 and [13], Proposition IV.3.2.5); the sequences $\{x_{n}\}$ and $\{x_{n}^{p}\}$ are therefore bounded by construction. In what follows, $\bar{f}$ will denote the minimal value of $f$.

Combining (2.8) and (2.9), we have

$$
\frac {1}{2} \left\langle W _ {n} g _ {n} ^ {p}, g _ {n} ^ {p} \right\rangle \leqslant \frac {1}{m} \left(f (x _ {n}) - f (x _ {n + 1})\right), \tag {2.15}
$$

which gives by summation

$$
\sum_ {n = 1} ^ {\infty} \left\langle W _ {n} g _ {n} ^ {p}, g _ {n} ^ {p} \right\rangle \leqslant \frac {2}{m} (f (x _ {1}) - \bar {f}) <   \infty
$$

and therefore

$$
\sum_ {n = 1} ^ {\infty} \lambda_ {\min} (W _ {n}) \left| g _ {n} ^ {p} \right| ^ {2} <   \infty .
$$

In view of (2.14), the sequence $\{|g_{n}^{p}|^{2}\}$ cannot be bounded away from 0: there exists a subset $N_{1} \subset \mathbb{N}$ such that $\lim_{n \in N_{1}} g_{n}^{p} = 0$ .

Extract from $N_{1}$ a further subset, say $N_{2} \subset N_{1}$, such that $\{x_{n}^{p}\}_{n \in N_{2}}$ tends to some limit $\bar{x}$. Because of (2.3), the closedness of the subdifferential mapping implies that $0 \in \partial f(\bar{x})$ : $\bar{x}$ minimizes $f$ and $f(\bar{x}) = \bar{f}$.

Now $\{f(x_n)\}$ is non-increasing and has a limit $f^*$ ; also $\langle W_n g_n^p, g_n^p \rangle \to 0$ in view of (2.15). Pass to the limit in (2.9), written for $n \in N_2$ ; we obtain

$$
f ^ {*} \leqslant f ^ {*} - m (f ^ {*} - \bar {f}),
$$

which implies $f^{*}=\bar{f}$. Then any accumulation point of $\{x_{n}\}$ is also optimal. ☐

# 3. Local convergence

From now on, $f$ is assumed differentiable (and therefore finite everywhere). We use the notation $g(x)$ for the gradient of $f$ at $x$, as well as $g_{n} = g(x_{n})$ and $g_{n}^{p} = g(x_{n}^{p})$.

We specialize in this section the General Algorithm Pattern of Section 2 along the lines of (AP3) in Section 1: we suppose the proximal point $x_{n}^{p}$ is computed exactly and the symmetric positive definite matrix $M_{n}$ is updated at each iteration by a formula such that the quasi-Newton equation holds:

$$
M _ {n + 1} s _ {n} = y _ {n}, \tag {3.1}
$$

where

$$
s _ {n} := x _ {n + 1} - x _ {n}, \quad y _ {n} := g _ {n + 1} - g _ {n}.
$$

In these circumstances, the pure prox-form of (AP3) is clumsy, as observed in [28,20]. Indeed, take the 'ideal' situation in which $f$ is quadratic with a positive definite Hessian matrix $A$, and take $M_{n} = A$ in the algorithm. Then, $x_{n}^{p}$ is the minimizer of

$$
\langle g _ {n}, x - x _ {n} \rangle + \frac {1}{2} \left\langle 2 A (x - x _ {n}), x - x _ {n} \right\rangle ,
$$

which is only half-way towards the real minimum of $f$. A natural cure would be to do a line-search along the direction $x_{n}^{p} - x_{n}$. This idea will be used in Section 4, but in the present local study, we assume that the 'ideal' step size of 2 is taken.

In a word, we consider in this section the following algorithm:

# Quasi-Newton proximal algorithm (qN-AP3)

Step 0. Start with some initial point $x_{1}$ and a positive definite matrix $M_{1}$. Set n=1.

Step 1. Compute $x_{n}^{p} := p_{M_{n}}(x_{n})$.

Step 2. Update

$$
x _ {n + 1} := x _ {n} - 2 M _ {n} ^ {- 1} g _ {n} ^ {p} = x _ {n} + 2 (x _ {n} ^ {p} - x _ {n}). \tag {3.2}
$$

Step 3. Update $M_{n}$ by a quasi-Newton formula satisfying (3.1). Increase $n$ by 1 and loop to Step 1.

Keeping here the notation of the preceding sections, we set

$$
e _ {n} := x _ {n} - \bar {x}, \qquad e _ {n} ^ {p} := x _ {n} ^ {p} - \bar {x} \quad \text {and} \quad \sigma_ {n} := | e _ {n + 1} | + | e _ {n} |. \tag {3.3}
$$

Recall that we have from Lemma 2.1, with $g_{n}^{p} := g(x_{n}^{p})$,

$$
g _ {n} ^ {p} + M _ {n} (x _ {n} ^ {p} - x _ {n}) = 0. \tag {3.4}
$$

Finally, remark that (3.2) gives

$$
x _ {n} ^ {p} = \frac {1}{2} x _ {n} + \frac {1}{2} x _ {n + 1} \quad \text {and} \quad e _ {n} ^ {p} = \frac {1}{2} e _ {n} + \frac {1}{2} e _ {n + 1}. \tag {3.5}
$$

In this section, we study the local convergence properties of the sequence $\{x_{n}\}$ generated by Algorithm (qN–AP3). We always assume that the gradient of f has directional derivatives at $\bar{x}$, a minimum point of f; our smoothness assumptions are reviewed in Section 3.1. In Section 3.2, we prove the linear convergence of $\{x_{n}\}$, assuming that $(x_{1}, M_{1})$ is ‘good enough’ and that a bounded deterioration property holds for $\{M_{n}\}$ as is done in [14] for standard quasi-Newton algorithms. We characterize the superlinear convergence in Section 3.3, giving the prox-version of the well-known characterization for superlinear convergence of [6]. Finally, under stronger smoothness assumptions, we obtain local and superlinear convergence results for a wide class of quasi-Newton formulae, including the prox-versions of the PSB and DFP algorithms. For this we extend the approach of Grzegórski [12] to variational quasi-Newton methods with variable norms and to the ‘proximal’ framework.

# 3.1. Smoothness assumptions

In this subsection we state the assumptions needed for the sequel. We start by recalling some classical notions. An operator $H$ from $\mathbb{R}^N$ to $\mathbb{R}^N$ is positively homogeneous when $H(tv) = tHv$, for all $v \in \mathbb{R}^N$ and all $t \geqslant 0$. Such an operator is said bounded if

$$
| H | := \sup _ {| v | = 1} | H v |
$$

is finite. It is equivalent to say that $H$ is continuous at 0. Observe that we use the same notation for the Euclidean norm in $\mathbb{R}^N$ and for the induced operator norm.

For the local analysis, only the behaviour of $f$ in some neighbourhood of $\bar{x}$ is relevant. Actually, our assumptions throughout involve a convex neighbourhood $\Omega$ of $\bar{x}$.

\- First of all, we require the gradient to be locally Lipschitzian around $\bar{x}$ : there is a constant $L_{g}$ such that

$$
\forall x, y \in \Omega , \quad | g (x) - g (y) | \leqslant L _ {g} | x - y |. \tag {3.6}
$$

\- We postulate that $g$ admits at $\bar{x}$ a directional derivative $g'(\bar{x}, d)$, for all $d \in \mathbb{R}^N$. To stress that we are only interested in $g'$ at the fixed solution point $\bar{x}$, we will generally use the notation $\bar{H}$ for the mapping $d \mapsto g'(\bar{x}, d)$. In other words,

$$
\bar {H} d := \bar {H} (d) = \lim _ {t \downarrow 0} \frac {g (\bar {x} + t d) - g (\bar {x})}{t}. \tag {3.7}
$$

Observe that $\bar{H}$ is positively homogeneous by definition and bounded because of (3.6): $|\bar{H}| \leqslant L_g$.

\- We will often suppose that the directional derivative (3.7) exists in a strong sense at $\bar{x}$ ([22,23], see also [4], where the word strict is used). This means

$$
\lim_ {\substack {(x, y) \to (\bar {x}, \bar {x}) \\ x \neq y}} \frac {g (x) - g (y) - \bar {H} (x - y)}{| x - y |} = 0. \tag{3.8}
$$

\- Our final results need the difference quotient in (3.8) to converge at a specific rate, namely: for some positive constant $L$ and all $x, y \in \Omega$,

$$
\left| g (x) - g (y) - \bar {H} (x - y) \right| \leqslant L (\left| x - \bar {x} \right| + \left| y - \bar {x} \right|) \left| x - y \right|. \tag {3.9}
$$

Needless to say, (3.9) implies (3.8), which in turn implies (3.7).

It is interesting to relate our assumptions with some other notions of weakened differentiability already stated in the literature; see for example $[23,16,14,24]$. We recall first that, under the Lipschitz property (3.6), the limit in (3.7) becomes uniform in d: (3.7) is then equivalent to

$$
g (\bar {x} + h) = g (\bar {x}) + \bar {H} h + o (| h |), \quad \text {when} h \rightarrow 0, \tag {3.10}
$$

that is, $\bar{H}$ is the B-derivative of $g$ at $\bar{x}$, in the sense of [29].

Assumption (3.8) turns out to be rather strong, even though it is a purely punctual condition. In fact, it can be seen as in the proof of [23, Theorem 2], that it implies the linearity of $\bar{H}$ ; and this just means that $\bar{H}$ is the strong Fréchet derivative of $g$ at $\bar{x}$. To grasp the essence of (3.8), consider the case when $g$ has directional derivatives in a neighbourhood of $\bar{x}$ : (3.8) just expresses the continuity of the mapping $x \mapsto g'(x, \cdot)$ at $\bar{x}$ ; this comes from the following theorem, which is an equivalent formulation of Theorem 2 in [23].

Theorem 3.1. Let $g: \mathbb{R}^N \to \mathbb{R}^N$ be a mapping satisfying (3.6) and having directional derivatives $g'(x, \cdot)$ for all $x \in \Omega$. Then the three statements below are equivalent:

(i) the directional derivative $\bar{H}$ of (3.7) satisfies the stronger limit property (3.8),

(ii) $g$ is Fréchet differentiable at $\bar{x}$ in the strong sense,

(iii) the mapping $x \mapsto g'(x, \cdot)$ is continuous at $\bar{x}$ ; in other words,

$$
\sup _ {| d | = 1} \left| g' (x, d) - g' (\bar {x}, d) \right|\rightarrow 0, \quad w h e n x \rightarrow \bar {x}.
$$

For an interpretation of our last assumption (3.9), assume again the existence of $g'(x, \cdot)$ in a neighbourhood of $\bar{x}$ : (3.9) connotes something stronger than the above continuity property (iii), namely the 'radially Lipschitz' property stated in (3.11). This

comes from the next result, an equivalent formulation of Lemma 2.2 in [14]. It is here that the convexity of $\Omega$ is important.

Theorem 3.2. The hypotheses are those of Theorem 3.1. In addition, assume there exists a constant $L$ such that

$$
\sup _ {| d | = 1} | g' (x, d) - g' (\bar {x}, d) | \leqslant L | x - \bar {x} | \quad \text {for all} x \in \Omega . \tag {3.11}
$$

Then, for all $x$ and $y \in \Omega$ :

$$
\left| g (x) - g (y) - \bar {H} (x - y) \right| \leqslant L \max \{\left| x - \bar {x} \right|, \left| y - \bar {x} \right| \} \left| x - y \right|,
$$

so that (3.9) holds.

# 3.2. Linear convergence and bounded deterioration

In this subsection, we prove the linear convergence of Algorithm (qN-AP3) when the generated matrices $M_{n}$ satisfy a 'Bounded Deterioration' property (Theorem 3.4). Before doing this, it is useful and instructive to analyze one step of the algorithm (Lemma 3.3). Our results are obtained under an extra assumption: there exists a positive definite matrix $\bar{M}$ such that

$$
\left| I - \bar {M} ^ {- 1} \bar {H} \right| \leqslant \bar {r} <   1. \tag {3.12}
$$

Assumption (3.12) is just a way of expressing that the positively homogeneous operator $\bar{H}$ is not too far from the open set of positive definite matrices that is convenient for the convergence analysis. This assumption was also made by Ip and Kyparisis [14]. When $\bar{H}$ is linear, condition (3.12) implies the non-singularity of $\bar{H}$. When $\bar{H}$ is only a continuous positively homogeneous operator, however, the surjectivity of $\bar{H}$ is guaranteed (see the proof of Lemma 2 in [23]) but not its injectivity.

Lemma 3.3. Suppose that (3.6), (3.7) and (3.12) hold. Then, for all $r > \bar{r} / (2 - \bar{r})$, there exist positive constants $\hat{\epsilon}_1, \hat{\epsilon}_2$ and $\mu$ such that if one iterate $(x_n, M_n)$ of Algorithm (qN-AP3) satisfies

$$
\left| x _ {n} - \bar {x} \right| \leqslant \hat {\epsilon} _ {1} \quad a n d \quad \left| M _ {n} - \bar {M} \right| \leqslant \hat {\epsilon} _ {2}, \tag {3.13}
$$

then $M_{n}$ is positive definite with $|M_{n}^{-1}| \leqslant \mu$ and the next iterate $x_{n+1}$ satisfies

$$
\left| x _ {n + 1} - \bar {x} \right| \leqslant r \left| x _ {n} - \bar {x} \right|. \tag {3.14}
$$

Proof. Let $r > \bar{r} / (2 - \bar{r})$ ; there exists $r' > \bar{r}$ such that $r = r' / (2 - r')$ : just take $r' := 2r / (1 + r)$. Now, choose $\hat{\epsilon}_2 > 0$ so that

$$
\hat {\epsilon} _ {2} <   \frac {1}{| \bar {M} ^ {- 1} |} \quad \text {and} \quad \hat {\epsilon} _ {2} | \bar {M} ^ {- 1} | | \bar {H} | \left(\frac {1}{| \bar {M} ^ {- 1} |} - \hat {\epsilon} _ {2}\right) ^ {- 1} \leqslant \frac {r' - \bar {r}}{2}, \tag {3.15}
$$

and set

$$
\mu := \left(\frac {1}{| \bar {M} ^ {- 1} |} - \hat {\epsilon} _ {2}\right) ^ {- 1}. \tag {3.16}
$$

By the first inequality of (3.15), $\mu$ is a positive constant. Now, because $g(\bar{x}) = 0$, we have in (3.10) $g(x) - \bar{H}(x - \bar{x}) = o(|x - \bar{x}|)$. Therefore, there exists $\epsilon_1 > 0$ such that

$$
| x - \bar {x} | \leqslant \epsilon_ {1} \quad \Rightarrow \quad | g (x) - \bar {H} (x - \bar {x}) | \leqslant \frac {r' - \bar {r}}{2 \mu} | x - \bar {x} |. \tag {3.17}
$$

Then, define $\hat{\epsilon}_1 > 0$ by

$$
\hat {\epsilon} _ {1} := \frac {\epsilon_ {1}}{\mu^ {1 / 2} (| \bar {M} | + \hat {\epsilon} _ {2}) ^ {1 / 2}}. \tag {3.18}
$$

Having determined the positive constants $\hat{\epsilon}_1, \hat{\epsilon}_2$ and $\mu$, we now prove the conclusions of the lemma, assuming (3.13).

First, by (3.13) and (3.15), we have

$$
| M _ {n} - \bar {M} | \leqslant \hat {\epsilon} _ {2} <   \frac {1}{| \bar {M} ^ {- 1} |}.
$$

Then, the identity $M_{n} = \bar{M}[I + \bar{M}^{-1}(M_{n} - \bar{M})]$ and the Banach perturbation lemma imply that $M_{n}$ is non-singular (in fact positive definite) and that $|M_n^{-1}| \leqslant \mu$, with $\mu$ defined in (3.16).

Next, we observe that $x_{n+1} = x_n - 2M_n^{-1}g_n^p = x_n^p - M_n^{-1}g_n^p$. Thus an easy calculation gives

$$
\begin{aligned} e _ {n + 1} &= e _ {n} ^ {p} - M _ {n} ^ {- 1} g _ {n} ^ {p} \\ &= (I - M _ {n} ^ {- 1} \bar {H}) e _ {n} ^ {p} - M _ {n} ^ {- 1} (g _ {n} ^ {p} - \bar {H} e _ {n} ^ {p}) \\ &= (I - \bar {M} ^ {- 1} \bar {H}) e _ {n} ^ {p} + \bar {M} ^ {- 1} (M _ {n} - \bar {M}) M _ {n} ^ {- 1} \bar {H} e _ {n} ^ {p} - M _ {n} ^ {- 1} (g _ {n} ^ {p} - \bar {H} e _ {n} ^ {p}). \tag {3.19} \\ \end{aligned}
$$

We are going to bound the norm of the right-hand side of (3.19) by a multiple of $|e_n^p|$. There is no difficulty with the first two terms. For the last term we shall use the implication (3.17) after having shown that $|e_n^p| \leqslant \epsilon_1$. To do this, observe that Lemma 2.1(iv) with $y = \bar{x}$ gives

$$
\frac {1}{| M _ {n} ^ {- 1} |} \left| e _ {n} ^ {p} \right| ^ {2} \leqslant \left| M _ {n} \right| \left| e _ {n} \right| ^ {2}.
$$

Hence, using (3.13), $|e_n| \leqslant \hat{\epsilon}_1$ and (3.18), we get

$$
\left| e _ {n} ^ {p} \right| \leqslant \left| M _ {n} ^ {- 1} \right| ^ {1 / 2} \left| M _ {n} \right| ^ {1 / 2} \left| e _ {n} \right| \leqslant \mu^ {1 / 2} \left(\left| \bar {M} \right| + \hat {\epsilon} _ {2}\right) ^ {1 / 2} \hat {\epsilon} _ {1} = \epsilon_ {1}.
$$

Now, using (3.12) and (3.17), (3.19) gives

$$
\left| e _ {n + 1} \right| \leqslant \left(\bar {r} + \left| \bar {M} ^ {- 1} \right| \hat {\epsilon} _ {2} \mu | \bar {H} | + \mu \frac {r' - \bar {r}}{2 \mu}\right) \left| e _ {n} ^ {p} \right| \leqslant r' \left| e _ {n} ^ {p} \right|,
$$

where we used the second inequality of (3.15) and (3.16). Finally, by (3.5), $|e_n^p| \leqslant (|e_n| + |e_{n+1}|)/2$, and the last inequality becomes

$$
\left(1 - \frac {r'}{2}\right) | e _ {n + 1} | \leqslant \frac {r'}{2} | e _ {n} |.
$$

The conclusion of the lemma follows from the definition of $r'$ :

$$
\mid e _ {n + 1} \mid \leqslant \frac {r'}{2 - r'} \mid e _ {n} \mid = r \mid e _ {n} \mid . \quad \square
$$

Since $\bar{r} / (2 - \bar{r}) < 1$, Lemma 3.3 allows us to take $r < 1$. Then an easy consequence of this result is: if the matrices $M_n$ are maintained in a ball of radius $\hat{\epsilon}_2$ around $\bar{M}$ and if the first iterate $x_1$ is taken sufficiently close to $\bar{x}$, the sequence $\{x_n\}$ generated by Algorithm (qN-AP3) converges to $\bar{x}$ linearly with rate $r$. As we shall see, this property of the matrices $M_n$ is satisfied when they are updated by a large class of formulae, namely those satisfying the bounded deterioration assumption defined below. This assumption depends on a particular matrix norm $\| \cdot \|$ possibly different from $|\cdot|$. Note that, since all norms are equivalent in $\mathbb{R}^{N \times N}$, there exists a positive constant $\eta$ such that

$$
\frac {1}{\eta} \left\| \cdot \right\| \leqslant | \cdot | \leqslant \eta \| \cdot \|. \tag {3.20}
$$

Bounded Deterioration Assumption (BDA). Let there exist a positive constant $C_{\mathrm{BD}}$, a symmetric positive definite matrix $\bar{M}$ and a neighbourhood $\mathcal{U} = \Omega_x \times \Omega_M$ of $(\bar{x}, \bar{M})$, with $\Omega_M$ containing only non-singular matrices, with the following property. If $(x_n, M_n)$ is in $\mathcal{U}$, if $(x_{n+1}, M_{n+1})$ is generated by Algorithm (qN-AP3) from $(x_n, M_n)$ and if $x_{n+1}$ is also in $\Omega_x$, then

$$
\| M _ {n + 1} - \bar {M} \| \leqslant (1 + C _ {\mathrm{BD}} \sigma_ {n}) \| M _ {n} - \bar {M} \| + C _ {\mathrm{BD}} \sigma_ {n}, \tag {3.21}
$$

where the matrix norm $\| \cdot \|$ satisfies (3.20) and $\sigma_{n}$ is defined by (3.3).

This assumption is weaker than the one usually obtainable in standard quasi-Newton methods (see [2]) in the sense that here inequality (3.21) is only assumed to be satisfied when $x_{n}$ and $x_{n + 1}$ are close to $\bar{x}$. Usually no restriction of this type is supposed for (3.21) to be valid, but when variational quasi-Newton updates with variable norms are involved (see Section 3.4), only the above weak form of BDA can be obtained. As far as local convergence is concerned, however, our weaker form suffices: indeed, as shown in Lemma 3.3 (with $r < 1$ ), once $(x_{n}, M_{n})$ is close enough to $(\bar{x}, \bar{M})$, $x_{n + 1}$ is even closer to $\bar{x}$ than $x_{n}$.

Conditions for linear convergence are given in the next theorem. We denote by $B(z, \rho)$ the ball of radius $\rho > 0$ centered at $z$ (in a normed space depending on the context).

Theorem 3.4. Suppose that (3.6), (3.7) and (3.12) hold and that the update of the matrices in Algorithm (qN-AP3) satisfies (BDA) with the same matrix $\bar{M}$ as in (3.12). Then, for all $r\in ]\bar{r} /(2 - \bar{r})$, $1[$, there exist positive constants $\epsilon_{1}$ and $\epsilon_{2}$, such that

$$
| x _ {1} - \bar {x} | \leqslant \epsilon_ {1} \quad a n d \quad | M _ {1} - \bar {M} | \leqslant \epsilon_ {2} \tag {3.22}
$$

imply the following statements:

(i) Algorithm (qN-AP3) is well defined in the sense that, for all $n \geqslant 1$, $M_n$ is positive definite and $x_n^p$ and $x_n$ lie in $\Omega_x$.  
(ii) The sequences $\{M_n\}$ and $\{M_n^{-1}\}$ are bounded and the sequence $\{\| M_n - \tilde{M}\|\}$ converges.  
(iii) The sequence $\{x_{n}\}$ converges linearly to $\bar{x}$ at rate $r$ :

$$
\left| x _ {n + 1} - \bar {x} \right| \leqslant r \left| x _ {n} - \bar {x} \right|, \quad \forall n \geqslant 1. \tag {3.23}
$$

Proof. Take $r \in ]\bar{r} / (2 - \bar{r}), 1[ \neq \phi$ and let $\hat{\epsilon}_1 > 0$ and $\hat{\epsilon}_2 > 0$ be given by Lemma 3.3. Then choose $\epsilon_2 > 0$ such that

$$
B (\bar {M}, 2 \eta \epsilon_ {2}) \subset \Omega_ {M} \quad \text {and} \quad 2 \eta^ {2} \epsilon_ {2} \leqslant \hat {\epsilon} _ {2}; \tag {3.24}
$$

here $\eta$ is defined in (3.20), $\Omega_{M}$ is introduced in (BDA) and $B(\cdot, \cdot)$ refers to $\|\cdot\|$. Next, choose $\epsilon_{1} > 0$ such that

$$
B (\bar {x}, \epsilon_ {1}) \subset \Omega_ {x}, \qquad \epsilon_ {1} \leqslant \hat {\epsilon} _ {1} \quad \text {and} \quad 2 C _ {\mathrm{BD}} \epsilon_ {1} (2 \eta \epsilon_ {2} + 1) \frac {1}{1 - r} \leqslant \eta \epsilon_ {2}, \tag {3.25}
$$

where $\Omega_{x}$ and $C_{BD}$ were introduced in (BDA).

The positive constants $\epsilon_{1}$ and $\epsilon_{2}$ being determined, suppose that (3.22) holds and let us prove by induction that for all $n\geqslant 1$ :

$$
\| M _ {n} - \bar {M} \| \leqslant 2 \eta \epsilon_ {2}, \tag {3.26}
$$

$$
\left| x _ {n + 1} - \bar {x} \right| \leqslant r \left| x _ {n} - \bar {x} \right|. \tag {3.27}
$$

First, by (3.20),

$$
\| M _ {1} - \bar {M} \| \leqslant \eta | M _ {1} - \bar {M} | \leqslant \eta \epsilon_ {2}. \tag {3.28}
$$

Therefore, (3.26) is satisfied for $n = 1$. As $\epsilon_1 \leqslant \hat{\epsilon}_1$ and $\epsilon_2 \leqslant \hat{\epsilon}_2$ (by (3.24) and $\eta \geqslant 1$ ), we have

$$
| x _ {1} - \bar {x} | \leqslant \hat {\epsilon} _ {1} \quad \text {and} \quad | M _ {1} - \bar {M} | \leqslant \hat {\epsilon} _ {2}.
$$

By Lemma 3.3, this implies that the next iterate $x_{2}$ is well defined and that (3.27) holds for $n = 1$.

Now, assume for induction that (3.26) and (3.27) are satisfied for $n=1,\ldots,m-1$. By (3.27), (3.22) and (3.25), the points $x_{1},\ldots,x_{m}$ are in $B(\bar{x},\epsilon_{1})\subset\Omega_{x}$, and by (3.26) and (3.24), the matrices $M_{1},\ldots,M_{m-1}$ are in $B(\bar{M},2\eta\epsilon_{2})\subset\Omega_{M}$. Therefore, we can use (BDA) for $n=1,\ldots,m-1$ to obtain:

$$
\begin{aligned} \| M _ {n + 1} - \bar {M} \| - \| M _ {n} - \bar {M} \| &\leqslant C _ {\mathrm{BD}} \sigma_ {n} (\| M _ {n} - \bar {M} \| + 1) \\ &\leqslant 2 C _ {\mathrm{BD}} \left| x _ {n} - \bar {x} \right| (\left\| M _ {n} - \bar {M} \right\| + 1) \\ &\leqslant 2 C _ {\mathrm{BD}} r ^ {n - 1} \epsilon_ {1} (2 \eta \epsilon_ {2} + 1), \\ \end{aligned}
$$

where we have used (3.22), (3.26) and (3.27). Adding up from 1 to $m - 1$ and using (3.28) and (3.25), we get

$$
\| M _ {m} - \bar {M} \| \leqslant \| M _ {1} - \bar {M} \| + 2 C _ {\mathrm{BD}} \epsilon_ {1} (2 \eta \epsilon_ {2} + 1) \frac {1}{1 - r} \leqslant 2 \eta \epsilon_ {2}.
$$

This proves (3.26) for $n = m$. To get (3.27) for $n = m$, we use as before Lemma 3.3 after having observed that $|x_{n} - \bar{x}| \leqslant \hat{\epsilon}_{1}$ (by (3.27) and (3.22)) and $|M_{n} - \bar{M}| \leqslant \hat{\epsilon}_{2}$ (by (3.26) and (3.24)). This completes our induction argument.

The boundedness of $\{M_n^{-1}\}$ is given by Lemma 3.3.

Finally, the proof of the convergence of $\{\|M_{n}-\bar{M}\|\}$ follows a classical scheme. The sequence $\{M_{n}\}$ being bounded, the sequence $\{\|M_{n}-\bar{M}\|\}$ has limit points. Then, we proceed by contradiction, supposing that there are two limit points: $l_{1}<l_{2}$. As the series $\sum_{n=1}^{\infty}\sigma_{n}$ converges, there is an index $n_{0}$ such that

$$
\sum_ {n = n _ {0}} ^ {\infty} \sigma_ {n} \leqslant \frac {l _ {2} - l _ {1}}{3} C _ {\mathrm{BD}} ^ {- 1} (2 \eta \epsilon_ {2} + 1) ^ {- 1}.
$$

We can also choose an index $n_1 \geqslant n_0$ such that $\| M_{n_1} - \bar{\mathbf{M}} \| \leqslant l_1 + (l_2 - l_1) / 3$. Then, using (BDA) and (3.26), we can write, for all $n \geqslant n_1$,

$$
\begin{aligned} \| M _ {n} - \bar {M} \| &\leqslant \| M _ {n _ {1}} - \bar {M} \| + C _ {\mathrm{BD}} \sum_ {i = n _ {1}} ^ {n - 1} \left(\sigma_ {i} (\| M _ {i} - \bar {M} \| + 1)\right) \\ &\leqslant \| M _ {n _ {1}} - \bar {M} \| + C _ {\mathrm{BD}} (2 \eta \epsilon_ {2} + 1) \sum_ {i = n _ {0}} ^ {\infty} \sigma_ {i} \\ &\leqslant \| M _ {n _ {1}} - \bar {M} \| + \frac {l _ {2} - l _ {1}}{3} \\ &\leqslant l _ {2} - \frac {l _ {2} - l _ {1}}{3}, \\ \end{aligned}
$$

contradicting the fact that $l_{2}$ is another limit point.

Let us point out that the ‘implicit’ form of (qN–AP3) allows a better rate of convergence than the one obtained in [14] for ‘standard’ quasi-Newton formulae, namely $r \in ]\bar{r}, 1[$.

# 3.3. Characterization of superlinear convergence

In this subsection we characterize the $q$ -superlinear convergence of a sequence $\{x_{n}\}$ generated by Algorithm (qN-AP3) by comparing the effect of $M_{n}$ and $\bar{H}$ on $(-s_{n})$. In [14], $\bar{M}$ in (3.12) is used as an intermediate matrix in the comparison. A similar result can be obtained here but, instead of assuming (3.12), we prefer to impose more regularity on $\bar{H}$. When $\bar{H}$ is linear, both results are similar to the well-known characterization of Dennis and Moré [6].

Lemma 3.5. Let $H: \mathbb{R}^N \mapsto \mathbb{R}^N$ be positively homogeneous, continuous and injective. Then the following properties hold:

(i) there exists a constant $C_H$ such that $|Hu| \geqslant C_H|u|$ for all $u \in \mathbb{R}^N$,  
(ii) for any two bounded sequences $\{u_n\}$ and $\{v_n\}$ in $\mathbb{R}^N$,

$$
H u _ {n} - H v _ {n} \rightarrow 0 \quad \Rightarrow \quad u _ {n} - v _ {n} \rightarrow 0,
$$

(iii) if $u_{n} \to 0$ then

$$
H (u _ {n} + o (\mid u _ {n} \mid)) = H u _ {n} + o (\mid u _ {n} \mid) . \tag {3.29}
$$

Proof. (i) Let $C_H := \min_{|u| = 1} |Hu| \geqslant 0$ ; by continuity there exists $u_0$ of norm 1 such that $|Hu_0| = C_H$. Then the injectivity of $H$ implies $C_H > 0$ ; the conclusion follows from positive homogeneity.

(ii) Having an arbitrary cluster point $w$ of $\{u_n - v_n\}$, extract a subsequence such that $u_n \to u, v_n \to v$ and $u_n - v_n \to w = u - v$. By continuity, $Hu_n \to Hu, Hv_n \to Hv$ and by assumption, $Hu = Hv$. Since $H$ is injective, $u = v, w = 0$ ; the result follows.

(iii) If $H$ is continuous, it is uniformly continuous on the ball $B(0,2) \subset \mathbb{R}^N$. When $u_n \neq 0$, $u_n / |u_n| + o(1) \in B(0,2)$ for large $n$. Hence, by uniform continuity,

$$
H \bigg (\frac {u _ {n}}{| u _ {n} |} + o (1) \bigg) = H \frac {u _ {n}}{| u _ {n} |} + o (1) .
$$

Thanks to positive homogeneity, we have proved (3.29). $\square$

Theorem 3.6. Let $\{x_{n}\}$ be a sequence generated by the recursion formula (3.2) converging to a solution point $\bar{x}$. Suppose that (3.6), (3.7) hold and that $\bar{H}$ is continuous and injective. Then

$$
x _ {n} \rightarrow \bar {x} q \text {-superlinearly} \Leftrightarrow (M _ {n} - \bar {H}) (- s _ {n}) = o (| s _ {n} |). \tag {3.30}
$$

Proof. First, remembering that $s_n = -2M_n^{-1}g_n^p$, we have, due to (3.10),

$$
M _ {n} s _ {n} = - 2 g _ {n} ^ {p} = - 2 \bar {H} e _ {n} ^ {p} + o (| e _ {n} ^ {p} |).
$$

Hence,

$$
(M _ {n} - \bar {H}) (- s _ {n}) = 2 \bar {H} e _ {n} ^ {p} - \bar {H} (- s _ {n}) + o (| e _ {n} ^ {p} |) . \tag {3.31}
$$

Let us prove the ‘⇒’ part. As $e_{n+1} = o(|e_n|)$, we have

$$
2 e _ {n} ^ {p} = e _ {n + 1} + e _ {n} = e _ {n} + o (| e _ {n} |),
$$

$$
- s _ {n} = - e _ {n + 1} + e _ {n} = e _ {n} + o (| e _ {n} |).
$$

The last estimate also implies that $e_n = O(|s_n|)$. Combining these estimates with (3.31) and using (3.29) with $H = \bar{H}$, we get

$$
(M _ {n} - \bar {H}) (- s _ {n}) = o (| e _ {n} |) = o (| s _ {n} |).
$$

Consider now the ‘←’ part. From (3.31),

$$
\bar {H} (- s _ {n}) + o \left(\left| s _ {n} \right|\right) = \bar {H} \left(2 e _ {n} ^ {p}\right) + o \left(\left| e _ {n} ^ {p} \right|\right). \tag {3.32}
$$

Taking norms and applying Lemma 3.5(i), we get

$$
C _ {H} \left| s _ {n} \right| \leqslant \left| \bar {H} (- s _ {n}) \right| \leqslant \left| \bar {H} (2 e _ {n} ^ {p}) \right| + o (\left| e _ {n} ^ {p} \right|) + o (\left| s _ {n} \right|).
$$

Using the boundedness of $\bar{H}$ we conclude

$$
\left| s _ {n} \right| = O (\left| e _ {n} ^ {p} \right|). \tag {3.33}
$$

On the other hand, after division of (3.32) by $|e_{n}^{p}|$ :

$$
\frac {o (| e _ {n} ^ {p} |)}{| e _ {n} ^ {p} |} + \frac {o (| s _ {n} |)}{| e _ {n} ^ {p} |} = \frac {\bar {H} (2 e _ {n} ^ {p})}{| e _ {n} ^ {p} |} - \frac {\bar {H} (- s _ {n})}{| e _ {n} ^ {p} |}.
$$

Thanks to (3.33), the left-hand side tends to 0. We are in a position to apply Lemma 3.5(ii) with $u_{n} = 2e_{n}^{p} / |e_{n}^{p}|$ and $v_{n} = -s_{n} / |e_{n}^{p}|$. Thus

$$
\frac {2 e _ {n} ^ {p} + s _ {n}}{| e _ {n} ^ {p} |} = \frac {2 e _ {n + 1}}{| e _ {n} ^ {p} |} \to 0,
$$

which can be written $e_{n+1} = o(|e_n^p|) = o(|e_{n+1} + e_n|) = o(|e_{n+1}|) + o(|e_n|)$. This implies $e_{n+1} = o(|e_n|)$ and the $q$ -superlinear convergence of $\{x_n\}$.

With this result, the relation corresponding to the classical characterization of [6] can be recovered. Note, incidentally, that the above proof still works for non-smooth equations (instead of minimization) where $g$ is not a gradient. When assuming more regularity on $f$, we can also establish a very useful characterization:

Corollary 3.7. Let $\{x_{n}\}$ be a sequence generated by Algorithm (qN-AP3) converging to a solution point $\bar{x}$. Suppose that (3.6)-(3.8) hold and that $\bar{H}$ is invertible. Then

$$
x _ {n} \rightarrow \bar {x} q \text {-superlinearly} \Leftrightarrow (M _ {n + 1} - M _ {n}) s _ {n} = o (\left| s _ {n} \right|). \tag {3.34}
$$

Proof. Due to the quasi-Newton equation (3.1), the second statement in (3.34) is equivalent to $y_{n}-M_{n}s_{n}=o(|s_{n}|)$. Apply (3.8) with $x=x_{n+1}$, $y=x_{n}$ : we have $y_{n}=\bar{H}s_{n}+o(|s_{n}|)$ ; since (3.8) also implies the linearity of $\bar{H}$, the conclusion follows from Theorem 3.6. ☐

# 3.4. Superlinear convergence of variational quasi-Newton algorithms

In this subsection, we go more concretely into the specification of the matrices $M_{n}$ for Algorithm (qN-AP3). We propose an update scheme and show (Lemma 3.8) that it satisfies (BDA) in Section 3.2. Then, the linear convergence follows from Theorem 3.4 (Theorem

3.9). We also show (Theorem 3.10) that the scheme can provide the $q$-superlinear convergence of the generated sequences.

The analysis relies on a Hilbert matrix norm $|\cdot|_n$ (e.g., a weighted Frobenius norm); typically $|\cdot|_n$ depends on $x_n$ and $x_{n+1}$. With $\sigma_n$ defined in (3.3), the norm $|\cdot|_n$ is said locally comparable to a fixed norm $\| \cdot \|$ if

$$
\exists \sigma_ {\mathrm{LC}} > 0, \exists C _ {\mathrm{LC}} > 0, \quad \forall \sigma_ {n} \leqslant \sigma_ {\mathrm{LC}}, \quad \forall M \in \mathbb {R} ^ {N \times N},
$$

$$
\text {we have} | | M | _ {n} - \| M \| | \leqslant C _ {\mathrm{LC}} \| M \| \sigma_ {n}. \tag {3.35}
$$

Our approach follows that of [12]. Let $\mathcal{K}$ be a closed convex set of symmetric matrices intersecting the set $\{M\in\mathbb{R}^{N\times N}:Ms_{n}=y_{n}\}$, when $\sigma_{n}$ is small. By a variational quasi-Newton formula, we mean a method associating to the current matrix $M_{n}$ the (symmetric) update $M_{n+1}:=\mathrm{qN}(M_{n},y_{n},s_{n})$, unique solution of

$$
\min _ {M} \{| M - M _ {n} | _ {n} ^ {2}: M \in \mathscr {K}, M s _ {n} = y _ {n} \}. \tag {3.36}
$$

We state here a ‘technical hypothesis’ expressing that a fixed matrix $\bar{M}$ is close enough to the feasible set of (3.36):

$$
\exists \bar {M} \in \mathbb {R} ^ {N \times N} \text {symmetric positive definite,} \exists \sigma_ {\mathrm{TEX}} > 0, \exists C _ {\mathrm{TEX}} > 0,
$$

$$
\forall \sigma_ {n} \leqslant \sigma_ {\mathrm{TEX}}, \exists \hat {M} _ {n} \in \mathbb {R} ^ {N \times N}, \text {such that} \tag {3.37}
$$

$$
\hat {M} _ {n} \in \mathscr {K},   \hat {M} _ {n} s _ {n} = y _ {n},   | \hat {M} _ {n} - \bar {M} | _ {n} \leqslant C _ {\mathrm{TEX}} \sigma_ {n}.
$$

Before giving the convergence theorems, let us check that (BDA) is satisfied for the scheme above.

Lemma 3.8. Suppose that Algorithm (qN–AP3) updates the matrices $M_{n}$ according to the scheme (3.36) and that conditions (3.35) and (3.37) are satisfied. Then Assumption (BDA) holds with $\bar{M}$ given by (3.37).

Proof. Let

$$
\sigma := \min \left(\sigma_ {\mathrm{LC}}, \sigma_ {\mathrm{TEX}}, \frac {1}{3 C _ {\mathrm{LC}}}\right).
$$

Since $M_{n+1}$ is the orthogonal projection of $M_n$ onto a closed convex set containing $\hat{M}_n$, we have

$$
\left| M _ {n} - M _ {n + 1} \right| _ {n} ^ {2} + \left| M _ {n + 1} - \hat {M} _ {n} \right| _ {n} ^ {2} \leqslant \left| M _ {n} - \hat {M} _ {n} \right| _ {n} ^ {2}. \tag {3.38}
$$

In particular,

$$
\left| M _ {n + 1} - \hat {M} _ {n} \right| _ {n} \leqslant \left| M _ {n} - \hat {M} _ {n} \right| _ {n}. \tag {3.39}
$$

Let us show that (BDA) holds with $C_{\mathrm{BD}} := 3\max(C_{\mathrm{LC}}, C_{\mathrm{TEX}})$ and $\bar{M}$ given by (3.37), when $\sigma_n \leqslant \sigma$. We have, using (3.39) and (3.37),

$$
\begin{aligned} \left| M _ {n + 1} - \bar {M} \right| _ {n} &\leqslant \left| M _ {n + 1} - \hat {M} _ {n} \right| _ {n} + \left| \hat {M} _ {n} - \bar {M} \right| _ {n} \\ &\leqslant \left| M _ {n} - \hat {M} _ {n} \right| _ {n} + C _ {\mathrm{TEX}} \sigma_ {n} \\ &\leqslant \left| M _ {n} - \bar {M} \right| _ {n} + 2 C _ {\mathrm{TEX}} \sigma_ {n}. \\ \end{aligned}
$$

Then, using (3.35), we get

$$
\left(1 - C _ {\mathrm{LC}} \sigma_ {n}\right) \left\| M _ {n + 1} - \bar {M} \right\| \leqslant \left(1 + C _ {\mathrm{LC}} \sigma_ {n}\right) \left\| M _ {n} - \bar {M} \right\| + 2 C _ {\mathrm{TEX}} \sigma_ {n},
$$

$$
\| M _ {n + 1} - \bar {M} \| \leqslant \left(\frac {1 + C _ {\mathrm{LC}} \sigma_ {n}}{1 - C _ {\mathrm{LC}} \sigma_ {n}}\right) \| M _ {n} - \bar {M} \| + \left(\frac {2 C _ {\mathrm{TEX}}}{1 - C _ {\mathrm{LC}} \sigma_ {n}}\right) \sigma_ {n}.
$$

Since $\sigma_{n} \leqslant \sigma \leqslant 1 / (3C_{\mathrm{LC}})$ :

$$
\frac {1 + C _ {\mathrm{LC}} \sigma_ {n}}{1 - C _ {\mathrm{LC}} \sigma_ {n}} \leqslant 1 + 3 C _ {\mathrm{LC}} \sigma_ {n} \quad \text {and} \quad \frac {2 C _ {\mathrm{TEX}}}{1 - C _ {\mathrm{LC}} \sigma_ {n}} \leqslant 3 C _ {\mathrm{TEX}}.
$$

Hence

$$
\| M _ {n + 1} - \bar {M} \| \leqslant (1 + 3 C _ {\mathrm{LC}} \sigma_ {n}) \| M _ {n} - \bar {M} \| + 3 C _ {\mathrm{TEX}} \sigma_ {n},
$$

which is just a bounded deterioration property of the type (BDA). □

Then, we can show linear convergence under the assumptions of Theorem 3.9 and superlinear convergence when (3.8) holds (Theorem 3.10).

Theorem 3.9. Suppose that (3.6), (3.7) and (3.12) hold. Suppose also that Algorithm (qN–AP3) updates the matrices $M_n$ according to the scheme (3.36) and that conditions (3.35) and (3.37) hold, the latter with the same matrix $\bar{M}$ as in (3.12). Then, if $(x_1, M_1)$ is close enough to $(\bar{x}, \bar{M})$, Algorithm (qN–AP3) is well defined and generates a sequence $\{x_n\}$ converging q-linearly to $\bar{x}$ and a sequence of symmetric positive definite matrices $\{M_n\}$ such that

$$
(M _ {n + 1} - M _ {n}) \rightarrow 0. \tag {3.40}
$$

Proof. According to Lemma 3.8, (BDA) is satisfied with the same matrix $\bar{M}$ as in (3.12). Then, Theorem 3.4 gives the first part of the result (the linear convergence of the sequence $\{x_{n}\}$ ), as well as

$$
\| M _ {n} - \bar {M} \| \rightarrow \delta . \tag {3.41}
$$

It remains to prove (3.40).

Due to the linear convergence of $\{x_{n}\}$ to $\bar{x}$, we can suppose that $\sigma_{n} \leqslant \min(\sigma_{\mathrm{LC}}, \sigma_{\mathrm{TEX}})$ for all $n \geqslant 1$. As in the proof of Lemma 3.8, we have the inequality

$$
\left| M _ {n} - M _ {n + 1} \right| _ {n} ^ {2} + \left| M _ {n + 1} - \hat {M} _ {n} \right| _ {n} ^ {2} \leqslant \left| M _ {n} - \hat {M} _ {n} \right| _ {n} ^ {2}, \tag {3.42}
$$

and we proceed to show that both $|M_{n+1} - \hat{M}_n|_n$ and $|M_n - \hat{M}_n|_n$ tend to $\delta$. From (3.35), (3.41) implies

$$
\left| M _ {n} - \bar {M} \right| _ {n} \rightarrow \delta \quad \text {and} \quad \left| M _ {n + 1} - \bar {M} \right| _ {n} \rightarrow \delta . \tag {3.43}
$$

Using (3.37), we get

$$
\begin{aligned} \left|\left| M _ {n} - \hat {M} _ {n} \right| _ {n} - \left| M _ {n} - \bar {M} \right| _ {n} \right| &\leqslant \left| \hat {M} _ {n} - \bar {M} \right| _ {n} \rightarrow 0, \\ \left|\left| M _ {n + 1} - \hat {M} _ {n} \right| _ {n} - \left| M _ {n + 1} - \bar {M} \right| _ {n} \right| &\leqslant \left| \hat {M} _ {n} - \bar {M} \right| _ {n} \rightarrow 0. \\ \end{aligned}
$$

From this and (3.43), we deduce

$$
\left| M _ {n} - \hat {M} _ {n} \right| _ {n} \rightarrow \delta \quad \text {and} \quad \left| M _ {n + 1} - \hat {M} _ {n} \right| _ {n} \rightarrow \delta .
$$

Then, (3.42) implies

$$
\left| M _ {n + 1} - M _ {n} \right| _ {n} \to 0
$$

and by (3.35),

$$
\| M _ {n + 1} - M _ {n} \| \to 0  . \qquad \square
$$

Theorem 3.10. Suppose that (3.6)-(3.8) hold and that $\bar{H}$ is positive definite. Suppose also that Algorithm (qN-AP3) updates the matrices $M_{n}$ according to the scheme (3.36) and that conditions (3.35) and (3.37) hold, the latter with $\bar{M} = \bar{H}$. Then, if $(x_{1}, M_{1})$ is close enough to $(\bar{x}, \bar{H})$, Algorithm (qN-AP3) is well defined and generates a sequence $\{x_{n}\}$ converging $q$ -superlinearly to $\bar{x}$.

Proof. Assumption (3.8) implies that $\tilde{H}$ is linear, hence (3.12) holds with $\tilde{M} = \tilde{H}$ ; we can apply then Theorem 3.9, which gives the $q$ -linear convergence of the sequence $\{x_n\}$ and $(M_{n+1} - M_n) \to 0$. Now the $q$ -superlinear convergence of $\{x_n\}$ follows from Corollary 3.7. $\square$

# 3.5. Application to some quasi-Newton methods

We now apply the theory of the previous subsection to some particular quasi-Newton update formulae. The main issue is to check condition (3.37), and it is here that assumption (3.9) comes into play.

We first show that (3.37) holds for general quasi-Newton methods, provided $f$ is sufficiently smooth. As in the previous subsection, $\mathcal{K}$ is a general closed convex set of symmetric matrices.

Proposition 3.11. Suppose that $f$ is twice Fréchet differentiable in a neighbourhood $\mathcal{N}$ of $\bar{x}$, with a Lipschitz continuous Hessian. If $\nabla^2 f(x) \in \mathcal{K}$ for all $x \in \mathcal{N}$ and (3.35) holds, then (3.37) is satisfied for $\bar{M} = \nabla^2 f(\bar{x})$.

Proof. Let $\sigma_{\mathrm{LC}} > 0$ be given by (3.35) and take $\sigma \in ]0, \sigma_{\mathrm{LC}}]$ such that $B(\bar{x}, \sigma) \subset \mathcal{N}$. When $\sigma_n < \sigma$, the segment $[x_n, x_{n+1}]$ is in $\mathcal{N}$, so that we can define

$$
\hat {M} _ {n} := \int_ {0} ^ {1} \nabla^ {2} f (x _ {n} + \tau s _ {n}) \mathrm{d} \tau .
$$

Clearly, $\hat{M}_n\in \mathcal{K}$ and $\hat{M}_ns_n = y_n$. Furthermore, with $\bar{M} = \nabla^2 f(\bar{x})$,

$$
| \hat {M} _ {n} - \bar {M} | \leqslant \int_ {0} ^ {1} | \nabla^ {2} f (x _ {n} + \tau s _ {n}) - \bar {M} | \mathrm{d} \tau \leqslant \frac {L _ {H}}{2} \sigma_ {n},
$$

where $L_{H}$ is a Lipschitz constant of the map $\mathcal{N} \ni x \mapsto \nabla^{2}f(x)$. Combine this, (3.20) and (3.35) to obtain

$$
\begin{aligned} \left| \hat {M} _ {n} - \bar {M} \right| _ {n} &\leqslant \left(1 + C _ {\mathrm{LC}} \sigma_ {n}\right) \| \hat {M} _ {n} - \bar {M} \| \leqslant \eta \left(1 + C _ {\mathrm{LC}} \sigma_ {n}\right) \left| \hat {M} _ {n} - \bar {M} \right| \\ &\leqslant \eta (1 + C _ {\mathrm{LC}} \sigma_ {\mathrm{LC}}) \frac {L _ {H}}{2} \sigma_ {n}. \\ \end{aligned}
$$

We recognize (3.37). $\square$

We consider now the prox-versions of the PSB and DFP algorithms. Let $\mathscr{K}$ be the set of symmetric matrices and take the Frobenius norm $|\cdot|_F$ for $|\cdot|_n$ and $\|\cdot\|$. Then the solution of (3.36) is given by the PSB update formula (see [7]): $M_{n+1} = \mathrm{PSB}(M_n, y_n, s_n)$, where

$$
\mathrm{PSB} (M, y, s) := M + \frac {(y - M s) s ^ {\mathrm{T}} + s (y - M s) ^ {\mathrm{T}}}{| s | ^ {2}} - \frac {\langle y - M s , s \rangle}{| s | ^ {4}} s s ^ {\mathrm{T}}.
$$

Recall that $\langle u, v \rangle$ and $u^{\mathrm{T}}v$ denote the same operation. We note here that more general scalar products can also be used, as described for example in [11] and in the appendix of [10]. Reproducing the present theory in this framework is then an easy exercise.

For this method, we have

Proposition 3.12. Suppose that (3.6)-(3.9) hold and that $\bar{H}$ is positive definite. Assume that Algorithm (qN-AP3) uses the PSB formula: $M_{n+1} = \mathrm{PSB}(M_n, y_n, s_n)$. If $(x_1, M_1)$ is close enough to $(\bar{x}, \bar{H})$, then the algorithm is well defined and $x_n \to \bar{x}$ q-superlinearly.

Proof. Take

$$
\hat {M} _ {n} := \mathrm{PSB} (\bar {H}, y _ {n}, s _ {n})
$$

and define $\delta_{n}:= y_{n}-\bar{H}s_{n}$. Then

$$
\hat {M} _ {n} - \bar {H} = \frac {\delta_ {n} s _ {n} ^ {\mathrm{T}} + s _ {n} \delta_ {n} ^ {\mathrm{T}}}{\left| s _ {n} \right| ^ {2}} - \frac {\left\langle \delta_ {n} , s _ {n} \right\rangle}{\left| s _ {n} \right| ^ {4}} s _ {n} s _ {n} ^ {\mathrm{T}}.
$$

Taking $x = x_{n}$ and $y = x_{n + 1}$ in (3.9), we obtain $\delta_{n} = O(|s_{n}||\sigma_{n}|)$. Recall also that $|uv^{\mathrm{T}}| = |u||v|$. Therefore

$$
\left| \hat {M} _ {n} - \bar {H} \right| = O (\left| \sigma_ {n} \right|).
$$

On the other hand, since $\hat{M}_n \in \mathscr{K}$ and $\hat{M}_n s_n = y_n$, condition (3.37) holds with $|\cdot|_n = |\cdot|_F$ and $\bar{M} = \bar{H}$. We can now apply Theorem 3.10 to terminate the proof. $\square$

Consider now the DFP formula ([7]):

$$
\mathrm{DFP} (M, y, s) := M + \frac {(y - M s) y ^ {\mathrm{T}} + y (y - M s) ^ {\mathrm{T}}}{\langle y , s \rangle} - \frac {\langle y - M s , s \rangle}{\langle y , s \rangle^ {2}} y y ^ {\mathrm{T}}.
$$

This formula is well defined when $\langle y, s \rangle \neq 0$ and gives a symmetric positive definite matrix when $M$ is itself symmetric positive definite and $\langle y, s \rangle > 0$. The updated matrix can be characterized as the solution of a variational problem. For this, let us introduce the weighted Frobenius norm associated to a symmetric positive definite matrix $W$ :

$$
M \mapsto | M | _ {W, F} := | W ^ {- 1 / 2} M W ^ {- 1 / 2} | _ {F}.
$$

Then, when $\langle y_n, s_n \rangle$ is positive, $\mathrm{DFP}(M_n, y_n, s_n)$ is the solution of problem (3.36) in which $\mathcal{K}$ is the set of symmetric matrices and $|\cdot|_n$ is the norm $|\cdot|_{W_n,F}$ where $W_n$ is any matrix satisfying $W_n s_n = y_n$ (see [7]). As we shall see in the proof of the next proposition, an appropriate choice of the matrix $W_n$ will allow us to satisfy (3.35) and (3.37).

Proposition 3.13. Suppose that (3.6)-(3.9) hold and that $\bar{H}$ is positive definite. Assume that Algorithm (qN-AP3) uses the DFP formula: $M_{n+1} = \mathrm{DFP}(M_n, y_n, s_n)$. If $(x_1, M_1)$ is close enough to $(\bar{x}, \bar{H})$, then the algorithm is well defined and $x_n \to \bar{x}$ q-superlinearly.

Proof. Because $\bar{H}$ is positive definite, it is easy to see that when $\sigma_{n} := |x_{n} - \bar{x}| + |x_{n+1} - \bar{x}|$ is sufficiently small, we have

$$
\langle y _ {n}, s _ {n} \rangle \geqslant \alpha | s _ {n} | ^ {2} \quad \text {and} \quad | y _ {n} | \leqslant L | s _ {n} |, \tag {3.44}
$$

for some positive constants $\alpha$ and $L$. From now on, we suppose that $\sigma_{n}$ is sufficiently small to have (3.44).

The matrix

$$
\hat {M} _ {n} := \mathrm{DFP} (\bar {H}, y _ {n}, s _ {n})
$$

is positive definite and verifies $\hat{M}_n s_n = y_n$. Then $M_{n+1}$ is solution of (3.36) with $|\cdot|_n := |\cdot|_{\hat{M}_n, F}$.

Defining $\delta_{n}:= y_{n}-\bar{H}s_{n}$, we have

$$
\hat {M} _ {n} - \bar {H} = \frac {\delta_ {n} y _ {n} ^ {\mathrm{T}} + y _ {n} \delta_ {n} ^ {\mathrm{T}}}{\left\langle y _ {n} , s _ {n} \right\rangle} - \frac {\left\langle \delta_ {n} , s _ {n} \right\rangle}{\left\langle y _ {n} , s _ {n} \right\rangle^ {2}} y _ {n} y _ {n} ^ {\mathrm{T}}.
$$

By (3.9), $\delta_n = O(|s_n||\sigma_n|)$. Therefore, using (3.44),

$$
\left| \hat {M} _ {n} - \bar {H} \right| = O (\left| \sigma_ {n} \right|). \tag {3.45}
$$

It follows that $\hat{M}_n^{-1 / 2}$ is bounded for $\sigma_{n}$ small enough, then

$$
\left| \hat {M} _ {n} - \bar {H} \right| _ {n} = \left| \hat {M} _ {n} ^ {- 1 / 2} (\hat {M} _ {n} - \bar {H}) \hat {M} _ {n} ^ {- 1 / 2} \right| _ {F} = O (\left| \hat {M} _ {n} - \bar {H} \right|).
$$

Since $\hat{M}_{n}$ is symmetric and $\hat{M}_{n}s_{n}=y_{n}$, condition (3.37) holds with $\bar{M}=\bar{H}$.

Let us now prove condition (3.35) with $\| \cdot \| = |\cdot |_{\hat{H},F}$. Observe that

$$
\left| M \right| _ {W, F} = (\operatorname{tr} (W ^ {- 1 / 2} M W ^ {- 1} M W ^ {- 1 / 2})) ^ {1 / 2} = (\operatorname{tr} (M W ^ {- 1}) ^ {2}) ^ {1 / 2}.
$$

Then, for $M \in \mathbb{R}^{N \times N}$ with $\| M \| = 1$,

$$
\left| \left| M \right| _ {n} - \| M \| \right| = \frac {\left| \left| M \right| _ {n} ^ {2} - \| M \| ^ {2} \right|}{\left| M \right| _ {n} + \| M \|} \leqslant \left| \operatorname{tr} (M \hat {M} _ {n} ^ {- 1}) ^ {2} - \operatorname{tr} (M \bar {H} ^ {- 1}) ^ {2} \right|,
$$

because $|M|_n + \| M\| \geqslant 1$. Now, $A \in \mathbb{R}^{N \times N} \mapsto \operatorname{tr} A$ is linear. Therefore, for some constant $C_1 > 0$,

$$
\left| \left| M \right| _ {n} - \| M \| \right| \leqslant C _ {1} \left| (M \hat {M} _ {n} ^ {- 1}) ^ {2} - (M \bar {H} ^ {- 1}) ^ {2} \right|.
$$

Using the relation $|B^2 - A^2| = |B(B - A) + (B - A)A| \leqslant (|A| + |B|) |B - A|$, we get

$$
\left| \left| M \right| _ {n} - \| M \| \right| \leqslant C _ {1} \left| M \right| \left(\left| \hat {M} _ {n} ^ {- 1} \right| + \left| \bar {H} ^ {- 1} \right|\right) \left| \hat {M} _ {n} ^ {- 1} - \bar {H} ^ {- 1} \right|.
$$

Because the norms $|\cdot|$ and $\| \cdot \|$ are equivalent and $A \mapsto A^{-1}$ is infinitely differentiable on the set of non-singular matrices, one has for $\sigma_n$ sufficiently small

$$
\left| \left| M \right| _ {n} - \left\| M \right\| \right| = O (\left| \sigma_ {n} \right|),
$$

where we used (3.45). Now condition (3.35) holds by homogeneity in $M$.

The conclusion of the theorem follows from Theorem 3.10. $\square$

# 4. A BFGS-proximal method

In this section, we study the particularization of the algorithm pattern (AP3), in which the proximal point $x_{n}^{p}$ is computed exactly and the BFGS formula is used to update the matrices $M_{n}$. In this case, satisfactory global and $q$ -superlinear convergence results can be obtained, in the sense that, given any initial pair $(x_{1}, M_{1})$, with $M_{1}$ symmetric and positive definite, the generated sequence $\{x_{n}\}$ converges superlinearly to a solution of problem (1.1). The precise results are given in Theorems 4.2 and 4.8 below.

To obtain these convergence results, $f$ is always supposed differentiable (and therefore finite everywhere). Then we will again use the notation $g(x)$ for the gradient of $f$ at $x$, as well as $g_{n} = g(x_{n})$ and $g_{n}^{p} = g(x_{n}^{p})$.

For given vectors $s$ and $y$ in $\mathbb{R}^N$, the BFGS update of an $N \times N$ symmetric matrix $M$ is the matrix

$$
\mathrm{BFGS} (M, y, s) := M - \frac {M s s ^ {\mathrm{T}} M}{\langle M s , s \rangle} + \frac {y y ^ {\mathrm{T}}}{\langle y , s \rangle} \tag {4.1}
$$

(see [7] for instance). Observe that the trace of the matrix $M_{+} = \mathrm{BFGS}(M, y, s)$ is given by

$$
\mathrm{tr} M _ {+} = \mathrm{tr} M - \frac {| M s | ^ {2}}{\langle M s , s \rangle} + \frac {| y | ^ {2}}{\langle y , s \rangle}. \tag {4.2}
$$

When $M$ is positive definite, the BFGS formula is well defined if $\langle y, s \rangle \neq 0$. However, the stronger condition

$$
\langle y, s \rangle > 0
$$

is generally required since this is a necessary and sufficient condition to have the updated matrix positive definite.

The algorithm considered in this section is stated as follows:

# BFGS-proximal algorithm (BFGS-AP3)

Step 0. Choose an initial point $x_1 \in \mathbb{R}^N$ and an initial symmetric positive definite matrix $M_1$. Take $m$ in $]0, 1[$. Set $n = 1$.

Step 1. Given $x_{n}$ and $M_{n}$, compute $x_{n}^{p}:=p_{M_{n}}(x_{n})$ and set $s_{n}^{p}:=x_{n}^{p}-x_{n}$.

Step 2. Compute the next iterate by:

$$
x _ {n + 1} := x _ {n} + t _ {n} s _ {n} ^ {p}.
$$

The stepsize $t_n \geqslant 1$ is chosen to satisfy the general descent condition (2.9) and

$$
\langle y _ {n}, s _ {n} \rangle > 0, \tag {4.3}
$$

where $s_n = x_{n+1} - x_n$ and $y_n = g_{n+1} - g_n$. We also suppose that $t_n = 2$ is taken when the line-search conditions (2.9) and (4.3) allow it.

Step 3. Update $M_{n}$ by the BFGS formula:

$$
M _ {n + 1} = \mathrm{BFGS} (M _ {n}, y _ {n}, s _ {n}).
$$

Increase $n$ by 1 and loop to Step 1.

In Step 2, the additional condition (4.3) is only required to guarantee the well posedness of the BFGS formula and the positive definiteness of the generated matrices. Note also that from Section 3 it is important to take $t_n = 2$ whenever possible for the sake of superlinear convergence. Step 2 is actually a line-search generating trial stepsizes $t \geqslant 1$ until (2.9) and (4.3) are simultaneously satisfied.

Remark 4.1. Feasibility of this line-search is easy to establish. First of all, the requirement $t \geqslant 1$ is not classical but $x_{n}^{p}$, obtained for $t = 1$, satisfies the descent test (2.9) with a strict inequality. Then, by convexity of $f$, the stepsizes that satisfy (2.9) form a closed interval, say $\mathcal{S}_1$, containing 1 in its interior. As for (4.3), remark that the function

$$
0 \leqslant t \mapsto \left\langle g (x _ {n} + t s _ {n} ^ {p}) - g _ {n}, s _ {n} ^ {p} \right\rangle =: d (t)
$$

is non-negative and non-decreasing and cannot be identically zero when $f$ is bounded below in the direction $s_n^p$. This implies that the stepsizes satisfying (4.3) form an open interval $\mathcal{I}_2 = ]t^a, +\infty[$, with finite $t^a$. We have to show that $\mathcal{I}_1$ and $\mathcal{I}_2$ intersect. There are 2 cases:

1. If $t^a < 1$, $\mathcal{I}_1 \cap \mathcal{I}_2$ contains some neighbourhood of 1.

2. If $1 \leqslant t^a < +\infty$, the key is to observe that $f(x_n + ts_n^p)$ has the constant slope $\langle g_n^p, s_n^p \rangle = -\langle M_n s_n^p, s_n^p \rangle$ at any $t \in [0, t^a]$ (recall (2.2)). Hence

$$
\langle M _ {n} s _ {n} ^ {p}, s _ {n} ^ {p} \rangle = f (x _ {n}) - f (x _ {n} ^ {p}) \geqslant \delta_ {n}.
$$

Then, since $t^a \geqslant 1 > m$, we can write

$$
f (x _ {n} + t ^ {a} s _ {n} ^ {p}) = f (x _ {n}) - t ^ {a} \langle M _ {n} s _ {n} ^ {p}, s _ {n} ^ {p} \rangle <   f (x _ {n}) - m \delta_ {n}.
$$

Thus, there is $\epsilon > 0$ such that any stepsize in $]t^a, t^a + \epsilon]$ satisfies (2.9) and (4.3).

Exploiting these properties, the line-search can then be implemented by a simple bracketing algorithm as in [17]. Start from t=2 and, at the current trial stepsize $t \geqslant 1$,

(i) perform the descent test; if it is not satisfied, t is too large, compute a smaller t;  
(ii) if satisfied, test $d(t) > 0$ ; if yes, we are done; otherwise $t$ is too small, compute a larger $t$.

# 4.1. Global convergence

Our global convergence result is a simple consequence of Theorem 2.3.

Theorem 4.2. Assume that the convex function $f$ has a nonempty bounded set of minima and that its gradient mapping is locally Lipschitz continuous. Let $\{x_{n}\}$ be the sequence generated by Algorithm (BFGS-AP3). Then, all the accumulation points of $\{x_{n}\}$ and $\{x_{n}^{p}\}$ minimize $f$.

Proof. In view of Theorem 2.3, we only have to prove (2.14). Let $L$ be a Lipschitz constant for $g$ on the set $\{x: f(x) \leqslant f(x_1)\}$ which, as already seen in the proof of Theorem 2.3, is compact. Applying for example [25] or Theorem X.4.2.2 of [13], we obtain

$$
L \langle y _ {n}, s _ {n} \rangle \geqslant | y _ {n} | ^ {2},
$$

and the trace relation (4.2) gives

$$
\mathrm{tr} M _ {n + 1} \leqslant \mathrm{tr} M _ {n} + L \leqslant \mathrm{tr} M _ {1} + n L \leqslant (n + 1) C,
$$

where $C := \max(\operatorname{tr} M_1, L)$.

As the largest eigenvalue is less than the trace, we get

$$
\lambda_ {\min} (M _ {n} ^ {- 1}) = \frac {1}{\lambda_ {\max} (M _ {n})} \geqslant \frac {1}{\operatorname{tr} M _ {n}} \geqslant \frac {1}{n C}.
$$

Therefore, the convergence condition (2.14) holds and the result follows. $\square$

# 4.2. The $r$-linear convergence

To prove superlinear convergence, it is known that a technically useful property is the $r$-linear convergence. This last property, interesting per se, can be established for (BFGS-

AP3) under rather mild assumptions on $f$. We start with a result of general interest in convex analysis.

Lemma 4.3. Assume that the convex function $f$ is differentiable. With $\bar{x}$ minimizing $f$, let $\alpha > 0$ and $x \in \mathbb{R}^N$ satisfy

$$
f (x) \geqslant f (0 \bar {x}) + \alpha | x - \bar {x} | ^ {2}. \tag {4.4}
$$

Then

$$
f (x) \leqslant f (\bar {x}) + (1 / \alpha) | g (x) | ^ {2}. \tag {4.5}
$$

Proof. Write the subgradient inequality at $x$ and obtain with the Cauchy-Schwarz inequality

$$
f (x) \leqslant f (\bar {x}) + | g (x) | | \bar {x} - x |,
$$

so that with (4.4) and the non-negativity of $f(x) - f(\bar{x})$,

$$
f (x) - f (\bar {x}) \leqslant | g (x) | \sqrt {[ f (x) - f (\bar {x}) ] / \alpha}.
$$

The result follows. □

The next lemma is part of the theory of BFGS updates and can be stated independently of the present framework. We denote by $\theta_{n}$ the angle between $M_{n}s_{n}$ and $s_n$ :

$$
\cos \theta_ {n} := \frac {\left\langle M _ {n} s _ {n} , s _ {n} \right\rangle}{\left| M _ {n} s _ {n} \right| \left| s _ {n} \right|} = \frac {\left\langle M _ {n} s _ {n} ^ {p} , s _ {n} ^ {p} \right\rangle}{\left| M _ {n} s _ {n} ^ {p} \right| \left| s _ {n} ^ {p} \right|},
$$

and by $\lceil \cdot \rceil$ the roundup operator: $\lfloor x\rfloor = i$, when $i - 1 < x\leqslant i$ and $i\in \mathbb{N}$.

Lemma 4.4. Let $\{M_n\}$ be generated by the BFGS formula using pairs of vectors $(y_{n}, s_{n})$ satisfying

$$
\left\langle y _ {n}, s _ {n} \right\rangle \geqslant \alpha_ {1} \left| s _ {n} \right| ^ {2} \quad a n d \quad \left\langle y _ {n}, s _ {n} \right\rangle \geqslant \alpha_ {2} \left| y _ {n} \right| ^ {2} \tag {4.6}
$$

for all $n \geqslant 1$, where $\alpha_{1} > 0$ and $\alpha_{2} > 0$ are independent of $n$. Then for any $r \in ]0, 1[$, there exist positive constants $\gamma_{1}$ and $\gamma_{2}$, such that

$$
\cos \theta_ {j} \geqslant \gamma_ {1}, \tag {4.7}
$$

$$
\frac {\left| M _ {j} s _ {j} \right|}{\left| s _ {j} \right|} \leqslant \gamma_ {2}, \tag {4.8}
$$

for at least $[rn]$ indices $j$ in $\{1, \dots, n\}$.

Condition (4.7) on $\cos \theta_{j}$ was proved by [25], when the BFGS update is used for unconstrained problems with the Wolfe line-search. Byrd and Nocedal [3] showed that this result is true independently of any line-search: it can be stated, as above, only in terms of the updated matrices $M_{n}$ and the vectors $y_{n}$ and $s_n$. We found condition (4.8) also in [3].

We recall that the differentiable function $f$ is said strongly convex on a domain $D \subset \mathbb{R}^N$, if it satisfies the equivalent properties for some $\alpha > 0$ (see [13] Theorem VI.6.1.2):

$$
f (y) \geqslant f (x) + \langle g (x), y - x \rangle + \frac {\alpha}{2} | y - x | ^ {2}, \quad \text {for all} x, y \in D,
$$

$$
\langle g (y) - g (x), y - x \rangle \geqslant \alpha | y - x | ^ {2}, \quad \text {for all} x, y \in D.
$$

Theorem 4.5. Assume that $\{x_{n}\}$ converges to a minimum point $\bar{x}$, in the neighbourhood of which $f$ is strongly convex and has a Lipschitz continuous gradient mapping. Then the convergence of $\{x_{n}\}$ is $r$ -linear; this implies in particular that $\sum_{n\geqslant 1}|x_n - \bar{x}| < \infty$.

Proof. Since this is an asymptotic statement, we limit our attention to large enough n in all the proof below. The Lipschitz property of g ensures the second condition in (4.6) (see again [25]). The first one, as well as the growth condition (4.4), are ensured by strong convexity (i.e., strong monotonicity of the gradient mapping). Then our proof is based on an over-estimation of $f(x_{n}) - f(\bar{x})$ and begins by over-estimating $f^{p}(x_{n}) - f(\bar{x})$.

Inequality (2.8) gives $\langle M_n s_n^p, s_n^p \rangle / 2 \leqslant \delta_n = f(x_n) - f^p(x_n)$, so that

$$
f ^ {p} (x _ {n}) - f (\bar {x}) \leqslant f (x _ {n}) - f (\bar {x}) - \frac {1}{2} \left\langle M _ {n} s _ {n} ^ {p}, s _ {n} ^ {p} \right\rangle . \tag {4.9}
$$

To obtain an over-estimation of $f^p(x_n) - f(\bar{x})$, we under-estimate $\langle M_n s_n^p, s_n^p \rangle$, first in terms of $|g_n^p|^2$ and next in terms of $f^p(x_n) - f(\bar{x})$, using (4.5).

We start from

$$
\langle M _ {n} s _ {n} ^ {p}, s _ {n} ^ {p} \rangle = | M _ {n} s _ {n} ^ {p} | | s _ {n} ^ {p} | \cos \theta_ {n}, \quad \text {for all} n \geqslant 1.
$$

Fixing $r$ in ]0, 1[, we denote by $N_r^n$ the set of indices $j$ in $\{1, \dots, n\}$ for which (4.7) and (4.8) hold. Using successively (4.7), (4.8) and (4.5), and remembering from Lemma 2.1 that $g_n^p = -M_n s_n^p$, we write for all $j \in N_r^n$,

$$
\langle M _ {j} s _ {j} ^ {p}, s _ {j} ^ {p} \rangle \geqslant \gamma_ {1} \left| M _ {j} s _ {j} ^ {p} \right| \left| s _ {j} ^ {p} \right| \geqslant \frac {\gamma_ {1}}{\gamma_ {2}} \left| M _ {j} s _ {j} ^ {p} \right| ^ {2} = \frac {\gamma_ {1}}{\gamma_ {2}} \left| g _ {j} ^ {p} \right| ^ {2} \geqslant C _ {1} (f (x _ {j} ^ {p}) - f (\bar {x})) ,
$$

where $C_1 = \alpha \gamma_1 / \gamma_2$. Adding $(C_1 / 2)\langle M_j s_j^p, s_j^p\rangle$ to the extreme sides and using (2.6) give

$$
\left(1 + \frac {C _ {1}}{2}\right) \langle M _ {j} s _ {j} ^ {p}, s _ {j} ^ {p} \rangle \geqslant C _ {1} (f ^ {p} (x _ {j}) - f (\bar {x})) \text {, for all} j \in N _ {r} ^ {n},
$$

so that, as wished,

$$
\frac {1}{2} \left\langle M _ {j} s _ {j} ^ {p}, s _ {j} ^ {p} \right\rangle \geqslant C _ {2} (f ^ {p} (x _ {j}) - f (\bar {x})), \quad \text {for all} j \in N _ {r} ^ {n},
$$

where $C_2 = C_1 / (2 + C_1)$. Combining this with (4.9) gives

$$
f ^ {p} (x _ {j}) - f (\bar {x}) \leqslant \left(\frac {1}{1 + C _ {2}}\right) (f (x _ {j}) - f (\bar {x})), \quad \text {for all} j \in N _ {r} ^ {n}.
$$

Now, using the line-search condition (2.9), we have for $j \in N_r^n$,

$$
\begin{aligned} f \left(x _ {j + 1}\right) - f (\bar {x}) &\leqslant (1 - m) \left(f \left(x _ {j}\right) - f (\bar {x})\right) + m \left(f ^ {p} \left(x _ {j}\right) - f (\bar {x})\right) \\ &\leqslant \left(1 - \frac {m C _ {2}}{1 + C _ {2}}\right) \left(f \left(x _ {j}\right) - f (\bar {x})\right). \\ \end{aligned}
$$

Remark that we can write $1 - mC_2 / (1 + C_2) =: \tau^{1/r}$ for some $\tau$ in ]0, 1[. Furthermore, as $|N_r^n| \geqslant rn$ (Lemma 4.4) and $f(x_{j+1}) - f(\bar{x}) \leqslant f(x_j) - f(\bar{x})$ for all $j$, we have

$$
f (x _ {n + 1}) - f (\bar {x}) \leqslant \tau^ {| N _ {r} ^ {n} | / r} (f (x _ {1}) - f (\bar {x})) \leqslant \tau^ {n} (f (x _ {1}) - f (\bar {x})), \quad \text {for all} n \geqslant 1.
$$

Finally (4.4) allows us to deduce

$$
\left| x _ {n} - \bar {x} \right| \leqslant \left[ \frac {f (x _ {n}) - f (\bar {x})}{\alpha} \right] ^ {1 / 2} \leqslant \left[ \frac {f (x _ {1}) - f (\bar {x})}{\alpha} \right] ^ {1 / 2} (\sqrt {\tau}) ^ {n - 1}.
$$

This implies that $\limsup_{n\to \infty}|x_n - \bar{x}|^{1 / n}\leqslant \sqrt{\tau} < 1$, characterizing the $r$ -linear convergence of $x_{n}$ to $\bar{x}$. Finiteness of $\sum_{n\geqslant 1}|x_n - \bar{x} |$ follows.

# 4.3. Acceptability of the ideal stepsize

An important point for fast convergence is whether the stepsize $t_n = 2$ is accepted asymptotically by the line-search conditions (2.9) and (4.3). For this, and in particular for the descent condition (2.9), the candidate

$$
x _ {n} ^ {+} := x _ {n} + 2 s _ {n} ^ {p} \tag {4.10}
$$

must be 'superlinearly closer' to the minimum point $\bar{x}$ than $x_{n}$. This is the last condition involved in the next result.

Theorem 4.6. Assume that $\bar{x}$ is a minimum point of $f$ at which (3.6) and (3.7) hold, and such that the directional-derivative operator $\bar{H}$ of $g$ satisfies the following property:

$$
\exists \alpha > 0 \text {such that} \langle \bar {H} z, z \rangle \geqslant \alpha | z | ^ {2} \quad \text {for all} z \in \mathbb {R} ^ {N}. \tag {4.11}
$$

If

$$
\left| x _ {n} ^ {+} - \bar {x} \right| = o (\left| x _ {n} - \bar {x} \right|), \tag {4.12}
$$

then the point $x_{n}^{+}$ of (4.10) is accepted by the line-search of Algorithm (BFGS-AP3) for $n$ large enough.

Proof. From (3.10), we have for $z$ arbitrary in the neighbourhood of $\bar{x}$ :

$$
g (z) = \bar {H} (z - \bar {x}) + o (| z - \bar {x} |), \tag {4.13}
$$

so that in particular,

$$
\langle g _ {n} ^ {p}, s _ {n} ^ {p} \rangle = \langle \bar {H} e _ {n} ^ {p}, s _ {n} ^ {p} \rangle + o (| e _ {n} ^ {p} | | s _ {n} ^ {p} |).
$$

For $n$ large enough, we write (4.13) with $z = \bar{x} + \tau(x_n - \bar{x})$ ; we multiply by $x_n - \bar{x}$ and we integrate from $\tau = 0$ to $\tau = 1$ :

$$
f (x _ {n}) = f (\bar {x}) + \frac {1}{2} \left\langle \bar {H} e _ {n}, e _ {n} \right\rangle + o (\left| e _ {n} \right| ^ {2}).
$$

The same operation with $x_{n}^{p}$ instead of $x_{n}$ gives

$$
f (x _ {n} ^ {p}) = f (\bar {x}) + \frac {1}{2} \left\langle \bar {H} e _ {n} ^ {p}, e _ {n} ^ {p} \right\rangle + o (\left| e _ {n} ^ {p} \right| ^ {2}).
$$

These three relations give an estimate of $\delta_{n}=f(x_{n})-f(x_{n}^{p})+\frac{1}{2}\langle g_{n}^{p},s_{n}^{p}\rangle$ :

$$
\delta_ {n} = \frac {1}{2} \langle \tilde {H} e _ {n}, e _ {n} \rangle - \frac {1}{2} \langle \bar {H} e _ {n} ^ {p}, e _ {n} \rangle + o (| e _ {n} | ^ {2}),
$$

where we have used (4.12): $s_n^p$ and $e_n^p$ have the order of magnitude of $e_n$. In the second term, use the relation

$$
e _ {n} = 2 e _ {n} ^ {p} - (x _ {n} ^ {+} - \bar {x}) = 2 e _ {n} ^ {p} + o (| e _ {n} |)
$$

to obtain

$$
\delta_ {n} = \frac {1}{2} \left\langle \bar {H} e _ {n}, e _ {n} \right\rangle - \left\langle \bar {H} e _ {n} ^ {p}, e _ {n} ^ {p} \right\rangle + o (\left| e _ {n} \right| ^ {2}).
$$

In summary, we have the following estimate for the right-hand side in (2.9):

$$
\begin{aligned} f (x _ {n}) - m \delta_ {n} &= f (\bar {x}) + \frac {1 - m}{2} \langle \bar {H} e _ {n}, e _ {n} \rangle + m \langle \bar {H} e _ {n} ^ {p}, e _ {n} ^ {p} \rangle + o (| e _ {n} | ^ {2}) \\ &\geqslant f (\bar {x}) + \frac {1 - m}{2} \alpha | e _ {n} | ^ {2} + o (| e _ {n} | ^ {2}), \\ \end{aligned}
$$

because $m \in ]0, 1[$. On the other hand, (4.13) can again be used to obtain the estimate (we set $e_n^+ := x_n^+ - \bar{x}$ )

$$
f (x _ {n} ^ {+}) = f (\bar {x}) + \frac {1}{2} \left\langle \bar {H} e _ {n} ^ {+}, e _ {n} ^ {+} \right\rangle + o (\left| e _ {n} ^ {+} \right| ^ {2}) = f (\bar {x}) + o (\left| e _ {n} \right| ^ {2}).
$$

Because $(1 - m)\alpha /2 > 0$, we conclude that our $q$ -superlinear assumption ensures that (2.9) is eventually satisfied.

It remains to take care of (4.3). From (4.13), setting $s_{n}^{+} := x_{n}^{+} - x_{n} = -e_{n} + o(|e_{n}|)$, we write

$$
\begin{aligned} \langle g (x _ {n} ^ {+}), s _ {n} ^ {+} \rangle &= \langle \bar {H} e _ {n} ^ {+}, s _ {n} ^ {+} \rangle + o (\left| e _ {n} ^ {+} \right\Vert s _ {n} ^ {+} |) = o (\left| e _ {n} \right| ^ {2}), \\ \langle g (x _ {n}), s _ {n} ^ {+} \rangle &= \langle \bar {H} e _ {n}, s _ {n} ^ {+} \rangle + o (\left| e _ {n} \right| ^ {2}) = - \langle \bar {H} e _ {n}, e _ {n} \rangle + o (\left| e _ {n} \right| ^ {2}). \\ \end{aligned}
$$

We therefore obtain

$$
\langle g (x _ {n} ^ {+}) - g (x _ {n}), s _ {n} ^ {+} \rangle = \langle \bar {H} e _ {n}, e _ {n} \rangle + o (\left| e _ {n} \right| ^ {2}) \geqslant \alpha \left| e _ {n} \right| ^ {2} + o (\left| e _ {n} \right| ^ {2}).
$$

and this again is eventually positive. □

# 4.4. The $q$-superlinear convergence

Let us give one more general result from the theory of BFGS updates (see [3]).

Lemma 4.7. If $\{M_n\}$ is generated by the BFGS formula using pairs of vectors $(y_{n}, s_{n})$ such that

$$
\langle y _ {n}, s _ {n} \rangle > 0 \quad f o r a l l n \geqslant 1 \quad a n d \quad \sum_ {n \geqslant 1} \frac {| y _ {n} - M s _ {n} |}{| s _ {n} |} <   \infty ,
$$

where $M$ is a fixed symmetric positive definite matrix, then

$$
(M _ {n} - M) s _ {n} = o (\left| s _ {n} \right|). \tag {4.14}
$$

We now have all the necessary material to give our superlinear convergence result.

Theorem 4.8. Assume that the sequence $\{x_{n}\}$ generated by Algorithm (BFGS-AP3) converges to an optimal point $\bar{x}$, and that (3.6), (3.9) hold. Assume also that $\bar{H}$ is positive definite. Then, the convergence of $x_{n}$ to $\bar{x}$ is $q$ -superlinear.

Proof. First of all, we establish the necessary local properties of the gradient mapping. Take $x$ and $y$ in the neighbourhood of $\bar{x}$ and apply (3.10):

$$
g (x) - g (y) = \bar {H} (x - y) + o (| x - y |).
$$

This implies the Lipschitz continuity of $g$ near $\bar{x}$. Multiply this last relation by $x - y$ : because $\bar{H}$ is positive definite, $g$ is (locally) strongly monotone, i.e., $f$ is (locally) strongly convex. Thus, starting with Theorem 4.5 (all the assumptions required are satisfied): $\{x_n\}$ converges $r$ -superlinearly to $\bar{x}$.

Now, since (3.9) holds, we have

$$
\frac {| y _ {n} - \bar {H} s _ {n} |}{| s _ {n} |} \leqslant L (  | x _ {n + 1} - \bar {x} | + | x _ {n} - \bar {x} |) .
$$

Therefore, by the $r$ -linear convergence of $\{x_{n}\}$,

$$
\sum_ {n \geqslant 1} \frac {| y _ {n} - \bar {H} s _ {n} |}{| s _ {n} |} <   + \infty .
$$

This and Lemma 4.7 give $(M_n - \bar{H})s_n = o(|s_n|)$.

Finally, the latter estimate and Theorem 3.6 imply that $x_{n} + 2s_{n}^{p} - \bar{x} = o(|e_{n}|)$. Then Theorem 4.6 shows that the stepsize $t_n = 2$ is accepted by the line-search. Hence $e_{n+1} = o(|e_n|)$ and the convergence is $q$ -superlinear.

Let us conclude this section by a consequence of Theorems 4.2 and 4.8: if $g$ is locally Lipschitzian, and if $f$ has a minimum point $\bar{x}$ satisfying the assumptions of Theorem 4.8, then Algorithm (BFGS-AP3) is globally and $q$-superlinearly convergent.

# 5. Conclusion

The essential content of this paper is a theoretical investigation of algorithms for non-smooth optimization combining quasi-Newton techniques with Moreau–Yosida regularizations. When doing so, we have privileged approaches lending themselves to implementations via bundle methods.

Ideally, this should be achieved by the algorithmic pattern AP2; see [18] for implementable proposals. However, the local properties of this algorithm turn out to be rather hard to analyze; as for AP1, studied by [20], some technicalities are needed when turning to implementation aspects. We have therefore adopted here AP3, which appears as a good compromise between theoretical simplicity and practical significance.

As stated in Sections 3 and 4, AP3 is quite comparable to a standard quasi-Newton algorithm. By analogy with differential equations, AP3 could be viewed as a trapezoidal integration scheme: two successive iterates are computed using the derivatives $g$ and $H$ at their mid-point $x_{n}^{p}$. As a by-product, the tools of the present work could therefore be applied to standard quasi-Newton algorithms (i.e., explicit integration schemes). Keeping this in mind, our local theory of Section 3 is then fairly comparable to that of [14]. In particular, it should be pointed out that the relevant smoothness assumptions are basically the same. Our role in this matter has been to extract from [14] the key properties of $f$, to be satisfied at the solution point $\bar{x}$ only. In other words, we used the conclusions of Theorems 3.1 and 3.2 instead of their premises.

On the other hand, such a local study with weakened assumptions is related to the resolution of non-smooth equations, studied in [23,27,16,26,24], among others. There exist Newton formulae which converge superlinearly under fairly general assumptions (semi-smoothness of $g$ ). Indeed, a Newton scheme uses directly the Hessian $\nabla^2 f(x_n)$, which gives by definition reliable second-order information at $x_n$ ; the role of semi-smoothness is then to ensure that this information remains valid all the way to convergence. By contrast, we need here apparently restrictive assumptions such as (3.8); in a quasi-Newton context, however, they seem rather minimal. For the quasi-Newton equation (3.1) to be any good, the values $g(x_n)$ and $g(x_{n + 1})$ must reflect the values $g(x)$ at neighbouring $x$ 's; this is precisely the role of (3.8).

# Acknowledgements

We are indebted to an anonymous referee, whose constructive remarks were very helpful for the final version of this paper.

# References

[1] A. Auslender, “Numerical methods for non-differentiable convex optimization,” Mathematical Programming Study 30 (1987) 102–126.

[2] C.G. Broyden, J.E. Dennis and J.J. Moré, “On the local and superlinear convergence of quasi-Newton methods,” Journal of the Institute of Mathematics and its Applications 12 (1973) 223–245.  
[3] R.H. Byrd and J. Nocedal, “A tool for the analysis of quasi-Newton methods with application to unconstrained minimization,” SIAM Journal on Numerical Analysis 26 (1989) 727–739.  
[4] F.H. Clarke, Optimization and Non-Smooth Analysis (Wiley, New York, 1983).  
[5] R. Correa and C. Lemaréchal, “Convergence of some algorithms for convex minimization,” Mathematical Programming 62 (1993) 261–275.  
[6] J.E. Dennis and J.J. Moré, “A characterization of superlinear convergence and its application to quasi-Newton methods,” Mathematics of Computation 28 (1974) 549–560.  
[7] J.E. Dennis and J.J. Moré, “Quasi-Newton methods, motivation and theory,” SIAM Review 19 (1977) 46–89.  
[8] J.E. Dennis and R.B. Schnabel, “A view of unconstrained optimization,” in: G.L. Nemhauser, A.H.G. Rinnooy Kan and M.J. Todd, eds., Handbook in Operations Research and Management Science, Vol. 1 (North-Holland, Amsterdam, 1989) 1–72.  
[9] M. Fukushima, “A descent algorithm for non-smooth convex programming,” Mathematical Programming 30 (1984) 163–175.  
[10] J.Ch. Gilbert and C. Lemaréchal, “Some numerical experiments with variable-storage quasi-Newton algorithms,” Mathematical Programming 45 (1989) 407–435.  
[11] W.A. Gruver and E. Sachs, Algorithmic Methods in Optimal Control, Research Notes in Mathematics No. 47 (Pitman, London, 1980).  
[12] S.M. Grzegórski, “Orthogonal projections on convex sets for Newton-like methods”, SIAM Journal on Numerical Analysis 22 (1985) 1208–1219.  
[13] J.B. Hiriart-Urruty and C. Lemaréchal, Convex Analysis and Minimization Algorithms, Vols. 1 and 2 (Springer-Verlag, Berlin, Heidelberg, New York, 1993).  
[14] C.-M. Ip and J. Kyparisis, “Local convergence of quasi-Newton methods for B-differentiable equations,” Mathematical Programming 56 (1992) 71–89.  
[15] K.C. Kiwiel, “Proximity control in bundle methods for convex non-differentiable minimization,” Mathematical Programming 46 (1990) 105–122.  
[16] B. Kummer, “Newton’s method based on generalized derivatives for non-smooth functions: convergence analysis,” in: W. Oettli and D. Pallaschke, eds., Advances in Optimization, Lecture Notes in Economics and Mathematical Systems No. 382 (Springer-Verlag, Berlin, Heidelberg, New York, 1991) 171–194.  
[17] C. Lemaréchal, “A view of line-searches,” in: A Auslender, W. Oettli and J. Stoer, eds., Optimization and Optimal Control, Lecture Notes in Control and Information Science No. 30 (Springer-Verlag, Berlin, Heidelberg, New York, 1981) 59–78.  
[18] C. Lemaréchal and C. Sagastizábal, “An approach to variable metric bundle methods,” in: J. Henry and J.P. Yvor, eds., Proceedings IFIP Conference Systems Modelling and Optimization, Lecture Notes in Control and Information Sciences No. 197 (Springer-Verlag, New York, 1994).  
[19] B. Martinet, “Régularisation d’inéquations variationelles par approximations successives,” Revue Française d’Informatique et Recherche Opérationelle R-3 (1970) 154–179.  
[20] R. Mifflin, “A quasi-second-order proximal bundle algorithm,” Technical Report 93-3, University of Washington (Pullman, Washington, 1993).  
[21] J.J. Moreau, “Proximité et dualité dans un espace hilbertien,” Bulletin de la Société Mathématique de France 93 (1965) 273–299.  
[22] J.M. Ortega and W.C. Rheinboldt, Iterative Solution of Non-linear Equations in Several Variables (Academic Press, New York, 1970).  
[23] J.-S. Pang, “Newton’s method for B-differentiable equations,” Mathematics of Operations Research 15 (1990) 311–341.  
[24] J.S. Pang and L.Q. Qi, “Non-smooth equations: motivation and algorithms,” SIAM Journal on Optimization 3 (1993) 443–465.  
[25] M.J.D. Powell, “Some global convergence properties of a variable metric algorithm for minimization without exact line searches,” in: R.W. Cottle and C.E. Lemke, eds., Non-linear Programming, SIAM–AMS Proceedings No. 9 (American Mathematical Society, Providence, RI, 1976).  
[26] L. Qi and J. Sun, “A non-smooth version of Newton’s method,” Mathematical Programming 58 (1993) 353–367.  
[27] L.Q. Qi, “Convergence analysis of some algorithms for solving non-smooth equations,” Mathematics of Operations Research 18 (1993) 227–244.  
[28] M. Qian, “The variable metric proximal point algorithm: global and super-linear convergence,” Manuscript GN-50, University of Washington, Department of Mathematics (Seattle, WA, 1992).  
[29] S.M. Robinson, “Local structure of feasible sets in non-linear programming, part III: stability and sensitivity,” Mathematical Programming Study 30 (1987) 45–66.  
[30] R.T. Rockafellar, Convex Analysis (Princeton University, Princeton, NJ, 1970).  
[31] R.T. Rockafellar, “Monotone operators and the proximal point algorithm,” SIAM Journal on Control and Optimization 14 (1976) 877–898.  
[32] C.A. Sagastizábal, “Quelques méthodes numériques d’optimisation. Application en gestion de stocks,” Ph.D. thesis, University of Paris I, Panthéon–Sorbonne (Paris, 1993).
