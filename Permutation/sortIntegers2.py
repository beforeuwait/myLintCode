# coding=utf-8

"""
 整数排序 II

描述:给一组整数，请将其在原地按照升序排序。使用归并排序，快速排序，堆排序或者任何其他 O(n log n) 的排序算法。
注意: 并不是返回一个新的数组，而是对给定的本身进行操作

找到中间数 pivot  然后左右对比 交换位置
"""


class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        self.qucikSort(A, 0, len(A) - 1)
        
    def qucikSort(self, nums, start, end):
        if start >= end:
            return
        left, right = start, end
        pivot = nums[(start + end) // 2]
        # 开始装逼了
        while left <= right:
            while left <=right and nums[left] < pivot:
                left += 1
            while left <=right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        self.qucikSort(nums, start, right)
        self.qucikSort(nums, left, end)