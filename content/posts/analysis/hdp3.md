---
title: "Random vectors in high dimensions"
date: 2021-01-01
draft: false
slug: hdp3
categories: ["分析与概率", "高维概率"]
tags: ["随机向量", "次高斯分布"]
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---


<!-- # Random vectors in high dimensions -->

本书第三章主要讲的是高维空间中的随机向量。


第二章介绍了随机变量的集中程度，自然我们会进一步关注随机向量的集中程度。本章研究的主要内容就是维数非常高的随机向量 $X = (X_1, X_2, \dots, X_n) \in \mathbb{R}^n$。数据科学中高维分布无处不在！

## Concentration of the norm

高维的随机向量 $X$ 的样本是欧式空间中的一个点，因此我们会用**到原点的欧式距离$\|X \|_2$来刻画它的集中程度**。

首先从最简单的随机向量考虑起，如果 $X=(X_1, X_2, ..., X_n)$ 各个分量都是独立零均值且单位方差的随机变量，则：

$$
\mathbb{E}\|X\|_{2}^{2}=\mathbb{E} \sum_{i=1}^{n} X_{i}^{2}=\sum_{i=1}^{n} \mathbb{E} X_{i}^{2}=n \\
$$

这说明大致上 $\lVert X \rVert_2 \sim \sqrt{n}$。 **如果 $X$ 的各个分量都是次高斯随机变量，那么这足以保证 $X$ 大致分布在以 $\sqrt{n}$ 为半径的球面附近了。** 此时成立不等式：

$$
\mathbb{P}\left\{\left|\|X\|_{2}-\sqrt{n}\right| \geq t\right\} \leq 2 \exp \left(-\frac{c t^{2}}{K^{4}}\right) \quad \text { for all } t \geq 0 \\
$$

这意味着，$X$ 的样本点都集中在半径为 $\sqrt{n}$ 的球面附近！

## Isotropic random vectors

不失一般性，只考虑那些零均值的随机向量，这时候它们的协方差矩阵表示为 $\mathbb{E}XX^T$。

协方差矩阵一定是一个半正定矩阵。高斯分布协方差矩阵的特征值和特征向量揭示了分布情况，在最大特征值对应的特征向量方向，分布得更加广泛一些。如果随机向量 $X$ 的协方差矩阵只有几个较大的特征值，而剩余的特征值都很小，说明该随机向量只在很小的几个维度包含信息。

定义 **Isotropic random vectors** 是那些零均值并且满足 $\Sigma=\mathbb{E}XX^T=\mathrm{I}_n$ 的随机向量。这种随机向量的各个分量之间没有相关性，但并不代表它们是独立的。对于一般的随机向量，可以用变换 $Z:=\Sigma^{-1/2}(X - \mu)$ 来标准化，这可以消除分量之间的相关性。

各向同随机向量有一个等价的定义：
$$
X \text{ is isotropic} \Longleftrightarrow \mathbb{E}\langle X, x \rangle ^2 = \|x \|_2^2  \;\; \text{ for all } x \in \mathbb{R}^n
$$
这说明，各向同随机向量投影到任何一个一维分量上都具有单位方差。

各向同随机向量只是一种抽象的存在，但是它所具有的性质非常让人惊讶，而这些性质都可以落到更具体的分布之上。

首先，是 $\mathbb{E}\| X\|_2^2=\operatorname{tr}(\mathbb{E}XX^T)=n$，这是一个显而易见的长度上的性质。

接着，**设 $X, Y$ 都是各向同随机向量，那么 $X, Y$ 的夹角，会呈现出随着维数 $n$ 的增加而趋于正交的特点**。

$$
\mathbb{E}\langle X, Y\rangle^{2}=\mathbb{E}_{Y} \mathbb{E}_{X}\left[\langle X, Y\rangle^{2} \mid Y\right] = \mathbb{E}\langle X, Y\rangle^{2}=\mathbb{E}_{Y}\|Y\|_{2}^{2} = n \\
$$

所以 $|\langle X, Y \rangle| \sim \sqrt{n},\, \|X\| \sim \sqrt{n}, \|Y\| \sim \sqrt{n}$，即有：$| \langle X, Y \rangle| \sim \displaystyle\frac{1}{\sqrt{n}}$。如果$X_i \sim X,\; Y_i \sim Y$，这两个高维空间中的样本点，随着维数的增加，其夹角的余弦值是趋于0的。

举个例子，当 $n$ 很大的时候，从 ${N}(0, \mathrm{I}_n)$ 中抽两个样本点，这两个点几乎是正交的。

最后是关于两个各向同随机向量距离的性质，结合上述两点，联系勾股定理不难注意到： $\mathbb{E}\| X - Y \|_2^2 = 2n$。

<br>

接下来是各向同随机向量的例子：

+ 球面上的均匀分布：$X \sim \operatorname{Unif}\left(\sqrt{n} S^{n-1}\right)$

注意，该分布不包含球的内部。这是一个典型的，各分量不相关，但是不独立的随机向量。它各向同的证明要用到曲线积分。

+ 高维对称伯努利分布：$X \sim \operatorname{Unif}\left(\{-1,1\}^{n}\right)$

+ 标准的多元正态分布：$g \sim  N\left(0, I_{n}\right)$

正态分布的一大特点就是不相关即独立。**另一个重要性质是，任意的多元正态分布投影在某条直线上，得到的仍然是正态分布，这是后续定义次高斯随机向量的出发点。**

**Similarity of normal and spherical distributions**

虽然低维的标准正态分布，给我们的感觉是，集中在原点附近的球内，但是，随着维数的增加，它的次高斯性开始显现了，本文最开始提到，$\| g\|$ 在 $n$ 很大的时候集中在半径为 $\sqrt{n}$ 的球面上。

$$
{N} (0, \mathrm{I}_n) \to \operatorname{Unif}\left(\sqrt{n} S^{n-1}\right)\: \text{ as }\: n \to \infty \\
$$

<img src="../figures/hdp3/image-20220513162418407.png" alt="image-20220513162418407" style="zoom:50%;" />

如上图所示，左边表示低维的标准高斯分布，右边表示高维的标准高斯分布。



另外两个例子，分别是用在信号处理和凸几何中的。一个是 *frame*，它是非常稀疏的离散各向同分布。另一个讲的是，对于$\mathrm{R}^n$中每个内点非空的凸集$K$，都可以对应一个零均值随机向量$X$。如果$\Sigma = \mathbb{E} XX^T$，那么$Z \sim \operatorname{Unif}\left(\Sigma^{-1 / 2} K\right)$是一个各向同随机向量。线性变换$\Sigma ^ {-1/2}$可以把凸集$K$的形状变得更加规整。

## Sub-gaussian distributions in higher dimensions

次高斯分布，本质是正态分布集中性质的推广，它的定义思想，来自正态分布的一条重要性质：投影在任意一个方向上都是正态分布，并且分布被这些投影所决定！

因此，定义 $X$ 是次高斯随机向量，当且仅当对任意的 $x \in \mathrm{R}^n$，$\langle X, x \rangle$ 是次高斯随机变量，且定义其次高斯模为：

$$
\|X\|_{\psi_{2}}=\sup _{x \in S^{n-1}}\|\langle X, x\rangle\|_{\psi_{2}} \\
$$

如果随机向量 $X=(X_1, \dots, X_n) \in \mathbb{R}^n$ 的各个分量都是次高斯随机变量，那么它自然能成为次高斯随机向量，且有 $\| X \|_{\psi_2} \leq C \max \|X_i\|_{\psi_2}$ 。



## Application: Grothendieck’s inequality and semideﬁnite programming



**Grothendieck’s inequality**

考虑矩阵 $$
