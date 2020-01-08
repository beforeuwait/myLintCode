# coding=utf-8

"""
数字组合 II
描述:给定一个数组 num 和一个整数 target. 找到 num 中所有的数字之和为 target 的组合.

思路: 同前一道题一模一样，就是仅仅多一个去重

"""

class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here
        num.sort()
        res = []
        self.dfs(num, target, 0, res, [])
        return res
    
    def dfs(self, num, target, index, res, temp):
        if target < 0:
            return
        if target == 0 and temp not in res:
            res.append(list(temp))
        
        for i in range(index, len(num)):
            temp.append(num[i])
            self.dfs(num, target - num[i], i+1, res, temp)
            temp.pop()
