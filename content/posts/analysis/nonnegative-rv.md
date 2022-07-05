---
title: "非负随机变量的特殊性质"
date: 2020-03-23
draft: false
slug: nonnegative-rv
categories: ["分析与概率"]
tags: []
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---

非负的随机变量有一些特殊的性质。

首先，如果随机变量 $X$ 的期望存在，那么：

$$
\\mathrm{E}X=\\int\_0^{\\infty}[1\-F(x)]\\mathrm{d}x\-\\int\_{\-\\infty}^0F(x)\\mathrm{d}x \\tag{1}
$$

$F(x)$ 是 $X$ 的分布函数。这个式子可以用 $F(x)$ 的曲线与坐标轴围成的面积来辅助记忆。
关于证明，需要用反常积分的理论证明

$$
\\lim\_{x\\to\-\\infty}xF(x)=0\\; ;\\lim\_{x\\to\+\\infty}x[1\-F(x)]=0
$$

如果 $X$ 是非负随机变量，那么直接就有

$$
\\mathrm{E}X=\\int\_0^{\\infty}[1\-F(x)]\\mathrm{d}x
$$

如果 $X$ 只取非负整数，那么很明显，根据上式，直接就有：

$$
\\mathrm{E}X=\\sum\_{n=1}^{\+\\infty}P(X\\ge n)=\\sum\_{n=0}^{\+\\infty}P(X>n)
$$

（ps： 如果 $X$ 取全体整数，通过式 (1) 可以很容易得到相似结论）


一般地，对于随机变量 $X$，如果它的 $n$ 阶矩存在（即 $X\\in L^n(p)}$ ）

$$
\\mathrm{E}X^n=\\int\_0^{\\infty}nx^{n\-1}[1\-F(x)]\\mathrm{d}x\-\\int\_{\-\\infty}^0 nx^{n\-1}F(x)\\mathrm{d}x  \\tag{2}
$$

类似的，如果 $X$ 只取非负整数，那么 (2) 式的第二项为 $0$，根据 $F(x)$ 是一个阶梯函数的情况：

$$
\\mathrm{E}X^n=\\sum\_{k=0}^{\+\\infty}[(k\+1)^n\-k^n]P(X>k)=\\sum\_{k=1}^{\+\\infty}[k^n\-(k\-1)^n]P(X>=k)
$$
