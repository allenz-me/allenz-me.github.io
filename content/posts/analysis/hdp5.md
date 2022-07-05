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

令 $(X, d\_X)$ 和 $(Y, d\_Y)$ 分别是度量空间，$f: X\\to Y$ 是一个 Lipschitz 函数，如果：
$$
d\_Y(f(u), f(v)) \\leq L \\cdot d\_X(u, v) \\;\\; \\text{ for all } u, v \\in X
$$
所有 $L$ 的下确界叫做 $f$ 的 Lipschitz norm (constant)，记作 $\\|f\\|\_{\\text{Lip}}$







Concentration of Lipschitz functions on the sphere

这一章首先证明了一个定理，记 $X \\sim \\text{Unif}(\\sqrt{n} S^{n\-1})$，如果 $f$ 是 $\\sqrt{n} S^{n\-1}$ 上的一个 Lipschitz 函数，那么 $f(X)$ 是集中在 $\\mathbb{E} f(X)$ 附近的。即证明了：

$$
\\|f(X)\-\\mathbb{E} f(X)\\|\_{\\psi\_{2}} \\leq C\\|f\\|\_{\\text {Lip }}
$$

这说明：

$$
\\mathbb{P}\\left(|f(X)\-\\mathbb{E} f(X)| \\geq t\\right) \\leq 2 \\exp \\left(\-\\frac{c t^{2}}{\\|f\\|\_{\\text {Lip }}^{2}}\\right)
$$

在这个定理证明过程中，用到了高维空间一个非常反直觉的结果。





## Application: Johnson-Lindenstrauss Lemma





#### 矩阵函数

对于一个 $p$ 次的多项式函数
$$
f(x)=a\_{0}\+a\_{1} x\+\\cdots\+a\_{p} x^{p}
$$
可以类似定义其矩阵函数：
$$
f(X)=a\_{0} I\+a\_{1} X\+\\cdots\+a\_{p} X^{p}
$$
这里 $X$ 是一个方阵。

比如，如果 $f$ 是 $X$ 的 minimal polynomial / characteristic polynomial，那么 $f(X) = 0$ .



甚至我们可以定义幂级数的矩阵函数：

$$
f(x) = \\sum\_{i=0}^\\infty a\_i x^i \\;\\; \\Rightarrow \\;\\; f(X) = \\sum\_{i=0}^\\infty a\_i X^i
$$

**如果 $f$ 的收敛半径为 $r$，且 $X$ 的最大特征值的模长小于 $r$，那么 $f(X)$ 收敛！**



> 如果 $X$ 的 Jordan 分解是 $X=P^{\-1}JP$，那么 $f(X) = P^{\-1} f(J)P$
>
> $J$ 可以分解为若干 Jordon 块， $J = \\operatorname{diag} \\{J\_1, J\_2, \\dots, J\_k\\}  \\Longrightarrow J^m = \\text{diag}\\{J\_1^m, J\_2^m, \\dots, J\_k^m\\}$
>
> 如果 $J\_i$ 是 $r$ 阶方阵
> $$
> J\_i = \\begin{pmatrix}
> \\lambda\_i & 1 & & \\\\
> &\\lambda\_i & 1 & \\\\
> &&\\ddots & \\ddots \\\\
> && &  \\lambda\_i &1 \\\\
> &&& & \\lambda\_i \\\\
> \\end{pmatrix}\_{r \\times r}
> $$
> 则
> $$
> f(J\_i) = \\begin{pmatrix}
> f(\\lambda\_i) & \\displaystyle\\frac{1}{1!} f^\\prime (\\lambda\_i) & \\displaystyle\\frac{1}{2!} f^{(2)} (\\lambda\_i)  & \\cdots & \\displaystyle\\frac{1}{(r\-1)!} f^{(r\-1)} (\\lambda\_i) \\\\
> & f(\\lambda\_i) & \\displaystyle\\frac{1}{1!} f^\\prime (\\lambda\_i) & \\cdots  & \\displaystyle\\frac{1}{(r\-2)!} f^{(r\-2)} (\\lambda\_i) \\\\
> & & f(\\lambda\_i) & \\cdots & \\displaystyle\\frac{1}{(r\-3)!} f^{(r\-3)} (\\lambda\_i) \\\\
> &&& \\ddots & \\vdots \\\\
> &&&& f(\\lambda\_i)
> \\end{pmatrix}
> $$
> 所以
> $$
> f(X) = f(P^{\-1} J P) = P^{\-1}f(J) P = P^{\-1} \\,\\text{diag}\\{f(J\_1) , f(J\_2), \\dots, f(J\_k)\\} \\, P
> $$
>
> 上面这个式子也可以用来定义矩阵函数！
>
> 如果 $X$ 是正定矩阵，那么可以这样定义 $\\log X$ .




由复分析知道：
$$
\\begin{gather}
\\mathrm{e}^{z}=1\+\\frac{1}{1 !} z\+\\frac{1}{2 !} z^{2}\+\\frac{1}{3 !} z^{3}\+\\cdots, \\\\
\\sin z=z\-\\frac{1}{3 !} z^{3}\+\\frac{1}{5 !} z^{5}\-\\frac{1}{7 !} z^{7}\+\\cdots, \\\\
\\cos z=1\-\\frac{1}{2 !} z^{2}\+\\frac{1}{4 !} z^{4}\-\\frac{1}{6 !} z^{6}\+\\cdots,
\\end{gather}
$$
这3个级数在整个复平面上收敛，于是对一切方阵，定义
$$
\\begin{gather}
e^X = I \+ \\frac{1}{1!} X \+ \\frac{1}{2!} X^2 \+ \\frac{1}{3!} X^3 \+ \\cdots \\\\ 
\\sin X = X \- \\frac{1}{3!} X^3 \+ \\frac{1}{5!} X^5 \-\\frac{1}{7!}X^7 \+ \\cdots \\\\
\\cos X = I \- \\frac{1}{2!} X^2 \+ \\frac{1}{4!} X^4 \- \\frac{1}{6!} X^6 \+ \\cdots
\\end{gather}
$$
若 $X$ 的特征值的模长都小于 1，也可定义
$$
\\ln (I \+ X) = X \- \\frac{1}{2} X^2 \+ \\frac{1}{3} X^3 \- \\frac{1}{4} X^4 \+ \\cdots
$$
矩阵函数在分析数学中有重要的应用。

矩阵函数的计算方法可能与数值函数有区别，如果 $XY=YX$，那么 $e^X \\cdot e^Y = e^{X\+Y}$；但是 $e^X \\cdot e^Y = e^{X\+Y}$ 并不必然成立。



> 如对 $A= \\begin{pmatrix} 0 & 0 \\\\ 1 & 1 \\\\ \\end{pmatrix}, B = \\begin{pmatrix} 1 & 1 \\\\ 0 & 0 \\\\ \\end{pmatrix}$，可验证 $e^A \\cdot e^B \\neq e^{A \+ B}$ .





**Golden-Thompson inequality**

对于对称矩阵 $A, B$ 来说
$$
\\operatorname{tr}  (e^{A\+B} ) \\leq \\operatorname{tr} (e^Ae^B )
$$
注意：$\\operatorname{tr}\\left(e^{A\+B\+C}\\right) \\leq \\operatorname{tr}\\left(e^{A} e^{B} e^{C}\\right)$ 一般不成立。



