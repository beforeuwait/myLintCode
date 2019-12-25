# coding=utf-8

"""
链表组件
思路: 找断点，有一个断点则产生一个组件
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
    @param head: the head
    @param G: an array
    @return: the number of connected components in G
    """
    def numComponents(self, head, G):
        # Write your code here
        # 算断点
        set_g = set(G)
        result = 0
        while head:
            if head.val in set_g and (head.next is None or head.next.val not in set_g):
                result += 1
            head = head.next
        return result