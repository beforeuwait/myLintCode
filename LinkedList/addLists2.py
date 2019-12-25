# coding=utf-8

"""
链表求和 II

描述: 假定用链表表示两个数，其中每个节点仅包含一个数字。
假设这两个数的数字顺序排列，请设计一种方法将两个数相加，并将其结果表现为链表的形式。

思路: 这题没啥好说的
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
    @param l1: The first list.
    @param l2: The second list.
    @return: the sum list of l1 and l2.
    """
    def addLists2(self, l1, l2):
        # write your code here
        l1_list, l2_list = [], []
        while l1 is not None:
            l1_list.append(str(l1.val))
            l1 = l1.next
        while l2 is not None:
            l2_list.append(str(l2.val))
            l2 = l2.next
        result = str(int(''.join(l1_list)) + int(''.join(l2_list)))
        tail = dummy = ListNode(-1)
        for i in result:
            tmp = ListNode(int(i))
            tail.next = tmp
            tail = tail.next
        return dummy.next
        