# coding=utf-8

"""
二叉树的锯齿形层次遍历

给出一棵二叉树，返回其节点值的锯齿形层次遍历（先从左往右，下一层再从右往左，层与层之间交替进行） 
思路:
就是 层次遍历的一次变形
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
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        if not root:
            return []
        result = []
        queue = [root]
        n = 1
        while queue:
            next_queue = []
            if n % 2 != 0:
                result.append([node.val for node in queue])
            else:
                result.append([node.val for node in queue][::-1])
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
            n += 1
        return result