# coding=utf-8

"""
单词搜索

描述:给出一个二维的字母板和一个单词，寻找字母板网格中是否存在这个单词。
单词可以由按顺序的相邻单元的字母组成，其中相邻单元指的是水平或者垂直方向相邻。每个单元中的字母最多只能使用一次。

思路:
回溯法和深度优先搜索的应用

什么是回溯法，就是一直前进，这一步行不通，那就退一步找别的解法
也属于暴利破解。
"""


class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        # write your code here
        if word == []:
            return True
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        if n == 0:
            return False
        
        # 创建一个矩阵
        matrix = [[False for __ in range(n)] for _ in range(m)]
        # 开始DFS 深度优先遍历
        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, matrix, i, j):
                    return True
        return False
                
    
    def dfs(self, board, word, matrix, row, col):
        if word == '':
            return True
        m, n = len(board), len(board[0])
        if row < 0 or row >= m or col < 0 or col >= n:
            return False
        
        if board[row][col] == word[0] and not matrix[row][col]:
            matrix[row][col] = True
            print(matrix)
            if self.dfs(board, word[1:], matrix, row -1, col) or self.dfs(board, word[1:], matrix, row + 1, col) or self.dfs(board, word[1:], matrix, row, col - 1) or self.dfs(board, word[1:], matrix, row, col + 1):
                return True
            else:
                matrix[row][col] = False
        return False
