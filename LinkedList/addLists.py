# coding=utf-8

"""
链表求和
描述: 你有两个用链表代表的整数，其中每个节点包含一个数字。
数字存储按照在原来整数中相反的顺序，使得第一个数字位于链表的开头。
写出一个函数将两个整数相加，用链表形式返回和。

思路:
这题可以在偷懒的地方，算出和后，先倒置，然后按顺序插入

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
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2 
    """
    def addLists(self, l1, l2):
        # write your code here
        integer_1, integer_2 = [], []       # 先定义2个列表
        new_head = ListNode(-1)
        tail = new_head
        while l1 is not None:               # 放l1的元素
            integer_1.insert(0, str(l1.val))
            l1 = l1.next
        while l2 is not None:               # 放l2的元素
            integer_2.insert(0, str(l2.val))    
            l2 = l2.next
        result = int(''.join(integer_1)) + int(''.join(integer_2))  # 求和
        for i in str(result):
            temp = ListNode(val=i)          # 实例化一个新的链表元素
            temp.next = tail.next           # 插入到第一个
            tail.next = temp
            
        return new_head.next
        