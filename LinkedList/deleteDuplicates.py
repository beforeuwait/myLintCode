# coding=utf-8

"""
删除排序链表中的重复元素

描述:给定一个排序链表，删除所有重复的元素每个元素只留下一个。
思路: 链表的去重，就是 当前元素连到不等于当前元素的那个元素，略过中间元素
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
    @param head: head is the head of the linked list
    @return: head of linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        if head is None:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        tail = dummy
        while tail.next is not None:
            if tail.val == tail.next.val:
                tail.next = tail.next.next      # 下一个等于下下个， 一直在当前tail循环，一直到下一个ornull结束
            else:
                tail = tail.next
        return dummy.next