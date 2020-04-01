# codinh=utf-8

"""
二叉树的后序遍历

给出一棵二叉树，返回其节点值的后序遍历。

思路:

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
        
        res = self.dfs(root)
        return res[::-1]
    
    def dfs(self, root):
        if not root:
            return None
        res = []
        res.append(root.val)
        if root.right:
            res += self.dfs(root.right)
        if root.left:
            res += self.dfs(root.left)
        
        return res