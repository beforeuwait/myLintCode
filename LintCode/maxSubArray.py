# coding=utf-8

"""
最大子数组
说实话我一开始并没有想出这个方法
想的是老老实实计算和比较

这题值得反复体会
"""

class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        s, t = 0, 0
        for num in nums:
            t += num
            t = max(0, t)
            s = max(s, t)
        if s == 0:
            return max(nums)
        return s