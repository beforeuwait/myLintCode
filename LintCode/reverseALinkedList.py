# coding=utf-8

"""
翻转一个链表

关于链表简单来讲，每一个元素有2个指针知道自己前一个和后一个元素
！！那至少 每个元素至少有一个指针指向自己后一个元素

我最初在思考的时候，总是带入list的想法，总是想着有固定的顺序
其实呢，知道一个元素，就知道下一个元素，并不关心这个元素到底具体位置
所以啊，并不是如我最初想的那样前后交换位置是个冒泡程序

input: 1->2->3->null
1指向2， 2指向3， 3指向null 结束
思路: 这里要做到的是，  1指向 null 结束， 2指向1， 3指向2
output: 3->2->1->null
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
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        new_head = None # 对于第一个元素指向 null
        while head is not None:
            temp = head.next    # 当前元素的下一个元素
            head.next = new_head # 重新定义当前元素指向
            new_head = head     # new_head 值为当前元素，相当于下一次元素指向当前元素
            head = temp         # 为当前元素赋值为temp , 因为链表里原先的 temp 后面的指向并没有变只是当前元素并不指向temp了而已
        return new_head


"""
虽说该题为 EASY
对于链表概率不熟悉的我，还是纠结了一会儿
至少通过这个题，明白了链表的基本概念，顺带贯通了一些链表的用法
"""