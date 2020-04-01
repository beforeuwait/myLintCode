# coding=utf-8


"""
二叉树的所有路径

给一棵二叉树，找出从根节点到叶子节点的所有路径。

思路:

一条支一条支看，放入列表，将多余的pop出
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
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if not root:
            return []
        
        res = []
        self.dfs(root, [str(root.val)], res)
        return res
    

    def dfs(self, node, tmp, res):
        if not node.left and not node.right:
            res.append('->'.join(tmp))
        
        if node.left:
            tmp.append(str(node.left.val))
            self.dfs(node.left, tmp, res)
            tmp.pop()
        
        if node.right:
            tmp.append(str(node.right.val))
            self.dfs(node.right, tmp, res)
            tmp.pop()
