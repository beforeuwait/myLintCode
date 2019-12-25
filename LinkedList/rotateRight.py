# coding=utf-8

"""
旋转链表

描述:给定一个链表，旋转链表，使得每个节点向右移动k个位置，其中k是一个非负数

思路: 每一次遍历到倒数第二位停， 然后把最后一个元素放到第一位去
k是多大，就迭代几次 ，因此时间复杂度为 (n-1)*k 即为 O(n)
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
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotateRight(self, head, k):
        # write your code here
        if head is None:
            return head
        for _ in range(k):
            head = self.doCycle(head)
        return head
    
    def doCycle(self, head):
        # 前进一位
        if head.next is None:
            return head
        tail = head
        tmp = None
        while head is not None:
            if head.next.next is None:
                tmp = head
                break
            head = head.next
        start = tmp.next
        start.next = tail
        tmp.next = None
        return start