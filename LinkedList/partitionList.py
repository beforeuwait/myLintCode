# coding=utf-8


"""
链表划分

描述:给定一个单链表和数值x，划分链表使得所有小于x的节点排在大于等于x的节点之前。
你应该保留两部分内链表节点原有的相对顺序。

思路:
遍历head
然后定义2个链表，一个存储比x小的部分，一个存比x大的部分
然后拼接他们
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
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        # write your code here
        if head is None:
            return None
        left, right = ListNode(0), ListNode(0)  # 定义两个链表
        right_start = right                     # 右边的起始位置
        left_start = left                       # 左边的起始位置
        while head is not None:
            val = head.val
            if val >= x:                        # 大于x 添加到右边
                right.next = head
                right = right.next
            else:
                left.next = head                # 小于x，添加到左右
                left = left.next
            head = head.next
        right.next = None                       # 给右边收个尾
        left.next = right_t.next                # 左边右接右边起始位置
        return left_t.next                      # 返回左边第一位