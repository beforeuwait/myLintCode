# coding=utf-8

"""
寻找丢失的数 II

描述:给一个由 1 - n 的整数随机组成的一个字符串序列，其中丢失了一个整数，请找到它。

input: n = 20 和 str = 19201234567891011121314151618
output: 17
解释:
19'20'1'2'3'4'5'6'7'8'9'10'11'12'13'14'15'16'18

思路: 切片
"""

class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, strs):
        # write your code here
        res = []
        self.dfs(strs, [], n, res)
        sums = 0
        for _ in res[0]:
            sums += int(_)
        return n*(n+1)//2 - sums

    def dfs(self, strs, temp, n, res):
        if len(temp) == n-1 and strs == '':
            res.append(temp[:])
            return 
        
        for i in range(1, 3):
            if i > len(strs):
                break
            nums = strs[:i]
            if int(nums) > n or nums in temp:
                continue
            if i == 2 and nums[0] == '0':
                continue
            temp.append(nums)
            self.dfs(strs[i:], temp, n, res)
            temp.pop()
