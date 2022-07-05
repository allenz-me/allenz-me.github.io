---
title: "Ellipsoid Algorithm"
date: 2022-04-21
draft: false
slug: ellipsoid-algo
toc: false
categories: ["运筹与优化", "整数和组合优化"]
tags: ["线性规划"]
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---

椭球算法最早于1977年由俄罗斯数学家Shor提出用于解决一般的凸优化问题，后在1979年被 Leonid Khachiyan 用于线性规划。椭球算法是第一个解线性规划的多项式时间的算法，虽然效果不好，但是在组合优化中有理论价值。

## Ellipsoid

欧式空间中的一个椭球，可以用一个正定矩阵和一个向量来表示：
$$
\\begin{aligned}
E(A, c) &= \\{ x \\in \\mathbb{R}^n : (x\-c)^T A^{\-1} (x\-c) \\leq 1\\} \\\\
 &=  A^{1/2}S(0, 1) \+ c
\\end{aligned}
$$
任何一个椭球都可以看成是单位球 $S(0, 1)$ 在线性变换的作用下的像再平移的结果。

椭球的体积：
$$
\\operatorname{vol} (E(A, c)) = \\sqrt{\\det A} \\cdot \\operatorname{vol}(S(0, 1)) = \\sqrt{\\det A} \\cdot\\frac{\\pi^{n/2}}{\\Gamma(n/2\+1)}
$$

## Ellipsoid Algorithm

Ellipsoid algorithm 意在解决这样一个问题：
$$
\\text{Given a bounded polytope } P \\in \\mathbb{R}^n \\text{ find } x \\in P \\text{ or assert  } P \\text{ empty}
$$
假设我们有这样一个 *separation oracle* :给定一个 $x$，oracle 返回结果：$x \\in P$ 或者一个 violated constraint $c^T x \\leq d$ .

其实就是当 $x \\notin P$ 的时候返回一个 weakly seperating hyperplane between $x$ and $P$ . 这个 Oracle 能在多项式时间内运行是椭球法多项式时间结论的基本要求。

椭球算法的基本思想如下：

- Let $E\_{0}$ be an ellipsoid containing $P$
- while center $a\_{k}$ of $E\_{k}$ is not in $P$ do:
  - Let $c^{T} x \\leq c^{T} a\_{k}$ be such that $\\left\\{x: c^{T} x \\leq c^{T} a\_{k}\\right\\} \\supseteq P$
  - Let $E\_{k\+1}$ be the minimum volume ellipsoid containing $E\_{k} \\cap\\left\\{x: c^{T} x \\leq c^{T} a\_{k}\\right\\} \\supseteq P$ 
  - $k \\leftarrow k\+1$

一次迭代的过程如下图所示：

<img src="../../figures/ellipsoid/image-20220421160023125.png" alt="image-20220421160023125" style="zoom:50%;" />

能这样迭代地找到满足条件的椭球的理论依据是 **Löwner-John theorem**

对于 $\\mathbb{R}^n$ 中的一个凸紧集 $S$，存在最小的椭球 $E(S) \\supseteq S$，且 $E(S) \\supseteq S \\supseteq \\displaystyle\\frac{1}{n} E(S)$ .

由 $E\_k(A\_k, a\_k)$ 确定 $E\_{k\+1}(A\_{k\+1}, a\_{k\+1})$ 的过程如下：

While $a\_{k} \\notin P$ do:
- Let $c^{T} x \\leq d$ be an inequality that is valid for all $x \\in P$ but $c^{T} a\_{k}>d$.
- Let $b=\\frac{A\_{k} c}{\\sqrt{c^{T} A\_{k} c}}$.
- Let $a\_{k\+1}=a\_{k}\-\\frac{1}{n\+1} b$.
- Let $A\_{k\+1}=\\frac{n^{2}}{n^{2}\-1}\\left(A\_{k}\-\\frac{2}{n\+1} b b^{T}\\right)$.

每一轮迭代都能将椭球的体积缩小，成立关系：
$$
\\frac{\\operatorname{vol}\\left(E\_{k\+1}\\right)}{\\operatorname{vol}\\left(E\_{k}\\right)}<\\exp \\left(\-\\frac{1}{2(n\+1)}\\right) < 1
$$
缩小的比例只于维数有关，而与迭代步数是无关的。

当算法的迭代步数很大的时候，便可以认为 $P$ 是空集了。因为，一般来说 $P=\\{x: Cx \\leq d\\}$，$\\displaystyle\\frac{\\operatorname{vol}(E\_0)}{\\operatorname{vol}(P)}$ 关于 encoding length ($\\langle C, d \\rangle$) 是多项式的。

### From feasibility to Optimization

上述算法能检验线性不等式组的可行性 (feasibility)，要求解 $\\max \\{c^T x : x \\in P\\}$，只需令 $Q\_t=P\\cap \\{c^T x \\leq t\\}$，对 $t$ 进行二分查找即可。

所以，总的来说，椭球算法的时间复杂度就是多项式的。(weakly polynomial)

椭球法还能解决一般的凸优化问题。

### Oracles and Computational Complexity

椭球算法可以分解为：calls to a separation oracle + basic arithmetic operations.

事实上，**separation 和 optimization 在计算上是等价的 (computationally equivalent)**，给定凸集 $K$，对于：

+ Separate $({K}):$ Given as input a vector $\\vec{x}$, output yes if $\\vec{x} \\in \\mathcal{K}$, or a hyperplane separating $\\vec{x}$ from ${K}$.
- Optimize $({K}):$ Given as input a vector $\\vec{w}$, output $\\arg \\max \_{\\vec{x} \\in {K}}\\{\\vec{x} \\cdot \\vec{w}\\}$.

椭球算法实质上说明了，如果能在多项式时间内计算Separate $({K})$ ，那么也能在多项式时间内计算  Optimize $({K})$。

除了 separation oracle，还有其它的 oracle，比如：

+ Violation oracle
+ Optimization oracle
+ Validity oracle
+ Membership Oracle

见：https://en.wikipedia.org/wiki/Separation_oracle
