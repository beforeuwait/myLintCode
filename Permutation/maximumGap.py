# coding=utf-8

"""
最大间距

给定一个未经排序的数组, 请找出这个数组排序之后的两个相邻元素之间最大的间距.
如果数组中少于 2 个元素, 返回 0.

思路： 这个和最小差思路一模一样
"""


class Solution:
    """
    @param nums: an array of integers
    @return: the maximun difference
    """
    def maximumGap(self, nums):
        # write your code here
        if len(nums) < 2:
            return 0
        nums.sort()
        res = None
        for i in range(0, len(nums) -1):
            if res is None:
                res = nums[i+1] - nums[i]
            else:
                res = max(res, nums[i+1] - nums[i])
        return res