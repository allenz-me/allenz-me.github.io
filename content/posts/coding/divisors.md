---
title: "给定自然数 N，如何求出所有约数？"
date: 2019-10-23
draft: false
slug: none
categories: ["算法与程序设计"]
tags: []
# 四个大类: 分析与概率, 算法与程序设计, 运筹与优化, 论文简读
---


**问题：给定自然数 N，如何求出 N 的所有约数？**

如 N = 198，它的约数有：[1, 2, 3, 6, 9, 11, 18, 22, 33, 66, 99, 198]

一个很自然的想法是：对从 2 到 $\\displaystyle\\frac{N}{2}$ 的所有数进行遍历，看这个数是否能整除N。这样的时间复杂度是 $O(N)$

有没有更快一点的呢？

我们可以这样考虑：如果有非平方数 $N=a\\times b$，其中 $a<b$，那么一定有 $a<\\sqrt N, b > \\sqrt N$，对于每一个小于 $\\sqrt N$ 的 $N$ 的约数 $a$，都有一个对应的 $b>\\sqrt N$，$b$ 也是 $N$ 的约数，因此我们只需要遍历 2 到 $\\sqrt N$ 就可以了，每一次整除都对应了 $N$ 的两个约数，最后只需要再考虑一下 $N$ 是不是平方数就可以了。这样，时间复杂度就被优化到了$\\sqrt N$，是个非常大的进步了。

下面贴代码

Python：

```python
from typing import List

def divisors(N:int) -> List[int]:
	'''return all the factors of N'''
    if N == 1:
		return [1]
    res = [1, N]
	sqrt = int(pow(N, 1/2))
	for i in range(2, sqrt + 1):
		if N % i == 0:
			res.append(i)
			res.append(N // i)
	if sqrt ** 2 == N:
		res.append(sqrt)

	return res

print(sorted(divisors(198)))    
# [1, 2, 3, 6, 9, 11, 18, 22, 33, 66, 99, 198]
```



Java：

```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Divisors {
    public static List<Integer> divisors(int N) {
        List<Integer> res = new ArrayList<>();
        res.add(1);
        if (N == 1) return res;
        res.add(N);
        final int sqrt = (int) Math.sqrt(N);
        for (int i = 2; i < sqrt; i++) {
            if (N % i == 0) {
                res.add(N / i);
                res.add(i);
            }
        }
        if (sqrt * sqrt == N) res.add(sqrt);
        return res;
    }

    public static void main(String[] args) {
        List<Integer> res = divisors(198);
        // stream是Java 8的新语法
        System.out.println(Arrays.toString(res.stream().sorted().toArray()));
    }
}

```

C++

```c++
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

vector<int> divisors(int N) {
    vector<int> res{1};
    if (N == 1) return res;
    res.push_back(N);
    const int sq = sqrt(N);
    for (int i = 2; i < sq; i++) {
        if (N % i == 0) {
            res.push_back(i);
            res.push_back(N / i);
        }
    }
    if (sq * sq == N) res.push_back(sq);
    return res;
}

int main() {
    vector<int> res = divisors(198);
    sort(res.begin(), res.end());
    for (auto n : res) {
        cout << n << " ";
    }
}
```
