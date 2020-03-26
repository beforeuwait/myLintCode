# coding=utf-8

"""
子树

有两个不同大小的二叉树： T1 有上百万的节点； T2 有好几百的节点。请设计一种算法，判定 T2 是否为 T1的子树。

思路：
将其序列化
然后转化为 字符串
然后判断 是否是子集
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
    @param T1: The roots of binary tree T1.
    @param T2: The roots of binary tree T2.
    @return: True if T2 is a subtree of T1, or false.
    """
    def isSubtree(self, T1, T2):
        # write your code here
        # 将两个数序列化变成str，然后用find函数
        if not T1 and not T2:
            return True
        elif not T1 and T2:
            return False
        elif T1 and not T2:
            return True

        return ''.join(self.dfs(T1, [])).find(''.join(self.dfs(T2, []))) != -1
        
    
    def dfs(self, root, tmp):
        if not root:
            tmp.append('#')
            return
        
        tmp.append(str(root.val))
        self.dfs(root.left, tmp)
        self.dfs(root.right, tmp)
        return tmp
        
        