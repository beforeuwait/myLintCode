# coding=utf-8

"""
生成括号

描述:给定 n，表示有 n 对括号, 请写一个函数以将其生成所有的括号组合，并返回组合结果。
样例
input: 3
output: ["((()))", "(()())", "(())()", "()(())", "()()()"] 

思路:
仍旧是 dfs

两遍添加，注意 ）的数量是不能大于 （ 的
"""

class Solution:
    """
    @param n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        # write your code here
        res = []
        def dfs(l, r, temp, res):
            if r < l:
                return
            if l == 0 and r == 0:
                res.append(temp)
            if l > 0:
                dfs(l-1, r, temp+'(', res)
            if r > 0:
                dfs(l, r-1, temp+')', res)
        dfs(n, n, '', res)
        return res
