# coding=utf-8

"""
最近公共祖先
描述:给定一棵二叉树，找到两个节点的最近公共父节点(LCA)。
最近公共祖先是两个节点的公共的祖先节点且具有最大深度

思路:

两种情况：
当两个节点位于不同树上面
当两个节点位于同一枝

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
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if not root:
            return None
    
        # 找到节点
        if root == A or root == B:
            return root

        # 向下搜索
        root_left = self.lowestCommonAncestor(root.left, A, B)
        root_right = self.lowestCommonAncestor(root.right, A, B)

        # 两个节点都存在, 说明一个父节点
        if root_left and root_right:
            return root

        # 同一个分支上
        if root_left:
            return root_left
        
        if root_right:
            return root_right
        
        # 都不在
        return None