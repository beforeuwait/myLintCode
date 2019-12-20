# coding=utf-8

"""
链表排序

虽说是中等，但是我觉得还是有点难
刚刚才去做了一遍快排
思路和快排类似
找到 pivot 分成3块 左边 右边分别排序
最后组装起来
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
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def sortList(self, head):
        pass

    def quickSort(self, head):
        """这里进行快排"""
        pivot = self.findPivot(head)
        left, mid, right = ListNoe(-1), ListNoe(-1), ListNoe(-1)
        tail_l, tail_m, tail_r = left, mid, right
        while head is not None:
            if head.val < pivot.val:    # 小于放左边
                tail_l.next = head      # 当前left指向当前head
                tial_l = head           # 并且当前left指向完后跳到当前head位置
            elif head.val > pivot.val:  # 大于放右边
                tail_r.next = head      # 当前right指向当前head
                tail_r = head           # 并且当前right指向完后跳到当前的head位置
            else:
                tail_m.next = head      # 当前middler指向当前head
                tail_m = head           # 并且当前middle指向完后跳到当前head位置
        tail_l, tial_m, tail_r = None, None, None   # 加个尾巴，当前链表结束
        left_node = self.quickSort(left.next)       # 完成左边的排序
        right_node = self.quickSort(right.next)     # 完成右边的排序
        return self.connect(left_node, mid.next, right_node)
    
    def connect(left, middle, right):
        head = ListNoe(-1)
        cur = head
        cur.next = left
        while cur is not None:
            cur = cur.next
        cur.next = middle
        while cur is not None:
            cur = cur.next
        cur.next = right
        return head

    def findPivot(self, node):
        if node is None:
            return node
        if node.next is None:   # 就一位，还找啥pivot 就是本身
            return node
        # 这里利用快慢来达到，快到达边界，然后慢的刚好在中间
        slow, fast = node, node
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.next