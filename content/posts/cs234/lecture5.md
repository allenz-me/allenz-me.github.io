---
title: "Lecture 5: Value Function Approximation"
date: 2022-02-13
draft: false
slug: lecture5
toc: false
categories: ["算法与程序设计", "cs234"]
tags: []
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---


Many real world problems have enormous state and/or action spaces, so tabular representation is insufficient.


### Value Function Approximation

Represent a (state/state-action) value function with a parameterized function instead of a table

<img src="../figures/lecture5/image-20220212205318557.png" alt="image-20220212205318557" style="zoom:50%;" />





Many possible function approximators including

- Linear combinations of features
- Neural networks
- Decision trees
- Nearest neighbors
- Fourier/ wavelet bases






$$
\begin{aligned}
\mathbf{w}_{t+1} & \doteq \mathbf{w}_{t}-\frac{1}{2} \alpha \nabla\left[v_{\pi}\left(S_{t}\right)-\hat{v}\left(S_{t}, \mathbf{w}_{t}\right)\right]^{2} \\
&=\mathbf{w}_{t}+\alpha\left[v_{\pi}\left(S_{t}\right)-\hat{v}\left(S_{t}, \mathbf{w}_{t}\right)\right] \nabla \hat{v}\left(S_{t}, \mathbf{w}_{t}\right)
\end{aligned}
$$






### Monte Carlo VFA



![image-20220213154452411](../figures/lecture5/image-20220213154452411.png)

