# coding=utf-8
"""
链表节点计数
描述:计算链表中有多少个节点.

就是遍历一遍数一下元素
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
    @param head: the first node of linked list.
    @return: An integer
    """
    def countNodes(self, head):
        # write your code here
        if head is None:
            return 0
        count = 0
        while head is not None:
            head = head.next
            count += 1
        return count