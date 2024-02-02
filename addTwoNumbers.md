# 两数相加

给你两个 **非空** 的链表，表示两个非负的整数。它们每位数字都是按照 **逆序** 的方式存储的，并且每个节点只能存储 **一位** 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

 

**示例 1：**

![jupyter](images/2_1.jpg)

>**输入：**l1 = [2,4,3], l2 = [5,6,4]

>**输出：**[7,0,8]

>**解释：**342 + 465 = 807.

**示例 2：**

>**输入：**l1 = [0], l2 = [0]

>**输出：**[0]

**示例 3：**

>**输入：**l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]

>**输出：**[8,9,9,9,0,0,0,1]

 

**提示：**

- 每个链表中的节点数在范围 `[1, 100] `内

- `0 <= Node.val <= 9`

- 题目数据保证列表表示的数字不含前导零


```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result_whole=ListNode(0)
        result=result_whole
        upgrade=0
        while l1 or l2:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            n=val1+val2+upgrade
            upgrade=n//10
            result.next=ListNode(n%10)
            result=result.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        if upgrade:
            result.next=ListNode(upgrade)
        return result_whole.next

        
```
