---
title: "线段树—Python"
date: 2020-04-10
draft: false
slug: segment-tree
categories: ["算法与程序设计"]
tags: ["线段树", "Python"]
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---

线段树是能够在 $O(\log n)$ 时间内完成查询数组区间和，以及修改数组某一处的值的数据结构。

本质上是一棵树，因此可以用数组来表示（参考堆是怎么表示的）。

用一个**长度是原数组长度4倍**的新数组足矣。

线段树的各个操作都是递归进行的。

以下是线段树的一个 Python 实现

```python
class SegmentTree:
    def __init__(self, nums):
        self._nums = nums
        self._length = len(nums)
        self._array = [None] * (len(nums) * 4)
        self.build(0, len(nums), 0)

    def build(self, left, right, k):
        if left == right - 1:
            self._array[k] = self._nums[left]
        else:
            mid = (left + right) // 2
            self.build(left, mid, 2 * k + 1)
            self.build(mid, right, 2 * k + 2)
            self._array[k] = self._array[2*k+1] + self._array[2*k+2]

    def update(self, idx, val):
        """将num的idx处的值修改为val"""
        assert 0 <= idx < self._length
        self._update(0, self._length, 0, idx, val)

    def _update(self, left, right, k, idx, val):
        if left == right - 1 == idx:
            self._array[k] = val
        else:
            mid = (left + right) // 2
            if idx < mid:
                self._update(left, mid, 2*k+1, idx, val)
            else:
                self._update(mid, right, 2*k+2, idx, val)
            self._array[k] = self._array[2*k+1] + self._array[2*k+2]

    def query(self, begin, end):
        """查询数组[begin, end)的和"""
        assert 0 <= begin < end <= self._length
        return self._query(begin, end, 0, self._length, 0)

    def _query(self, begin, end, left, right, k):
        if begin >= end:
            return 0
        if begin == left and end == right:
            return self._array[k]
        mid = (left + right) // 2
        if mid <= begin:
            return self._query(begin, end, mid, right, 2*k+2)
        elif begin < mid < end:
            return self._query(begin, mid, left, mid, 2*k+1) + \
                    self._query(mid, end, mid, right, 2*k+2)
        else:    # end <= mid
            return self._query(begin, end, left, mid, 2*k+1)
```

以上刚好50行代码。
附上写过的一个单元测试：

```python
class TreeTest(unittest.TestCase):

    def testSegmentTree(self):
        for _ in range(1000):
            nums = [randint(0, 200) for _ in range(randint(10, 1000))]
            st = SegmentTree(nums)
            for _ in range(1000):
                update = [randint(0, len(nums) - 1), randint(-100, 1000)]  # (idx, val)
                nums[update[0]] = update[1]
                st.update(update[0], update[1])
                query = sorted([randint(0, len(nums)), randint(0, len(nums))])
                if query[0] == query[1]:
                    continue
                self.assertEqual(st.query(query[0], query[1]), sum(nums[query[0]:query[1]]))
```