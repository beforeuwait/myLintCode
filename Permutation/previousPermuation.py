# coding=utf-8

"""
上一个排列

描述:给定一个整数数组来表示排列，找出其上一个排列。

思路: 这道题， 让我知道了什么是字典排序

1-2-3
1-3-2
2-1-3
2-3-1
3-1-2
3-2-1
在“字典序”中，我们将升序记为第一个排列，
而将降序记为最后一个排列，显然，对于上面这个有4个元素的数组来说，
一共有4!个排列，也就是说，除了我上面写出来的两个，
还有22个排列。这些排列的顺序，就是“字典序”。

也就是说，一个排列中，如果元素A在元素B的左边，
则说A是高位，B是低位。
而“字典序”就是一个不断增大高位数值，减小低位数值的过程。
"""

class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers that's previous permuation
    """
    def previousPermuation(self, nums):
        # write your code here
        if nums is None or len(nums) == 0:
            return []
        
        # 因为是向左递增的，首先找到从左往右最小那个
        n = len(nums) - 1
        while n > 0 and nums[n] >= nums[n-1]:
            n -= 1
        # 找到那个点，特征就是 左右两边都比它大
        if n == 0:
            # n = 0则是一个标准升序,前一个就是倒序了
            return list(reversed(nums))
        # 找到比 nums[n-1] 大的点，没有则是最后一位 
        m = len(nums) - 1
        while nums[m] >= nums[n-1]:
            m -= 1
        return nums[:n] + list(reversed(nums[n:]))