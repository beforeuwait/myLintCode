# coding=utf-8

"""
四数之和

描述:给一个包含n个数的整数数组S，在S中找到所有使得和为给定整数target的四元组(a, b, c, d)。

思路:这题首先让我想到最大子数组这个题
思路不一样

这里呢，用3sum的思路
固定2位数，然后2个指针
"""

class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, nums, target):
        # write your code here
        # 固定2数, 然后两个指针
        nums.sort()
        res = []
        nums_len = len(nums)
        for i in range(0, nums_len - 3):
            if nums[i] == nums[i-1]:
                continue
            for i in range(i + 1, nums_len - 2):
                if j != n+1 and nums[j] == nums[j-1]:
                    continue
                sum = target - nums[i] - nums[j]
                left, right = j + 1, nums_len - 1
                while left < right:
                    if nums[left] + nums_len[right] == sum:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif nums[left] + nums[right] > sum:
                        right -= 1
                    else:
                        left += 1
        return res