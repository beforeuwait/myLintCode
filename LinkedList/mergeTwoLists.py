# coding=utf-8

"""
合并两个排序链表

描述:将两个排序链表合并为一个新的排序链表

思路: 本身是排序了链表，就像拉链一样合并就行了
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
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        dummy = ListNode(-1)
        tail = dummy
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1 is not None:
            tail.next = l1
        else:
            tail.next = l2
        return dummy.next