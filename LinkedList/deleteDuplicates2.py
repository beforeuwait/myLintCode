# coding=utf-8 

"""
删除排序链表中的重复数字 II

描述:给定一个排序链表，删除所有重复的元素只留下原链表中没有重复的元素。

思路: 遇到重复跳过，只是不留而已
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
    @return: head of the linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        if head is None:
            return head
        tail = dummy = ListNode(-1)
        cur = None
        while head is not None:
            c = head.val
            if head.next:
                next_c = head.next.val
            else:
                next_c = None
                    
            if c == next_c and c == cur:
                head.next = head.next.next
                if head.next.next is None:  # 这里比较骚，能解决  24->25->25->null的问题
                    tail.next = None
                    break
                continue
            elif c == next_c and c != cur:
                cur = c
                head.next = head.next.next
                continue
            elif c != next_c and c == cur:
                pass                        # 嗯哼
            else:
                tail.next = head
                tail = tail.next
                cur = c
            head = head.next
        return dummy.next