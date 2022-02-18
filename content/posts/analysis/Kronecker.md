---
title: "克罗内克积（Kronecker）"
date: 2020-07-07
draft: false
slug: kronecker
toc: false
categories: ["分析与概率"]
tags: []
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---


克罗内克积是两个任意大小的矩阵间的运算，对于$A_{m\times n}, B_{p\times q}$，其克罗内克积是一个$mp\times nq$的矩阵：

$$A \otimes B=\left[\begin{array}{ccc}a_{11} B & \cdots & a_{1 n} B \\ \vdots & \ddots & \vdots \\ a_{m 1} B & \cdots & a_{m n} B\end{array}\right]$$

**克罗内克积满足双线性性和结合律：**

+ $A \otimes(B+C)=A \otimes B+A \otimes C \quad(\text { if } B \text { and } C \text { have the same size })$
+ $(A+B) \otimes C=A \otimes C+B \otimes C \quad(\text { if } A \text { and } B \text { have the same size })$
+ $(k A) \otimes B=A \otimes(k B)=k(A \otimes B)$
+ $(A \otimes B) \otimes C=A \otimes(B \otimes C)$

**克罗内克积通常不满足交换律。**

**混合乘积性质**

$(\mathbf{A} \otimes \mathbf{B})(\mathbf{C} \otimes \mathbf{D})=\mathbf{A} \mathbf{C} \otimes \mathbf{B} \mathbf{D}$

**克罗内克和**

对 $A_{n\times n}, B_{m\times m}$，定义：

$$
\mathbf{A} \oplus \mathbf{B}=\mathbf{A} \otimes \mathbf{I}_{m}+\mathbf{I}_{n} \otimes \mathbf{B}
$$

**克罗内克积与迹和行列式**

+ $\operatorname{tr}(\mathbf{A} \otimes \mathbf{B})=\operatorname{tr} \mathbf{A} \operatorname{tr} \mathbf{B} \quad$ 
+ $\operatorname{det}(\mathbf{A} \otimes \mathbf{B})=(\operatorname{det} \mathbf{A})^{m}(\operatorname{det} \mathbf{B})^{n} \quad \mathrm{for}\;\; A_{n\times n}, B_{m\times m}$
+ $\operatorname{rank}(\mathbf{A} \otimes \mathbf{B})=\operatorname{rank} \mathbf{A} \operatorname{rank} \mathbf{B}$

$vec(X)$ 表示矩阵 $X$ 的向量化，它是把 $X$ 的所有列堆起来所形成的列向量。