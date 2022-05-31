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







Concentration of Lipschitz functions on the sphere

这一章首先证明了一个定理，记 $X \sim \text{Unif}(\sqrt{n} S^{n-1})$，如果 $f$ 是 $\sqrt{n} S^{n-1}$ 上的一个 Lipschitz 函数，那么 $f(X)$ 是集中在 $\mathbb{E} f(X)$ 附近的。即证明了：

$$
\|f(X)-\mathbb{E} f(X)\|_{\psi_{2}} \leq C\|f\|_{\text {Lip }}
$$

这说明：

$$
\mathbb{P}\left(|f(X)-\mathbb{E} f(X)| \geq t\right) \leq 2 \exp \left(-\frac{c t^{2}}{\|f\|_{\text {Lip }}^{2}}\right)
$$

在这个定理证明过程中，用到了高维空间一个非常反直觉的结果。





## Application: Johnson-Lindenstrauss Lemma



