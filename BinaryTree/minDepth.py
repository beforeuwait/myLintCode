# coding=utf-8

"""
二叉树的最小深度
给定一个二叉树，找出其最小深度。

二叉树的最小深度为根节点到最近叶子节点的最短路径上的节点数量。

思路：
有这几种情况

1.有左右树的
2.只有左树的
3.只有右树的
4.无树的
针对 1 找到min就行了
针对2，3，4找到max就行了

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
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        if not root:
            return 0
        
        deep_left = self.minDepth(root.left)
        deep_right = self.minDepth(root.right)

        if deep_left and deep_right:
            return min(deep_left, deep_right) + 1
        else:
            return max(deep_left, deep_right) + 1