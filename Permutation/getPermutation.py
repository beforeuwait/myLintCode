# coding=utf-8

"""
第k个排列

描述:给定 n 和 k，求n的全排列中字典序第k个排列.

思路: 没啥好说，从第一个开始推
不过这样的 时间复杂度为 O(n*k)
"""


class Solution:
    """
    @param n: n
    @param k: the k th permutation
    @return: return the k-th permutation
    """
    def getPermutation(self, n, k):
        # write your code here
        if n == 1:
            return 1
        n_list = [i for i in range(1, n+1)]
        for _ in range(k-1):
            n_list = self.nextPermutation_NEW(n_list)
        res = ''
        for __ in n_list:
            res += str(__)
        return res
    
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