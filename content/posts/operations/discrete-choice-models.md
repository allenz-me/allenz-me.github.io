---
title: "Discrete Choice Models"
date: 2022-02-15
draft: false
slug: discrete-choice-models
categories: ["运筹与优化"]
tags: ["Choice Model"]
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---

## Discrete Choice Models

离散选择模型已成为研究消费者面对多种产品的购买行为的重要工具，并已广泛应用于经济、营销、交通和运营等多个领域。




记 $q_i(S)$ 为选择 item $i \in S$ 的概率

**Regularity Condition**
the choice probability for any product in the offer set decreases as the offer set enlarges.

**choice axiom**
$$
q_i(S) = q_{S^\prime}(S) \cdot q_i (S^\prime) \quad \forall i \in S^\prime \subseteq S
$$


Luce 证明了满足 choice axiom 的 $q$ 一定有如下形式：
$$
q_{i}(S)= \frac{a_{i}}{\sum_{j \in S} a_{j}}
$$






**Substitution Effect**

The choice probability decreases as any other alternative becomes more appealing



## Pricing Optimization

价格影响顾客选择商品的概率，假定效用关于价格是线性的：
$$
u_i = \alpha_i - \beta_i p_i
$$
这时候的选择模型：
$$
q_{i}\left(S^{+}, \mathbf{p}\right)=\frac{\exp \left(\alpha_{i}-\beta_{i} p_{i}\right)}{1+\sum_{j \in S} \exp \left(\alpha_{j}-\beta_{j} p_{j}\right)}, \quad \forall i \in S,  \quad (S^+ = S \cup \{0\})\quad
$$
以最大化期望收益为目标，定价优化问题可表示为：

$$
\max _{\mathbf{p}} R(S, \mathbf{p}):=\sum_{i \in S}\left(p_{i}-c_{i}\right) \cdot q_{i}\left(S^{+}, \mathbf{p}\right)
$$




## Assortment Optimization

另一种零售策略，如果商品的价格是给定的，商家只能调整展示给顾客的商品种类。

这时候的优化目标变为：
$$
\max _{S \subseteq N} R(S):=\sum_{i \in S}\left(p_{i}-c_{i}\right) \cdot q_{i}\left(S^{+}\right)
$$


更进一步地，如果商品种类和价格都是可以变化的，这时商家面临 Joint Assortment and Price Optimization。

