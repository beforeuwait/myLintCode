# coding=utf-8

"""
二叉查找树中搜索区间

描述：给定一个二叉查找树和范围[k1, k2]。按照升序返回给定范围内的节点值

思路:考察对二叉树的理解，二叉树就是一个左边节点根节点最大，右边节点根节点最小，左边子节点小于右边子节点
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
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        self.res = []
        self.dfs(root, k1, k2)
        return self.res
        
    
    def dfs(self, root, k1, k2):
        if not root:
            return 
        if root.val >= k1:
            self.dfs(root.left, k1, k2)
        if k1 <= root.val <= k2:
            self.res.append(root.val)
        if root.val <= k2:
            self.dfs(root.right, k1, k2)
            