# "The heavy ball with friction method".

# I. The continuous dynamical system

Global exploration of the local minima of a real-valued function by asymptotic analysis of a dissipative dynamical system.

# H. ATTOUCH X. GOUDOU P. REDONT

ACSIOM-CNRS EP 2066

Département de Mathématiques, case 51

Université Montpellier II

Place Eugène Bataillon

34095 Montpellier cedex 5

France

# Abstract

Let H be a real Hilbert space and $\Phi: H \to \mathbf{R}$ a continuously differentiable function, whose gradient is Lipschitz continuous on bounded sets. We study the nonlinear dissipative dynamical system: $\ddot{x}(t) + \lambda\dot{x}(t) + \nabla\Phi(x(t)) = 0$, $\lambda > 0$, plus Cauchy data, mainly in view of the unconstrained minimization of the function $\Phi$. New results concerning the convergence of a solution to a critical point are given in various situations, including when $\Phi$ is convex (possibly with multiple minima) or is a Morse function (the critical point being then generically a local minimum); a counterexample shows that, without peculiar assumptions, a trajectory may not converge. By following the trajectories, we obtain a method for exploring local minima of $\Phi$. A singular perturbation analysis links our results with those concerning gradient systems.

Key-words: dissipative dynamical system, optimization, local minima, convex minimization, asymptotic behaviour, gradient system, Morse function, heavy ball with friction.

AMS classification: 34A12, 34Dxx, 49Mxx.

# 1 Introduction

Throughout this paper, we consider a real Hilbert space H with scalar product and norm denoted by $\langle.,.\rangle$ and $|.|$ respectively, while $\Phi:x\in H\mapsto\Phi(x)\in\mathbf{R}$ is a continuously differentiable function, whose gradient is denoted by $\nabla\Phi$ . The critical points of $\Phi$ are the solutions of the equation $\nabla\Phi(x)=0$ .

We are concerned with dynamical systems whose trajectories asymptotically converge to local minima of $\Phi$. Our purpose is to develop a numerical method, which consists in following the trajectories of such a dynamical system as the time t goes to $+\infty$, in order to explore in a global way the local minima of $\Phi$.

The dynamical system which we consider in this paper is the “heavy ball with friction” system. It is a non-linear oscillator with damping

$$
\ddot {x} (t) + \lambda \dot {x} (t) + \nabla \Phi (x (t)) = 0 \tag {HBF}
$$

where $\lambda$ is a positive real number ( $\lambda > 0$ ).

A straight computation yields that the energy $E(.)$ of this system

$$
E (t) := \frac {1}{2} | \dot {x} (t) | ^ {2} + \Phi (x (t))
$$

verifies

$$
\dot {E} (t) = - \lambda | \dot {x} (t) | ^ {2}.
$$

It follows that the energy is dissipated as t increases. The advantage of using a dissipative dynamical system lies in the fact that the trajectories of such systems asymptotically converge to equilibria (or get close to the set of equilibria), which, for our concern, are typically the local minima of $\Phi$. For a recent account of the theory, we refer the reader to Haraux [19], Hale [17]. This system modelizes the motion of a heavy material point $M(t) = (x(t), \Phi(x(t)))$ sliding on a profile defined by $\Phi$. The damping term $\lambda\dot{x}(t)$ corresponds to a viscous mechanical friction. Because of this mechanical interpretation, we call this system, the "heavy ball with friction" dynamical system, in short "HBF".

The intuition provided by this mechanical interpretation will help us in order to derive a global strategy for the numerical computation of the local minima of $\Phi$.

![](images/909bf868d88cc3522321656a9af4677da19f90a4b61d469c91ec842bdb075409.jpg)

<details>
<summary>line</summary>

| Point | X-axis (H) | Y-axis (IR) |
| --- | --- | --- |
| M0 | x0 | High |
| M(t) | x(t) | Medium |
| M-bar | x̄ | Low |
| M# | x# | Low |
</details>

Figure 1:

As an illustration, let us consider the following situation (see figure 1) and the corresponding Cauchy problem for (HBF):

$$
\left\{ \begin{aligned} \ddot {x} (t) + \lambda \dot {x} (t) + \nabla \Phi (x (t)) &= 0 \\ x (0) &= x _ {0}, \dot {x} (0) = \dot {x} _ {0} \end{aligned} \right. \tag {HBF}
$$

Intuitively, if we think to the mechanical interpretation of this system, we can conceive that, depending on the initial energy given to the ball $(E_{0}=\frac{1}{2}|\dot{x}_{0}|^{2}+\Phi(x_{0}))$, and on the value of the friction parameter $\lambda$, $M(t)$ asymptotically tends to stabilize in $\overline{M}$ or $M^{\#}$, with some possible damped oscillations.

That is the starting point of the method which is developed in this paper. We can think of the initial data, namely the initial position $x_{0}$ and the initial velocity $\dot{x}_{0}$, and of the friction parameter $\lambda > 0$ as control variables which allow us to reach asymptotically, via the dynamical system, several local minima of $\Phi$. For example, when starting from $x_{0}$, depending on the velocity $\dot{x}_{0}$, one can reach asymptotically $\overline{x}$ or $x^{\#}$. Even more, when starting from $\overline{x}$, by taking an initial velocity which is large enough, the trajectory can escape from the attraction domain of $\overline{x}$, and asymptotically converge to $x^{\#}$.

The heavy ball with friction system is a second order (in time) dissipative dynamical system. By contrast, the steepest descent method, also called the continuous gradient method, which is a first order in time system,

$$
\left\{ \begin{aligned} \dot {x} (t) + \nabla \Phi (x (t)) &= 0 \\ x (0) &= x _ {0} \end{aligned} \right. \tag {SD}
$$

has several drawbacks. The (SD) system modelizes the motion of a drop of water sliding on the profile represented by $\Phi$. It is a “slow” motion, and

when starting from $x_0$ (see figure 1), the trajectory asymptotically converge to $\overline{x}$. There is no way, when starting from $x_0$, to reach $x^\#$. It is a first order (in time) system, the trajectory is completely determined by its initial position. In the (HBF) system, which is a second order (in time) system, for a given initial position $x_0$, one can play with the initial velocity $\dot{x}_0$ to reach asymptotically different critical points. To complete the comparison between these two dynamical systems, it is worth pointing out that (SD) is a descent method (this explains why, having reached $\overline{M}$, which is a local minimum, it is not possible to go further), while (HBF) is not a descent method. In the (HBF) system, the trajectories may exhibit damped oscillations around the equilibrium. It is one important aspect of the numerical method to deal with these oscillations (see section 6). Each of the two systems offers specific advantages. Just retain that (HBF) offers much more flexibility and possibilities of control than (SD), in order to explore the local minima of a given function $\Phi$.

At this point, it is important to notice that, in order to explore and compute the critical points of $\Phi$, it is not necessary to know precisely the exact trajectories of the (HBF) system. We may replace it, or approximate it, by a simpler or discrete dynamical system which preserves the asymptotic behaviour of the solutions. That's also what we do when passing from the complete heavy ball with friction mechanical system to the simplified equations of the (HBF) system.

When developing numerical methods, we shall not work with the (HBF) system. From a numerical point of view, it is too expensive to compute the “whole” trajectories. We shall work on discretized dynamical versions, which enjoy quite similar asymptotic behaviour (Attouch-Goudou-Redont [6]).

The paper is organized as follows.

In Section 2, we establish the equations of the “heavy ball with friction mechanical system”. We show that the (HBF) system is a natural approximation of this quite involved system. This is an important step in order to justify the mechanical intuition of the (HBF) system.

In Section 3, a global existence and uniqueness result is established for the (HBF) dynamical system, just assuming $\Phi$ to be bounded from below, and $\nabla\Phi$ Lipschitz continuous on bounded sets (theorem 3.1).

In Section 4, we study different cases where the trajectories of the (HBF) system converge as $t \to +\infty$. In theorem 4.1., this asymptotic convergence

property is proved when $\Phi$ is a Morse function with precompact HBF trajectories. Moreover, one can prove that, generically, for this class of functions $\Phi$, the trajectories of the (HBF) system asymptotically converge, as $t \to +\infty$, to local minima of $\Phi$. This justifies the use of the (HBF) system in optimization theory. In theorem 4.3., it is proved that, when $\Phi$ is convex and $\argmin\Phi \neq \emptyset$, the trajectories of the (HBF) system are weakly convergent in $H$ as $t \to +\infty$. This is a deep result, which has been recently established by Alvarez [2], and which is intimately linked with the Brézis [11] and Bruck [12] theorem on the asymptotic convergence of the trajectories of the steepest descent method. These positive results naturally raise the question whether, for any smooth $\Phi$, the trajectories of the corresponding (HBF) system converge? In section 4.3., we construct a function $\Phi: \mathbf{R}^2 \to \mathbf{R}$ which is $\mathcal{C}^1$, with $\nabla\Phi$ Lipschitz continuous, and coercive, such that at least one trajectory of the (HBF) system does not converge as $t \to +\infty$. This is a quite involved construction, we start from a non convergent trajectory $t \to x(t)$, which is indeed a spiral. Then, we construct, by interpolation techniques, a function $\Phi$, satisfying the prescribed conditions, such that $t \to x(t)$ is a trajectory of the corresponding (HBF) system.

In section 5, we look more closely at the connection between the heavy ball with friction dynamical system (HBF) and the steepest descent method (SD). Indeed, (SD) can be viewed as a limit case of the (HBF) system. At this point, it is important to consider the (HBF) system with all its physical parameters, m, $\lambda_{f}$, g

$$
m \ddot {x} + \lambda_ {f} \dot {x} + m g \nabla \Phi (x) = 0
$$

where m is the mass, $\lambda_{f}$ the friction parameter and g the gravity constant. Equivalently,

$$
\frac {1}{g} \ddot {x} + \frac {\lambda_ {f}}{m g} \dot {x} + \nabla \Phi (x) = 0.
$$

When taking $g = \frac{1}{\varepsilon} \rightarrow +\infty$ and $\frac{\lambda_{f}}{mg} \rightarrow 1$, we obtain, at least formally, that the (SD) system

$$
\dot {x} + \nabla \Phi (x) = 0 \tag {SD}
$$

is the limit as $\varepsilon \rightarrow 0$ of the (HBF) $_{\varepsilon}$ system

$$
(H B F) _ {\varepsilon} \qquad \qquad \varepsilon \ddot {x} + \dot {x} + \nabla \Phi (x) = 0.
$$

The uniform convergence on all bounded intervals $[0,T]$ of the trajectories of $(\mathrm{HBF})_{\varepsilon}$ to the corresponding trajectories of (SD) is proved in theorem 5.1. In theorem 5.2, when $\Phi$ is convex, it is proved that the convergence of the trajectories as $\varepsilon\to0$, holds for the uniform convergence on $[0,+\infty[$. This result shows that, for a smooth $\Phi$, the Brézis-Bruck asymptotic convergence theorem can be obtained as a consequence of the (HBF) asymptotic convergence theorem 4.3.

In section 6, we indicate how the (HBF) dynamical system can be used in order to explore the local minima of a given function $\Phi$. We first examine the local problem, which consists in computing a local minimum. We illustrate on several examples the importance of the choice of a good friction parameter $\lambda$, which has to be a compromise between the damping of the oscillations ( $\lambda$ “large”) and the dynamical interest of the acceleration term ( $\lambda$ “small”). Then, we briefly sketch a method, which is based on the (HBF) dynamical system, which permits to explore the local minima. We stress the fact that, having reached a local minimum, the (HBF) dynamical system may allow to restart from this local minimum, escape from its attraction domain and asymptotically reach an other local minimum. It is not our purpose in this paper to study the numerical aspects of the method. We are only concerned with the general ideas underlying the method. Indeed, the numerical exploitation of the method, relies on the utilization of discretized versions of the (HBF) system. This will be developed in a separated paper [6].

As we already noticed for some of them, many interesting aspects of the (HBF) system have not been examined in this paper, their complete study largely exceeding the scope of this paper. It is a natural objective for the future, beyond the numerical development of the method, to develop it as a global optimization method, and to consider the constrained case. One may conjecture that some of the asymptotic results have extensions to the case where $\Phi$ is non-smooth (lower semicontinuous and convex), which is important in view of partial differential equations (the damped wave equation for example).

# 2 The mechanical problem

Let us consider a real Hilbert space H, with scalar product $\langle.,.\rangle$ and a mapping $\Phi:H\to R$, of class $C^{1}$. Given a material point M of mass m which

moves on the manifold defined by $\Sigma := \text{Graph}(\Phi)$, $\overrightarrow{r(t)}$ denotes the position of M at time t :

$$
\overrightarrow {r (t)} = \binom{x (t)}{\Phi (x (t))} \quad \text {when} x (t) \in H.
$$

According to the fundamental principle of the dynamics, F.P.D. in short, the motion of M is governed by the equation :

$$
m \stackrel {\cdot \cdot} {r} = \overrightarrow {G} + \overrightarrow {F} + \overrightarrow {R} \tag {2.1}
$$

the second member of this equality being the sum of the forces which are applied to M :

- The gravity force $\overrightarrow{G} = \binom{0}{-mg}$.  
- A force of friction of viscous type: this force is opposed to the movement of the particle (friction), and is proportional to the speed (viscous friction): $\overrightarrow{F} = -\lambda_f \dot{\vec{r}}(t)$, where $\lambda_f > 0$ is the friction coefficient.  
- The reaction $\overrightarrow{R}$ of the surface ( $\Sigma$ ), which expresses that the particle does not penetrate into ( $\Sigma$ ): $\overrightarrow{R} = R\overrightarrow{n}$ where $R > 0$ and $\overrightarrow{n}$ is the outwards unitary normal to ( $\Sigma$ ) at $M$.

![](images/3d93c6e47e9e5c53df829c4ee43da9df488666da0ab13962008991cfdd29b5b2.jpg)

<details>
<summary>text_image</summary>

IR
Φ(x)
M
R
F
G
Σ
x
H
</details>

Figure 2:

Classically, $\overrightarrow{n}(x)=\frac{1}{\sqrt{1+|\nabla\Phi(x)|^{2}}}\left(-\nabla\Phi(x)\atop1\right)$

and :

$$
\overrightarrow {r} (t) = \binom{x (t)}{\Phi (x (t))}
$$

$$
\dot{\overrightarrow {r}} (t) = \binom{\dot {x} (t)}{\nabla \Phi (x (t)) \dot {x} (t)}
$$

$$
\ddot{\overrightarrow {r}} (t) = \binom{\ddot {x} (t)}{\dot {x} (t) \left(H _ {\Phi} (x (t)) \dot {x} (t) + \nabla \Phi (x (t)) \ddot {x} (t)\right)}
$$

where $H_{\Phi}(x)$ is the Hessian of $\Phi$ at x (also denoted by $\nabla^{2}\Phi(x)$ ).

The F.P.D. gives us :

$$
\left\{ \begin{aligned} m \ddot {x} &= - \lambda_ {f} \dot {x} - \frac {R}{\sqrt {1 + | \nabla \Phi (x) | ^ {2}}} \nabla \Phi (x) \\ m (\dot {x} H _ {\Phi} (x) \dot {x} + \nabla \Phi (x) \ddot {x}) &= - m g - \lambda_ {f} \nabla \Phi (x) \dot {x} + \frac {R}{\sqrt {1 + | \nabla \Phi (x) | ^ {2}}} \end{aligned} \right. \tag {2.2}
$$

We still have to determine the amplitude R of the reaction of the surface $(\Sigma)$ : this amplitude must be positive, non zero, and by projection on $\overrightarrow{n}$ of the equation (2.1) we obtain :

$$
R = \frac {m}{\sqrt {1 + | \nabla \Phi (x) | ^ {2}}} (g + \dot {x} H _ {\Phi} \dot {x}).
$$

The condition “R > 0” (which expresses the contact between the particle M and the surface ( $\Sigma$ )) becomes :

$$
g + \dot {x} H _ {\Phi} \dot {x} > 0. \tag {2.3}
$$

As $g$ is strictly positive, this condition is satisfied when $\dot{x}$ is small enough (which is the case in slow movements), or when $H_{\Phi}$ is non negative ( $\Phi$ convex).

Finally, we obtain :

$$
m \ddot {x} + \lambda_ {f} \dot {x} + \frac {m}{1 + | \nabla \Phi (x) | ^ {2}} (g + \dot {x} H _ {\Phi} (x) \dot {x}) \nabla \Phi (x) = 0 \tag {2.4}
$$

This equation is relatively complicated, and is not easy to handle.

We know experimentally that (because of the friction coefficient $\lambda_{f}>0$ ) the dynamical system defined by (2.4) is dissipative, and $x(t)$ tends towards a local minimum of $\Phi$, and $\dot{x}(t)$ tends to zero.

Since we are interested in the asymptotic behaviour of $x(t)$, we notice that

\- $|\nabla \Phi (x)|$ is negligible with respect to 1

\- $\dot{x} H_{\Phi}(x)\dot{x}$ is negligible with respect to $g$,

which gives us the following system :

$$
m \ddot {x} + \lambda_ {f} \dot {x} + m g \nabla \Phi (x) = 0.
$$

Let us now define $\lambda = \lambda_{f}/m$. We finally obtain the (HBF) system

$$
(H B F) \quad \ddot {x} + \lambda \dot {x} + g \nabla \Phi (x) = 0
$$

This equation only possesses a mechanical sense when $\dot{x}$ is small.

Despite that, our approach is to consider that (HBF) (with initial conditions $x(0)$ and $\dot{x}(0)$ ) constitutes a dynamical system which will be studied intrinsically, independently from the fact that is attached to a mechanical situation, or not. In particular, we will have to consider (HBF) at times for which $\dot{x}(t)$ is not necessarily small. But, in order to study the asymptotic behaviour of $x(t)$ when $t \to +\infty$ , the mechanical origin of the equation will give us an intuitive framework permitting to guess what would happen.

# 3 Global existence

Let H be a real Hilbert space. Let us consider a mapping $\Phi: H \rightarrow R$ which satisfies the following conditions :

$$
(\mathcal {H}) \left\{ \begin{array}{l l} \Phi \text {is continuously differentiable on} H \\ \Phi \text {is bounded from below on} H \\ \nabla \Phi \text {is Lipschitz continuous on the bounded subsets of} H. \end{array} \right.
$$

The second order system, in $H$ :

$$
\ddot {x} + \lambda \dot {x} + g \nabla \Phi (x) = 0 \tag {3.1}
$$

can be written as a first order system in $H \times H$ :

$$
\dot {Y} = F (Y)
$$

with

$$
Y (t) &= \big ( \begin{aligned} x (t) \\ \dot {x} (t) \end{aligned} \big) \quad \text {and} \quad F (u, v) &= \big ( \begin{array}{l} v \\ - \lambda v - g \nabla \Phi (u) \end{array} \big).\tag {3.2}
$$

For $Y_0 &= \left( \begin{aligned}x_0\\ \dot{x}_0 \end{aligned} \right)$ given in $H\times H$ , the Cauchy-Lipschitz theorem and hypothesis (H) ensure the existence of a unique local solution to the problem:

$$
\left\{ \begin{aligned} \dot {Y} &= F (Y) \\ Y (0) &= Y _ {0} \end{aligned} \right. \tag {3.3}
$$

On the other hand, we can define along every trajectory of (3.1) the energy by:

$$
E (t) = \frac {1}{2} | \dot {x} (t) | ^ {2} + g \Phi (x (t)).
$$

The central result of this section is given by the following theorem.

Theorem 3.1 Let us assume that $\Phi : \mathcal{H} \to \mathbf{R}$ satisfies the assumptions (H) and that the friction parameter $\lambda$ is positive ( $\lambda > 0$ ). Then, the following properties

(i) for all $(x_{0},\dot{x}_{0})$ in $H\times H$, there exists a unique solution $x(t)$ of (3.1) defined on the whole interval $[0,+\infty[$, which is of class $C^{2}$ on $[0,+\infty[$, and which satisfies the initial conditions $x(0)=x_{0}$ and $\dot{x}(0)=\dot{x}_{0}$.  
(ii) for every trajectory $x(t)$ of (3.1), the corresponding energy $E(t)$ is decreasing on $[0, +\infty[$ and bounded from below, and hence converges to some real value $E_{\infty}$. Moreover,

$$
\dot {x} \in L ^ {\infty} (0, + \infty ; H) \cap L ^ {2} (0, + \infty ; H).
$$

(iii) Assuming moreover that $x$ is in $L^{\infty}(0, + \infty ;H)$, then we have

- $\dot{x}$ and $\ddot{x}$ belong to $L^{\infty}(0, +\infty; H)$,  
- $\lim_{t\to +\infty}\dot{x} (t) = 0$ and $\lim_{t\to +\infty}\ddot{x} (t) = 0,$  
- $\lim_{t\to +\infty}\nabla \Phi (x(t)) = 0$ and $\lim_{t\to +\infty}\Phi (x(t)) = \frac{E_{\infty}}{g}$.

Remark: When the HBF trajectory x is precompact for the norm topology in H, the main results of the theorem, $\lim_{t\to+\infty}\dot{x}(t)=0$ and $\lim_{t\to+\infty}\nabla\Phi(x(t))=0$, may be obtained as consequences of the Lasalle invariance principle (Ball [8], Haraux [20], Dafermos [14]). Yet we give a direct proof getting out of compactness hypotheses, and whose techniques will prove to be useful later (see sections 4 and 5).

Proof of theorem 3.1. i) For any choice of initial conditions $(x_{0},\dot{x}_{0})\in H\times H$, the existence and uniqueness of a local solution for (3.1), follows from the Cauchy-Lipschitz theorem. Let $x(t)$ denote the corresponding maximal solution which is defined on some interval $[0,T_{max}]$ with $0<T_{max}\leq+\infty$. In order to prove that $T_{max}=+\infty$, let us show that $\dot{x}(t)$ is bounded.

We first observe that equation (3.1) and the regularity assumptions on $\Phi$ automatically imply that $x(.)$ is $C^{2}$ on $[0, T_{max}]$. By differentiation of $E(t)$, and by using (3.1), we obtain

$$
\begin{aligned} \dot {E} (t) &= \left\langle \dot {x} (t), \ddot {x} (t) + g \nabla \Phi (x (t)) \right\rangle \tag {3.4} \\ &= - \lambda | \dot {x} (t) | ^ {2}. \\ \end{aligned}
$$

Thus, the function $E(.)$ is decreasing and for all $t \in [0, T_{max}[$

$$
E (t) \leq E (0).
$$

Equivalently,

$$
\frac {1}{2} | \dot {x} (t) | ^ {2} + g \Phi (x (t)) \leq \frac {1}{2} | \dot {x} _ {0} | ^ {2} + g \Phi (x _ {0}). \tag {3.5}
$$

Since $\Phi$ is bounded from below, we obtain that

$$
\sup _ {t \in [ 0, T _ {m a x} [} | \dot {x} (t) | := C <   + \infty .
$$

It is a standard argument to derive from such estimation, that $T_{max} = +\infty$. Indeed, let us argue by contradiction, and assume that $T_{max} < +\infty$. We have

$$
| x (t) - x (t') | \leq C | t - t' |,
$$

and since $T_{max} < +\infty$, $\lim_{t \to T_{max}} x(t) := x_{\infty}$ exists. So, $x(.)$ and $\dot{x}(.)$ are bounded on $[0, T_{max}]$, and by equation (3.1), $\ddot{x}(.)$ is bounded too on this interval. So $\lim_{t \to T_{max}} \dot{x}(t) = \dot{x}_{\infty}$ exists. But, applying again the local existence theorem with initial data $(x_{\infty}, \dot{x}_{\infty})$, we can extend the maximal solution to a strictly larger interval, which is a clear contradiction. So, $T_{max} = +\infty$, which completes the proof of i).

ii) We already proved that $E(.)$ is decreasing. Since $\Phi$ is bounded from below, and since $E(t) \geq g\Phi(x(t))$, we have that $E(.)$ is also bounded from below. As a consequence, $\lim_{t \to +\infty} E(t) = E_\infty$ exists, with $E_\infty \in R$. Using

(3.4), and the fact that $\Phi$ is bounded from below, we obtain that, for all $t \geq 0$

$$
\frac {1}{2} | \dot {x} (t) | ^ {2} \leq \frac {1}{2} | \dot {x} _ {0} | ^ {2} + g \Phi (x _ {0}) - g \inf \Phi .
$$

Hence,

$$
\dot {x} \in L ^ {\infty} (0, + \infty ; H).
$$

From (3.4), we derive that, for all $0 \leq t < +\infty$

$$
\int_ {0} ^ {t} | \dot {x} (s) | ^ {2} d s = \frac {1}{\lambda} (E _ {0} - E (t)).
$$

Since $E(t)$ decreases to $E_{\infty}$ as $t$ increases to $+\infty$, we obtain that

$$
\int_ {0} ^ {+ \infty} | \dot {x} (s) | ^ {2} d s = \frac {1}{\lambda} (E _ {0} - E _ {\infty}),
$$

and $\dot{x} \in L^{2}(0, +\infty; H)$.

iii) We now assume that $x$ is in $L^{\infty}(0, + \infty ;H)$.

We already proved in ii) that $\dot{x} \in L^{\infty}(0, +\infty; H)$. The equation (3.1), and the fact that $\nabla \Phi$ is bounded on the bounded subsets of $H$, imply that $\ddot{x} \in L^{\infty}(0, +\infty; H)$.

Let us now observe that the function $h(t) := \dot{x}(t)$ satisfies both

$$
h \in L ^ {2} (0, + \infty ; H) \quad \text {and} \quad \dot {h} \in L ^ {\infty} (0, + \infty ; H).
$$

According to a classical result, these two properties imply: $\lim_{t\to +\infty}h(t) = 0$ . (Indeed, arguing by contradiction and owing to $h$ being Lipschitzian, there would exist $\varepsilon >0$ , $\eta >0$ and a sequence of non-overlapping intervals $[t_n - \eta ,t_n + \eta ]\subseteq [0, + \infty [$ such that $|t - t_n| <   \eta \Rightarrow |h(t)| > \varepsilon$ ; which is inconsistent with $h\in L^{2}(0, + \infty ;H)$ ). Therefore, in our situation, we have $\lim_{t\to +\infty}\dot{x} (t) = 0$ .

It follows from equation (3.1) that

$$
\lim _ {t \to + \infty} [ \ddot {x} (t) + g \nabla \Phi (x (t)) ] = 0.
$$

If we are able to prove that $\lim_{t\to+\infty}\ddot{x}(t)=0$, then we automatically infer that $\lim_{t\to+\infty}\nabla\Phi(x(t))=0$.

So, let us prove that $\lim_{t\to+\infty}\ddot{x}(t)=0$. Let us first prove this result in the simpler case where $\Phi\in C^{2}$, then we shall see how one can adapt this argument when $\Phi$ is only $C^{1}$.

Returning to equation (3.1), since $\Phi$ is $\mathcal{C}^2$, we have that the solution $x$ is $\mathcal{C}^3$. By differentiating the equation we obtain

$$
\dddot {x} + \lambda \ddot {x} = f (t) \tag {3.6}
$$

with

$$
f (t) = - g H _ {\Phi} (x (t)) \dot {x} (t) \tag {3.7}
$$

where $H_{\Phi}$ is the Hessian of $\Phi$.

Since $\nabla\Phi$ is Lipschitz continuous on the bounded subsets of H, we have that $H_{\Phi}$ is bounded on the bounded subsets of H. Using this property and the fact that $x\in L^{\infty}(0,+\infty;H)$ and $\lim_{t\to+\infty}\dot{x}(t)=0$, we obtain that

$$
\lim _ {t \to + \infty} f (t) = 0. \tag {3.8}
$$

If we set $z = \ddot{x}$, equation (3.6) becomes: $\dot{z} + \lambda z = f$. After integration of this equation it is easy to verify that (3.8) implies convergence of $z(t) = \ddot{x}(t)$ to 0 as $t \to +\infty$.

When $\Phi$ is not $\mathcal{C}^2$, we are going to adapt the preceding argument. The idea is to replace the derivative $\ddot{x}$, which a priori makes no sense, by a differential quotient. For any $h > 0$, let us define

$$
u _ {h} (t) := \frac {1}{h} (\dot {x} (t + h) - \dot {x} (t)).
$$

Let us write the equation (3.1) at the points t and $t + h$, let us make the difference and divide by h. We obtain

$$
\dot {u} _ {h} (t) + \lambda u _ {h} (t) = f _ {h}
$$

where

$$
f _ {h} (t) = - g \frac {\nabla \Phi (x (t + h)) - \nabla \Phi (x (t))}{h}.
$$

We may now follow the lines of the preceding argument $(\Phi \in \mathcal{C}^2)$ to obtain

$$
\lim _ {t \to + \infty} \left(\sup _ {h > 0} | u _ {h} (t) |\right) = 0.
$$

Since, for all $t \geq 0$, the following inequality holds

$$
| \ddot {x} (t) | \leq \sup _ {h > 0} | u _ {h} (t) |
$$

we conclude that $\lim_{t\to +\infty}\ddot{x} (t) = 0$

We complete the proof of iii) by noticing that, since

$$
E (t) = \frac {1}{2} | \dot {x} (t) | ^ {2} + g \Phi (x (t)) \rightarrow E _ {\infty} \quad \text {as} t \rightarrow + \infty
$$

and since $\dot{x}(t)\to 0$ as $t\to +\infty$, we have that

$$
\lim _ {t \to + \infty} \Phi (x (t)) = \frac {E _ {\infty}}{g}. \qquad \square
$$

Corollary 3.1 Assume that $\Phi : \mathcal{H} \to \mathbf{R}$ satisfies the assumptions (H) and that the friction parameter $\lambda$ is positive ( $\lambda > 0$ ). Assume moreover that $\Phi$ is coer $\lim_{|x| \to +\infty} \Phi(x) = +\infty$ , then $x$ is in $L^{\infty}(0, +\infty; H)$ and the conclusions of theorem 3.1 hold.

Proof. It is enough to observe that the inequality (3.5) gives

$$
\Phi (x (t)) \leq \Phi (x _ {0}) + \frac {1}{2 g} | \dot {x} _ {0} | ^ {2}.
$$

This majorization on $\Phi(x(t))$ and the coerciveness of $\Phi$ imply that the trajectory $x(.)$ remains bounded, i.e. $x \in L^{\infty}(0, +\infty; H)$. $\square$

It is worth noticing that, by contrast with the steepest descent method, the heavy ball with friction method is not a descent method.

In addition, provided that the friction coefficient $\lambda > 0$ is not too large, in general the ball is going to oscillate (with damped oscillations) around its limit position.

Nevertheless, the method can be used to perform minimization of $\Phi$ . Let us notice that the energy $E(t)=\frac{1}{2}|\dot{x}(t)|^{2}+g\Phi(x(t))$ is decreasing. Hence, if we start from some initial point $x_{0}\in H$ and with an initial velocity $\dot{x}_{0}$ equal to zero, we have:

$$
E _ {\infty} \leq E _ {0} = g \Phi (x _ {0}).
$$

On the other hand, using that $\lim_{t\to+\infty}\dot{x}(t)=0$, we derive

$$
E _ {\infty} = g \lim _ {t \to + \infty} \Phi (x (t)).
$$

Combining these results, we obtain

$$
\lim _ {t \to + \infty} \Phi (x (t)) \leq \Phi (x _ {0}).
$$

Indeed, if $\nabla\Phi(x_{0})\neq0$ (i.e. if $x_{0}$ is not a critical point), noticing that $\dot{E}(t)=-\lambda|\dot{x}(t)|^{2}$ and that $\dot{x}(t)$ cannot be identically zero on $R^{+}$, we have that $E_{\infty}<E_{0}$ and hence

$$
\lim _ {t \to + \infty} \Phi (x (t)) <   \Phi (x _ {0}).
$$

So, from the point of view of minimizing $\Phi$, by taking t large enough one can strictly improve the criteria. This is summarized in the following

Proposition 3.1 For a given $x_0 \in H$ which satisfies $\nabla \Phi(x_0) \neq 0$, let us consider the trajectory $x(.)$ of (3.1) starting from $x_0$ with initial velocity equal to zero:

$$
\left\{ \begin{array}{l} \ddot {x} (t) + \lambda \dot {x} (t) + g \nabla \Phi (x (t)) = 0 \\ x (0) = x _ {0}, \dot {x} (0) = 0 \end{array} \right.
$$

Then,

$$
\lim _ {t \to + \infty} \Phi (x (t)) <   \Phi (x _ {0}).
$$

# 4 Convergence of the trajectories

In this section, in addition to the assumptions of the preceding section, $\Phi \in (\mathcal{H})$ and $\lambda > 0$ , we need to make further assumptions, of topological nature (precompactness of the HBF trajectory), or geometrical nature ( $\Phi$ convex), or differential nature (Morse functions), to obtain convergence of the trajectories as $t \to +\infty$ . In order to lighten the (HBF) equation, we shall suppose in this section that the gravity constant g is equal to 1, which is harmless since it amounts to replacing $\Phi$ by $g\Phi$ .

# 4.1 Morse functions

We first need to recall some classical notions related to the asymptotic behaviour of general dynamical systems.

For a given initial condition $y_{0}=(x_{0},\dot{x}_{0})\in H\times H$, let us denote $x_{y_{0}}(.)$, or shortly $x(.)$ when there is no ambiguity on $y_{0}$, the unique maximal solution

of (3.1): $\ddot{x}(t) + \lambda\dot{x}(t) + \nabla\Phi(x(t)) = 0$ with initial data $y_{0}$. The $\omega$ -limit set $\omega_{y_{0}}$ of the trajectory $x_{y_{0}}$ is defined by

$$
\omega_ {y _ {0}} = \bigcap_ {t > 0} \overline {{x _ {y _ {0}} ([ t , + \infty [)}}.
$$

The set $\omega_{y_{0}}$ can also be obtained as the set of the limit points of $x_{y_{0}}(.)$ as $t \to +\infty$

$$
\omega_ {y _ {0}} = \{\xi \in H: \exists (t _ {n}) _ {n \in \mathbf {N}}, \quad t _ {n} \to + \infty \quad \text {and} x (t _ {n}) \underset {n \to + \infty} {\longrightarrow} \xi \}.
$$

The set of the critical points of $\Phi$ is denoted by S

$$
S = \{x \in H: \nabla \Phi (x) = 0 \}.
$$

Proposition 4.1 Let us assume $\Phi \in \mathcal{H}$, $\lambda > 0$. Then, for any $y_0 = (x_0, \dot{x}_0) \in H \times H$ such that the trajectory $x_{y_0}$ is precompact for the topology of the norm in $H$ :

(i) $\omega_{y_{0}}$ is a compact connected non empty set in H,  
(ii) $\Phi$ is constant on $\omega_{y_0}$,  
(iii) $d(x_{y_0}(t),\omega_{y_0})\longrightarrow 0$ as $t\to +\infty$  
$(iv)\omega_{y_0}\subset S,$  
(v) $d(x_{y_0}(t),S)\longrightarrow 0$ as $t\to +\infty$

Proof. The proof is a mere variation of classical arguments on Liapunof functions and will be omitted (see e. g. [19]).

Statement $(v)$ is less precise than statement $(iii)$, but is easier to handle, since, practically, we have more information on the set S of critical points of $\Phi$ than on the $\omega$ -limit set of a trajectory.

In order to obtain convergence of the trajectories we need to make further assumptions on $\Phi$.

We recall that $\Phi:H\to R$ is a Morse function if $\Phi\in C^{2}$ and its Hessian $H_{\Phi}(\bar{x})$ possesses a continuous inverse at every critical point $\bar{x}$. It is a trivial result that all the critical points of a Morse function are isolated. We can now state

Theorem 4.1 Let H be a Hilbert space, and $\Phi: \mathcal{H} \to R$ a Morse function, with $\nabla\Phi$ Lipschitz continuous on bounded sets. For $y_{0} = (x_{0}, \dot{x}_{0}) \in H \times H$ , let $x be the solution of (HBF)

$$
\left\{ \begin{aligned} \ddot {x} (t) + \lambda \dot {x} (t) + \nabla \Phi (x (t)) &= 0 \\ x (0) &= x _ {0}, \dot {x} (0) = \dot {x} _ {0} \end{aligned} \right.
$$

For any $y_{0}$ such that the trajectory $x_{y_{0}}$ is precompact for the topology of the norm in H, then $x_{y_{0}}(t)$ converges as t goes to infinity to a critical point of $\Phi$.

Proof. By Proposition 4.1., we have that

$$
\omega_ {y _ {0}} \subset S,
$$

where $S = \{x \in H : \nabla \Phi(x) = 0\}$. By assumption, $\Phi$ is a Morse function, and all the elements of S are isolated. But $\omega_{y_{0}}$ is a connected set after Proposition 4.1. (i). So $\omega_{y_{0}}$ is a connected set contained in a set whose elements are all isolated. This implies that $\omega_{y_{0}}$ is reduced to a singleton, $\omega_{y_{0}} = \{\bar{x}\}$. The trajectory $x_{y_{0}}$ which is contained in a compact set, and which has a unique limit point necessarily converges to this unique element $\bar{x} \in S$. ☐

It is now natural to ask if the limit point $x_{\infty}$ of the trajectory $x(t)$ is a local minimum of $\Phi$ indeed. Let us first remark that this may not be the case when, for example, the initial position $x_{0}$ is a local maximum (or a saddle point) of $\Phi$, with an initial velocity equal to 0! However the mechanical interpretation of (HBF) allows to guess that such a situation is very exceptional. In fact, in the finite dimensional case, the limit point $x_{\infty}$ of (HBF) is, generically with respect to the initial condition $(x_{0}, \dot{x}_{0})$, a local minimum of $\Phi$. More precisely, the following can be shown:

Theorem 4.2 Under the assumptions of theorem 4.1, and for a finite dimensional space H, the set of initial conditions ensuring convergence of $x(t)$ towards a local minimum of $\Phi$, is an open dense subset of $H \times H$.

This property is important, because it validates the interest of (HBF) in relation to optimization. The ingredients of the proof are on the one hand the existence of a strict Liapunof function for (HBF), and on the other hand, the Hartman-Grobman theorem; the latter is a deep result claiming

that near an equilibrium point the behaviour of the solution of an ODE is, in some sense, equivalent to the behaviour of the flow corresponding to its linearized part (Perko [24]). Other results such as the “stable manifold theorem” (Chaperon-Coudray [13]) may also be used. For a more detailed presentation of the theorem above see Goudou [16].

# 4.2 $\Phi$ convex

In this section, H is a Hilbert space, $\Phi: \mathcal{H} \to R$ is a convex function which is $C^{1}$ , with $\nabla\Phi$ Lipschitz continuous on the bounded sets of H, and which satisfies: $\Phi$ isrom below and $S = \arg\min\Phi \neq \emptyset$ .

Note that, for a convex function $\Phi$, the critical points are the global minima of $\Phi$. Hence, S is a closed convex non-empty subset of H which may contain an infinite number of elements.

In the following theorem, which is due to F. Alvarez [2], it is established that each trajectory of the (HBF) system, in the convex case, weakly converges to a global minimum of $\Phi$. It is a deep result which presents striking similarities with the Brézis-Bruck convergence theorem for the continuous steepest descent method in the convex case. Indeed, in the next section, we shall justify the similarities between the two theorems, whose proofs both rely on the Opial lemma.

Theorem 4.3 Let H be a Hilbert space and $\Phi: \mathcal{H} \to R$ be a convex function which is $C^{1}$ , with $\nabla\Phi$ Lipschitz continuous on the bounded sets of H and which satisfies: $\Phi$ i from below and $S = \arg\min\Phi \neq \emptyset$ . Then, for all $x_{0} \in H$ , $\dot{x}_{0} \in H$ , the unique solution of the (HBF) system

$$
\left\{ \begin{aligned} \ddot {x} (t) + \lambda \dot {x} (t) + \nabla \Phi (x (t)) &= 0 \\ x (0) &= x _ {0}, \dot {x} (0) = \dot {x} _ {0} \end{aligned} \right.
$$

satisfies: there exists $\bar{x} \in \arg\min \Phi$ such that $x(t) \to \bar{x}$ weakly in $H$ as $t \to +\infty$. Moreover, $\lim_{t \to +\infty} \Phi(x(t)) = \min \Phi$.

Proof of theorem 4.3. For convenience of the reader, we give a self-contained proof which presents some slight variants with respect to the original paper [2]; in particular the hypothesis argmin $\Phi \neq \emptyset$ allows to get straightforward at the conclusion $\lim_{t\to+\infty}\Phi(x(t))=\min\Phi$.

The central idea is to prove the weak convergence of the trajectory $x(.)$ by using the Opial lemma [22]:

Lemma 4.1 (Opial) Let H be a Hilbert space and $x : [0, +\infty[ \to H$ be a function such that there exists a non void set $S \subset H$ which verifies :

(i) $\forall t_n \to +\infty$ with $x(t_n) \to \bar{x}$ weakly in $H$, we have $\bar{x} \in S$.

(ii) $\forall z\in S,\lim_{t\to +\infty}|x(t) - z|$ exists.

Then, $x(t)$ weakly converges as $t \to +\infty$ to some element $\bar{x}$ of $S$.

The proof of the Opial lemma is not complicated. Just notice that by (ii) the trajectory $x(.)$ is bounded. Let $x(t_{n}) \rightharpoonup z_{1}$ and $x(t_{m}) \rightharpoonup z_{2}$ be two weak limit points of the trajectory and prove that necessarily $z_{1} = z_{2}$ . Indeed, by i), $z_{1}$ and $z_{2}$ belong to S which, by ii), implies that

$$
\lim _ {t \to + \infty} | x (t) - z _ {1} | ^ {2} \quad \text {and} \quad \lim _ {t \to + \infty} | x (t) - z _ {2} | ^ {2} \quad \text {exist}.
$$

Hence

$$
\lim _ {t \to + \infty} (| x (t) - z _ {1} | ^ {2} - | x (t) - z _ {2} | ^ {2}) \quad \text {exists,}
$$

which, after simplification, yields

$$
\lim _ {t \to + \infty} \langle x (t), z _ {2} - z _ {1} \rangle \quad \text {exists.}
$$

Hence

$$
\lim _ {t _ {n} \to + \infty} \langle x (t _ {n}), z _ {2} - z _ {1} \rangle = \lim _ {t _ {m} \to + \infty} \langle x (t _ {m}), z _ {2} - z _ {1} \rangle
$$

that is,

$$
\langle z _ {1}, z _ {2} - z _ {1} \rangle = \langle z _ {2}, z _ {2} - z _ {1} \rangle .
$$

Equivalently, $|z_2 - z_1|^2 = 0$, i.e., $z_2 = z_1$. $\square$

Proof of theorem 4.3. continued. Let us apply the Opial lemma with

$$
S = \operatorname{argmin} \Phi = \{x \in H: \nabla \Phi (x) = 0 \}.
$$

The first property (i) is clearly satisfied: We know by theorem 3.1. that $\nabla \Phi(x(t)) \to 0$ as $t \to +\infty$. If $x(t_n) \rightharpoonup z$ weakly, by using the graph closedness property of the maximal monotone operator $\nabla \Phi$ in $w - H \times s - H$, we conclude that $\nabla \Phi(z) = 0$. Indeed, this can be obtained more elementary by noticing that

$$
\forall \xi \in H \quad \Phi (\xi) \geq \Phi (x (t _ {n})) + \langle \nabla \Phi (x (t _ {n})), \xi - x (t _ {n}) \rangle .
$$

By using the weak lower semicontinuity of the convex continuous function $\Phi$, and noticing that, in the duality bracket $\langle\nabla\Phi(x(t_{n})),\xi-x(t_{n})\rangle$, the two terms are respectively norm converging to zero and weakly convergent, we can pass to the lower limit to obtain

$$
\forall \xi \in H, \Phi (\xi) \geq \Phi (z),
$$

that is, $z \in \operatorname{argmin} \Phi = S$.

So, we just need to prove that for any $z \in S$, $\lim_{t \to +\infty} |x(t) - z|$ exists, or equivalently that $\lim_{t \to +\infty} |x(t) - z|^2$ exists.

Let us set $h(t) := \frac{1}{2} |x(t) - z|^2$. We have

$$
\begin{aligned} \dot {h} (t) &= \langle x (t) - z, \dot {x} (t) \rangle \\ \ddot {h} (t) &= | \dot {x} (t) | ^ {2} + \langle x (t) - z, \ddot {x} (t) \rangle . \\ \end{aligned}
$$

It follows that

$$
\ddot {h} (t) + \lambda \dot {h} (t) = | \dot {x} (t) | ^ {2} + \langle x (t) - z, \ddot {x} (t) + \lambda \dot {x} (t) \rangle .
$$

Since $x(.)$ is solution of (HBF)

$$
\ddot {x} (t) + \lambda \dot {x} (t) = - \nabla \Phi (x (t)).
$$

This, combined with the above equality, yields

$$
\ddot {h} (t) + \lambda \dot {h} (t) = | \dot {x} (t) | ^ {2} - \langle x (t) - z, \nabla \Phi (x (t)) \rangle . \tag {4.1}
$$

By assumption, we have $z \in S$ and $\nabla \Phi(z) = 0$. By monotonicity of $\nabla \Phi$,

$$
\langle x (t) - z, \nabla \Phi (x (t)) \rangle = \langle x (t) - z, \nabla \Phi (x (t)) - \nabla \Phi (z) \rangle \geq 0
$$

which yields

$$
\ddot {h} (t) + \lambda \dot {h} (t) \leq | \dot {x} (t) | ^ {2}. \tag {4.2}
$$

Let us now recall that $\dot{x} \in L^{2}(0, +\infty; H)$ (we just need to assume $\Phi$ bounded from below to obtain this property). We conclude thanks to the following lemma.

Lemma 4.2 Let $h \in \mathcal{C}^1(0, +\infty; \mathbf{R}^+)$ satisfy the following differential inequality

$$
\ddot {h} (t) + \lambda \dot {h} (t) \leq g (t)
$$

with $g \in L^{1}(0, +\infty; \mathbf{R}^{+})$. Then, $(\dot{h})_{+}$ the positive part of $\dot{h}$ belongs to $L^{1}(0, +\infty; \mathbf{R})$ and, as a consequence, $\lim_{t \to +\infty} h(t)$ exists.

Proof of lemma 4.2. Set $f(t) = \dot{h}(t)$. We have

$$
\dot {f} (t) + \lambda f (t) \leq g (t).
$$

Let us multiply this inequality by $e^{\lambda t}$ and integrate on (0,t) to obtain

$$
f (t) \leq e ^ {- \lambda t} f (0) + e ^ {- \lambda t} \int_ {0} ^ {t} e ^ {\lambda s} g (s) d s.
$$

Thus, by using the increasing property of the function $r \to r_{+} = \max(r, 0)$

$$
f _ {+} (t) \leq e ^ {- \lambda t} f (0) _ {+} + e ^ {- \lambda t} \int_ {0} ^ {t} e ^ {\lambda s} g (s) d s.
$$

Let us now notice that, by Fubini theorem

$$
\begin{aligned} \int_ {0} ^ {+ \infty} e ^ {- \lambda t} d t \int_ {0} ^ {t} e ^ {\lambda s} g (s) d s &= \int_ {0} ^ {+ \infty} d s \int_ {s} ^ {+ \infty} g (s) e ^ {\lambda s} e ^ {- \lambda t} d t \\ &= \frac {1}{\lambda} \int_ {0} ^ {+ \infty} g (s) d s <   + \infty . \\ \end{aligned}
$$

Hence, $f_{+}(t) = \dot{h}(t)_{+} \in L^{1}(0, +\infty)$.

It is now a standard argument to derive the convergence of $h(t)$ as $t \to +\infty$. Indeed, for any $0 < s < t < +\infty$

$$
\begin{aligned} h (t) - h (s) &= \int_ {s} ^ {t} \dot {h} (\tau) d \tau \\ &\leq \int_ {s} ^ {t} (\dot {h}) _ {+} (\tau) d \tau . \\ \end{aligned}
$$

It follows that

$$
h (t) - \int_ {0} ^ {t} (\dot {h}) _ {+} (\tau) d \tau \leq h (s) - \int_ {0} ^ {s} (\dot {h}) _ {+} (\tau) d \tau
$$

i.e. $t\to d(t):= h(t)-\int_{0}^{t}(\dot{h})_{+}(\tau)d\tau$ is a decreasing function.

Since $h \geq 0$ and $(\dot{h})_{+} \in L^{1}(0, +\infty; \mathbf{R})$, it follows that $d$ is minorized. Therefore $\lim_{t \to \infty} d(t)$ exists and $\lim_{t \to +\infty} h(t) = \lim_{t \to +\infty} d(t) + \int_{0}^{+\infty} (\dot{h})_{+}(\tau) d\tau$ exists too.

End of the proof of theorem 4.3. Let us complete the proof of theorem 4.3. and prove that $\lim_{t\to +\infty}\Phi (x(t)) = \min \Phi$.

For any $\xi\in H$, let us write the convexity inequality

$$
\Phi (\xi) \geq \Phi (x (t)) + \langle \nabla \Phi (x (t)), \xi - x (t) \rangle . \tag {4.3}
$$

Since $x(t) \to \bar{x}$ weakly in $H$ and $\nabla \Phi(x(t)) \to 0$ strongly in $H$, it follows that

$$
\Phi (\xi) \geq \operatorname * {l i m s u p} _ {t \to + \infty} \Phi (x (t)) \geq \operatorname * {l i m i n f} _ {t \to + \infty} \Phi (x (t)) \geq \Phi (\bar {x}).
$$

This being true for any $\xi \in H$, we conclude that

$$
\Phi (\bar {x}) = \min \Phi = \lim _ {t \to + \infty} \Phi (x (t)).
$$

It is worth completing the previous theorem by a strong convergence result when $\Phi$ is strongly convex.

Proposition 4.2 In addition to the assumptions of theorem 4.3., let us assume that $\Phi$ is strongly convex, that is, for any $R > 0$, there exists a function $\beta_{R}:\mathbf{R}^{+}\to \mathbf{R}^{+}$ with $\beta_R(t_n)\to 0\Longrightarrow t_n\to 0$, such that

$\forall x,y\in H\text{ with }|x|<R,|y|<R,$

$$
\langle \nabla \Phi (x) - \nabla \Phi (y), x - y \rangle \geq \beta_ {R} (| x - y |). \tag {4.4}
$$

Then each trajectory $x(.)$ of the HBF system is norm convergent as t goes to $+\infty$ to the unique global minimizer $\bar{x}$ of $\Phi$.

Proof of proposition 4.2. Let us give a direct proof of Proposition 4.2. which does not use the results of theorem 4.3. Let us consider a trajectory $x(.)$ of the (HBF) system. We already know that the trajectory is bounded. So, there exists some $R > 0$ such that for all $t \in [0, +\infty[$, $|x(t)| \leq R$. Since $\Phi$ is strongly convex, it has a unique minimizer say $\bar{x} = \arg\min \Phi$. Let us write the strong monotonicity property (4.4) at $\bar{x}$ and $x(t)$ :

$$
\langle \nabla \Phi (\bar {x}) - \nabla \Phi (x (t)), \bar {x} - x (t) \rangle \geq \beta_ {R} (| x (t) - \bar {x} |).
$$

Since $\nabla \Phi (\bar{x}) = 0$ and $\nabla \Phi (x(t)) = -\ddot{x} (t) - \lambda \dot{x} (t)$, it follows that

$$
\beta_ {R} (| x (t) - \bar {x} |) \leq \langle \ddot {x} (t) + \lambda \dot {x} (t), \bar {x} - x (t) \rangle . \tag {4.5}
$$

We already know, by theorem 3.1., that $\lim_{t\to +\infty}\dot{x} (t) = \lim_{t\to +\infty}\ddot{x} (t) = 0$ (note that, in order to obtain this result, in theorem 3.1., we don't really need to assume $\Phi$ to be coercive, we just use that the trajectories are bounded, which is precisely the case when $\Phi$ is convex with argmin $\Phi \neq \emptyset$ ). Since $x(.)$ is bounded, it follows from (4.5) that $\lim_{t\to +\infty}\beta_R(|x(t) - \bar{x}|) = 0$. From this we deduce that $x(t)\rightarrow \bar{x}$ strongly as $t\rightarrow +\infty$.

# 4.3 A counterexample

The asymptotic convergence, as the time t goes to $+\infty$, of the trajectories of the (HBF) system has been proved in various situations :

a) When H = R, in the unidimensional case, it follows from [19], example 2.2.6, that any bounded trajectory of the (HBF) system converges to a critical point of $\Phi$, just assuming $\Phi$ to be $C^{2}$ and minorized.  
b) The case of a Morse function, with precompact HBF trajectories, has been considered in theorem 4.1.  
c) When $\Phi$ is a convex function satisfying argmin $\Phi \neq \emptyset$, the weak convergence of the trajectories has been proved in theorem 4.3.

Indeed, it is a natural question to ask whether it is true that, at least in the finite-dimensional case, for any function $\Phi: R^{N} \rightarrow R$ which is smooth and coercive, all the trajectories of the (HBF) system asymptotically converge as t goes to $+\infty$.

In this section, we give a negative answer to this question by providing a counterexample. We are going to exhibit a function $\Phi: R^{2} \rightarrow R$ which is $C^{1}$, coercive, whose gradient is Lipschitz continuous on the bounded sets, and such that the (HBF) system

$$
\ddot {x} (t) + \lambda \dot {x} (t) + \nabla \Phi (x (t)) = 0 \tag {4.6}
$$

admits a solution $t \mapsto x(t)$ which does not converge as $t \to +\infty$.

Surprisingly, it is a quite involved construction. For pedagogical reasons and in order to avoid too long and technical developments, we omit some

proofs which are straight computations, and whose details can be found in Redont [26].

Indeed, it is difficult to give a direct analytic description of a function $\Phi: R^{2} \rightarrow R$ such that the associated (HBF) system admits a trajectory which does not converge as $t \rightarrow +\infty$. Therefore we adopt the opposite strategy :

We first construct a function $t \to x(t) \in \mathbf{R}^{2}$ which is bounded and which does not converge as $t \to +\infty$. Then, we look for a function $\Phi : R^{2} \to R$ such that $t \to x(t)$ is a trajectory of the corresponding (HBF) system. This can be seen as an inverse problem method.

We choose for $x(.)$ the spiral $S$

$$
t \in ] 1, + \infty [ \rightarrow x (t) := \bar {x} (\log t) \tag {4.7}
$$

where $\bar{x}$ is defined by

$$
\theta \in ] 0, + \infty [ \rightarrow \bar {x} (\theta) = \left(\left(1 + \frac {1}{\theta}\right) \cos \theta , \left(1 + \frac {1}{\theta}\right) \sin \theta\right). \tag {4.8}
$$

The parametrization $\theta = \log t$ has been chosen in order to obtain $\dot{x} \in L^2(0, +\infty; \mathbf{R}^2)$. Let us recall that this property has to be satisfied by all the trajectories of any (HBF) system, just assuming that $\Phi$ is bounded from below.

Clearly, the trajectory $x(.)$ admits the unit circle as a limit cycle. Since the trajectory $t \to x(t)$ is given, we also know $\dot{x}(t)$ and $\ddot{x}(t)$. From

$$
\nabla \Phi (x (t)) = - \ddot {x} (t) - \lambda \dot {x} (t) \tag {4.9}
$$

we also know $\nabla\Phi$ on the spiral S.

On the other hand, from (4.8)

$$
\begin{aligned} \frac {d}{d t} \Phi (x (t)) &= \langle \nabla \Phi (x (t)), \dot {x} (t) \rangle \\ &= \langle - \ddot {x} (t) - \lambda \dot {x} (t), \dot {x} (t) \rangle \\ &= - \lambda | \dot {x} (t) | ^ {2} - \frac {1}{2} \frac {d}{d t} | \dot {x} (t) | ^ {2}. \\ \end{aligned}
$$

By integration of this inequality from $t_0$ to $t$

$$
\Phi (x (t)) = \Phi (x (t _ {0})) - \frac {1}{2} | \dot {x} (t) | ^ {2} - \lambda \int_ {t _ {0}} ^ {t} | \dot {x} (s) | ^ {2} d s + \frac {1}{2} | \dot {x} (t _ {0}) | ^ {2}. \tag {4.10}
$$

Let us notice that $\Phi$ is defined up to an additive constant by (4.10). So, we may take for $\Phi$

$$
\Phi (x (t)) = - \frac {1}{2} | \dot {x} (t) | ^ {2} + \lambda \int_ {t} ^ {+ \infty} | \dot {x} (s) | ^ {2} d s \tag {4.11}
$$

and then observe that $\Phi$ and $\nabla\Phi$ are completely defined along the trajectory S (of equation $t \rightarrow x(t)$ ) by the formulae (4.9) and (4.11).

Our problem is to reconstruct $\Phi$ on the whole of $R^{2}$, just using that $\Phi$ and $\nabla\Phi$ are known on S. To do that, we use the polar coordinates r and $\theta$ and notice that

$$
\begin{array}{l} \frac {\partial \Phi}{\partial r} (x (t)) = \langle \nabla \Phi (x (t)), \frac {x (t)}{| x (t) |} \rangle \\ = \langle - \ddot {x} (t) - \lambda \dot {x} (t), w (t) \rangle \\ \end{array}
$$

where $w(t) := \frac{x(t)}{|x(t)|}$.

Conversely, let us verify that the two relations

$$
\frac {\partial \Phi}{\partial r} (x (t)) = \langle - \ddot {x} (t) - \lambda \dot {x} (t), w (t) \rangle \tag {4.12}
$$

$$
\Phi (x (t)) = - \frac {1}{2} | \dot {x} (t) | ^ {2} + \lambda \int_ {t} ^ {+ \infty} | \dot {x} (s) | ^ {2} d s \tag {4.13}
$$

imply that $x(t)$ is a solution of the (HBF) system (4.6). By derivation of (4.13), we obtain

$$
\langle \nabla \Phi (x (t)), \dot {x} (t) \rangle = \langle - \ddot {x} (t) - \lambda \dot {x} (t), \dot {x} (t) \rangle . \tag {4.14}
$$

On the other hand, (4.12) can be written as

$$
\langle \nabla \Phi (x (t)), w (t) \rangle = \langle - \ddot {x} (t) - \lambda \dot {x} (t), w (t) \rangle . \tag {4.15}
$$

Since $\dot{x}(t)$ and $w(t)=\frac{x(t)}{|x(t)|}$ are linearly independent (this fact is checked by computing $\dot{x}(t)$ and $w(t)$ ), it follows from (4.14) and (4.15) that

$$
\nabla \Phi (x (t)) = - \ddot {x} (t) - \lambda \dot {x} (t)
$$

and, as a consequence, $x(.)$ is a solution of (HBF) system.

Let us introduce

$$
\varphi (t) := - \frac {1}{2} | \dot {x} (t) | ^ {2} + \lambda \int_ {t} ^ {+ \infty} | \dot {x} (s) | ^ {2} d s
$$

and

$$
\delta (t) := \langle - \ddot {x} (t) - \lambda \dot {x} (t), w (t) \rangle .
$$

The system we have to solve is

$$
\Phi (x (t)) = \varphi (t) \tag {4.16}
$$

$$
\frac {\partial \Phi}{\partial r} (x (t)) = \delta (t). \tag {4.17}
$$

Let us write $\varphi(t)=\bar{\varphi}(\log t)$ and $\delta(t)=\bar{\delta}(\log t)$, the system (4.16), (4.17) turns to be equivalent to

$$
\Phi (\bar {x} (\theta)) = \bar {\varphi} (\theta) \tag {4.18}
$$

$$
\frac {\partial \Phi}{\partial r} (\bar {x} (\theta)) = \bar {\delta} (\theta). \tag {4.19}
$$

We have to find $\Phi:R^{2}\to R$ which is sufficiently smooth ( $C^{1}$ with $\nabla\Phi$ Lipschitz continuous on the bounded sets) and which takes prescribed values and prescribed radial derivatives on the spiral S. In figure (3) are represented the elements allowing to reconstruct $\Phi$.

First we define $\Phi$ satisfying (4.18) and (4.19) on an outer neighbourhood of the unit circle. It is enough to define $\Phi$ on every radius issuing from O. Let $A(1 + \frac{1}{\theta}, \theta)$ and $B(1 + \frac{1}{\theta - 2\pi}, \theta)$ be two consecutive points on the intersection of the spiral S with such a radius. The values of $\Phi$ and $\frac{\partial\Phi}{\partial r}$ are known at points A and B:

$$
\Phi (A) = \bar {\varphi} (\theta), \Phi (B) = \bar {\varphi} (\theta - 2 \pi), \frac {\partial \Phi}{\partial r} (A) = \bar {\delta} (\theta), \frac {\partial \Phi}{\partial r} (B) = \bar {\delta} (\theta - 2 \pi).
$$

If $M(r, \theta)$ ( $1 + \frac{1}{\theta} < r < 1 + \frac{1}{\theta - 2\pi}$ ) is a point of segment $AB$, it is natural to define $\Phi(M)$ as the value at point $M$ of the Hermite interpolation polynomial defined by the prescribed values of $\Phi$ and $\frac{\partial \Phi}{\partial r}$ at points $A$ and $B$. Namely, if we set $\rho = \frac{\theta - 2\pi}{2\pi}[\theta(r - 1) - 1]$ :

$$
\begin{aligned} \Phi (M) &= \bar {\varphi} (\theta) H (\rho) + \bar {\varphi} (\theta - 2 \pi) H (1 - \rho) \\ + \frac {2 \pi}{\theta (\theta - 2 \pi)} [ \bar {\delta} (\theta) K (\rho) - \bar {\delta} (\theta - 2 \pi) K (1 - \rho) ], \\ \end{aligned}
$$

![](images/1059e19de4f31df67990286f6595ba323dcf8c429a851c4ff816d394b1ce9e2e.jpg)

<details>
<summary>natural_image</summary>

Blank white image with no visible content, text, or symbols
</details>

Figure 3: The data allowing to reconstruct $\Phi$

where $H$ and $K$ are the basic Hermite interpolation polynomials on segment $[0,1]$ :

$$
H (x) = (1 - x) ^ {2} (2 x + 1), K (x) = (1 - x) ^ {2} x.
$$

This defines $\Phi$ on, say, the annulus $1 < r < 1 + 1/4\pi$ ; further $\Phi$ is extended by $\Phi \equiv 0$ on the unit disk. Verifying that $\Phi$ has a gradient which is Lipschitz continuous on the disk $r < 1 + 1/4\pi$ is somewhat lengthy; details are to be found in [26]. Finally $\Phi$ can be extended radially to the whole of $R^{2}$ while retaining its regularity properties.

To help visualize the function $\Phi$, we give below, figure (4), a wireframe representation of the surface it defines in $R^{3}$.

Note that our function $\Phi$ is not $C^{2}$ ; its second derivatives need not be continuous when crossing the spiral S. Maybe to exhibit a $\Phi$ which is $C^{\infty}$ is not so easy.

Yet in the case of the gradient system (SD) we know of a $C^{\infty}$ potential $\Phi: R^{2} \rightarrow R$ with a non-convergent trajectory; see Palis-de Melo [23] p. 14, and observe that the trajectory likely is unique and instable. It is easy to modify that potential, while retaining its $C^{\infty}$ regularity, so as to get a whole family of solutions of (SD) which do not converge; see [26]. To get an idea

![](images/7973dfe13be0f2888596ee0a246dfcae1051fa526813a48d56c05eecee74d85d.jpg)

<details>
<summary>natural_image</summary>

Blank white image with no visible content, text, or symbols
</details>

Figure 4: A glimpse at $\Phi$

of that potential imagine a furrow winding down around the unit circle and which traps (SD) trajectories.

Nevertheless this function has been of no use as a counterexample for the (HBF) equation because, in that case, we were unable to exhibit a trajectory which remains in the furrow.

# 5 The steepest descent as a limit case of the heavy ball with friction

In section 2, the heavy ball with friction dynamical system (HBF) has been introduced with its two mechanical parameters $\lambda$ (friction) and g (gravity):

$$
\ddot {x} (t) + \lambda \dot {x} (t) + g \nabla \Phi (x (t)) = 0 \tag {5.1}
$$

Let us take $\lambda = g$ and examine the situation $\lambda \to +\infty$. Let us introduce $\lambda = \frac{1}{\varepsilon}$, with $\varepsilon \to 0$ ; the equation (5.1) becomes

$$
\varepsilon \ddot {x} (t) + \dot {x} (t) + \nabla \Phi (x (t)) = 0. \tag {5.2}
$$

Formally, one may expect that the solutions of the above system converge as $\varepsilon \rightarrow 0$ to the corresponding solutions of the steepest descent system

$$
\dot {x} (t) + \nabla \Phi (x (t)) = 0.
$$

This is a singular perturbation problem, since one passes from a second order differential system to a first order one. Singular perturbation problems for hyperbolic partial differential equations are extensively addressed in the literature; cf. e.g. Lions [21], and Hale-Raugel [18] for the convergence of attractors. Let us first state a convergence result which holds for a general $\Phi$.

Theorem 5.1 Let us assume that $\Phi : H \to \mathbf{R}$ is a $\mathcal{C}^1$ function, bounded from below, with compact sublevel sets, and such that $\nabla \Phi$ is Lipschitz continuous on bounded sets. For any Cauchy data $x_0 \in H$, $\dot{x}_0 \in H$ and for any $\varepsilon > 0$ let $x_{\varepsilon}$ denote the unique global solution of the $(HBF)_\varepsilon$ system

$$
(\mathrm{HBF}) _ {\varepsilon} \qquad \varepsilon \ddot {x} _ {\varepsilon} (t) + \dot {x} _ {\varepsilon} (t) + \nabla \Phi (x _ {\varepsilon} (t)) = 0, x _ {\varepsilon} (0) = x _ {0}, \dot {x} _ {\varepsilon} (0) = \dot {x} _ {0}.
$$

a) When $\varepsilon \to 0$, the sequence $(x_{\varepsilon})_{\varepsilon \to 0}$ converges uniformly on $[0,T]$ for all $T > 0$ to the unique solution $x$ of (SD)

$$
\dot {x} (t) + \nabla \Phi (x (t)) = 0, \quad x (0) = x _ {0}. \tag {SD}
$$

Moreover, $\dot{x}_{\varepsilon} \rightarrow \dot{x}$ weakly in $L^{2}(0, +\infty; H)$ and strongly in $L^{2}(0, T; H)$ for any $T < +\infty$.

b) If in addition $\Phi$ is $\mathcal{C}^2$ then $\varepsilon \ddot{x}_{\varepsilon}\to 0$ strongly in $L^2 (0, + \infty ;H)$.

Proof of theorem 5.1.

a) According to theorem 3.1, for every $\varepsilon > 0$, the system $(\mathrm{HBF})_{\varepsilon}$ does possess a unique global $\mathcal{C}^2$ solution $x_{\varepsilon}: [0, +\infty[\to H]$. Similarly, one could show that (SD) has a unique global $\mathcal{C}^1$ solution $x: [0, +\infty[\to H]$.

The energy equation for $(\mathrm{HBF})_{\varepsilon}$ :

$$
\frac {\varepsilon}{2} | \dot {x} _ {\varepsilon} (t) | ^ {2} + \Phi (x _ {\varepsilon} (t)) + \int_ {0} ^ {t} | \dot {x} _ {\varepsilon} (s) | ^ {2} d s = \frac {\varepsilon}{2} | \dot {x} _ {0} | ^ {2} + \Phi (x _ {0}) \tag {5.3}
$$

yields the following uniform bounds:

$$
\sup_{\substack{0 <   \varepsilon \leq 1\\ t\in [0, + \infty [}}\Phi (x_{\varepsilon}(t)) <   + \infty , \tag{5.4}
$$

$$
\sup _ {0 <   \varepsilon \leq 1} \int_ {0} ^ {+ \infty} | \dot {x} _ {\varepsilon} (t) | ^ {2} d t \leq C, \text {for some} C > 0. \tag {5.5}
$$

Since $\Phi$ has compact sublevel sets, (5.4) shows that the ranges of the $(x_{\varepsilon})_{0 < \varepsilon \leq 1}$ family lie within a compact set of $H$.

As a consequence of (5.5), the $(\dot{x}_{\varepsilon})_{0<\varepsilon\leq1}$ family is a bounded set in $L^{2}(0,+\infty;H)$ and the $(x_{\varepsilon})_{0<\varepsilon\leq1}$ family is equicontinuous in $\mathcal{C}([0,+\infty[;H)$ (note: $|x_{\varepsilon}(t)-x_{\varepsilon}(s)|\leq\int_{s}^{t}|\dot{x}_{\varepsilon}(\tau)|d\tau\leq\sqrt{C(t-s)}$ for any $0\leq s\leq t$ ).

Fix $T > 0$. Resorting to Ascoli's theorem in $\mathcal{C}([0,T];H)$ and the weak relative compactness of bounded sets in $L^2 (0, +\infty ;H)$ we may assert the existence of a sequence $(x_{\varepsilon_{\nu}})_{\nu \in \mathcal{N}}$ with $\varepsilon_{\nu}\to 0,\nu \rightarrow +\infty$ and of limit points $u\in \mathcal{C}([0,T];H)$ and $v\in L^{2}(0, + \infty ;H)$ such that:

- $x_{\varepsilon_{\nu}} \to u$ in $\mathcal{C}([0,T];H)$ equipped with the uniform convergence norm,  
- $\dot{x}_{\varepsilon_{\nu}} \to v$ weakly in $L^2(0, +\infty; H)$,  
- $v_{||0,T|} = u'$ the distribution derivative of $u$.

Now as a distribution sequence: $\ddot{x}_{\varepsilon_{\nu}} \rightarrow v'$, hence $\varepsilon_{\nu}\ddot{x}_{\varepsilon_{\nu}} \rightarrow 0$. Passing to the limit in $(\mathrm{HBF})_{\varepsilon}$ we get: $u' + \nabla\Phi(u) = 0$. So $u'$ is a continuous function and therefore is the classical derivative of u. Thus u is $C^{1}$ and satisfies (SD) on the interval $[0, T]$ (note: $u(0) = \lim x_{\varepsilon_{\nu}}(0) = x_{0}$ ); hence u coincides with x, the solution of (SD) on $[0, T]$, and $v = \dot{x}$.

Summing up, the family $(x_{\varepsilon})_{0<\varepsilon\leq1}$ has exactly one limit point in $\mathcal{C}([0,T];H)$ as $\varepsilon\to0$, namely $x_{|[0,T]}$ and furthermore $\dot{x}_{\varepsilon}\to\dot{x}$ weakly in $L^{2}(0,+\infty;H)$, as was to be proved.

To complete the proof of part $(a)$, we just need to prove that the convergence of $\dot{x}_{\varepsilon}$ to $\dot{x}$ holds for the norm convergence of $L^{2}(0,T;H)$ for any $0 \leq T < +\infty$. Let us return to (5.3)

$$
\int_ {0} ^ {t} | \dot {x} _ {\varepsilon} (s) | ^ {2} d s \leq \frac {\varepsilon}{2} | \dot {x} _ {0} | ^ {2} + \Phi (x _ {0}) - \Phi (x _ {\varepsilon} (t)). \tag {5.6}
$$

We know that $x_{\varepsilon}(t)\to x(t)$ strongly in $H$ as $\varepsilon \rightarrow 0$. By continuity of $\Phi$

$$
\Phi (x _ {\varepsilon} (t)) \rightarrow \Phi (x (t)) \quad \text {as} \varepsilon \rightarrow 0. \tag {5.7}
$$

From (5.6) and (5.7) we conclude that

$$
\operatorname * {l i m s u p} _ {\varepsilon \to 0} \int_ {0} ^ {t} | \dot {x} _ {\varepsilon} (s) | ^ {2} \leq \Phi (x _ {0}) - \Phi (x (t)). \tag {5.8}
$$

On the other hand, since x is the solution of $\dot{x} + \nabla\Phi(x) = 0$, $x(0) = x_{0}$, we have

$$
\int_ {0} ^ {t} | \dot {x} (s) | ^ {2} d s = \Phi (x _ {0}) - \Phi (x (t)). \tag {5.9}
$$

From (5.8) and (5.9), we have

$$
\operatorname * {l i m s u p} _ {\varepsilon \to 0} \int_ {0} ^ {t} | \dot {x} _ {\varepsilon} (s) | ^ {2} d s \leq \int_ {0} ^ {t} | \dot {x} (s) | ^ {2} d s
$$

which, combined with the weak convergence of $\dot{x}_{\varepsilon}$ to $\dot{x}$ in $L^{2}(0,T;H)$ yields that

$$
\forall T <   + \infty \quad \dot {x} _ {\varepsilon} \to \dot {x} \quad \text {strongly in} L ^ {2} (0, T; H).
$$

b) Let us take the derivative of (5.2) with respect to $t$,

$$
\varepsilon \ddot {x} _ {\varepsilon} (t) + \ddot {x} _ {\varepsilon} (t) + H _ {\Phi} (x _ {\varepsilon} (t)) \dot {x} _ {\varepsilon} (t) = 0
$$

and put $u_{\varepsilon}(t) = \ddot{x}_{\varepsilon}(t)$. We have

$$
\varepsilon \dot {u} _ {\varepsilon} (t) + u _ {\varepsilon} (t) = f _ {\varepsilon} (t) \tag {5.10}
$$

with

$$
f _ {\varepsilon} (t) = - H _ {\Phi} (x _ {\varepsilon} (t)) \dot {x} _ {\varepsilon} (t). \tag {5.11}
$$

Recall that the $(x_{\varepsilon}(t))_{0<\varepsilon\leq1,t\geq0}$ lie within a compact set of H, then from (5.5) and the continuity of $H_{\Phi}$ it follows that

$$
\sup _ {0 <   \varepsilon \leq 1} \int_ {0} ^ {+ \infty} | f _ {\varepsilon} (t) | ^ {2} d t <   + \infty . \tag {5.12}
$$

By taking the scalar product of (5.10) with $u_{\varepsilon}(t)$, we obtain

$$
\frac {\varepsilon}{2} \frac {d}{d t} | u _ {\varepsilon} (t) | ^ {2} + | u _ {\varepsilon} (t) | ^ {2} = \langle f _ {\varepsilon} (t), u _ {\varepsilon} (t) \rangle ,
$$

which, by integration from 0 to t, gives

$$
\frac {\varepsilon}{2} | u _ {\varepsilon} (t) | ^ {2} + \int_ {0} ^ {t} | u _ {\varepsilon} (s) | ^ {2} d s = \int_ {0} ^ {t} \langle f _ {\varepsilon} (s), u _ {\varepsilon} (s) \rangle d s + \frac {\varepsilon}{2} | u _ {\varepsilon} (0) | ^ {2}.
$$

After multiplication by $\varepsilon$ and application of the Cauchy-Schwartz inequality we obtain

$$
\begin{array}{l} \frac {\varepsilon^ {2}}{2} | u _ {\varepsilon} (t) | ^ {2} + \varepsilon \int_ {0} ^ {t} | u _ {\varepsilon} (s) | ^ {2} d s \\ \leq \varepsilon \left(\int_ {0} ^ {t} | f _ {\varepsilon} (s) | ^ {2} d s\right) ^ {1 / 2} \left(\int_ {0} ^ {t} | u _ {\varepsilon} (s) | ^ {2} d s\right) ^ {1 / 2} + \frac {\varepsilon^ {2}}{2} | u _ {\varepsilon} (0) | ^ {2} \\ \leq \frac {\varepsilon}{2} \int_ {0} ^ {t} | f _ {\varepsilon} (s) | ^ {2} d s + \frac {\varepsilon}{2} \int_ {0} ^ {t} | u _ {\varepsilon} (s) | ^ {2} d s + \frac {\varepsilon^ {2}}{2} | u _ {\varepsilon} (0) | ^ {2} \\ \end{array}
$$

After simplification

$$
\frac {\varepsilon^ {2}}{2} | u _ {\varepsilon} (t) | ^ {2} + \frac {\varepsilon}{2} \int_ {0} ^ {t} | u _ {\varepsilon} (s) | ^ {2} d s \leq \frac {\varepsilon}{2} \int_ {0} ^ {t} | f _ {\varepsilon} (s) | ^ {2} d s + | \varepsilon u _ {\varepsilon} (0) | ^ {2}.
$$

Let us now observe that, by (5.2),

$$
\begin{aligned} \varepsilon u _ {\varepsilon} (0) &= \varepsilon \ddot {x} _ {\varepsilon} (0) = - \dot {x} _ {\varepsilon} (0) - \nabla \Phi (x _ {\varepsilon} (0)) \\ &= - \dot {x} _ {0} - \nabla \Phi (x _ {0}). \\ \end{aligned}
$$

Hence,

$$
\frac {1}{2} | \varepsilon u _ {\varepsilon} (t) | ^ {2} + \frac {\varepsilon}{2} \int_ {0} ^ {t} | u _ {\varepsilon} (s) | ^ {2} d s \leq \frac {\varepsilon}{2} \int_ {0} ^ {+ \infty} | f _ {\varepsilon} (s) | ^ {2} d s + \frac {1}{2} | \dot {x} _ {0} + \nabla \Phi (x _ {0}) | ^ {2}. (5. 1 3)
$$

From (5.12) and (5.13), we deduce that

$$
\begin{aligned} \sup \quad | \varepsilon \ddot {x} _ {\varepsilon} (t) | &<   + \infty \tag {5.14} \\ t &\in [ 0, + \infty [ \begin{array}{c} 0 <   \varepsilon \leq 1 \end{aligned} ] \\ \end{array}
$$

$$
\sup _ {0 <   \varepsilon \leq 1} \varepsilon \int_ {0} ^ {+ \infty} | \ddot {x} _ {\varepsilon} (t) | ^ {2} d t <   + \infty . \tag {5.15}
$$

From (5.15), it follows that

$$
\int_ {0} ^ {+ \infty} | \varepsilon \ddot {x} _ {\varepsilon} (t) | ^ {2} d t = \varepsilon \int_ {0} ^ {+ \infty} \varepsilon | \ddot {x} _ {\varepsilon} (t) | ^ {2} d t \underset {\text {as} \varepsilon \to 0} {\longrightarrow} 0.
$$

Equivalently,

$$
\varepsilon \ddot {x} _ {\varepsilon} \rightarrow 0 \quad \text {strongly in} L ^ {2} (0, + \infty ; H) \text {as} \varepsilon \rightarrow 0. \quad \square \tag {5.16}
$$

Remark: It can be easily seen that, without any further assumptions on $\Phi$, the conclusions of theorem 5.1. are nearly optimal. One cannot in general expect the sequence $(x_{\varepsilon})$ to converge uniformly on the whole interval $[0, +\infty[$. Take $H = \mathbf{R}$, $\Phi(x) = (x^2 - 1)^2$. Clearly $\nabla \Phi(x) = 0$ at $x = 0$ and $x = \pm 1$. Take $x_0 = 0$, the solution of the (SD) system is $x \equiv 0$. When $\dot{x}_0 > 0$, the solution $x_{\varepsilon}$ of the $(\mathrm{HBF})_{\varepsilon}$ system verifies

$$
\lim _ {t \to + \infty} x _ {\varepsilon} (t) = + 1.
$$

One can verify that the uniform convergence of $(x_{\varepsilon})_{\varepsilon\to0}$ to x holds on all bounded intervals $[0,T]$, $T<+\infty$, but not on $[0,+\infty[$, because

$$
\sup _ {t \in [ 0, + \infty [} | x _ {\varepsilon} (t) - x (t) | \to 1 \quad \text {as} \varepsilon \to 0. \quad \square
$$

We are now going to examine the convex case and prove that, in this case, the sequence $(x_{\varepsilon})$ of the $(\mathrm{HBF})_{\varepsilon}$ system converges uniformly on $[0,+\infty[$ to the solution x of the (SD) system.

Theorem 5.2 Let us assume that $\Phi : H \to \mathbf{R}$ is convex, $\mathcal{C}^1$, minorized with $\nabla \Phi$ Lipschitz continuous on bounded sets. For any Cauchy data $x_0 \in H$, $\dot{x}_0 \in H$ and for any $\varepsilon > 0$, let $x_\varepsilon$ be the solution of

$$
\varepsilon \ddot {x} _ {\varepsilon} + \dot {x} _ {\varepsilon} + \nabla \Phi (x _ {\varepsilon}) = 0, x _ {\varepsilon} (0) = x _ {0}, \dot {x} _ {\varepsilon} (0) = \dot {x} _ {0}.
$$

a) When $\varepsilon$ goes to zero, the sequence $(x_{\varepsilon})_{\varepsilon \to 0}$ converges uniformly on $[0, +\infty[$ to $x$ the unique solution of the (SD) system

$$
\dot {x} + \nabla \Phi (x) = 0, x (0) = x _ {0}.
$$

Moreover, the following estimation holds: there exists some constant $C \in \mathbf{R}^{+}$ such that

$$
\| x _ {\varepsilon} - x \| _ {L ^ {\infty} (0, + \infty ; H)} \leq C \sqrt {\varepsilon}.
$$

b) Let us assume in addition that $argmin\Phi \neq \emptyset$ and set $x_{\varepsilon}(\infty) = w - \lim_{t \to +\infty} x_{\varepsilon}(t)$ ; then:

$b1) x(\infty) = w - \lim_{t\to +\infty}x(t)\text{exists},$  
$b2) x_{\varepsilon}(\infty) \to x(\infty)$ strongly in $H$ as $\varepsilon \to 0$,  
$b\mathcal{B})\dot{x}_{\varepsilon}\to \dot{x}\text{ in} L^{2}(0, + \infty ;H)\text{ as }\varepsilon \rightarrow 0.$

Remark: Point $(b1)$ is a theorem of Brézis and Bruck [11, 12].

Proof:

a) We have $\nabla\Phi(x_{\varepsilon})=-\varepsilon\ddot{x}_{\varepsilon}-\dot{x}_{\varepsilon}$ and $\nabla\Phi(x)=-\dot{x}$. By monotonicity of $\nabla\Phi$,

$$
\langle - \varepsilon \ddot {x} _ {\varepsilon} - \dot {x} _ {\varepsilon} + \dot {x}, x _ {\varepsilon} - x \rangle \geq 0.
$$

Equivalently,

$$
\frac {1}{2} \frac {d}{d t} | x _ {\varepsilon} - x | ^ {2} + \varepsilon \langle \ddot {x} _ {\varepsilon}, x _ {\varepsilon} - x \rangle \leq 0.
$$

Let us integrate this inequality from 0 to $t$, and notice that $x_{\varepsilon}(0) = x(0)$,

$$
\frac {1}{2} | x _ {\varepsilon} (t) - x (t) | ^ {2} + \varepsilon \int_ {0} ^ {t} \langle \ddot {x} _ {\varepsilon} (s), x _ {\varepsilon} (s) - x (s) \rangle d s \leq 0. \tag {5.17}
$$

Let us make an integration by parts on $(5.17)$. We obtain:

$$
\frac {1}{2} | x _ {\varepsilon} (t) - x (t) | ^ {2} + \varepsilon \langle x _ {\varepsilon} (t) - x (t), \dot {x} _ {\varepsilon} (t) \rangle \leq \varepsilon \int_ {0} ^ {t} \langle \dot {x} _ {\varepsilon} (s) - \dot {x} (s), \dot {x} _ {\varepsilon} (s) \rangle d s. \tag {5.18}
$$

Let us now observe that the energy estimate on $(\mathrm{HBF})_{\varepsilon}$ yields (see (5.3)) the existence of some constant C, independent of $\varepsilon$, such that

$$
\left| \varepsilon \dot {x} _ {\varepsilon} (t) \right| \leq C \sqrt {\varepsilon} \quad \text {for all} t \in [ 0, + \infty [ \quad \text {and} 0 <   \varepsilon \leq 1. \tag {5.19}
$$

On the other hand, the same energy estimate on $(\mathrm{HBF})_{\varepsilon}$ yields (see (5.5))

$$
\sup _ {0 <   \varepsilon \leq 1} \left(\int_ {0} ^ {+ \infty} | \dot {x} _ {\varepsilon} (t) | ^ {2} d t\right) \leq C \quad \text {for some} C <   + \infty .
$$

Furthermore, $\dot{x}$ is in $L^{2}(0,+\infty;H)$ (indeed $\frac{1}{2}\|\dot{x}\|_{L^{2}(0,+\infty;H)}^{2}\leq\Phi(x_{0})-inf\Phi$ from the energy equation for (SD)). Hence the inequalities:

$$
\int_ {0} ^ {t} \langle \dot {x} _ {\varepsilon} (s) - \dot {x} (s), \dot {x} _ {\varepsilon} (s) \rangle d s \leq \int_ {0} ^ {t} | \dot {x} _ {\varepsilon} (t) | ^ {2} d t + \left(\int_ {0} ^ {t} | \dot {x} _ {\varepsilon} (t) | ^ {2} d t\right) ^ {1 / 2} \left(\int_ {0} ^ {t} | \dot {x} | ^ {2} d t\right) ^ {1 / 2}
$$

$$
\int_ {0} ^ {t} \langle \dot {x} _ {\varepsilon} (s) - \dot {x} (s), \dot {x} _ {\varepsilon} (s) \rangle d s \leq C \tag {5.20}
$$

for some $C > 0$ and for every $t > 0$ and $\varepsilon > 0$.

Combining (5.18) with the two above estimations (5.19) and (5.20), we obtain

$$
\frac {1}{2} | x _ {\varepsilon} (t) - x (t) | ^ {2} \leq C \sqrt {\varepsilon} | x _ {\varepsilon} (t) - x (t) | + C \varepsilon , f o r 0 <   \varepsilon \leq 1.
$$

Whence it is elementary to conclude that there exists some constant C (we use the same letter for simplicity) such that

$$
\| x _ {\varepsilon} - x \| _ {L ^ {\infty} (0, + \infty ; H)} \leq C \sqrt {\varepsilon}. \tag {5.21}
$$

And point (a) is proved.

b) Let us now assume that $\arg\min\Phi \neq \emptyset$. We know, by theorem 4.3., that, for any $\varepsilon > 0$, $w - \lim_{t \to +\infty} x_{\varepsilon}(t) := x_{\varepsilon}(\infty)$ exists and that $x_{\varepsilon}(\infty) \in \arg\min\Phi$. Let us show how, by combining theorem 4.3 with the estimation (5.21), one can derive the Brézis-Bruck theorem ([11, 12]), that is the weak convergence of $x(t)$ as $t \to +\infty$. For any $z \in H$, for any $\varepsilon > 0$ and for any $0 < s \leq t < +\infty$,

$$
\langle x (t) - x (s), z \rangle = \langle x (t) - x _ {\varepsilon} (t), z \rangle + \langle x _ {\varepsilon} (t) - x _ {\varepsilon} (s), z \rangle + \langle x _ {\varepsilon} (s) - x (s), z \rangle .
$$

From (5.21), we see that

$$
| \langle x (t) - x (s), z \rangle | \leq 2 C \sqrt {\varepsilon} | z | + \langle x _ {\varepsilon} (t) - x _ {\varepsilon} (s), z \rangle .
$$

By theorem 4.3., the weak-limit of $x_{\varepsilon}(t)$ as $t \to +\infty$ exists. Hence

$$
\limsup _ {s, t \to + \infty} | \langle x (t) - x (s), z \rangle | \leq 2 C \sqrt {\varepsilon} | z |.
$$

This being true for any $\varepsilon > 0$, we obtain that for any $z \in H$, $\lim_{t \to +\infty} \langle x(t), z \rangle$ exists ( $t \to \langle x(t), z \rangle$ is a Cauchy net indeed). This implies, owing to the uniform boundedness principle, that $w - \lim_{t \to +\infty} x(t) := x(\infty)$ exists. And so is point (b1) proved.

From (5.21), we have

$$
\left| x _ {\varepsilon} (t) - x (t) \right| \leq C \sqrt {\varepsilon}.
$$

When t goes to $+\infty$, $x_{\varepsilon}(t)-x(t)$ weakly converges to $x_{\varepsilon}(\infty)-x(\infty)$. By the lower semicontinuity for the weak topology of the norm in H, we deduce that

$$
\left| x _ {\varepsilon} (\infty) - x (\infty) \right| \leq C \sqrt {\varepsilon}, \tag {5.22}
$$

which implies the norm convergence of $x_{\varepsilon}(\infty)$ to $x(\infty)$ as $\varepsilon \to 0$ and proves point (b2).

Let us now return to the energy estimate (5.6):

$$
\Phi (x _ {\varepsilon} (t)) + \int_ {0} ^ {t} | \dot {x} _ {\varepsilon} (s) | ^ {2} d s \leq \frac {\varepsilon}{2} | \dot {x} _ {0} | ^ {2} + \Phi (x _ {0}).
$$

Let us make $t \rightarrow +\infty$. By the weak lower semicontinuity of $\Phi$ :

$$
\Phi (x _ {\varepsilon} (\infty)) + \int_ {0} ^ {+ \infty} | \dot {x} _ {\varepsilon} (s) | ^ {2} d s \leq \frac {\varepsilon}{2} | \dot {x} _ {0} | ^ {2} + \Phi (x _ {0}).
$$

Hence

$$
\operatorname * {l i m s u p} _ {\varepsilon \to 0} \left[ \Phi (x _ {\varepsilon} (\infty)) + \int_ {0} ^ {+ \infty} | \dot {x} _ {\varepsilon} (s) | ^ {2} d s \right] \leq \Phi (x _ {0}). \tag {5.23}
$$

On the other hand, since $x$ is a solution of the (SD) system

$$
\Phi (x (t)) + \int_ {0} ^ {t} | \dot {x} (s) | ^ {2} d s = \Phi (x _ {0}). \tag {5.24}
$$

As in theorem 4.3., one can easily verify that

$$
\lim _ {t \to \infty} \Phi (x (t)) = \Phi (x (\infty)). \tag {5.25}
$$

Indeed, $\Phi(x(\infty)) \leq \liminf_{t \to +\infty} \Phi(x(t))$ is a consequence of the weak lower semicontinuity of $\Phi$, while the converse inequality

$$
\Phi (x (\infty)) \geq \limsup \Phi (x (t))
$$

follows from the convexity inequality

$$
\Phi (x (\infty)) \geq \Phi (x (t)) + \langle \nabla \Phi (x (t)), x (\infty) - x (t) \rangle
$$

and the fact that $\nabla\Phi(x(t))\to0$. This last property in the (SD) system is a direct consequence of $\int_{0}^{+\infty}|\dot{x}(t)|^{2}dt<+\infty$ and the fact that $|\dot{x}(t)|$ is decreasing and hence has a limit, which is necessarily zero, as $t\to+\infty$.

By combining (5.24) and (5.25), we obtain

$$
\Phi (x _ {0}) = \Phi (x (\infty)) + \int_ {0} ^ {+ \infty} | \dot {x} (s) | ^ {2} d s. \tag {5.26}
$$

Combining (5.23) and (5.25), we obtain

$$
\operatorname * {l i m s u p} _ {\varepsilon \to 0} \left[ \Phi (x _ {\varepsilon} (\infty)) + \int_ {0} ^ {+ \infty} | \dot {x} _ {\varepsilon} (s) | ^ {2} d s \right] \leq \Phi (x (\infty)) + \int_ {0} ^ {+ \infty} | \dot {x} (s) | ^ {2} d s.
$$

But $\Phi(x_{\varepsilon}(\infty)) = \Phi(x(\infty)) = \min \Phi$. As a consequence

$$
\limsup _ {\varepsilon \to 0} \int_ {0} ^ {+ \infty} | \dot {x} _ {\varepsilon} (s) | ^ {2} d s \leq \int_ {0} ^ {+ \infty} | \dot {x} (s) | ^ {2} d s.
$$

Since $\dot{x}_{\varepsilon}\rightarrow\dot{x}$ weakly in $L^{2}(0,+\infty;H)$, we conclude that the convergence holds for the strong topology of $L^{2}(0,+\infty;H)$, which completes the proof. ☐

Remark: In theorem 4.3. it has been stated that, when $\Phi$ is convex and argmin $\Phi \neq \emptyset$, the trajectories of the (HBF) system weakly converge in $H$ as $t \to +\infty$. One cannot expect in general this convergence to hold for the norm convergence, otherwise, by theorem 5.2., the trajectories of the (SD) system would also be norm convergent as $t \to +\infty$ :

Indeed, for any $0 < s < t < +\infty$

$$
| x (t) - x (s) | \leq | x (t) - x _ {\varepsilon} (t) | + | x _ {\varepsilon} (t) - x _ {\varepsilon} (s) | + | x _ {\varepsilon} (s) - x (s) |
$$

$$
\leq 2 C \sqrt {\varepsilon} + | x _ {\varepsilon} (t) - x _ {\varepsilon} (s) |.
$$

If $x_{\varepsilon}(t)$ norm converges as $t \to +\infty$, it would result that, for any $\varepsilon > 0$

$$
\operatorname * {l i m s u p} _ {s, t \to + \infty} | x (t) - x (s) | \leq 2 C \sqrt {\varepsilon}.
$$

Hence,

$$
\lim _ {s, t \to + \infty} | x (t) - x (s) | = 0
$$

and $x(t)$ would be norm convergent to some $x(\infty) \in \arg\min \Phi$ as $t \to +\infty$. But it is a well known result that, in general, the trajectories of the (SD) system are not norm convergent as $t \to +\infty$, see Baillon [7] for a counterexample.

# 6 Global Exploration

The present section is meant to illustrate the foregoing theoretical developments about the asymptotic behaviour of the HBF trajectories. To keep with concreteness, Morse functions of only two variables are considered.

# 6.1 Local Minimization

As it is readily guessed, the friction coefficient $\lambda$ greatly influences the asymptotic behaviour of the HBF trajectories.

The one-dimensional quadratic case $\Phi(x)=\frac{1}{2}ax^{2}\left(a>0\right)$ is worth studying because it allows explicit calculations. HBF trajectories are given by:

1. $x(t) = \alpha e^{-\frac{1}{2} (\lambda +\omega)t} + \beta e^{-\frac{1}{2} (\lambda -\omega)t}$, if $\lambda^2 >4a$,  
2. $x(t) = \alpha e^{-\frac{1}{2} (\lambda +i\omega)t} + \beta e^{-\frac{1}{2} (\lambda -i\omega)t}$, if $\lambda^2 < 4a$,  
3. $x(t) = (\alpha t + \beta)e^{-\frac{1}{2}\lambda t}$, if $\lambda^2 = 4a$,

![](images/16e7a3efb73a5ab6d6fc154dd4021c92c46d4a95707e49e64e688b849b177fb3.jpg)

<details>
<summary>natural_image</summary>

Blank white image with no visible content, text, or symbols
</details>

Figure 5: HBF trajectories

where $\omega = \sqrt{|\lambda^2 - 4a|}$, and $\alpha$ and $\omega$ are constants depending on $a$, $\lambda$ and the initial position and velocity. The rates of convergence of $x(t)$ towards the minimum 0 are respectively: $O(e^{-\frac{1}{2} (\lambda -\omega)t})$, $O(e^{-\frac{1}{2}\lambda t})$ and $O(te^{-\frac{1}{2}\lambda t})$. A good choice for $\lambda$ should provide a fast convergence while avoiding oscillations; values of $\lambda$ equal to $2\sqrt{a}$ or a bit less should do.

The situation in two, or more, dimensions is not so clear-cut. Take as an example the functional $\Phi(x,y)=\frac{1}{2}(ax^{2}+by^{2})$ with a<<b. The two-variable HBF equation for $\Phi$ writes down as two independent scalar HBF equations:

$$
\ddot {x} + \lambda \dot {x} + a x = 0 \text {and} \ddot {y} + \lambda \dot {y} + b y = 0.
$$

It is impossible to have a fast oscillation-free convergence for both variables. To overcome this difficulty it is suggested in $[2]$ to replace the scalar $\lambda$ by a matrix, operating as an anisotropic damping.

The importance of the friction coefficient $\lambda$ is now illustrated on Rosenbrock's function $(\Phi(x,y) = 100(y - x^2)^2 + (1 - x)^2)$, which is well known in the Optimization realm; it has only one minimum at point (1,1) lying at the bottom of a long narrow curved valley. Starting from point $(-1.2,1)$ and with zero initial velocity, several HBF trajectories are computed for different values of the friction coefficient ( $\lambda = 10,5,2,1$ ); refer to figure (5). The motion of the ball is arbitrarily stopped after 20 time units to give an idea of the way completed during a fixed amount of time. Higher values of $\lambda$ are seen to give rise to slow trajectories resembling the steepest descent's while lesser values give rise to fast trajectories with oscillations getting wilder as $\lambda$ decreases.

The previous examples obviously show that some control should be exerted on $\lambda$ to get a fast oscillation-free trajectory; we do not currently have any general theoretical result on this point. It is to be noticed that a fast-convergent trajectory does not necessarily reflect a low computational burden to get at the minimum; neither does a slow-convergent trajectory mean a heavy computational burden.

# 6.2 Global Exploration

Whichever the initial conditions and the friction coefficient $\lambda$, the ball eventually rests at a critical point, $x_{\infty}$ say, which is a local minimum in general. In order to turn the HBF method into an exploratory method one has somehow to restart the procedure with some other initial conditions. A random choice would be too bad however, since information can be gathered along the trajectory.

As the HBF method is not a descent method, it may happen that some points on the trajectory yield lower values of $\Phi$ than $\Phi(x_{\infty})$. New trajectories can advantageously start from those points.

To exemplify this strategy, although rudimentary, consider the function $\Phi(x,y)=(2x^{2}+y^{2}-xy)/50-\cos(x)\cos(y/\sqrt{2})+1$. It has sixteen or so local minima and one global minimum at point O with $\Phi(O)=0$ ; refer to figure (6).

The first trajectory starts from point A with zero initial velocity and yields the local minimum B (note: $\lambda = 0.5$ ). The ball is then given an initial velocity large enough to escape from B, and it finally stops at point C another local minimum; unfortunately point C is worse than B: $\Phi(B) = 1.12$

![](images/9b5e2d583c47aa8dd1337bcca58c2add58ca64a27e3d5a23f6114c2563db2b00.jpg)

<details>
<summary>natural_image</summary>

Blank white image with no visible content, text, or symbols
</details>

Figure 6: Exploration of minima with HBF trajectories

while $\Phi(C)=1.75$. Yet an examination of the trajectory reveals that $\Phi$ attains its minimum at point D with $\Phi(D)=0.88$. So the ball is allowed to start anew with zero initial velocity from point D, and it reaches point E which is up to now the best of local minima: $\Phi(E)=0.77$. And so on till a sufficient number of local minima are explored.

# References

[1] R. Abraham and J. Robbin, Transversal mappings and flows, W. A. Benjamin, New York, 1967.  
[2] F. Alvarez, On the minimizing property of a second order dissipative sys-  
tem in Hilbert space, preprint 98-05, Département de Mathématiques, Université Montpellier II, to appear in SIAM J. of Control and Optimization.  
[3] A.S. Antipin, Second order proximal differential systems with feedback control, Differential Equations, 29 (11), (1993), 1597-1607.  
[4] J.P. Aubin and I. Ekeland, Applied Nonlinear Analysis, Wiley, (1984).  
[5] H. Attouch and R. Cominetti, A dynamical approach to convex minimization coupling approximation with the steepest descent method, J. Differential Equations, 128 (2), (1996), 519-540.  
[6] H. Attouch, X. Goudou and P. Redont, The heavy ball with friction method: II the discrete dynamical system, working paper, Département de Mathématiques, Université de Montpellier II.  
[7] J.-B. Baillon, Un exemple concernant le comportement asymptotique de la solution du problème $du/dt + \partial\phi(u) = 0$, Journal of Functional Analysis 28, 369-376 (1978).  
[8] J. M. Ball, On the asymptotic behaviour of generalized processes, with applications to nonlinear evolution equations, J. Diff. Eq., 27(1978), 224-265.  
[9] Bertsekas, Nonlinear Programming, MIT, Athena Scientific, Belmont, Massachusetts, 1995.  
[10] H. Brézis, Monotonicity methods in Hilbert spaces and some applications to nonlinear partial differential equations, in "Contributions to Nonlinear Analysis" (E.H. Zarantonello Ed.), Academic Press, New York, (1971), 101-156.  
[11] H. Brézis, Asymptotic behaviour of some evolution systems, Nonlinear evolution equations, Academic Press, (1978).  
[12] R.E. Bruck, Asymptotic convergence of nonlinear contraction semigroups in Hilbert space, Journal of Functional Analysis, 18, (1975), 15-26.  
[13] M. Chaperon and F. Coudray, Invariant manifolds conjugacies and blowup, Ergodic Theory and Dynamical Systems, 17, 783-791, 1997.  
[14] C. M. Dafermos, Asymptotic behaviour of solutions of evolution equations, Nonlinear Evolution Equations, M. G. Crandall Ed., Academic Press, New York (1978), 103-123.  
[15] H. Furuya, K. Miyashiba and N. Kenmochi, Asymptotic behaviour of solutions to a class of nonlinear evolution equations, J. Differential Equations 62 (1986), 73-94.  
[16] X. Goudou, Genericity of the convergence towards a local minimum of the heavy ball method, to appear.  
[17] J.K. Hale, Asymptotic behaviour of dissipative systems, Mathematical Surveys and Monographs, vol. 25, A.M.S., Providence, RI (1987).  
[18] J.K. Hale and G. Raugel, Upper semicontinuity of the attractor for a singularly perturbed hyperbolic equation, Journal of Differential Equations 73, 197-214, (1988).  
[19] A. Haraux, Systèmes dynamiques dissipatifs et applications, RMA 17, Masson, Paris, (1991).  
[20] A. Haraux, Nonlinear evolution equations: Global behaviour of solutions, Lecture Notes in Math. 481, Springer (1981).  
[21] J.L. Lions, Perturbations singulières dans les problèmes aux limites et en contrôle optimal, Lecture Notes in Math., 323, Springer (1973).  
[22] Z. Opial, Weak convergence of the sequence of successive approximations for nonexpansive mappings, Bull. of the American Math. Society, 73 (1967), 591-597.  
[23] J. Palis and W. de Melo, Geometric theory of dynamical systems, Springer, 1982.  
[24] L. Perko, Differential equations and dynamical systems, Texts in Applied Mathematics 7, Springer, 1996.  
[25] B.T. Polyack, Some methods of speeding up the convergence of iterative methods, Z. Vylist Math. Fiz., 4, (1964), 1-17.  
[26] P. Redont, Equation de la boule pesante avec frottement: exemple de solution non convergente, Prépublication 99, Département de Mathématiques, Université de Montpellier II, http://www.math.univmontp2.fr.  
[27] S. Smale, A Convergent process of price adjustment and global Newton method, Journal of Mathematical Economics, 3, 1976, 107-120.
