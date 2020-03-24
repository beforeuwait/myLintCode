# coding=utf-8

"""
前序遍历和中序遍历树构造二叉树

思路: 同上一题的几乎一致

实际就是考察对 前序 中序 后序的理解

前序: 根-->左--->右
中序: 左-->根--->右
后序: 左-->右--->根
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
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # write your code here
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1: root_index+1], inorder[: root_index])
        root.right = self.buildTree(preorder[root_index+1: ], inorder[root_index+1: ])
        return root