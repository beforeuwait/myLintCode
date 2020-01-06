# coding=utf-8

"""
最长非公共子序列之2

描述：给定一组字符串，你需要找到这组字符串中最长的非公共子序列。
最长的非公共子序列被定义为这些字符串之一的最长子序列，并且此子序列不应该是其他字符串的子序列。
子序列是可以通过删除一些字符而不改变其余元素的顺序从一个序列导出的序列。可以说，任何字符串都是自身的子序列，空字符串是任何字符串的子序列。
输入将是字符串列表，输出需要是最长的非公共子序列的长度。 如果最长的非公共子序列不存在，则返回-1。

思路:就是 all()函数的应用


"""
class Solution:
    """
    @param strs: List[str]
    @return: return an integer
    """
    def findLUSlength(self, strs):
        # write your code here
        strs.sort(key = len, reverse = True)        # 这里是找到最长的子集合
        # strs.sort(key = len, reverse = False)        # 这里是找到最短的子集合
        for i, word1 in enumerate(strs):
            if all(not self.subSeq(word1, word2) for j, word2 in enumerate(strs) if i != j):
                return len(word1)
        return -1
    
    def subSeq(self, word1, word2):
        i = 0
        for word in word2:
            if i < len(word1) and word1[i] == word:
                i += 1
        return i==len(word1)