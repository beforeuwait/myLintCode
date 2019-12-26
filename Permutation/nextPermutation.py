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
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation_NEW(self, nums):
        """
        这个更提炼一些
        """
            # write your code here
        if nums is None or len(nums) == 0:
            return []
        n = len(nums) - 1
        # 找到第一个上升点
        while n > 0 and nums[n] <= nums[n - 1]:
            n -= 1
        # 如果n为0 则已经为降序了，下一个就是升序
        if n == 0:
            return list(reversed(nums))
        # 然后找到第一个比 nums[n-1]大的数
        for i in range(len(nums) - 1, n - 1, -1):
            if nums[i] > nums[n - 1]:
                nums[n - 1], nums[i] = nums[i], nums[n - 1]
                break
        return nums[:n] + list(reversed(nums[n:]))


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
            return list(reversed(nums))
        # 然后找到第一个比 nums[n-1]大的数
        nums_map = {}
        comp = []
        for i in range(len(nums) - 1, n - 1, -1):
            if nums[i] > nums[n - 1]:
                if nums_map.get(nums[i]):       # 防止  [3,3,3] 这种，应该取第 -1 位 而不是 第 1位
                    continue
                nums_map[nums[i]] = i
                comp.append(nums[i])
        j = nums_map.get(min(comp))
        # 互换位置
        nums[n - 1], nums[j] = nums[j], nums[n - 1]
        return nums[:n] + list(reversed(nums[n:]))
        
        


