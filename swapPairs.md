# 两两交换链表中的节点

给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

 

**示例 1：**

![jupyter](images/24_1.jpg)

>**输入：**head = [1,2,3,4]
>**输出：**[2,1,4,3]

**示例 2：**

>**输入：**head = []
>**输出：**[]

**示例 3：**

>**输入：**head = [1]
>**输出：**[1]
 

**提示：**

- 链表中节点的数目在范围 `[0, 100]` 内
- `0 <= Node.val <= 100`


```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result=ListNode(0)
        result.next=head
        temp=result
        if head==None:
            return head
        if head.next==None:
            return head
        while temp.next and temp.next.next:
            node1=temp.next
            node2=temp.next.next
            temp.next=node2
            node1.next=node2.next
            node2.next=node1
            temp=node1
        return result.next        
```
