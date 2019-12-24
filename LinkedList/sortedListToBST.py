# coding=utf-8

"""
有序链表转换为二分查找树

描述: 给出一个所有元素以升序排序的单链表，将它转换成一棵高度平衡的二分查找树

思路: 就是递归的想法
找到中间值，这个所谓中间值找法比较讲究, 利用快慢指针，相差一位开始找， 慢指针的下一位就是中间
"""


"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        # write your code here
        if head is None:
            return head
        if head.next is None:
            return TreeNode(head.val)
        
        dummy = ListNode(-1)
        dummy.next = head
        fast, slow = head, dummy                            # 这里是精辟
        while fast is not None and fast.next is not None:   # 条件别乱写
            fast = fast.next.next
            slow = slow.next
        
        tmp = slow.next                                     # 找到的点
        slow.next = None                                    # 断开链表
        parent = TreeNode(tmp.val)
        parent.left = self.sortedListToBST(head)
        parent.right = self.sortedListToBST(tmp.next)
        return parent
        