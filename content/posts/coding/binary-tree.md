---
title: "二叉树的非递归遍历"
date: 2020-04-08
draft: false
slug: binary-tree-nonrecursive
categories: ["算法与程序设计"]
tags: ["二叉树", "Python"]
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---

## 前序遍历

前序遍历是最简单的，每弹出一个节点，就将该节点的右节点、左节点分别入栈。

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        st, res = [root], []
        while st:
            cur = stack.pop()
            if cur is not None:
                res.append(cur.val)
                stack.append(cur.right)
                stack.append(cur.left)
        return res
```

## 中序遍历

中序遍历，对二叉搜索树，其实就是从小到大依序输出。对每个节点，先一直向左走，向左走到尽头就弹出并向右走一步，继续上面的步骤。

```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        st, res = [], []
        cur = root
        while st or cur is not None:
            while cur is not None:
                st.append(cur)
                cur = cur.left
            cur = st.pop()
            res.append(cur.val)
            cur = cur.right
        return res
```

## 后续遍历

后序遍历，利用 `pre` 记录上一个访问过的结点，与当前结点比较，如果是当前结点的子节点，说明其左右结点均已访问，将当前结点出栈，更新 `pre` 记录的对象。

另一方面，它可以看成前序遍历“根、右、左”的逆序。

```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: 
            return []
        st, res = [root], []
        pre = None
        while st:
            cur = st[-1]
            if (cur.left is None and cur.right is None) or \
        (pre is not None and (pre is cur.left or pre is cur.right)):
                res.append(cur.val)
                pre = cur
                st.pop()
            else:
                if cur.right is not None:
                    st.append(cur.right)
                if cur.left is not None:
                    st.append(cur.left)
        return res
```

以下为前序遍历逆序：

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        st, res = [root], []
        while st:
            cur = stack.pop()
            if cur is not None:
                res.append(cur.val)
                stack.append(cur.left)
                stack.append(cur.right)
        res.reverse()
        return res
```