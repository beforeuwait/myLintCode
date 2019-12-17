# coding=utf-8

"""
翻转链表中第m个节点到第n个节点的部分

这个是翻转链表的升级版
还是困惑了我2个小时的时间
再一次强化了链表不关心位置，只关心指针指向

大体思路:
找到 翻转的前一位 prev
翻转需要翻转的那一部分，同时找到翻转前最后一位指向元素 以及翻转前的第一位 (因为成为翻转后的最后一位)
然后 前一位 prv 指向翻转后
然后链接后的最后一位 指向翻转前指向的最后那位

m =3 , n = 5

input: 0->1-2->3->4->5->6->7->null
可见翻转的部分为 2->3->5
prev = 1
bf = 6

output: 0->1->4->3->2->5->6->7->null

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
    @param head: ListNode head is the head of the linked list 
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        if m == n:
            return head
        btn = ListNode(0)   # 定义一个新的链表
        btn.next = head     # 为新的链表下一元素指向为head
        prev = btn          # 定义需要翻转链表的前一位元素
        for _ in range(m - 1):
            prev = prev.next    # 找到该元素
        cur, bf = None, None    # 定义翻转后的链表 以及 需要翻转链表指向的后一位
        start = prev.next       # 翻转链表的第一位
        bf_prev = start         # 也是最后连接需要翻转链表指向的后一位的前一位
        for _ in range(n -m + 1):
            temp = start.next
            start.next = cur
            if _ == (n - m):    # 也就是最后一次迭代时候，找到需要翻转链表指向的后一位
                bf = temp
            cur, start = start, temp
        bf_prev.next = bf       # 重新指向
        prev.next = cur         # 重新指向
        return btn.next
            