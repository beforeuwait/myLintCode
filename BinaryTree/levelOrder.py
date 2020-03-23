# coding=utf-8

"""
二叉树的层次遍历

思路: 对于层次遍历用 队列or bfs 的思路来弄
我这个就是队列

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
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        if not root:
            return []
        
        queue = [root]
        result = []
        while queue:
            next_queue = []
            result.append([i.val for i in queue])
            for i in queue:
                if i.left:
                    next_queue.append(i.left)
                if i.right:
                    next_queue.append(i.right)
            queue = next_queue
        return result