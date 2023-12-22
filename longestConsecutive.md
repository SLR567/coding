# 最长连续序列

***题目：***
给定一个未排序的整数数组$nums$，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为$O(n)$的算法解决此问题。

题目要求 O(n) 复杂度。

* 用哈希表存储每个端点值对应连续区间的长度
* 若数已在哈希表中：跳过不做处理
* 若是新数加入：
  1. 取出其左右相邻数已有的连续区间长度 left 和 right
  2. 计算当前数的区间长度为：cur_length = left + right + 1
  3. 根据 cur_length 更新最大长度 max_length 的值
  4. 更新区间两端点的长度值


```python
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_dict = dict()
        
        max_length = 0
        for num in nums:
            if num not in hash_dict:
                left = hash_dict.get(num - 1, 0)
                right = hash_dict.get(num + 1, 0)
                
                cur_length = 1 + left + right
                if cur_length > max_length:
                    max_length = cur_length
                
                hash_dict[num] = cur_length
                hash_dict[num - left] = cur_length
                hash_dict[num + right] = cur_length
                
        return max_length
```
