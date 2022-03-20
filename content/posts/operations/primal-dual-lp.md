---
title: "线性规划的原始对偶算法"
date: 2022-03-19
draft: false
slug: primal-dual-lp
toc: false
categories: ["运筹与优化"]
tags: []
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---


线性规划的原始-对偶方法 (primal-dual method) 是设计组合优化问题算法的标准工具，它由 Dantzig、Ford 和 Fulkerson 提出，是一种多项式时间的算法。

PD方法的思路是从一个对偶可行解出发，逐步找到满足互补松弛条件的一组解。
$$
(\mathbf{P})\left\{\begin{array} { l l } 
{ \underset { \mathbf { x } \in \mathbb { R } ^ { n } } {\operatorname {minimize}} } & { \mathbf { c } ^ { \top } \mathbf { x } } \\
{ \text {subject to} } & { A \mathbf { x } = \mathbf { b } } \geq \mathbf{0} \\
{ } & { \mathbf { x } \geq \mathbf { 0 } }
\end{array} \qquad ( \mathbf { D } ) \left\{\begin{array}{ll}
\underset{\mathbf{u} \in \mathbb{R}^{m}}{\operatorname{maximize}} & \mathbf{u}^{\top} \mathbf{b} \\
\text {subject to} & \mathbf{u}^{\top} A \leq \mathbf{c}^{\top} \\
& \mathbf{u} \text { unrestricted }
\end{array}\right.\right.
$$
给定如上的原问题和对偶问题，$\mathbf{b} \geq 0$ 是一个 WLOG 但是有意义的条件。

线性规划的 complementary slackness 给出了可行解 $(\bar{\mathbf{x}}, \bar{\mathbf{u}})$ 是一组最优解的充要条件：

$$
\begin{align}
\bar{\mathbf{u}}^\top (A\bar{\mathbf{x}} - \mathbf{b}) = 0  \tag{1} \\
(\mathbf{A}^\top \bar{\mathbf{u}} - \mathbf{c})^\top \bar{\mathbf{x}} = 0 \tag{2}
\end{align}
$$

左边那个由解的可行性自动满足，右边

以下阐述 primal-dual 方法的思路和步骤。

首先，从一个对偶可行解 $\mathbf{u}$ 出发，我们希望找到一个方向 $\mathbf{v}$，使得从 $\mathbf{u}$ 出发沿着 $\mathbf{v}$ 方向前进一定距离，目标函数值 $\mathbf{u}^T \mathbf{b}$ 能得到提升。

记指标集 $J = \{i : u_i^\top A = c_i\}$，对于 $J$ 对应的约束，方向 $\mathbf{v}$ 必须满足 $\mathbf{v}^\top A_J \leq \mathbf{0}^\top$，这样才能保证存在 $t > 0$ 使得 $\mathbf{u} + t \mathbf{v}$ 依然是对偶可行的；对于其它约束，则并没有这样的限制。当然，必须谨记我们要找的是一个方向，此时 $\mathbf{v}$ 或者 $2 \mathbf{v}$ 都可以是我们的要的解，所以我们需要 normalize 一下。非线性规划里面，我们可以选择 $\| \mathbf{v} \|_2 \leq 1$ 作为 normalization constraint，但是在线性规划里面，选择 $\| \mathbf{v} \|_\infty \leq 1 \Rightarrow v_i \leq 1$ 是一个更好的选择！

由此我们得到寻找方向 $\mathbf{v}$ 的线性规划问题：
$$
\begin{array}{ll}
{\operatorname{maximize}} & \mathbf{v}^{\top} \mathbf{b} \\
\text {subject to } & \mathbf{v}^{\top} A_{J} \leq \mathbf{0}^{\top} \\
& v_{1}, \ldots, v_{m} \leq 1
\end{array} \tag{DRP}
$$
从这里可以看出 $\mathbf{b} \geq \mathbf{0}$ 的意义，normalization constraint $v_i \leq 1$ 是为了防止 $\mathbf{v}$ 无限增大，而那些小于0的 $v_i$ 趋于负无穷并不会增加目标函数值，所以没有必要添加相应的约束了。

这个问题我们把它叫做 dual restricted program (DRP)

+ 如果 DRP 的最优值是0，这意味着对偶问题(D)达到最优
+ 如果 DRP 的最优值大于0，这说明存在一个足够小的 $t>0$，使得 $\mathbf{u}$ 沿着 DRP 的解 $\mathbf{v}$ 前进一段距离能保持对偶可行性同时提升函数值！现在我们要找到最大的 $t$，$\mathbf{u} + t \mathbf{v}$ 必须要保证可行性，对于 指标集 $J$ 对应的约束，可行性是一定满足的。
  + 如果 $v_j^\top A \leq 0 , \; \forall j \notin J$ ，那么 $\mathbf{u}$ 沿着 $\mathbf{v}$ 前进多少都不会违背可行性，这说明对偶问题(D)是无上界的，从而原问题没有可行解。
  + 如果 $\exists j \notin J, \;v_j^\top A > 0$，那么可以选择的最大的 $t$ 是 $\min\limits_{j \notin J,\, v_j^\top A > 0} \displaystyle\frac{c_j - u_j^\top A}{v_j^\top A}$



这样，我们可以更新对偶可行解 $\mathbf{u} = \mathbf{u} + t \mathbf{v}$ .

继续这么做，就能不断逼近最优解。但是，这么做是很费力的，因为要不断地解一个新的线性规划。

注意到(DRP)的对偶问题是：











