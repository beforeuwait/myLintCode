# coding=utf-8

"""
向循环有序链表插入节点

描述:给一个来自已经排过序的循环链表的节点，
写一个函数来将一个值插入到循环链表中，并且保持还是有序循环链表。
给出的节点可以是链表中的任意一个单节点。返回插入后的新链表。

思路: 这题很有意思啊
首先是排序
链表本身是排序了的 有从大到小 有从小到大

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
    @param: node: a list node in the list
    @param: x: An integer
    @return: the inserted new list node
    """
    def insert(self, node, x):
        # write your code here
        new_node = ListNode(x)
        if node is None:
            node = new_node
            node.next = node
            return node
        cur, pre = node, None
        while cur:
            pre = cur
            cur = cur.next
            if x <= cur.val and x >= pre.val:
                break
            if pre.val > cur.val and (x < cur.val or x > pre.val):  # x pre > cur 大到小
                break
            if cur is node:
                break
            
        new_node.next = cur
        pre.next = new_node
        
        return new_node