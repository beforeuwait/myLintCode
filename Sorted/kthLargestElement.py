# coding=utf-8

"""
第k大元素

主要考察 快速排列
无论是升序还是降序

快排:
找到 中间数
排列左边
排列右边

"""
class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        # 快排
        new_nums = self.quick_sort(nums)
        return new_nums[n - 1]
    
    def quick_sort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = nums[len(nums) // 2]
        left, right, middle = [], [], []
        for num in nums:
            if num < mid:
                left.append(num)
            elif num > mid:
                right.append(num)
            else:
                middle.append(num)
        """
        left = [i for i in nums if i < mid]
        right = [i for i in nums if i > mid]
        middle = [i for i in nums if i == mid]
        """
        return self.quick_sort(right) + middle + self.quick_sort(left)