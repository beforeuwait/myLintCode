# coding=utf-8


"""
链表插入排序

描述:用插入排序对链表排序

思路: 采用双重遍历

input: 3->2->4->0->1->null

以3位第一个元素
- 3->null
然后是2 ,2< 3 所以放到第一个元素前，这时候第一个元素为2
然后是4， 4>2, 4>3， 因此要放到3后面，这时候第一个元素仍然为2
然后是0， 0<2，放到第一个元素前，这时候第一个元素为0
然后是1， 1>0, 1<2， 因此要放到2前
所以 output: 0->1->2->3->4->null

总之，比最后一个前的任一元素小的，插入当前应该插入的位置，大于一切的，插入最后一个后面
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
    @param head: The first node of linked list.
    @return: The head of linked list.
    """
    def insertionSortList(self, head):
        # write your code here
        dummy = ListNode(-1)
        while head is not None:
            temp = dummy
            every_next = head.next
            while temp.next and temp.next.val < head.val:
                temp = temp.next
            head.next = temp.next
            temp.next = head
            head = every_next
        return dummy.next