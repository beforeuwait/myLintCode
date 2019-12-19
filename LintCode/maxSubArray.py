# coding=utf-8

"""
最大子数组
说实话我一开始并没有想出这个方法
想的是老老实实计算和比较

这题值得反复体会

当前解法的意义在于，遍历过程中，一直加，对于让count < 0的元素，然后从那个点重新开始

input: -2   2   -3  4   -1  2   1   -5  3
t       0   2   0   4   3   5   6   1   4
s       0   2   2   4   4   5   6   6   6
t 记录从0开始加的最大子数列的和 整体必须大于0
s 记录t从0->0过程中产生的最大数

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