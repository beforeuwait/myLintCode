# coding=utf-8

"""
两数组的交集
描述:给出两个数组，写出一个方法求出它们的交集

思路:
如果是数组与数组的比较，则时间复杂度太大
既然是交集，无论谁做比照组，都是能找到交集
"""

class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        # 这个时间复杂度为 O(n^n)
        nums_1_new = list(set(nums1))
        nums_2_new = list(set(nums2))
        res = []
        for _ in nums_2_new:
            if _ in nums_1_new:
                res.append(_)
        return res

    def intersection(self, nums1, nums2):
        # write your code here
        # 这个用了hash表将每次查询的时间复杂度降为 O(1)
        hash_dict = {}
        for _ in nums1:
            hash_dict[_] = '1'
        
        res = []
        nums_2_new = list(set(nums2))
        for n in nums_2_new:
            if hash_dict.get(n, None) is not None:
                res.append(n)
        return res