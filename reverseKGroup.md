# K 个一组翻转链表

给你链表的头节点 `head` ，每 `k` 个节点一组进行翻转，请你返回修改后的链表。

`k` 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 `k` 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

 

**示例 1：**

![jupyter](images/25_1.jpg)

>**输入：**head = [1,2,3,4,5], k = 2

>**输出：**[2,1,4,3,5]

**示例 2：**

![jupyter](images/25_2.jpg)

>**输入：**head = [1,2,3,4,5], k = 3

>**输出：**[3,2,1,4,5]
 

**提示：**
- 链表中的节点数目为 `n`
- `1 <= k <= n <= 5000`
- `0 <= Node.val <= 1000`
 

**进阶：**你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？


```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self, head, tail):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        result=ListNode(0)
        count_head=ListNode(-1)
        count_head.next=head
        count=0
        while count_head.next:
            count=count+1
            count_head=count_head.next
        if count<k:
            return head
        result.next = head
        pre = result
        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return result.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next
        
        return result.next

        
```
