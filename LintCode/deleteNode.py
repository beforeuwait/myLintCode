# coding=utf-8

"""
在O(1)时间复杂度删除链表节点

描述:给定一个单链表中的一个等待被删除的节点(非表头或表尾)。请在在 O(1) 时间复杂度删除该链表节点。

思路: 当前待删除节点复制为下一节点就行了 
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
    @param: node: the node in the list should be deleted
    @return: nothing
    """
    def deleteNode(self, node):
        # write your code here
        if not node or not node.next:
            node = None
            return
        node.val = node.next.val
        node.next = node.next.next
            