# coding=utf-8

"""
摆动排序

描述:给你一个没有排序的数组，请将原数组就地重新排列满足如下性质
nums[0] <= nums[1] >= nums[2] <= nums[3]....

思路: 
要么先快排，然后两两互换
要么一开始两两比较互换
"""

class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """
    
    def wiggleSort(self, nums):
        # write your code here
        # quicksort fist
        self.quickSort(nums, 0, len(nums) - 1)
        left = 0
        while left < len(nums) - 2:
            nums[left + 1], nums[left + 2] = nums[left + 2], nums[left + 1]
            left += 2
    
    def quickSort(self, nums, start, end):
        if start >= end:
            return []
        pivot = nums[(start + end) // 2]
        left, right = start, end
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        self.quickSort(nums, start, right)
        self.quickSort(nums, left, end)