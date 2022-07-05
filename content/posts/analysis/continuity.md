---
title: "函数的连续性"
date: 2022-02-25
draft: false
slug: continuity
toc: true
categories: ["分析与概率"]
tags: []
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---

## 绝对连续 Absolute Continuity

A function $f:[a, b] \\rightarrow \\mathbb{R}$ is said to be absolutely continuous on $[a, b]$ if, given $\\varepsilon>0$, there exists some $\\delta>0$ such that
$$
\\sum\_{i=1}^{n}\\left|f\\left(y\_{i}\\right)\-f\\left(x\_{i}\\right)\\right|<\\varepsilon
$$
whenever $\\left\\{\\left[x\_{i}, y\_{i}\\right]: i=1, \\ldots, n\\right\\}$ is a finite collection of mutually disjoint subintervals of $[a, b]$ with $\\sum\_{i=1}^{n}\\left|y\_{i}\-x\_{i}\\right|<\\delta$.

绝对连续函数一定一致连续。Cantor 函数是一致连续的，但不绝对连续。

绝对连续最重要的是与积分的联系，对于可积的函数 $f$
$$
F(x):=\\int\_{a}^{x} f(t) d t, \\quad a \\leq x \\leq b
$$
在 $[a, b]$ 上是绝对连续的。

绝对连续函数一定是有界变差的，所以绝对连续函数几乎处处可微。

## 一致连续 Uniform Continuity

Given metric spaces $\\left(X, d\_{1}\\right)$ and $\\left(Y, d\_{2}\\right)$, a function $f: X \\rightarrow Y$ is called uniformly continuous if for every real number $\\varepsilon>0$ there exists real $\\delta>0$ such that for every $x, y \\in X$ with $d\_{1}(x, y)<\\delta$, we have that $d\_{2}(f(x), f(y))<\\varepsilon$.

对应到一元函数，区间 $X$ 上的函数 $f$ 一致连续，如果 $\\forall \\epsilon > 0, \\exists \\delta > 0, \\text{s.t. } \\; |x \- y| < \\delta \\Rightarrow |f(x) \- f(y) | < \\epsilon$

Heine–Cantor theorem 说明了紧集上的连续函数一定是一致连续的。

不一致连续的函数的例子，如 $f(x) = 1/x, \\; x\\in (0, 1)$、$f(x) = e^x , x \\in \\mathrm{R}$ .


## 半连续 Semi-Continuity

半连续是对连续性的一种弱化，跟连续性类似，它有分析学上的定义，也有拓扑学意义上的定义。

**分析学意义**

称 $f$ 在 $\\bar{x}$ 下半连续, 如果 $\\displaystyle\\liminf \_{x \\rightarrow \\bar{x}} f(x)\\geq f(\\bar{x})$

称 $f$ 在 $\\bar{x}$ 上半连续, 如果 $\\displaystyle\\limsup \_{x \\rightarrow \\bar{x}} f(x) \\leq  f(\\bar{x})$

上（下）半连续函数是在各个点都上（下）半连续的函数。

**拓扑学意义**

Let $f$ be a real (or extended-real) function on a topological space. If
$$
\\{x: f(x)>\\alpha\\}
$$
is open for every real $\\alpha, f$ is said to be *lower semi-continuous*. If
$$
\\{x: f(x)<\\alpha\\}
$$
is open for every real $\\alpha, f$ is said to be *upper semi-continuous*.

最简单的例子是，开集的 indicator function $\\mathbf{1}\_A(x) = \\begin{cases} 1 & x\\in A\\\\ 0 & x \\notin A \\end{cases}$ 是下半连续的，闭集的 indicator function 是上半连续的。

$\\mathrm{R}$ 上的半连续函数：

<img src="../../figures/continuity/Lower-left-and-upper-right-semi-continuous-functions.png" alt="Lower (left) and upper (right) semi-continuous functions" style="zoom:67%;" />



**等价定义**

$f: X \\to \\mathrm{\\bar{R}}$ 是上半连续的等价于：

+ All superlevel sets $\\{x \\in X: f(x) \\geq y\\}$ with $y \\in \\mathrm{R}$ are closed in $X$.
+ The hypograph $\\{(x, t) \\in X \\times \\mathrm{R}: t \\leq f(x)\\}$ is closed in $X \\times \\mathrm{R}$.



$f: X \\to \\mathrm{\\bar{R}}$ 是下半连续的等价于：

+ All sublevel sets $\\{x \\in X: f(x) \\leq y\\}$ with $y \\in \\mathrm{R}$ are closed in $X$.
+ The epigraph $\\{(x, t) \\in X \\times \\mathrm{R}: t \\geq f(x)\\}$ is closed in $X \\times \\mathrm{R}$.



在凸优化中，有时把闭函数定义为 epigraph 为闭集的函数，它与下半连续函数是等价的。



**性质**

+ $f$ 连续当且仅当它是上半连续和下半连续的。
+ 下半连续函数的和是下半连续的；上半连续函数的和是下半连续的。
+ $f$ 下半连续当且仅当 $\-f$ 是上半连续的。
+ 紧集上的下半连续函数存在最小值；紧集上的上半连续函数存在最大值。两个联系起来就是紧集上的连续函数存在最值。(Weierstrass extreme value theorem)



