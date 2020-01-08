# coding=utf-8

"""
电话号码的字母组合

描述:给一个不包含'0'和'1'的数字字符串，每个数字代表一个字母，请返回其所有可能的字母组合。

思路:

这道题是对dfs一个很好的诠释
"""

class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def __init__(self):
        self.keyboard = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }
        self.res = []
        
    def letterCombinations(self, digits):
        # write your code here
        if not digits:
            return []
        self.dfs(digits, 0, '')
        return self.res
    
    def dfs(self, digits, index, temp):
        # print(index)
        if len(temp) == len(digits):
            self.res.append(temp)
            return
        for param in self.keyboard.get(digits[index]):
            self.dfs(digits, index+1, temp + param)
