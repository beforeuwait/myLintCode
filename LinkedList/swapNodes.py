# coding=utf-8 

"""
交换链表当中两个节点

描述:给你一个链表以及两个权值v1和v2，交换链表中权值为v1和v2的这两个节点。
保证链表中节点权值各不相同，如果没有找到对应节点，那么什么也不用做。

注意事项
你需要交换两个节点而不是仅仅交换节点的权值

思路:
我一开始就是皮一下，找到v1 和 v2 对于的节点是否存在
如果存在，则交换节点的val值

好了，正儿八经思路，需要知道 交换的2个节点的 前后位置
交换节点需要考虑的地方有

一。 v1 v2 不连续
二。 v1 v2 连续 且  v1.next = v2
三。 v1 v2 连续 且  v2.next = v1
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
    @param head: a ListNode
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """
    def swapNodes(self, head, v1, v2):
        # write your code here
        dummy = ListNode(-1)
        dummy.next = head
        v1_left, v1x, v1_right = None, None, None
        v2_left, v2x, v2_right = None, None, None
        tail = dummy
        prev = dummy
        while tail is not None:
            if tail.val == v1:
                v1_left = prev
                v1x = tail
                v1_right = tail.next
            elif tail.val == v2:
                v2_left = prev
                v2x = tail
                v2_right = tail.next
            prev = tail
            tail = tail.next
        if v1x is not None and v2x is not None:
            if v1x.next is v2x:
                v1_left.next = v2x
                v1x.next = v2_right
                v2x.next = v1x
            elif v2x.next is v1x:
                v2_left.next = v1x
                v2x.next = v1_right
                v1x.next = v2x
            else:
                v1_left.next = v2x
                v1x.next = v2_right
                v2_left.next = v1x
                v2x.next = v1_right
        return dummy.next

"""
皮一下
"""

class Solution_error:
    """
    @param head: a ListNode
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """
    def swapNodes(self, head, v1, v2):
    # 这是错误示范
    t1, t2 = False, False
    tail = gozi = head
    while tail:
        if tail.val == v1:
            t1 = True
        elif tail.val == v2:
            t2 = True
        tail = tail.next
    if t1 and t2:
        while gozi:
            if gozi.val == v1:
                gozi.val = v2
            elif gozi.val == v2:
                gozi.val = v1
            gozi = gozi.next
    return head