# coding=utf-8

"""
多关键字排序
描述:给定 n 个学生的学号(从 1 到 n 编号)以及他们的考试成绩，
表示为(学号，考试成绩)，请将这些学生按考试成绩降序排序，若考试成绩相同，则按学号升序排序。

这里就是对 sort的应用 对 key的应用

"""

class Solution:
    """
    @param array: the input array
    @return: the sorted array
    """
    def multiSort(self, array):
        # Write your code here
        array.sort(key=lambda x: (-x[1], x[0]))
        return array
