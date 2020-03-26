# coding=utf-8

"""
翻转二叉树

翻转一棵二叉树。左右子树交换。

思路:
是在自身翻转而不是新建一个
"""



"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invertBinaryTree(self, root):
        # write your code here
        self.dfs(root)
    
    def dfs(self, root):
        left = root.left
        right = root.right
        root.left = right
        root.right = left
        if left:
            self.dfs(left)
        if right:
            self.dfs(right)