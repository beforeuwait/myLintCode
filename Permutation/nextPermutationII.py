# coding=utf-8

"""
下一个排列

描述:给定一个整数数组来表示排列，找出其之后的一个排列

思路: 和寻找上一个类似

这个就是找到上升点， 然后从上升点开始算从右到左找到第一个也是最小的那个比上升点前那个数大的数
然后交换位置， 然后倒置从上升点开始的那一片
"""

class Solution:
    """
    @param nums: An array of integers
    @return: nothing
    """
    def nextPermutation(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return []
        n = len(nums) - 1
        # 找到第一个上升点
        while n > 0 and nums[n] <= nums[n - 1]:
            n -= 1
        # 如果n为0 则已经为降序了，下一个就是升序
        if n == 0:
            nums[:] = nums[:: -1]
            return
        # 然后找到第一个比 nums[n-1]大的数
        for i in range(len(nums) - 1, n - 1, -1):
            if nums[i] > nums[n -1]:
                nums[n - 1], nums[i] = nums[i], nums[n - 1]
                break
        nums[n:] = nums[n:][::-1]