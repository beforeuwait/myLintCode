# coding=utf-8

"""
中位数

描述:
给定一个未排序的整数数组，找到其中位数。

中位数是排序后数组的中间值，如果数组的个数是偶数个，则返回排序后数组的第N/2个数。

我把三种排序都列出来了
最快是用机器的 sorted
其次是 快排 1
然后最慢是 快排 2

"""

class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """
    
    
    #这是最快的
    def median_fast(self, nums):
        # write your code here
        nums_new = list(sorted(nums))
        index = round(len(nums_new) /2 + 0.001) - 1
        return nums_new[index]

    
    def median_middle(self, nums):
        # write your code here 
        self.quickSort(nums, 0, len(nums) -1)
        index = round(len(nums) /2 + 0.001) - 1
        return nums[index]
    
    def median_slow(self, nums):
        new_nums = self.permutation(nums)
        index = round(len(new_nums) /2 + 0.001) - 1
        return new_nums[index]
        
    def permutation(self, nums):
        if len(nums) <= 1:
            return nums
        pivot = nums[len(nums) // 2]
        left = [_ for _ in nums if _ < pivot]
        right = [_ for _ in nums if _ > pivot]
        mid = [_ for _ in nums if _ == pivot]
        return self.permutation(left) + mid + self.permutation(right)
    
    
    def quickSort(self, nums, start, end):
        if start >= end:
            return []
        left, right = start, end
        pivot = nums[(start + end) // 2]
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

