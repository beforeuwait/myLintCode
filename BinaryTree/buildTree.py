# coding=utf-8

"""
中序遍历和后序遍历树构造二叉树

思路: 
后续遍历的最后一个节点就是 根节点

而 中序遍历的方式是 左根右 
因此，可以找到 左边 右边 ，又知道根节点
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
    @param inorder: A list of integers that inorder traversal of a tree
    @param postorder: A list of integers that postorder traversal of a tree
    @return: Root of a tree
    """
    def buildTree(self, inorder, postorder):
        # write your code here
        if not inorder:
            return None
        
        root = TreeNode(postorder[-1])
        root_index = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[: root_index], postorder[: root_index])
        root.right = self.buildTree(inorder[root_index+1: ], postorder[root_index: -1])
        return root
        