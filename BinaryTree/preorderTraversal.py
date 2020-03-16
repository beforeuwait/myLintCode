# coding=utf-8

"""
二叉树的前序遍历

给出一棵二叉树，返回其节点值的前序遍历。

思路:
先去了解二叉树， 再来解决问题
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
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        ans = []
        ans.append(root.val)
        if root.left:
            ans += self.preorderTraversal(root.left)
        if root.right:
            ans += self.preorderTraversal(root.right)
        return ans