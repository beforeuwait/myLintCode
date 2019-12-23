# coding=utf-8

"""
链表倒数第n个节点
描述:找到单链表倒数第n个节点，保证链表中节点的最少数量为n。

思路: 
利用快慢指针的原理
快指针先走 n， 然后一起走
直到 fast指针到了null时候  slow指针就到了倒数第n个数了

实际呢, 倒数第n个， 为顺数第 (num + 1 - n) 个
比如: 1,2,3,4,5,6,7 
num = 7
n = 3
顺数第5个:  7 + 1 -3 = 5
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
    @param: head: The first node of linked list.
    @param: n: An integer
    @return: Nth to last node of a singly linked list. 
    """
    def nthToLast(self, head, n):
        # write your code here
        # 快慢指针
        if head is None or n < 1:
            return head
        fast, slow = head, head
        for _ in range(n):
            fast = fast.next
        if fast is None:
            return slow
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        return slow.next