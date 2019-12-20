# coding=utf-8

"""
删除链表中倒数第n个节点

描述: 给定一个链表，删除链表中倒数第n个节点，返回链表的头节点。

思路:
这题不看解析，我绝对是想不出还能这样解。 
按照我最初的思路，先将链表翻转，然后去顺数第n位，然后再翻转
这个时间复杂度为 O(3n)

最佳答案，还是快慢指针
快指针先跑n次，然后慢指针再一起跑。 当快指针为None时候 慢指针就是要删除的那一位

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
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # 利用快慢指针
        dummy = ListNode(-1)
        dummy.next = head
        tail = dummy
        for i in range(0, n):
            head = head.next
        while head is not None:
            head = head.next
            tail = tail.next
        tail.next = tail.next.next
        return dummy.next