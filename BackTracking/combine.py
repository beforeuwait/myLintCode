# coding=utf-8

"""
组合

描述:给定两个整数 n 和 k. 返回从 1, 2, ... , n 中选出 k 个数的所有可能的组合.

思路:
典型的dfs的应用

"""

class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        nlist = [i for i in range(1, n+1)]
        res = []
        self.dfs(nlist, res, 0, [], k)
        return res
    
    def dfs(self, nlist, res, start, temp, k):
        if len(temp) > k:
            return
        if len(temp) == k:
            res.append(list(temp))
        for i in range(start, len(nlist)):
            temp.append(nlist[i])
            self.dfs(nlist, res, i+1, temp, k)
            temp.pop()  # backTracking
