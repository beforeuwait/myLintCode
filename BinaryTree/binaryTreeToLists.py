# coding=utf-8

"""
将二叉树按照层级转化为链表

给一棵二叉树，设计一个算法为每一层的节点建立一个链表。也就是说，如果一棵二叉树有 D 层，那么你需要创建 D 条链表。

思路：
这道题就是考察 层次遍历和链表定义
"""



"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        # 我的思路就是，按照bfs来按层找到节点，再变换成链表
        
        if not root:
            return []
        
        queue = [root]
        res = []
        while queue:
            new_queue = []
            res.append([node.val for node in queue])
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
            
        
        # 开始生成链表
        linked_list = []
        for each in res:
            new_link = ListNode(-1)
            temp = new_link
            for i in each:
                new_link.next = ListNode(i)
                new_link = new_link.next
            linked_list.append(temp.next)
        
        return linked_list
            