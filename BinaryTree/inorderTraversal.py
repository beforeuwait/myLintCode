# coding=utf-8

"""
二叉树的中序遍历

给出一棵二叉树,返回其中序遍历

思路:
 首先什么是 中序遍历 ，中序遍历是先遍历左子树，再遍历根结点，最后才遍历右子树

 就是从左边最后一个节点找到根节点，然后遍历右子树

 首先创建一个栈，把左边子树都放进去，再取出来
 
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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        if not root:
            return []
        
        stack = []
        result = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result