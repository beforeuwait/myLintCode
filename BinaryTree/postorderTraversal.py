# coding=utf-8

"""
后序遍历

思路就是 前序遍历反过来
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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        result = self.preorderTraversal(root)
        result.reverse()
        return result
    
    def preorderTraversal(self, root):
        if not root:
            return []
        stack = []
        stack.append(root.val)
        if root.right:
            stack += self.preorderTraversal(root.right)
        if root.left:
            stack += self.preorderTraversal(root.left)
        return stack