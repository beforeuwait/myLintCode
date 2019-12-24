# coding=utf-8

"""
带环链表

描述:给定一个链表，判断它是否有环。

思路: 经典快慢指针，如果是环，快指针会遇到慢指针

偶数环 O(n)
奇数环 O(2n)
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
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        if head is None:
            return False
        fast, slow = head, head
        while True:
            if fast.next is not None:
                fast = fast.next.next
                slow = slow.next
                if fast is None or slow is None:
                    return False
                elif fast == slow:
                    return True
            else:
                return False
        return False
            