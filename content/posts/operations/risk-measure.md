---
title: "风险测度 — Risk Measure"
date: 2022-04-23
draft: false
slug: risk-measure
toc: false
categories: ["运筹与优化"]
tags: []
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---

在金融数学中，risk measure 用来度量一组资产的风险。经典的 MPT 使用方差作为风险的度量，



令 $(\\Omega, \\mathcal{F}, \\mathrm{P})$ 是一个概率空间，$\\mathcal{L}$ 是其上所有可积的随机变量，risk measure $\\rho$ 指的是 $\\mathcal{L} \\to [\-\\infty, \+\\infty]$ 的泛函。

Risk measure 经常提到如下的几个性质：

1. Monotonicity: $\\rho(X) \\leqslant \\rho(Y)$ if $X \\leqslant Y$.
2. Translation invariance: $\\rho(X\+c)=\\rho(X)\+c$ for any $c \\in \\mathbb{R}$.
3. Positive homogeneity: $\\rho(\\lambda X)=\\lambda \\rho(X)$ for any $\\lambda>0$.
4. Subadditivity: $\\rho(X\+Y) \\leqslant \\rho(X)\+\\rho(Y)$.

满足以上四点的度量称为 coherent risk measure。

## Dispersion Measures



## Downside Risk Measures

### Value at Risk

在险价值 VaR 是一种常用的风险测度。假设一个投资组合的损失 $L = \-r^T w$，则它置信度为 $1\-\\alpha$ 的 VaR 指的是概率不超过 $\\alpha$ 的最大损失。
$$
\\begin{aligned}
\\text{VaR}\_{1\-\\alpha}(L) = & \\inf\\, \\{x : \\mathrm{P}(L \\leqslant x) \\geqslant 1\-\\alpha\\} = \\inf\\, \\{x : \\mathrm{P}(L > x) \\leqslant \\alpha\\} \\\\
 = & \\inf\\, \\{x: F\_L(x) \\geqslant 1\- \\alpha \\}
\\end{aligned}
$$
<!--所以 VaR 越小越好-->

如果 $L \\sim \\mathcal{N}(\\mu, \\sigma^2)$，则 $\\text{VaR}\_{1\-\\alpha}(L) = \\mu \+ z\_{1\-\\alpha} \\sigma$ .

VaR 不是一致性风险测度，因为它不满足次可加性 (subadditivity)。

对于 VaR 和机会约束 (chance constraint)，有如下的等价关系：【待确定】
$$
\\text{VaR}\_{1\-\\alpha} (L) \\leqslant t \\,\\Longleftrightarrow \\, \\mathrm{P}(L \\leqslant t) \\geqslant 1\-\\alpha
$$

#### VaR 的优化

对于一个投资组合 $r^Tw$ 来说，最小化它的 VaR，即 $\\displaystyle\\min\_{w}\\, \\text{VaR}\_{1\-\\alpha}(\-r^T w)$ 等价于如下的优化问题：
$$
\\begin{aligned}
\\min\_{\\gamma, \\,w} \\; & \\gamma \\\\
\\text{s.t. } & \\mathrm{P}(\-r^T w > \\gamma) \\leqslant \\alpha \\\\
& \\sum\_{i=1}^n w\_i = 1
\\end{aligned}
$$
假设我们只有 $S$ 个 sample/senario，记 $y\_s = \\begin{cases}0, & \\text{otherwise} \\\\ 1, & \-\\hat{r}\_s^T w > \\gamma \\end{cases}$，则有：
$$
\\begin{aligned}
\\min\_{\\gamma, \\, \\vec{y}, \\, w} \\; & \\gamma \\\\
\\text{s.t. } & \\sum\_{s=1}^S y\_s \\leqslant \\lfloor \\alpha \\cdot S\\rfloor \\\\
& \\sum\_{i=1}^n w\_i = 1,\\;\\, y\_s = \\begin{cases}0, & \\text{otherwise} \\\\ 1, & \-\\hat{r}\_s^T w > \\gamma \\end{cases}
\\end{aligned}
$$
于是该问题最终可以写成：
$$
\\begin{aligned}
\\min\_{\\gamma, \\, \\vec{y}, \\, w} \\; & \\gamma \\\\
\\text{s.t. } & \-\\hat{r}\_s^T w \\leqslant  \\gamma \+ \\mathrm{M} \\cdot y\_s, \\; s=1, \\dots, S \\\\
& \\sum\_{s=1}^S y\_s \\leqslant \\lfloor \\alpha \\cdot S\\rfloor \\\\
& \\sum\_{i=1}^n w\_i = 1, \\;\\, y\_s \\in \\{0, 1\\}
\\end{aligned}
$$
这是一个混合整数优化问题！



### Conditional Value at Risk

CVaR 是一个一致的风险测度。
$$
\\text{CVaR}\_{1\-\\alpha}(L) = \\frac{1}{\\alpha} \\int\_\\alpha^1 \\text{VaR}\_u(L) \\mathrm{d} u = \\mathbb{E} [L \\mid L \\geq \\text{VaR}\_{1\-\\alpha}(L)]
$$


#### Portfolio Optimization with CVaR 

CVaR 有一个计算表达式：
**(Rockfellar & Uryasev 2000)**
$$
\\text{CVaR}\_{1\-\\alpha}(L) = \\min\_{\\xi\\in \\mathrm{R}} \\left[ \\xi \+ \\frac{1}{\\alpha}\\mathrm{E}(L\-\\xi)^\+\\right]
$$

优化 CVaR 是一个线性非整数的问题，对于 $\\displaystyle\\min\_w \\text{CVaR}\_{1\-\\alpha} (\-r^T w)$，利用上述命题，可以得到它的等价转化：


$$
\\begin{aligned}
\\min\_{\\xi, \\, \\vec{y}, \\, w} \\; & \\xi\+\\frac{1}{\\alpha \\cdot S} \\sum\_{s=1}^{S} y\_{s} \\\\
\\text {s.t. } & y\_{s} \\geq \-\\hat{r}\_s^T w \-\\xi, \\; s=1, \\ldots, S \\\\
& \\sum\_{i=1}^{n} w\_{i}=1, \\; y\_{s} \\geq 0,\\, s=1, \\ldots, S
\\end{aligned}
$$

对于一个特定的投资组合，即确定 $w$，解上述线性规划，可以得到这个投资组合的 CVaR。

对于给定的 $\\text{CVaR}\_{1\-\\alpha}$ level $\\beta$，找到期望收益最大的投资组合，这个问题是：
$$
\\begin{aligned}
\\min\_{\\xi, \\, \\vec{y}, \\, w} \\; & \- \\frac{1}{S} \\sum\_{s=1}^S \\hat{r}\_s^T w \\\\
\\text{s.t. } & \\xi \+ \\frac{1}{\\alpha \\cdot S} \\sum\_{s=1}^{S}(\-\\hat{r}\_s^T w\-\\xi)^\+ \\leqslant \\beta\\\\
& \\sum\_{i=1}^n w\_i = 1\\\\
\\end{aligned}
$$
引入 $y\_s = (\-\\hat{r}\_s^T w \-\\xi)^\+$，有：
$$
\\begin{aligned}
\\min\_{\\xi, \\, \\vec{y}, \\, w} \\; & \- \\frac{1}{S} \\sum\_{s=1}^S \\hat{r}\_s^T w \\\\
\\text{s.t. } & \\xi \+ \\frac{1}{\\alpha \\cdot S} \\sum\_{s=1}^{S} y\_s \\leqslant \\beta\\\\
& y\_s \\geqslant \-\\hat{r}\_s^T w \-\\xi, \\;y\_s \\geqslant 0, \\; s=1,\\dots, S\\\\
& \\sum\_{i=1}^n w\_i = 1\\\\
\\end{aligned}
$$











1. Law determination: $\\rho(X)=\\rho(Y)$ if $X$ and $Y$ have the same distribution.

