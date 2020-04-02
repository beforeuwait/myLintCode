# coding=utf-8

"""
二叉树最长连续序列

给一棵二叉树，找到最长连续路径的长度。
这条路径是指 
任何的节点序列中的起始节点到树中的任一节点都必须遵循 父-子 联系。最长的连续路径必须是从父亲节点到孩子节点（不能逆序）。

思路: 这题扯兮兮的
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
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        # write your code here
        return self.dfs(root, None, 0)
    
    def dfs(self, root, parent, lens):
        if not root:
            return lens
        
        if parent and root.val == parent.val + 1:
            lens += 1
        else:
            lens = 1
        return max(lens, max(self.dfs(root.left, root, lens), self.dfs(root.right, root, lens)))
            

