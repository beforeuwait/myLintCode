# coding=utf-8

"""
合并区间

描述:给出若干闭合区间，合并所有重叠的部分。

思路: 连续就合并，不连续则放入
始终都是 res[-1] 同做比较
"""

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        # 先排序
        intervals.sort(key=lambda x: x.start)
        res = []
        for inter in intervals:
            if res == [] or res[-1].end < inter.start:
                res.append(inter)
            else:
                res[-1].end = max(res[-1].end, inter.end)
        return res