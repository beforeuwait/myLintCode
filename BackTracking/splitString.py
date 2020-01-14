# coding=utf-8

"""
分割字符串

描述:给一个字符串,你可以选择在一个字符或两个相邻字符之后拆分字符串,使字符串由仅一个字符或两个字符组成,输出所有可能的结果

输入： "123"
输出： [["1","2","3"],["12","3"],["1","23"]]

思路: 切片 
"""

class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        res = []
        self.dfs(s, [], res)
        return res
    
    def dfs(self, s, temp, res):
        if s == '':
            if temp[:] not in res:
                res.append(temp[:])
            return
        # 切 1 位 或者 2位
        for i in range(1,3):
            sub = s[:i]
            temp.append(sub)
            self.dfs(s[i:], temp, res)
            temp.pop()