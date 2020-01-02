# coding=utf-8

"""
最接近零的子数组和
描述：给定一个整数数组，找到一个和最接近于零的子数组。返回第一个和最右一个指数。你的代码应该返回满足要求的子数组的起始位置和结束位置

思路: 我自己的一开始的思路，执行时间太久了

"""
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        # 单指针
        start, end = 0, 0
        nums_len = len(nums)
        most_min = nums[0]
        for i in range(0, nums_len):
            sum = 0
            for j in range(i, nums_len):
                if i == j:
                    sum = nums[i]
                else:
                    sum = sum + nums[j]
                if abs(sum) < abs(most_min):
                    most_min = sum
                    start, end = i, j
        return [start, end]
