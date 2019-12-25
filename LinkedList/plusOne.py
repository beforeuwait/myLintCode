# coding=utf-8

"""
加一链表

描述:给定一个非负整数，这个整数表示为一个非空的单链表，每个节点表示这个整数的一位。返回这个整数加一。
除了0本身，所有数字在最高位前都没有0。
列表的头节点存的是这个整数的最高位。

思路: 也是没啥好说的
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
    @param head: the first Node
    @return: the answer after plus one
    """
    def plusOne(self, head):
        # Write your code here
        if head is None:
            return head
        list_h = []
        while head:
            list_h.append(str(head.val))
            head = head.next
        result = int(''.join(list_h)) + 1
        tail = tmp = ListNode(-1)
        for i in str(result):
            tmp.next = ListNode(i)
            tmp = tmp.next
        return tail.next