# coding=utf-8

"""
奇偶链表

描述:给定单链表，将所有奇数节点连接在一起，然后将偶数节点连接在一起。
请注意，这里我们讨论的是节点编号，而不是节点中的值。

思路: 没啥好说的
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
    @param head: a singly linked list
    @return: Modified linked list
    """
    def oddEvenList(self, head):
        # write your code here
        if head is None:
            return head
        tmp_1 = ListNode(-1)
        tmp_2 = ListNode(-1)
        tail_1, tail_2 = tmp_1, tmp_2
        
        count = 1
        while head is not None:
            if count % 2 == 1:
                tmp_1.next = head
                tmp_1 = tmp_1.next
            else:
                tmp_2.next = head
                tmp_2 = tmp_2.next
            head = head.next
            count += 1
        tmp_2.next = None
        tmp_1.next = tail_2.next
        return tail_1.next