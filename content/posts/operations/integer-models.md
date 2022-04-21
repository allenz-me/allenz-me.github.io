---
title: "整数线性规划模型"
date: 2022-04-15
draft: false
toc: false
slug: integer-models
categories: ["运筹与优化", "整数和组合优化"]
tags: ["Polyhedron"]
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---

### Knapsack Problem

背包问题，指的是要往一个容量有限的背包里装尽可能价值更高的物品。

物品重量 $a_i$，背包容量 $b$，问题的可行域是：
$$
S:=\left\{x \in \mathbb{Z}^{n}: \sum_{i=1}^{n} a_{i} x_{i} \leq b, x \geq 0\right\}
$$
如果 $x$ 的取值是 0 或 1，那这就是 0-1 背包问题，其可行域：
$$
K:=\left\{x \in\{0,1\}^{n}: \sum_{i=1}^{n} a_{i} x_{i} \leq b\right\}
$$
对于 0-1 背包问题，其 minimal cover 指的是一个指标集，背包不能装下所有的物品，但是任少一件都可以装下。一个 minimal cover $C$ 可以诱导出一个集合：
$$
K^{C}:=\left\{x \in\{0,1\}^{n}: \sum_{i \in C} x_{i} \leq|C|-1 \text { for every minimal cover } C \text { for } K\right\} .
$$
可以证明 $K=K^C$ .

**虽然这两种表示方法是等价的，但是它们的线性松弛 (linear relaxation) 是不一样的。**

