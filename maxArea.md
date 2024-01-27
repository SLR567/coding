# 盛最多水的容器

给定一个长度为 `n` 的整数数组 `height` 。有 `n` 条垂线，第 `i` 条线的两个端点是 `(i, 0)` 和 `(i, height[i])` 。

找出其中的两条线，使得它们与 `x` 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

## 示例 1：
- 输入：[1,8,6,2,5,4,8,3,7]
- 输出：49 
- 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。


## 示例 2：

- 输入：height = [1,1]
- 输出：1


```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length=len(height)
        i=0
        j=length-1
        ma=0
        a=0
        while i<j:
            if height[i]<height[j]:
                a=height[i]*(j-i)
                ma=max(ma,a)
                i=i+1
            else:
                a=height[j]*(j-i)
                ma=max(ma,a)
                j=j-1
        return ma
```
