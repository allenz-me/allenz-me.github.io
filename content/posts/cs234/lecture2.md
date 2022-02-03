---
title: "Lecture 2: Making Sequences of Good Decisions Given a Model of the World"
date: 2022-02-03
draft: false
categories: ["算法与程序设计"]
tags: ["cs234"]
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---



这个 lecture 主要介绍了 MRP、MDP 的概念，以及在 model-based 情况下的策略评估、策略改进（PI + VI）。

对应到 Sutton 的书是 Chaper 3 Finite Markov Decision Processes 和 Chapter 4 Dynamic Programming。



---



+ Model: mathematical models of dynamics and reward
+ Policy: function mapping agent’s states to actions
+ Value function: future rewards from being in a state and/or action when following a particular policy

一个 Markov Process 由状态集 $\mathcal{S}$ 和转移概率 $P$ 组成，如果状态集是有限的，那么转移概率 $P$ 可以用一个矩阵来表示。

Markov Reward Process is a Markov Chain + rewards

定义 discounted sum of rewards $G_t = r_t + \gamma r_{t+1} + \gamma^2 r_{t+2} + \cdots \;(0 \leq\gamma \leq1)$

