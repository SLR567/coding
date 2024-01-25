# 移动零

给定一个数组 `nums`，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

`请注意` ，必须在不复制数组的情况下原地对数组进行操作。

## 示例 1:

- 输入: nums = [0,1,0,3,12]
- 输出: [1,3,12,0,0]

## 示例 2:

- 输入: nums = [0]
- 输出: [0]
 


```python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                zeros += 1
            else:
                i += 1
        nums.extend([0] * zeros)

```
