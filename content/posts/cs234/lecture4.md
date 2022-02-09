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

Lecture 4 主要介绍



- On-policy learning
  - Direct experience
  - Learn to estimate and evaluate a policy from experience obtained from following that policy
- Off-policy learning
  - Learn to estimate and evaluate a policy using experience gathered from following a different policy



### Monte Carlo Control



MC ES



$\epsilon$-greedy polies



#### On-policy control





**Greedy in the Limit of Infinite Exploration (GLIE)**

A simple GLIE strategy is $\epsilon$-greedy where $\epsilon$ is reduced to 0 with the following rate: $\epsilon_{i}=1 / i$



GLIE Monte-Carlo control converges to the optimal state-action value function $Q(s, a) \to Q^\ast(s, a)$.















