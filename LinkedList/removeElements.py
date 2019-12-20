# coding=utf-8

"""
删除链表中的元素

描述：删除链表中等于给定值 val 的所有节点。

一开始把我难住了，同时也发现一个问题

一开始的思路:
创建一个新的 ListNode

input:1->2->3->3->5->3
output: 1->2->5->3
一直不能处理 倒数第二个5->3 这个问题

新思路：

和第一个类似，但是并不创建新的链表
遇到等于 val 则指向后面的后面
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
    @param val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):
        # write your code here
        if head == None:
            return head
        temp = ListNode(-1)
        temp.next = head
        pre = temp
        while pre.next:
            if pre.next.val == val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return temp.next