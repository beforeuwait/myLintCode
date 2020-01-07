# coding=utf-8

"""
数字组合

描述：给定一个候选数字的集合 candidates 和一个目标值 target. 找到 candidates 中所有的和为 target 的组合.
在同一个组合中, candidates 中的某个数字不限次数地出现.

思路:

dfs backtricking的应用
"""


class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        candidates = sorted(list(set(candidates)))
        res = []
        self.rds(candidates, target, 0, [], res)
        return res
    
    def rds(self, candidates, target, start, combo, res):
        if target < 0:
            return
        
        if target == 0:
            return res.append(list(combo))
        
        for i in range(start, len(candidates)):
            combo.append(candidates[i])
            self.rds(candidates, target - candidates[i], i, combo, res)
            combo.pop()
