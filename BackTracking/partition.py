# coding=utf-8

"""
分割回文串
描述:给定字符串 s, 需要将它分割成一些子串, 使得每个子串都是回文串.
返回所有可能的分割方案.

思路:
要注意深拷贝和浅拷贝的区别

选定一个然后开始切，是回文就继续切，直到不能切 就换下一个了
"""

class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        if len(s) == 0 or s is None:
            return []
        res = []
        self.dfs(res, [], 0, s)
        return res
    
    def dfs(self, res, temp, index, s):
        if index == len(s):
            res.append(list(temp))      # 注意这里是个深拷贝
            return
        for i in range(index, len(s)):
            sub = s[index: i+1]
            if not self.isPalindrome(sub):
                continue
            temp.append(sub)
            self.dfs(res, temp, i + 1, s)
            temp.pop()
    
    def isPalindrome(self, s):
        start, end = 0, len(s)-1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
