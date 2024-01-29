## 反转链表

给你单链表的头节点 `head` ，请你反转链表，并返回反转后的链表。

**示例 1：**

![jupyter](images/206_1.jpg)

- **输入：**head = [1,2,3,4,5]

- **输出：**[5,4,3,2,1]

**示例 2：**

![jupyter](images/206_2.jpg)

- **输入：**head = [1,2]

- **输出：**[2,1]


**示例 3：**

- **输入：**head = []
- **输出：**[]

**提示：**

- 链表中节点的数目范围是 `[0, 5000]`
- `-5000 <= Node.val <= 5000`
 

**进阶：**链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？


```python
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previousH=None
        while head is not None:
            temp=head.next
            head.next=previousH
            previousH=head
            head=temp
        head=previousH
        return head
```
