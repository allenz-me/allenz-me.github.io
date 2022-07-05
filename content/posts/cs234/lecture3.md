---
title: "Lecture 3: Model Free Policy Evaluation"
date: 2022-02-04
draft: false
toc: false
slug: lecture3
categories: ["算法与程序设计", "cs234"]
tags: [""]
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---

Lecture3 主要介绍当我们不知道模型的各个参数的时候，如何评价一个 policy.

### Recall

+ Deﬁnition of Return
+ Deﬁnition of State Value Function
+ Deﬁnition of State-Action Value Function

Dynamic programming for policy evaluation

$$
V^{\\pi}(s) \\leftarrow \\mathbb{E}\_{\\pi}\\left[r\_{t}\+\\gamma V\_{k\-1} \\mid s\_{t}=s\\right]
$$

<img src="../../figures/lecture3/bts.png" alt="" style="zoom: 60%;" />


## Policy Evaluation without a Model

### Monte Carlo Policy Evaluation

- If trajectories are all finite, sample set of trajectories \& average returns
- Does not require MDP dynamics/rewards
- No bootstrapping
- Does not assume state is Markov (handles non-Markovian domains)
- Can only be applied to episodic MDPs
- Averaging over returns from a complete episode
- Requires each episode to terminate


Monte Carlo methods can be incremental in an episode-by-episode sense, but not in a step-by-step (online) sense.

Monte Carlo is particularly useful when a subset of states is required. One can generate many sample episodes starting from the states of interest, averaging returns from only these states, ignoring all others.



#### First-Visit

Initialize $N(s)=0, G(s)=0 \\;\\; \\forall s \\in S$
Loop

- Sample episode $i=s\_{i, 1}, a\_{i, 1}, r\_{i, 1}, s\_{i, 2}, a\_{i, 2}, r\_{i, 2}, \\ldots, s\_{i, T\_{i}}$
- Define $G\_{i, t}=r\_{i, t}\+\\gamma r\_{i, t\+1}\+\\gamma^{2} r\_{i, t\+2}\+\\cdots \\gamma^{T\_{i}\-1} r\_{i, T\_{i}}$ as return from time
step $t$ onwards in $i$ th episode
- For each time step $t$ till the end of the episode $i$
  - If this is the **first** time $t$ that state $s$ is visited in episode $i$
    - Increment counter of total first visits: $N(s)=N(s)\+1$
    - Increment total return $G(s)=G(s)\+G\_{i, t}$
    - Update estimate $V^{\\pi}(s)=G(s) / N(s)$

**Properties**

+ Unbiased

+ Consistent

By SLLN, the sequence of averages of the estimates converges to the expected value.



#### Every-Visit

Initialize $N(s)=0, G(s)=0 \\; \\forall s \\in S$
Loop

- Sample episode $i=s\_{i, 1}, a\_{i, 1}, r\_{i, 1}, s\_{i, 2}, a\_{i, 2}, r\_{i, 2}, \\ldots, s\_{i, T\_{i}}$
- Define $G\_{i, t}=r\_{i, t}\+\\gamma r\_{i, t\+1}\+\\gamma^{2} r\_{i, t\+2}\+\\cdots \\gamma^{T\_{i}\-1} r\_{i, T\_{i}}$ as return from time
step $t$ onwards in $i$ th episode
- For each time step $t$ till the end of the episode $i$
  - state $s$ is the state visited at time step $t$ in episodes $i$
  - Increment counter of total visits: $N(s)=N(s)\+1$
  - Increment total return $G(s)=G(s)\+G\_{i, t}$
  - Update estimate $V^{\\pi}(s)=G(s) / N(s)$

**Properties**

+ Biased

+ Consistent, and better MSE



#### Incremental Monte Carlo

A more computationally efficient way is:
$$
V^{\\pi}(s)=V^{\\pi}(s) \\frac{N(s)\-1}{N(s)}\+\\frac{G\_{i, t}}{N(s)}=V^{\\pi}(s)\+\\frac{1}{N(s)}\\left(G\_{i, t}\-V^{\\pi}(s)\\right)
$$


$$
V^{\\pi}(s)=V^{\\pi}(s)\+\\alpha\\left(G\_{i, t}\-V^{\\pi}(s)\\right)
$$

Incremental MC with $\\alpha>\\displaystyle\\frac{1}{N\\left(s\\right)}$ could help in non-stationary domains.



**Monte Carlo Policy Evaluation Key Limitations**

+ Generally high variance estimator
  + Reducing variance can require a lot of data
+ Requires episodic settings
  + Episode must end before data from that episode can be used to update the value function



**Problem of maintaining exploration**

+ Many state–action pairs may never be visited

**Monte Carlo with Exploring Starts**

Specify that the episodes start in a state–action pair, and that every pair has a nonzero probability of being selected as the start.



### MC off-policy evaluation

Aim: estimate *target policy* $\\pi$ given episodes generated under *behavior policy* $b$

Requirement
$$
\\pi(a \\mid s)>0 \\Longrightarrow b(a\\mid s) > 0  \\tag{coverage}
$$
*Importance-sampling ratio*
$$
\\rho\_{t: T\-1} \\doteq \\frac{\\prod\_{k=t}^{T\-1} \\pi\\left(A\_{k} \\mid S\_{k}\\right) p\\left(S\_{k\+1} \\mid S\_{k}, A\_{k}\\right)}{\\prod\_{k=t}^{T\-1} b\\left(A\_{k} \\mid S\_{k}\\right) p\\left(S\_{k\+1} \\mid S\_{k}, A\_{k}\\right)}=\\prod\_{k=t}^{T\-1} \\frac{\\pi\\left(A\_{k} \\mid S\_{k}\\right)}{b\\left(A\_{k} \\mid S\_{k}\\right)}
$$
Given episodes from $b$
$$
\\mathbb{E}\\left[\\rho\_{t: T\-1} G\_{t} \\mid S\_{t}=s\\right]=v\_{\\pi}(s)
$$
Unbiased and consistent.

+ Ordinary importance sampling — uausally unbiased; **may not converge**

  $$
  V(s) \\doteq \\frac{\\sum\_{t \\in \\mathcal{T}(s)} \\rho\_{t: T(t)\-1} G\_{t}}{|\\mathcal{T}(s)|}
  $$

+ Weighted importance sampling — biased but lower variance
  $$
  V(s) \\doteq \\frac{\\sum\_{t \\in \\mathcal{T}(s)} \\rho\_{t: T(t)\-1} G\_{t}}{\\sum\_{t \\in \\mathcal{T}(s)} \\rho\_{t: T(t)\-1}}
  $$

The estimates of ordinary importance sampling will typically have inﬁnite variance, and thus unsatisfactory convergence properties, whenever the scaled returns have inﬁnite variance.



### Temporal Difference Learning

> “If one had to identify one idea as central and novel to reinforcement learning, it would undoubtedly be temporal-difference (TD) learning.”   – Sutton and Barto 2017

Incremental MC

$$
V^{\\pi}(s)=V^{\\pi}(s)\+\\alpha\\left(G\_{i, t}\-V^{\\pi}(s)\\right)
$$
Replace $G\_{i,t}$ by bootstraping $r\_t \+ \\gamma V^\\pi(s\_{t\+1})$ .
$$
V^{\\pi}\\left(s\_{t}\\right)=V^{\\pi}\\left(s\_{t}\\right)\+\\alpha(\\underbrace{\\left[r\_{t}\+\\gamma V^{\\pi}\\left(s\_{t\+1}\\right)\\right]}\_{\\text {TD target }}\-V^{\\pi}\\left(s\_{t}\\right))
$$

+ TD error
  $$
  \\delta\_{t}=r\_{t}\+\\gamma V^{\\pi}\\left(s\_{t\+1}\\right)\-V^{\\pi}\\left(s\_{t}\\right)
  $$

+ Can immediately update value estimate after $\\left(s, a, r, s^{\\prime}\\right)$ tuple

+ Don't need episodic setting

+ Biased, but generally less high variance than MC


TD methods are often more efficient than Monte Carlo methods.



**Conplex convergence property**

+ TD(0) converges in the mean for a small constant $\\alpha$
+ TD(0) converges a.s. if $\\alpha$ decreases accordingly
+ TD(0) does not always converge with function approximation



**TD(0) converges to DP policy $V^\\pi$ for the MDP with the maximum likelihood model estimates** if there is available only a ﬁnite amount of experience.


> Maximum likelihood Markov decision process model
> $$
\\begin{gathered}
 \\hat{P}\\left(s^{\\prime} \\mid s, a\\right)=\\frac{1}{N(s, a)} \\sum\_{k=1}^{K} \\sum\_{t=1}^{L\_{k}\-1} \\mathbb{1}\\left(s\_{k, t}=s, a\_{k, t}=a, s\_{k, t\+1}=s^{\\prime}\\right) \\\\
 \\hat{r}(s, a)=\\frac{1}{N(s, a)} \\sum\_{k=1}^{K} \\sum\_{t=1}^{L\_{k}\-1} \\mathbb{1}\\left(s\_{k, t}=s, a\_{k, t}=a\\right) r\_{t, k}
\\end{gathered}
> $$

**TD exploits Markov structure.** As in the AB example

> A, 0, B, 0 
>
> B, 1 
>
> B, 1 
>
> B, 1
>
> B, 1 
>
> B, 1 
>
> B, 1 
>
> B, 0

