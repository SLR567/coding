# 回文链表

给你一个单链表的头节点 `head` ，请你判断该链表是否为回文链表。如果是，返回 `true` ；否则，返回 `false` 。

**示例 1：**



![jupyter](images/234_1.jpg)


**输入：**head = [1,2,2,1]

**输出：**true

**示例 2：**

![jupyter](images/234_2.jpg)

**输入：**head = [1,2]

**输出：**false

**提示：**

- 链表中节点数目在范围`[1, 105]` 内
- `0 <= Node.val <= 9`
 

**进阶：**你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？


```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp=head
        tail=[]
        count=0
        if head is None:
            return True
        if head.next is None:
            return True
        while temp:
            tail.append(temp.val)
            temp=temp.next
            count=count+1
        while head:
            if tail[count-1]!=head.val:
                return False
            head=head.next
            count=count-1
        return True
```
