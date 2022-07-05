---
title: "H-index 的计算"
date: 2022-03-02
draft: false
toc: false
slug: h-index
categories: ["算法与程序设计"]
tags: []
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---


一名科研人员的 h 指数是指 ta 的 (n 篇论文中) 总共有 h 篇论文分别被引用了至少 h 次。且其余的 n - h 篇论文每篇被引用次数不超过 h 次。

如果 n 篇论文已经排序好，那么使用二分法能达到 $O(\\log n)$ 的时间复杂度。

```python
def hIndex(self, citations: List[int]) -> int:
    n = len(citations)
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if citations[mid] < n - mid:
            lo = mid + 1
        else:
            hi = mid
    return n - lo
```

使用线性扫描的时间复杂度是 $O(n)$

```python
def hIndex(self, citations: List[int]) -> int:
    citations.sort(reverse=True)
    res = 0
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            res = max(res, i + 1)
    return res
```

如果未排序，排序后再二分的复杂度是 $O(n \\log n)$。

也可直接使用桶排序，发表 n 篇文章，h 指数最高能达到 n，因此维护一个 n + 1 大小的桶再线性扫描即可。


```python
def hIndex(self, citations: List[int]) -> int:
    n = len(citations)
    bucket = [0] * (n + 1)
    for i in citations:
        bucket[min(i, n)] += 1
    
    cnt = 0
    for i in reversed(range(n + 1)):
        cnt += bucket[i]
        if cnt >= i:
            return i
    return 0
```


