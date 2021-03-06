---
title: "Farkas 引理、线性规划的对偶"
date: 2021-12-01
draft: false
slug: farkas
categories: ["运筹与优化"]
tags: ["Duality"]
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---


## Farkas 引理

Farkas 引理在对偶理论中有重要的应用，并且还被用来证明KKT条件。这个引理代数形式可以有多种，但是它的几何意义是恒定而简明的。

Farkas 引理的内容是，给定矩阵 $A$ 和向量 $b$，以下两组式子有且仅有一个是可行的：

1. $Ax = b, x \\geq 0$
2. $A^T y \\geq 0, b^T y < 0$

一个矩阵 $A$ 的所有列向量可以张成一个锥 $K = \\{Ax \\mid x \\geq 0\\}$，另一个向量 $b$，与这个锥的位置关系只有两种：在锥内，不然就在锥外。所以 $b$ 在锥内和 $b$ 在锥外时成立的代数关系，恰好只有一个也必然有一个是成立的，同时另一个就不成立了。

+ 如果 $b \\in K$ ，那么可以找到一组非负的系数，使得 $b$ 能被 $A$ 的列向量线性表示，即存在 $x \\geq 0, Ax=b$。

+ 如果 $b \\notin K$ ，那么根据点与凸集的分离定理，$b$ 和 $A$ 的列向量张成的锥，可以被一个（过原点的）超平面分离，设这个超平面的法向量为 $y$，那么可以有：$A^T y \\geq 0, b^T y < 0$。

这个定理也可以通过替代定理的方式去证明。考虑一个线性规划问题和它的对偶问题：

$$
(\\mathcal{P})\\quad
\\begin{array}{ll}
\\operatorname{minimize} & \\quad 0 \\\\
\\text {subject to } & A x =b, x \\geq 0
\\end{array}  \\qquad 
(\\mathcal{D})\\quad
\\begin{array}{ll}
\\operatorname { maximize }  \\; \-b^T y \\\\
\\text {subject to }  \\; A^{T} y \\geq 0
\\end{array}
$$

+  如果(1)可行，那么两个LP的最优值都是0，那么对于任意满足 $A^T y \\geq 0$ 的 $y$ 都成立 $\-b^T y \\leq 0$，即(2)不可行。

+ 如果(1)不可行，那么(P)问题的最优值是 $\+\\infty$，所以(D)问题最大值无上界，所以存在 $y$ 使得 $\-b^T y > 0, A^Ty \\geq 0$，即(2)可行。

除此以外，Farkas引理还有纯代数的证明：

+ 如果 $\\exists\\, x \\geq 0$，使得 $Ax=b$，那么如果 $A^T y \\geq 0$，就有 $b^T y=x^T A^T y \\geq 0$ ；

+ 如果存在 $y$ 使得 $A^T y\\geq 0$ 并且 $b^T y < 0$，那么如果 $b \\geq 0$，$x^T A^T y \\geq 0$，从而 $Ax \\neq b$ 。

> 如果我们从锥的角度去看的话，Farkas 引理实质上说明了 $K = K^{\\circ\\circ}$ 
>
> A finite generated cone equals its bipolar cone
> $$
> b \\in K \\Leftrightarrow b^T y \\leq 0 \\, \\text{ for all } y \\in K^\\circ = \\{y \\mid A^T y \\leq 0\\} \\Leftrightarrow b \\in K^{\\circ\\circ}
> $$

## KKT 定理

对于一般的非线性规划：

$$
\\begin{aligned}
\\min \\; & f(\\boldsymbol{x}) \\\\
\\text {s.t. } & g\_{i}(\\boldsymbol{x}) \\leq 0, \\quad i=1, \\ldots, m \\\\
& h\_{i}(\\boldsymbol{x})=0, \\quad i=1, \\ldots, n
\\end{aligned}
$$

$\\boldsymbol{x}^\\ast \\in \\mathcal{X}$ 是局部极小点 (local minimum)，并满足一定的 constraint qualification，则存在 $\\lambda\_1, \\dots, \\lambda\_m \\geq 0$ 和 $\\mu\_1, \\dots, \\mu\_n$ 使得：
$$
\\begin{aligned}
\\nabla f\\left(\\boldsymbol{x}\_{\ast}\\right)\+\\sum\_{i=1}^{m} \\lambda\_{i} \\nabla g\_{i}\\left(\\boldsymbol{x}\_{\ast}\\right)\+\\sum\_{i=1}^{n} \\mu\_{i} \\nabla h\_{i}\\left(\\boldsymbol{x}\_{\ast}\\right)&=\\mathbf{0} \\\\
\\lambda\_{i} g\_{i}\\left(\\boldsymbol{x}\_{\ast}\\right)&=0, \\;\\;i=1, \\ldots, m
\\end{aligned}
$$
**以上定理给出了局部最优的必要条件，没有凸性的要求。**

$\\boldsymbol{x}^\\ast$ 处的 Linearized cone 是：
$$
L\_{\\mathcal{X}} (\\boldsymbol{x}^\\ast) = \\left\\{ d \\,\\middle\\vert\\,
\\begin{aligned}
\\nabla g\_i(\\boldsymbol{x}^\\ast)^T d \\leq 0 \\\\
\\nabla h\_i(\\boldsymbol{x}^\\ast)^T d  = 0
\\end{aligned}
\\right\\}
$$

在满足 CQ 条件的情况下，$L\_{\\mathcal{X}}(\\boldsymbol{x}^\\ast) = T\_{\\mathcal{X}}(\\boldsymbol{x}^\\ast)$ 即可行方向锥恰好与切锥相同，由 $\\boldsymbol{x}^\\ast$ 是局部极小得到：
$$
\\nabla f (\\boldsymbol{x}^\\ast) ^T d \\geq 0, \\quad \\forall d \\in T\_{\\mathcal{X}}(\\boldsymbol{x}^\\ast)
$$
记：
$$
A=\\left(\\begin{array}{c}
\-\\nabla g\_{i}(\\bar{x})^{T} \\\\
\-\\nabla h\_{j}(\\bar{x})^{T} \\\\
\\nabla h\_{j}(\\bar{x})^{T}
\\end{array}\\right) \\in \\mathrm{R}^{(|I|\+2 p) \\times n}
$$
则有：
$$
\\nabla f (\\boldsymbol{x}^\\ast) ^T d \\geq 0, Ad \\geq 0
$$
这说明：
$$
\\exists\\left(\\begin{array}{l}
\\lambda \\\\
\\mu\_{\+} \\\\
\\mu\_{\-}
\\end{array}\\right) \\geq 0,\\;\\;\\text{s.t. } A^{T}\\left(\\begin{array}{l}
\\lambda \\\\
\\mu\_{\+} \\\\
\\mu\_{\-}
\\end{array}\\right)=\\nabla f(\\bar{x})
$$
令 $\\mu = \\mu\_{\+} \- \\mu\_{\-}$ 即可。

## 线性规划强对偶性

设线性规划

$$
(\\mathcal{P})\\quad
\\begin{array}{ll}
\\operatorname{minimize} & \\quad c^T x \\\\
\\text {subject to } & A x =b, x \\geq 0
\\end{array}  \\qquad 
(\\mathcal{D})\\quad
\\begin{array}{ll}
\\operatorname { maximize }  \\; b^T y \\\\
\\text {subject to }  \\; A^{T} y \\leq c
\\end{array}
$$

的原问题(P)和对偶问题(D)分别具有最优值 $p^\\ast$ 和 $d^\\ast$。

弱对偶性是显然的，因为如果 $x^\\ast \\geq 0$ 满足 $Ax^\\ast=b$ 是原问题的最优值，那么 $y^T b=y^T A x^\\ast \\leq c^T x^\\ast=p^\\ast$，从而 $d^\\ast \\leq p^\\ast$。

弱对偶性可以推广到取值为无穷的情况：

+ 如果 $p^\\ast=\-\\infty$，原问题最优值是无界的，则必然有 $d^\\ast=\-\\infty$，也就是对偶问题不可行。
+ 如果 $d^\\ast=\+\\infty$，对偶问题最优值无界，也必然成立 $p^\\ast=\+\\infty$，也就是说，原问题不可行。

> 也可能出现情况：$d^\\ast = \-\\infty, p^\\ast = \+ \\infty$，即原问题和对偶问题都不可行！
>
> 如线性规划的原问题：
> $$
> \\begin{aligned}
> \\min \\; & x\_{1}\+2 x\_{2} \\\\
> \\text { s.t. } & x\_{1}\+x\_{2}=1 \\\\
> & 2 x\_{1}\+2 x\_{2}=3
> \\end{aligned}
> $$
> 和对偶问题：
> $$
> \\begin{aligned}
> \\max\\; & y\_{1}\+3 y\_{2} \\\\
> \\text { s.t. } & y\_{1}\+2 y\_{2}=1 \\\\
> & y\_{1}\+2 y\_{2}=2
> \\end{aligned}
> $$
> 都不可行！


**Farkas引理可以用来论证线性规划的强对偶性，强对偶性建立在原问题或对偶问题的某一个是可行的基础上。**

> 当两个问题都不可行，即有 $d^\\ast = \- \\infty, \\; p^\\ast = \+ \\infty$，强对偶性不再成立！
>
> **线性规划强对偶性指的是：如果原问题可行，并且最优值有界，那么对偶问题也可行，且两个最优值相等。**

设 $\\epsilon > 0$，以及：

$$
\\hat{A}=\\left(\\begin{array}{l}
A \\\\
c^{T}
\\end{array}\\right) \\quad \\hat{b}=\\left(\\begin{array}{l}
\\: b \\\\
p^{\\ast}
\\end{array}\\right) \\quad \\hat{b}\_{\\epsilon}=\\left(\\begin{array}{c}
b \\\\
p^{\\ast}\-\\epsilon
\\end{array}\\right)
$$

现在 $p^\\ast\-\\epsilon$ 是原问题的一个严格下界，所以 $\\{\\hat A x =\\hat b , x\\geq 0\\}$ 是可行的，而 $\\{\\hat A x =\\hat b\_\\epsilon , x\\geq 0\\}$ 是不可行的。应用两次 Farkas 引理，设 $\hat{y}=\left(\begin{array}{c}
y \\
\alpha 
\end{array}\right)$，我们有：

$$
\\left\\{\\begin{array}{l}
\\hat{A}^{T}\\left(\\begin{array}{l}
y \\\\
\\alpha
\\end{array}\\right)=A^{T} y\+\\alpha c \\geq 0 \\\\
\\hat{b}\_{\\epsilon}^{T}\\left(\\begin{array}{l}
y \\\\
\\alpha
\\end{array}\\right)=b^{T} y\+\\alpha\\left(p^{\\ast}\-\\xi\\right)=\\hat b^{T}\\left(\\begin{array}{l}
y \\\\
\\alpha
\\end{array}\\right) \-\\alpha \\epsilon<0 \\\\
\\hat b^{T}\\left(\\begin{array}{l}
y \\\\
\\alpha
\\end{array}\\right) \\geq 0
\\end{array}\\right.
$$

可知 $\\alpha > 0$、$\-\\alpha < 0$，从而

$$
\\left\\{\\begin{array}{l}
A^{T}\\left(\\displaystyle\\frac{y}{\-\\alpha}\\right) \\leq c \\\\
b^{T}\\left(\\displaystyle\\frac{y}{\-\\alpha}\\right)>p^{\\ast}\-\\epsilon
\\end{array}\\right.
$$

这样其实找到了对偶问题的一个可行点 $\\displaystyle\\frac{y}{\-\\alpha}$，从而：

$$
p^{\\ast}\-\\epsilon < d^{\\ast} \\leq p^{\\ast}
$$

因为 $\\epsilon$ 是任意的，所以 $d^\\ast=p^\\ast$，强对偶性成立！


### 互补松弛条件

从强对偶性出发，关于对偶变量，我们能够得到以下等式：

$$
\\left\\{\\begin{array}{l}
c^{T} x=b^{T} y \\\\
A x=b \\\\
A^{T} y\+\\lambda=c \\\\
x \\geqslant 0, \\lambda \\geqslant 0
\\end{array}\\right.
$$

上面的 $\\lambda$ 是约束条件 $x \\geqslant 0$ 的对偶变量。我们有：

$$
y^T Ax=y^T b \\Rightarrow (c\-\\lambda)^T x=c^T x \\Rightarrow \\lambda ^T x = 0
$$

因为 $x \\geqslant 0, \\lambda \\geqslant 0$，所以 $\\lambda\_i, x\_i$ 必有一为0，其中 $\\lambda \_i$ 即为 $(A\_i^T y \- c\_i)$ ，$A\_i$ 是矩阵 $A$ 的第 $i$ 列。

### 强互补松弛

对于线性规划式(*)，还成立强互补松弛性（strict complementary slackness）：

+ $x^\\ast\_j > 0$
+ $A\_j^T y^\\ast < c\_j$

以上两个关系有且仅有一个成立。其中 $(x^\\ast, y^\\ast)$ 是原问题和对偶问题的一组最优解。

> 意思就是，**总存在一组最优解使得强互补松弛条件（两个不等式中的一个）成立**。

$A^T \_j y^\\ast < c\_j \\Rightarrow x\_j^\\ast = 0$ 是容易的，直接用互补松弛就可以了；而 $x^\\ast\_j = 0 \\Rightarrow A^T\_j y^\\ast<c\_j$ 证明起来有点困难。

### 对偶问题与影子价格

要理解透影子价格，必须对线性规划的对偶有充分的认识！

不妨考虑资源约束下的不等式线性规划 ($b \\geq 0$)：
$$
(\\mathcal{P})\\quad
\\begin{array}{ll}
\\operatorname{minimize} & \\quad c^T x \\\\
\\text {subject to } & A x \\geq b, x \\geq 0
\\end{array}  \\qquad 
(\\mathcal{D})\\quad
\\begin{array}{ll}
\\operatorname { maximize }  \\; b^T y \\\\
\\text {subject to }  \\; A^{T} y \\leq c, y \\geq 0
\\end{array}
$$
对于最大化对偶问题(D)，可以看成是资源约束下的最大化利润问题，假如说 $(\\bar{x}, \\bar{y})$ 是一组最优解，如果资源约束增大为 $c\_\\epsilon = c \+ \\epsilon$，在保证最优性和可行性的条件下，目标函数值增大 $\\epsilon^T \\bar{x}$ .

## Farkas 引理的应用

利用 Farkas 引理能够得到一个有用的推论：

1. $Ax \\leq b$
2. $A^{T} y \\geq 0, b^{T} y<0, y \\geq 0$

有且仅有一个是可行的。注意到 $Ax \\leq b \\Leftrightarrow Ax \+ s = b, s  \\geq 0$，对
$$
[A \\;\\; I] \\left[\\begin{aligned} x \\\\ s \\end{aligned}\\right] = b
$$
使用 Farkas 引理，对应的另一组约束条件是 
$$
\\begin{bmatrix}
A^T \\\\
I
\\end{bmatrix} y \\geq 0, \\, b^T y < 0 \\Rightarrow A^T y \\geq 0, b^T y < 0, y \\geq 0
$$
得证！


> 与之相关的还有 Gordan 定理：
> (1) $Ax < 0$
> (2) $A^Ty=0, \\:y\\succeq 0, \\:y\\neq 0$
> 只能有一个有解！

---

总结：本文内容比较多，主要阐述了 Farkas 引理和线性规划的对偶，这两者可以说互为等价的关系。从强对偶性出发，我们可以轻松得到互补松弛条件。

