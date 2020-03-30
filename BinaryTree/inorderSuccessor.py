# coding=utf-8

"""
二叉查找树的中序后继

给定一个二叉查找树(什么是二叉查找树)，以及一个节点，求该节点在中序遍历的后继，如果没有则返回null

思路:
如果root的值大于p的值就向左，反之向右
"""


"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        Successor = None
        while root:
            if root.val > p.val:
                Successor = root
                root = root.left
            else:
                root = root.right
        return Successor