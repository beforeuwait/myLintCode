# coding=utf-8

"""
相反的顺序存储

思路：
就是遍历链表，然后把值都插入到list 的第0位
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
    @param head: the given linked list
    @return: the array that store the values in reverse order 
    """
    def reverseStore(self, head):
        # write your code here
        result = []
        while head is not None:
            result.insert(0, head.val)
            head = head.next
        return result