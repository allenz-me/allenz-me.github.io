---
title: "5. Concentration without independence"
date: 2021-01-01
draft: false
slug: hdp5
categories: ["分析与概率", "高维概率"]
tags: []
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---



**Lipschitz functions**

令 $(X, d_X)$ 和 $(Y, d_Y)$ 分别是度量空间，$f: X\to Y$ 是一个 Lipschitz 函数，如果：
$$
d_Y(f(u), f(v)) \leq L \cdot d_X(u, v) \;\; \text{ for all } u, v \in X
$$
所有 $L$ 的下确界叫做 $f$ 的 Lipschitz norm (constant)，记作 $\|f\|_{\text{Lip}}$







在一般的欧式空间上，
$$
\|f(X)-\mathbb{E} f(X)\|_{\psi_{2}} \leq C\|f\|_{\text {Lip }}
$$
