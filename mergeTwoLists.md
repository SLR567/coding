# 合并两个有序链表

将两个升序链表合并为一个新的 **升序** 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

**示例 1：**

![jupyter](images/21_1.jpg)

>**输入：**l1 = [1,2,4], l2 = [1,3,4]

>**输出：**[1,1,2,3,4,4]

**示例 2：**

>**输入：**l1 = [], l2 = []

>**输出：**[]

**示例 3：**

>**输入：**l1 = [], l2 = [0]

>**输出：**[0]
 

**提示：**

- 两个链表的节点数目范围是 `[0, 50]`

- `-100 <= Node.val <= 100`

- `l1` 和 `l2` 均按 **非递减顺序** 排列


```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result_whole=ListNode(-1)
        result=result_whole
        if list1==None and list2==None:
            return list1
        if list1==None:
            return list2
        if list2==None:
            return list1
        while list1!=None and list2!=None:
            if list1.val<=list2.val:
                result.next=list1
                list1=list1.next
            else:
                result.next=list2
                list2=list2.next
            result=result.next
        if list1!=None:
            result.next=list1
        if list2!=None:
            result.next=list2
        return result_whole.next

```
