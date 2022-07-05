---
title: "Convex Function — 续"
date: 2022-01-02
draft: false
slug: convex-function2
categories: ["运筹与优化", "凸优化"]
tags: []
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---

这是 convex function 的第二部分。

---


## 凸函数

对凸性的刻画，从弱到强，分别是：

### 拟凸 (quasiconvex)

$f$ 的所有 sublevel sets $L\_\\alpha = \\{x \\mid f(x) \\leq \\alpha\\}$ 是凸集。

### 凸 (convex)

定义在凸集上的函数 $f$ 满足 $\\forall x, y, \\lambda \\in [0, 1]$ 成立：
$$
f(\\lambda x \+ (1\-\\lambda )y) \\leq \\lambda f(x) \+ (1\-\\lambda) f(y)
$$
则称 $f$ 是凸函数。

#### Epigraph characterization of convexity

一个函数的 epigraph 指的是：
$$
\\text { epi } f=\\left\\{(x, r) \\in \\mathbb{R}^{n} \\times \\mathbb{R} \\mid f(x) \\leq r\\right\\}
$$
如果把上面的小于等于号换成小于号，就是 $f$ 的 strict epigraph $\\operatorname{epi}\_s(f)$ .

$f$ 是凸函数等价于：

+ $\\operatorname{epi}(f)$ 是凸集
+ $\\operatorname{epi}\_s(f)$ 是凸集

#### First-order characterization of convexity

如果函数 $f$ 可微，那么 $f$ 的凸性可以由一阶条件来刻画：
$$
f(x) \\geq f\\left(x\_{0}\\right)\+\\left\\langle\\nabla f\\left(x\_{0}\\right), x\-x\_{0}\\right\\rangle \\quad \\forall x, x\_0 \\in \\operatorname{dom} f
$$

**Monotonicity of gradient**

可微的函数 $f$ 是凸函数当且仅当：
$$
\\langle\\nabla f(x)\-\\nabla f(y), x\-y\\rangle \\geq 0 \\quad \\forall x, y \\in \\operatorname{dom} f
$$

#### Second-order characterization of convexity

二次可微的函数 $f$ 是凸函数的充要条件是： $\\nabla^2 f (x) \\succeq 0, \\;\\forall x \\in \\operatorname{dom} f$ .

### 严格凸 (strictly convex)

定义在凸集上的函数 $f$ 满足 $\\forall x \\neq y, \\lambda \\in (0, 1)$ 成立：
$$
f(\\lambda x \+ (1\-\\lambda )y) < \\lambda f(x) \+ (1\-\\lambda) f(y)
$$
则称 $f$ 是严格凸函数。

#### First-order characterization of strict convexity

如果函数 $f$ 可微，那么 $f$ 的严格凸性可以由一阶条件来刻画：
$$
f(x) >  f\\left(x\_{0}\\right)\+\\left\\langle\\nabla f\\left(x\_{0}\\right), x\-x\_{0}\\right\\rangle \\quad \\forall x \\neq x\_0 \\in \\operatorname{dom} f
$$

**Monotonicity of gradient**

可微的函数 $f$ 是严格凸函数当且仅当：
$$
\\langle\\nabla f(x)\-\\nabla f(y), x\-y\\rangle >  0 \\quad \\forall x \\neq y \\in \\operatorname{dom} f
$$

#### Second-order characterization of strict convexity

二次可微的函数 $f$ 是严格凸函数的充分条件是： $\\nabla^2 f \\succ 0, \\; \\forall x \\in \\operatorname{dom} f$ .

### 强凸 (strongly convex)

存在 $\\sigma > 0$ 使得定义在凸集上的函数 $f$ 满足 $\\forall x, y, \\lambda \\in [0, 1]$ 成立：
$$
f(\\lambda x\+(1\-\\lambda) y) \\leq \\lambda f(x)\+(1\-\\lambda) f(y)\-\\frac{\\sigma}{2} \\lambda(1\-\\lambda)\\|x\-y\\|^{2}
$$
则称 $f$ 是强凸函数，且 $\\sigma$ 称为强凸系数 (modulus of strong convexity)。上式的等价定义是：$f(x) \- \\displaystyle\\frac{\\sigma}{2} \\|x \\|^2$ 是凸函数。

#### First-order characterization of strong convexity

如果函数 $f$ 可微，那么 $f$ 以系数 $\\sigma$ 强凸可以由一阶条件来刻画：
$$
f(x) \\geq f\\left(x\_{0}\\right)\+\\left\\langle\\nabla f\\left(x\_{0}\\right), x\-x\_{0}\\right\\rangle\+\\frac{1}{2} \\sigma \\left\\|x\-x\_{0}\\right\\|^{2} .
$$

#### Monotonicity of gradient

可微的函数 $f$ 以系数 $\\sigma$ 强凸当且仅当：
$$
\\langle\\nabla f(x)\-\\nabla f(y), x\-y\\rangle \\geq \\sigma\\|x\-y\\|^{2} \\quad \\forall x, y \\in \\operatorname{dom} f
$$

#### Second-order characterization of strong convexity

二次可微的函数 $f$ 以系数 $\\sigma$ 强凸当且仅当 $\\nabla^2 f(x) \\succ \\sigma I$ .

## Infimal Convolution

函数 $f$ 和 $g$ 的 **infimal convolution** (or epi-sum) 指的是：

$$
\\begin{aligned}
(f\\, \\square\\, g)(x) &= \\inf\_{y \\in \\mathrm{R}^{n}} \\left\\{f(x\-y)\+g(y)\\right\\} \\\\
 &= \\inf \\{ f(x\_1) \+ g(x\_2) \\mid x\_1 \+ x\_2 = x\\}
\\end{aligned}
$$

其几何含义是：$\\operatorname{epi}(f \\,\\square\\, g) = \\operatorname{epi}(f) \+ \\operatorname{epi}(g)$ 或是 $\\operatorname{epi}\_s(f \\,\\square\\, g) = \\operatorname{epi}\_s(f) \+ \\operatorname{epi}\_s(g)$，由此可见，凸函数的 infimal convolution 是凸的。同时我们还得到：$\\operatorname{dom} (f \\,\\square\\, g) = \\operatorname{dom} f \+ \\operatorname{dom} g$ .

还可以定义一族函数的 infimal convolution:
$$
\\begin{aligned}
f(x) &=\\left(f\_{1} \\square f\_{2} \\square \\ldots f\_{m}\\right)(x) \\\\
&=\\inf \\left\\{\\sum\_{k=1}^{m} f\\left(x\_{k}\\right) \\mid x\_{k} \\in \\mathrm{R}^{n}, \\sum\_{k=1}^{m} x\_{k}=x\\right\\}
\\end{aligned}
$$

例：

1. $I\_C \\square \\| \\cdot \\| = d\_C(\\cdot)$ 
2. $I\_{C\_1} \\square I\_{C\_2} = I\_{C\_1 \+ C\_2}$
3. 如果 $f\_1(x)=\\displaystyle\\frac{1}{2} x^T A\_1 x,\\, f\_2(x)=\\displaystyle\\frac{1}{2} x^T A\_2 x$，则 $(f\_1 \\square f\_2) (x) = \\displaystyle\\frac{1}{2} x^T(A\_1^{\-1} \+ A\_2^{\-1})^{\-1} x$



infimal convolution 有以下性质：

+ commutativity: $f \\square g = g \\square f$
+ associativity: $(f \\square g) \\square h = f \\square (g \\square h)$
+ preserves the order: $f\_1 \\leq f\_2 \\Rightarrow f\_1 \\square g \\leq f\_2 \\square g$

**Infimal convolution of support functions**

Let $\\left\\{C\_{k}\\right\\}\_{k=1, \\ldots, m}$ be non-empty convex sets, $C\_{k} \\in \\mathbb{R}^{n}$. Then
$$
\\begin{gathered}
\\delta^{\ast}\\left(\\cdot \\mid C\_{1}\+\\ldots\+C\_{m}\\right)=\\delta^{\ast}\\left(\\cdot \\mid C\_{1}\\right)\+\\ldots\+\\delta^{\ast}\\left(\\cdot \\mid C\_{m}\\right) \\\\
\\delta^{\ast}\\left(\\cdot \\mid \\operatorname{cl} C\_{1} \\cap \\ldots \\cap \\operatorname{cl} C\_{m}\\right)=\\operatorname{cl}\\left\\{\\delta^{\ast}\\left(\\cdot \\mid C\_{1}\\right) \\square \\ldots \\delta^{\ast}\\left(\\cdot \\mid C\_{m}\\right)\\right\\}
\\end{gathered}
$$

## 凸函数的连续性

$\\mathrm{R}^n \\to \\mathrm{R}$的凸函数是连续函数。

**proper 的凸函数在相对内点集上是连续的。**

由此可见，$\\mathrm{R}^n$ 上的凸函数一定是闭的（下半连续）。



## Log-determinant

$\\mathrm{S}\_{\+\+}^n \\to \\mathrm{R}$ 的函数 $f(X) = \\log \\det X$ 称为 log-det function，其梯度：
$$
\\nabla f(X) = X^{\-1}
$$
先证明 $\\nabla f(I) = I$，设 $\\Delta \\in \\mathrm{S}^n$ 其特征值为 $\\lambda\_1, \\lambda\_2, \\dots, \\lambda \_n$
$$
\\begin{aligned}
f(I\+\\Delta)\-f(I)\-\\langle I, \\Delta\\rangle &=\\log \\left(\\prod\_{i=1}^{n}\\left(\\lambda\_{i}\+1\\right)\\right)\-\\operatorname{tr}(\\Delta)=\\sum\_{i=1}^{n}\\left[\\log \\left(\\lambda\_{1}\+1\\right)\-\\lambda\_{i}\\right] \\\\
&=o(\\operatorname{tr}(\\Delta))=o\\left(\\sqrt{\\operatorname{tr}\\left(\\Delta^{T} \\Delta\\right)}\\right)=o(\\|\\Delta\\|)
\\end{aligned}
$$
对于一般情形：
$$
\\begin{aligned}
& f(X\+\\Delta)\-f(X)\-\\left\\langle X^{\-1}, \\Delta\\right\\rangle \\\\
=& \\log \\left(\\operatorname{det}\\left(X^{\\frac{1}{2}}\\left(I\+X^{\-\\frac{1}{2}} \\Delta X^{\-\\frac{1}{2}}\\right) X^{\\frac{1}{2}}\\right)\\right)\-\\log (\\operatorname{det}(X))\-\\operatorname{tr}\\left(X^{\-1} \\Delta\\right) \\\\
=& \\log \\left(\\operatorname{det}\\left(I\+X^{\-\\frac{1}{2}} \\Delta X^{\-\\frac{1}{2}}\\right)\\right)\-\\operatorname{tr}\\left(X^{\-\\frac{1}{2}} \\Delta X^{\-\\frac{1}{2}}\\right) \\\\
=& o\\left(\\operatorname{tr}\\left(X^{\-\\frac{1}{2}} \\Delta X^{\-\\frac{1}{2}}\\right)\\right) = o(\\|\\Delta\\|)
\\end{aligned}
$$
以上的内积都是矩阵的 Frobenius 内积。

或者使用复合函数的求导公式：
$$
\\frac{\\partial}{\\partial X\_{i j}} \\log \\operatorname{det} X=\\frac{1}{\\operatorname{det} X} \\frac{\\partial \\operatorname{det} X}{\\partial X\_{i j}}=\\frac{1}{\\operatorname{det} X} \\operatorname{adj}(X)\_{j i}=\\left(X^{\-1}\\right)\_{j i}
$$
其中 $\\operatorname{adj}(X)$ 表示 $X$ 的伴随矩阵，满足 $\\operatorname{adj}(X) = \\det(X) \\cdot X^{\-1}$ .

**Jacobi's formula**

$$
\\frac{d}{d t} \\operatorname{det} A(t)=\\operatorname{tr}\\left(\\operatorname{adj}(A(t)) \\frac{d A(t)}{d t}\\right)=(\\operatorname{det} A(t)) \\cdot \\operatorname{tr}\\left(A(t)^{\-1} \\cdot \\frac{d A(t)}{d t}\\right)
$$

由此得到

$$
\\frac{\\partial \\det A}{\\partial A\_{ij}} = \\operatorname{adj}(A)\_{ji}
$$

根据 $f(X)$ 的梯度，我们能得到它的一阶近似：
$$
f(Z) \\approx f(X) \+ \\langle X^{\-1}, Z \- X \\rangle = f(X)\+\\operatorname{tr}\\left(X^{\-1}(Z\-X)\\right)
$$

### Convexity of log-determinant

【待】



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

<img src="../../figures/Convex-function-2/Lower-left-and-upper-right-semi-continuous-functions.png" alt="Lower (left) and upper (right) semi-continuous functions" style="zoom:67%;" />



**等价定义**

$f: X \\to \\mathrm{\\bar{R}}$ 是上半连续的等价于：

+ All superlevel sets $\\{x \\in X: f(x) \\geq y\\}$ with $y \\in \\mathrm{R}$ are closed in $X$.
+ The hypograph $\\{(x, t) \\in X \\times \\mathrm{R}: t \\leq f(x)\\}$ is closed in $X \\times \\mathrm{R}$.

$f: X \\to \\mathrm{\\bar{R}}$ 是下半连续的等价于：

+ All sublevel sets $\\{x \\in X: f(x) \\leq y\\}$ with $y \\in \\mathrm{R}$ are closed in $X$.
+ The epigraph $\\{(x, t) \\in X \\times \\mathrm{R}: t \\geq f(x)\\}$ is closed in $X \\times \\mathrm{R}$.

**在凸优化中，有时把闭函数定义为 epigraph 为闭集的函数，它与下半连续函数是等价的。**

**性质**

+ $f$ 连续当且仅当它是上半连续和下半连续的。
+ 下半连续函数的和是下半连续的；上半连续函数的和是下半连续的。
+ $f$ 下半连续当且仅当 $\-f$ 是上半连续的。
+ 紧集上的下半连续函数存在最小值；紧集上的上半连续函数存在最大值。两个联系起来就是紧集上的连续函数存在最值。(Weierstrass extreme value theorem)

