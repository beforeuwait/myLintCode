# coding=utf-8

"""
回文链表

描述:设计一种方式检查一个链表是否为回文链表。

思路: 什么是回文链表 ，就是前后一致
比如  1->2->2->1->null
比如  1->2->3->2->1->null

所以啊， 首先找到中点，将链表分为两块 left和 right
然后 转置 right 为 right_r
然后 开始对比 left 和 right_r
如果一致 则为 回文链表
不一致则不是 回文链表

奇数位的链表   1->2->3->2->1
left: 1->2->3->null
right: 2->1->null
对比的是前两位

偶数位的链表    1->2->3->3->2->1
left: 1->2->3->null
right: 3->2->1->null
对比的是全部
"""

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: A ListNode.
    @return: A boolean.
    """
    def isPalindrome(self, head):
        # write your code here
        if head is None or head.next is None:
            return True
        left = head
        pivot = self.findPivot(head)
        right = pivot.next
        pivot.next = None
        right_r = self.reverseList(right)
        result = True
        while left and right_r:
            if left.val != right_r.val:
                result = False
            left = left.next
            right_r = right_r.next
        return result
    
    def findPivot(self, node):
        if node is None:
            return node
        slow, fast = node, node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseList(self, node):
        if node is None:
            return node
        cur = None
        while node:
            tmp = node.next
            node.next = cur
            cur = node
            node = tmp
        return cur