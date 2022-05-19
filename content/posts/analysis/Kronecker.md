---
title: "张量积 Tensor product"
date: 2020-07-07
draft: false
slug: tensor-prod
toc: false
categories: ["分析与概率"]
tags: []
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---

### Tensor product of vectors

令 $x \in \mathbb{R}^m, y \in \mathbb{R}^n$，定义 $x, y$ 的张量积 $x \otimes y$ 为 $m \times n$ 的矩阵 $(x \otimes y)_{ij} = x_iy_j$，即 $x \otimes y = x y^T$ .

特别地，坐标向量的张量积 $e_i \otimes e_j \in \mathbb{R}^{m \times n}$ 是一个仅在第 $i$ 行第 $j$ 列为 1，其余为 0 的矩阵。



令 $\mathcal{E}_m = \{e_i\}_{i=1}^m$ 是 $\mathbb{R}^m$ 的一组基，$\mathcal{E}_n = \{e_i\}_{i=1}^n$ 是 $\mathbb{R}^n$ 的一组基，则：
$$
\mathcal{E}_{m, n}=\left\{{e}_{i} \otimes {e}_{j}\right\}_{(i, j)=(0,0)}^{(M-1, N-1)}
$$
是 $\mathbb{R}^{m \times n}$ 的一组基，也就是说，它也是线性空间 $\mathcal{L}(\mathbb{R}^m, \mathbb{R}^n)$ 的基。



映射 $F(x, y) = x \otimes y$ 是双线性的 (bi-linear)。



### Tensor product of matrices

如果 $S \in \mathcal{L}(\mathbb{R}^m), T \in \mathcal{L}(\mathbb{R}^n)$，定义 $S \otimes T$  是一个 $\mathcal{L}(\mathbb{R}^m, \mathbb{R}^n) \to \mathcal{L}(\mathbb{R}^m, \mathbb{R}^n)$ 的线性算子。

确定一个线性算子只需要确定它在一组基下的像即可：

$$
(S \otimes T) (e_i \otimes e_j) = (Se_i \otimes Te_j)
$$

因为 $(S\otimes T)$ 是线性的，所以如果 $x \in \mathbb{R}^m, y \in \mathbb{R}^n$ ，则 $(S \otimes T) (x \otimes y) = (Sx )\otimes (Ty) = (Sx)(Ty)^T$



### Computation

如果 $X \in \mathbb{R}^{m \times n}$，则 $(S \otimes T)X = SXT^T$，注意到：
$$
\begin{aligned}
(S \otimes T)\left(\boldsymbol{e}_{i} \otimes \boldsymbol{e}_{j}\right) &=\left(S \boldsymbol{e}_{i}\right) \otimes\left(T \boldsymbol{e}_{j}\right) \\
&=\left(\operatorname{col}_{i}(S)\right) \otimes\left(\operatorname{col}_{j}(T)\right)=\operatorname{col}_{i}(S)\left(\operatorname{col}_{j}(T)\right)^{T} \\
&=\operatorname{col}_{i}(S) \operatorname{row}_{j}\left(T^{T}\right)=S\left(\boldsymbol{e}_{i} \otimes \boldsymbol{e}_{j}\right) T^{T}
\end{aligned}
$$
此外：
$$
\begin{aligned}
&(S \otimes I) X=S X \\
&(I \otimes T) X=X T^{T}=\left(T X^{T}\right)^{T}
\end{aligned}
$$
因为：
$$
\left(S_{1} \otimes T_{1}\right)\left(S_{2} \otimes T_{2}\right) X=S_{1}\left(S_{2} X T_{2}^{T}\right) T_{1}^{T}=\left(S_{1} S_{2}\right) X\left(T_{1} T_{2}\right)^{T}=\left(\left(S_{1} S_{2}\right) \otimes\left(T_{1} T_{2}\right)\right) X
$$
所以：$(S_1 \otimes T_1)(S_2 \otimes T_2) = (S_1S_2) \otimes (T_1T_2)$



### Change of bases in tensor products

如果 $\mathcal{B}_1 = \{v_i\}_{i=1}^m$ 是 $\mathbb{R}^m$ 的一组基，$\mathcal{B}_2 = \{w_j\}_{j=1}^n$ 是 $\mathbb{R}^n$ 的一组基，那么 $\{v_i \otimes w_j\}_{(i, j) = (1, 1)}^{(m, n)}$ 是 $\mathbb{R}^{m \times n}$ 的一组基，记为 $\mathcal{B}_1 \otimes \mathcal{B}_2$ 。





克罗内克积是两个任意大小的矩阵间的运算，对于 $A_{m\times n}, B_{p\times q}$，其克罗内克积是一个 $mp\times nq$ 的矩阵：
$$
A \otimes B=\left[\begin{array}{ccc}a_{11} B & \cdots & a_{1 n} B \\ \vdots & \ddots & \vdots \\ a_{m 1} B & \cdots & a_{m n} B\end{array}\right]
$$

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