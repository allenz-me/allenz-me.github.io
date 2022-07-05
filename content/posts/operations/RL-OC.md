---
title: "Reinforcement Learning and Optimal Control"
date: 2022-07-01
draft: false
slug: rl-oc
toc: false
categories: ["运筹与优化"]
tags: []
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---

## Exact Dynamic Programming

### Deterministic Dynamic Programming

A deterministic DP problem involves a discrete-time dynamic system of the form
$$
x\_{k\+1} = f\_k(x\_k, u\_k), \\quad k = 0, 1, \\dots, N\-1
$$
where

+ $k$ is the time index
+ $x\_k$ is the state of the system
+ $u\_k$ is the control or decision, to be selected from some given set $U\_k(x\_k)$
+ $f\_k$ is a function of $(x\_k, u\_k)$ that describes the mechanism by which the state is updated from time $k$ to time $k\+1$
+ $N$ is the horizon

A cost incurred at time $k$, denoted by $g\_k(x\_k, u\_k)$, accumulates over time. For a given initial state $x\_0$, **the total costs of a control sequence** $\\{u\_0, \\dots, u\_{N\-1}\\}$ is
$$
J\\left(x\_{0} ; u\_{0}, \\ldots, u\_{N\-1}\\right)=g\_{N}\\left(x\_{N}\\right)\+\\sum\_{k=0}^{N\-1} g\_{k}\\left(x\_{k}, u\_{k}\\right)
$$
where $g\_N(x\_N)$ is a terminal cost incurred at the end of the process.

We want to minimize the total cost over all sequences $\\{u\_0, \\dots, u\_{N\-1}\\}$ that satisfy the control constraints, thereby obtaining the optimal value
$$
J^{\ast}\\left(x\_{0}\\right)=\\min \_{\\substack{u\_{k} \\in U\_{k}\\left(x\_{k}\\right) \\\\ k=0, \\ldots, N\-1}} J\\left(x\_{0} ; u\_{0}, \\ldots, u\_{N\-1}\\right)
$$
The picture below illustrates the main elements of the problem.

<img src="../../figures/RL-OC/image-20220701143017425.png" alt="image-20220701143017425" style="zoom:50%;" />



#### Dynamic Programming Algorithm

The DP algorithm rests on a simple idea, the *principle of optimality*.

##### Principle of Optimality

Let $\\left\\{u\_{0}^{\ast}, \\ldots, u\_{N\-1}^{\ast}\\right\\}$ be an optimal control sequence, which together with $x\_{0}$ determines the corresponding state sequence $\\left\\{x\_{1}^{\ast}, \\ldots, x\_{N}^{\ast}\\right\\}$ via the system equation. Consider the subproblem whereby we start at $x\_{k}^{\ast}$ at time $k$ and wish to minimize the "cost-to-go" from time $k$ to time $N$
$$
g\_{k}\\left(x\_{k}^{\ast}, u\_{k}\\right)\+\\sum\_{m=k\+1}^{N\-1} g\_{m}\\left(x\_{m}, u\_{m}\\right)\+g\_{N}\\left(x\_{N}\\right)
$$
over $\\left\\{u\_{k}, \\ldots, u\_{N\-1}\\right\\}$ with $u\_{m} \\in U\_{m}\\left(x\_{m}\\right), m=k, \\ldots, N\-1$. Then the truncated optimal control sequence $\\left\\{u\_{k}^{\ast}, \\ldots, u\_{N\-1}^{\ast}\\right\\}$ is optimal for this subproblem.

Stated succinctly, the principle of optimality says that *the tail of an optimal sequence is optimal for the tail subproblem*.

##### DP Algorithm for Deterministic Finite Horizon Problems

Start with
$$
J\_N^\\ast (x\_N) = g\_N(x\_N), \\quad \\text{ for all } x\_N
$$
and for $k=0, \\dots, N\-1$, let
$$
J\_{k}^{\ast}\\left(x\_{k}\\right)=\\min \_{u\_{k} \\in U\_{k}\\left(x\_{k}\\right)}\\left[g\_{k}\\left(x\_{k}, u\_{k}\\right)\+J\_{k\+1}^{\ast}\\left(f\_{k}\\left(x\_{k}, u\_{k}\\right)\\right)\\right], \\quad \\text { for all } x\_{k}
$$
The algorithm constructs functions $J\_N^\\ast(x\_N), J\_{N\-1}^\\ast(x\_{N\-1}), \\dots, J\_0^\\ast(x\_0)$ sequentially, starting from $J\_N^\\ast$, and proceeding backwards to $J\_{N\-1}^\\ast, J\_{N\-2}^\\ast, \\dots$ .

$J\_k^\\ast(x\_k)$ is the *optimal cost-to-go* at state $x\_k$ and time $k$ . We refer $J\_k^\\ast$ as the *optimal cost-to-go function*.



##### Construction of Optimal Control Sequence

Set
$$
u\_{0}^{\ast} \\in \\underset{u\_{0} \\in U\_{0}{\\left(x\_{0}\\right)} }{\\arg\\min}\\left[g\_{0}\\left(x\_{0}, u\_{0}\\right)\+J\_{1}^{\ast}\\left(f\_{0}\\left(x\_{0}, u\_{0}\\right)\\right)\\right]
$$
and
$$
x\_{1}^{\ast}=f\_{0}\\left(x\_{0}, u\_{0}^{\ast}\\right) .
$$
Sequentially, going forward, for $k=1,2, \\ldots, N\-1$, set
$$
u\_{k}^{\ast} \\in \\underset{u\_{k} \\in U\_{k}\\left(x\_{k}^{\ast}\\right)}{\\arg\\min}\\left[g\_{k}\\left(x\_{k}^{\ast}, u\_{k}\\right)\+J\_{k\+1}^{\ast}\\left(f\_{k}\\left(x\_{k}^{\ast}, u\_{k}\\right)\\right)\\right],
$$
and
$$
x\_{k\+1}^{\ast}=f\_{k}\\left(x\_{k}^{\ast}, u\_{k}^{\ast}\\right) .
$$

#### Approximation in Value Space

In practice, exact DP is often prohibitively time-consuming, because the number of possible $x\_k$ and $k$ can be very large. An alternative by *approximation in value space* constructs a suboptimal solution $\\{\\tilde{u}\_0, \\dots, \\tilde{u}\_{N\-1}\\}$ in place of the optimal $\\{u\_0^\\ast, \\dots, u\_{N\-1}^\\ast\\}$ based on using $\\tilde{J}\_k$ in place of $J\_k^\\ast$ in the DP procedure.





### Stochastic Dynamic Programming


$$
x\_{k\+1}=f\_{k}\\left(x\_{k}, u\_{k}, w\_{k}\\right), \\quad k=0,1, \\ldots, N\-1
$$




In a 

<img src="../../figures/RL-OC/image-20220627154726731.png" alt="image-20220627154726731" style="zoom:50%;" />





## Approximation in Value Space

Curse of di





