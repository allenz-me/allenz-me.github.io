---
title: "Lecture 4: Model Free Control"
date: 2022-02-05
draft: false
toc: false
slug: lecture4
categories: ["算法与程序设计", "cs234"]
tags: [""]
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---

Lecture 4 主要介绍无模型的 control，包含 MC control 和 TD control。




- On-policy learning
  - Direct experience
  - Learn to estimate and evaluate a policy from experience obtained from following that policy
- Off-policy learning
  - Learn to estimate and evaluate a policy using experience gathered from following a different policy



## Monte Carlo Control

### Monte Carlo with Exploring Starts

<img src="../../figures/lecture4/mces.png" alt="" style="zoom:67%;" />



A Blackjack game is presented to elucidate MCES.



### On-policy MC Control

Maintain an $\\epsilon$-greedy policy

<img src="../../figures/lecture4/mc-onpolicy.png" alt="" style="zoom:67%;" />

Only achieve the best policy among the $\\epsilon$-greedy policies.



**Greedy in the Limit of Infinite Exploration (GLIE)**

- All state-action pairs are visited an infinite number of times
$$
\\lim \_{i \\rightarrow \\infty} N\_{i}(s, a) \\rightarrow \\infty
$$
- Behavior policy (policy used to act in the world) converges to greedy policy
$\\lim \_{i \\rightarrow \\infty} \\pi(a \\mid s) \\rightarrow \\arg \\max \_{a} Q(s, a)$ with probability 1

A simple GLIE strategy is $\\epsilon$-greedy where $\\epsilon$ is reduced to 0 with the following rate: $\\epsilon\_{i}=1 / i$

GLIE Monte-Carlo control converges to the optimal state-action value function $Q(s, a) \\to Q^\\ast(s, a)$.



### Off-policy MC Control

Require that the behavior policy be soft, to ensure each pair of state and action be visited.




## TD Control

### On-policy SARSA

Quintuple of events $(S\_t, A\_t, R\_t, S\_{t\+1}, A\_{t\+1}) \\to \\text{SARSA}$  

$$
Q\\left(S\_{t}, A\_{t}\\right) \\leftarrow Q\\left(S\_{t}, A\_{t}\\right)\+\\alpha\\left[R\_{t\+1}\+\\gamma Q\\left(S\_{t\+1}, A\_{t\+1}\\right)\-Q\\left(S\_{t}, A\_{t}\\right)\\right]
$$

SARSA for finite-state and finite-action MDPs converges to the optimal action-value, $Q(s, a) \\rightarrow Q^{\ast}(s, a)$, under the following conditions (*Robbins-Munro sequence*)

1. The policy sequence $\\pi\_{t}(a \\mid s)$ satisfies the condition of GLIE
2. The step-sizes $\\alpha\_{t}$ satisfy the Robbins-Munro sequence such that
  $$
  \\begin{aligned}
  &\\sum\_{t=1}^{\\infty} \\alpha\_{t}=\\infty \\\\
  &\\sum\_{t=1}^{\\infty} \\alpha\_{t}^{2}<\\infty
  \\end{aligned}
  $$

A typical selection is $\\alpha\_t = o(1/t)$ .



### Off-policy Q-learning

$$
Q\\left(S\_{t}, A\_{t}\\right) \\leftarrow Q\\left(S\_{t}, A\_{t}\\right)\+\\alpha\\left[R\_{t\+1}\+\\gamma \\max \_{a} Q\\left(S\_{t\+1}, a\\right)\-Q\\left(S\_{t}, A\_{t}\\right)\\right]
$$

Directly approximates $q^\\ast$, the optimal state-action value function.

Converges to optimal $q^\\ast$ if visit all $(s, a)$ pairs infinitely often and $\\alpha\_t$ satisfy Robbins-Munro sequence. 



### Expected Sarsa

$$
\\begin{aligned}
Q\\left(S\_{t}, A\_{t}\\right) & \\leftarrow Q\\left(S\_{t}, A\_{t}\\right)\+\\alpha\\left[R\_{t\+1}\+\\gamma \\mathbb{E}\_{\\pi}\\left[Q\\left(S\_{t\+1}, A\_{t\+1}\\right) \\mid S\_{t\+1}\\right]\-Q\\left(S\_{t}, A\_{t}\\right)\\right] \\\\
& \\leftarrow Q\\left(S\_{t}, A\_{t}\\right)\+\\alpha\\left[R\_{t\+1}\+\\gamma \\sum\_{a} \\pi\\left(a \\mid S\_{t\+1}\\right) Q\\left(S\_{t\+1}, a\\right)\-Q\\left(S\_{t}, A\_{t}\\right)\\right]
\\end{aligned}
$$

Expected Sarsa eliminates the variance due to the random selection of $A\_{t\+1}$, thus outperforms Sarsa by and large.

It can safely set $\\alpha=1$ without suffering any degradation of asymptotic performance.

If $\\pi$ is a greedy policy, expected sarsa is exactly Q-learning.

**In a nutshell, expected Sarsa subsumes and generalizes Q-learning while reliably improving over Sarsa.**



### Maximization Bias

Consider single-state MDP $(|S|=1)$ with 2 actions, and both actions have 0-mean random rewards, ie. $\\mathbb{E}\\left(r \\mid a=a\_{1}\\right)=\\mathbb{E}\\left(r \\mid a=a\_{2}\\right)=0$.

Then $Q\\left(s, a\_{1}\\right)=Q\\left(s, a\_{2}\\right)=0=V(s)$ for any policy.

However, the esimate can be biased

$$
\\hat{V}^{\\hat{\\pi}}(s)=\\mathbb{E}\\left[\\max \\{ \\hat{Q}\\left(s, a\_{1}\\right), \\hat{Q}\\left(s, a\_{2}\\right)\\} \\right] > \\max \\left\\{ \\mathbb{E}\\left[\\hat{Q}\\left(s, a\_{1}\\right)\\right],\\left[\\hat{Q}\\left(s, a\_{2}\\right)\\right]\\right\\} =\\max [0,0]=V^{\\pi}
$$

The greedy policy w.r.t. estimated $Q$ values can yield a maximization bias during finite-sample learning.



### Double Q-learning

<img src="../../figures/lecture4/image-20220305161630917.png" alt="" style="zoom:50%;" />





