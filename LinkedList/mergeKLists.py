# coding=utf-8

"""
合并k个排序链表

描述: 合并k个排序链表，并且返回合并后的排序链表。尝试分析和描述其复杂度。

思路: 并归的思想

将数列里的链表 两两合并排序
不断重复，直到只剩一个
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
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        # 两两合并
        if not lists:
            return None
        while len(lists) > 1:
            new_lists = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    new_list = self.merge_2list(lists[i], lists[i + 1])
                else:
                    new_list = lists[i]
                new_lists.append(new_list)
            lists = new_lists
        return lists[0]

    def merge_2list(self, l1, l2):
        tail = dummy = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next