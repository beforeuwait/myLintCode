# coding=utf-8

"""
复制带随机指针的链表

描述:给出一个链表，每个节点包含一个额外增加的随机指针可以指向链表中的任何节点或空的节点。
返回一个深拷贝的链表。 

思路: 要用到 hash table 这样就完成深度拷贝了

mapping = {
    head1: rhead1,
    head2: rhead2,
    head3: rhead3,
        ...
    headn: rheadn
}
将copy后的 head1 里的换车 rhead1 就完成深拷贝了
"""


"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if head is None:
            return head
        mapping = {}
        new_head = RandomListNode(head.label)
        mapping[head] = new_head
        p, q = head, new_head
        while p is not None:
            q.random = p.random     #   这里random是浅拷贝
            if p.next is not None:
                q.next = RandomListNode(p.next.label)
                mapping[p.next] = q.next
            else:
                q.next = None
            p, q = p.next, q.next
        # 事已至此，完成浅拷贝
        tail = new_head
        while tail is not None:
            if tail.random is not None:
                tail.random = mapping.get(tail.random)
            else:
                tail.random = None
            tail = tail.next
        return new_head
    