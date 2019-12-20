# cdoing=utf-8

"""
两数相乘
给出两个链表形式表示的数字,写一个函数得到这两个链表相乘乘积。

思路: 两个list or str 记录两个链表的元素
返回 乘积

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
    @return: the product list of l1 and l2
    """
    def multiplyLists(self, l1, l2):
        # write your code here
        num_1, num_2 = [], []
        while l1 is not None:
            num_1.append(str(l1.val))
            l1 = l1.next
        while l2 is not None:
            num_2.append(str(l2.val))
            l2 = l2.next
        return int(''.join(num_1))*int(''.join(num_2))
    
    def multiplyLists_(self, l1, l2):
            # write your code here
        num_1, num_2 = '', ''
        while l1 is not None:
            num_1 += str(li.val)
            l1 = l1.next
        while l2 is not None:
            num_2 += str(l2.val)
            l2 = l2.next
        return int(num_1)*int(num_2)
    