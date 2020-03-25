# coding=utf-8

"""
验证二叉查找树
给定一个二叉树，判断它是否是合法的二叉查找树(BST)

一棵BST定义为：

节点的左子树中的值要严格小于该节点的值。
节点的右子树中的值要严格大于该节点的值。
左右子树也必须是二叉查找树。
一个节点的树也是二叉查找树。


思路:非常巧妙啊

不断压缩区间，反正左边小 右边大就行了
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
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        return self.validate(root, -4294967296, 4294967296)
    
    def validate(root, minVal, maxVal):
        if not root:
            return True
        
        if root.val <= minVal or root.val >= maxVal:
            return False

        return self.validate(root.left, minVal, root.val) and self.validate(root.right, root.val, maxVal)
        
