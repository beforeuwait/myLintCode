# coding=utf-8

"""
把排序数组转换为高度最小的二叉搜索树。
给一个排序数组（从小到大），将其转换为一棵高度最小的二叉搜索树。

思路:
类似的二分法
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
    @param: A: an integer array
    @return: A tree node
    """
    def sortedArrayToBST(self, A):
        # write your code here
    
    def dfs(self, A, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(A[start])
        
        mid = (start + end) // 2
        node = TreeNode(A[mid])

        node.left = self.dfs(A, start, mid-1)
        node.right = self.dfs(A, mid+1, end)
        return node
