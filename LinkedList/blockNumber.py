# coding=utf-8

"""
链表中的连通分量

描述:给定一个双向链表和一个节点数组。
如果节点彼此连接(这意味着我们可以通过其中任何一个节点访问任何节点)，那么我们可以将它们视为一个块。
查找给定数组中的块数。

思路: 没啥好说的，还是找断点
"""

"""
Definition of DoublyListNode
class ListNode(object):
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""

class Solution:
    """
    @param head: the given doubly linked list
    @param nodes: the given nodes array
    @return: the number of blocks in the given array
    """
    def blockNumber(self, head, nodes):
        # write your code here
        set_n = set(nodes)
        result = 0
        while head is not None:
            if head.val in set_n and (head.next is None or head.next.val not in set_n):
                result += 1
            head = head.next
        return result