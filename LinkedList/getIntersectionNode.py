# coding=utf-8

"""
两个链表的交叉

描述: 请写一个程序，找到两个单链表最开始的交叉节点。

思路:
我一开始的解法做了一个错误示范

我一开始想的是 把两个链表翻转
然后从头开始对比，不一致时。
那之前一个元素就是起点。
然后会发现一个问题就是

A:6->7->。。。->13->null
B:1->2->3->。。。->13->null

RA: 13->12->。。。->6->null
这对B的就有影响了
RB: 6->5->4->3->2->1->null
B的结构都变了
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
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        len_a, len_b = 0, 0
        tail_a, tail_b = headA, headB
        while tail_a:
            len_a += 1
            tail_a = tail_a.next
        while tail_b:
            len_b += 1
            tail_b = tail_b.next
        node_a, node_b = headA, headB
        while len_a > len_b:
            node_a = node_a.next
            len_a -= 1
        while len_a < len_b:
            node_b = node_b.next
            len_b -= 1
        while node_a is not node_b:
            node_a = node_a.next
            node_b = node_b.next
        return node_a

"""
错误示范
"""

class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        # 先翻转，然后向前读
        if headA is None or headB is None:
            return None
        head_b = self.reverseList(headB)
        head_a = self.reverseList(headA)
        print(head_a.val, head_b.val)
        xpoint = None
        while head_a and head_b:
            if head_a.val == head_b.val:
                xpoint = head_a.val
            head_a, head_b = head_a.next, head_b.next
        # 然后找到这段列表
        if xpoint:
            while True:
                if tail.val == xpoint:
                    break
                tail = tail.next
            return tail
        else:
            return None
    
    def reverseList(self, node):
        if node is None:
            return node
        cur = None
        while node:
            tmp = node.next
            node.next = cur
            cur = node
            node = tmp
        return cur 