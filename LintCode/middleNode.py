# coding=utf-8

"""
链表的中间结点

思路：利用快慢指针
也是之前一道题遇到的
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
    @param head: the head node
    @return: the middle node
    """
    def middleNode(self, head):
        # write your code here.
        # 用快慢的原理
        if head is None:
            return head
        if head.next is None:
            return head
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow