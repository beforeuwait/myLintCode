# coding=utf-8

""""
两两交换链表中的节点

描述:给一个链表，两两交换其中的节点，然后返回交换后的链表。
思路: 这题不难，就是绕

input: 1->2->3->4->null
先定一个一个链表
dummy = ListNode(-1)
dummy.next = 1->2->3->4->null

就变成 -1->1->2->3->4->null
也就是一次进2位， 第二位和第三位互换位置

-1->1->2->3
首先找到 2
再找到 1
将 1指向 2的next
然后将 2的next指向 1
再讲 -1的next指向 2
完成~

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
    @return: a ListNode
    """
    def swapPairs(self, head):
        # write your code here
        if head is None or head.next is None:
            return head
        dummy = ListNode(-1)    # 实例化一个链表
        dummy.next = head       # 后面跟着 head
        d_tail = dummy
        while d_tail.next and d_tail.next.next:
            temp = d_tail.next.next         # 找到当前节点后的第2个元素
            d_tail.next.next = temp.next    # 当前节点后的第1个元素指向 刚刚第2个元素的的指向
            temp.next = d_tail.next         # 刚刚第2个元素指向当前节点的指向
            d_tail.next = temp              # 当前节点指向刚刚第二个元素
            d_tail = d_tail.next.next       # 进2步
        return dummy.next
        