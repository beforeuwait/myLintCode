# coding=utf-8

"""
重排链表

描述: 
给定一个单链表L: L0→L1→…→Ln-1→Ln,

重新排列后为：L0→Ln→L1→Ln-1→L2→Ln-2→…

思路: 这道题很好的考察了 链表的中值和链表的翻转

值得回味，不过我的做法并没有在原地输出，还需要历练
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
    @param head: The head of linked list.
    @return: nothing
    """
    def reorderList(self, head):
        # write your code here
        if head is None or head.next is None or head.next.next is None:
            return head
        dummy = ListNode(-1)
        tail = dummy
        start = head
        mid = self.findPivot(head)          # 找中值
        # reverse 
        right = mid.next
        mid.next = None                     # 分割
        right_r = self.reverseList(right)   # 链表翻转
        # insert 开始骚操作
        while start is not None and right_r is not None:
            tmp_s, tmp_r = start.next, right_r.next
            tail.next, start.next = start, right_r
            tail = tail.next.next
            start, right_r = tmp_s, tmp_r
        if start is not None:               # 这里是针对偶数位的链表
            tail.next = start
        return dummy.next
        
    def findPivot(self, node):
        if node is None or node.next is None:
            return node
        # find pivot
        fast, slow = node, node
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverseList(self, node):
        # reverse current linkedList
        # 这里还需要注意就是，翻转翻转。每一次都指向前一个就行了
        if node is None or node.next is None:
            return node
        cur = None
        while node is not None:
            tmp = node.next
            node.next = cur
            cur = node
            node = tmp
        return cur
            