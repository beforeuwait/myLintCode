# coding=utf-8

"""
两数组的交集 II

描述: 给定两个数组，计算两个数组的交集
样例
样例1
输入: 
nums1 = [1, 2, 2, 1], nums2 = [2, 2]
输出: 
[2, 2]
样例2
输入: 
nums1 = [1, 1, 2], nums2 = [1]

思路:这个同上一个两数交集的区别在于
这个不用变成集合。
思路同上一个一致，但是要注意的就是  [1,2,3] 同 [1,1,2,3,3]
结果只能是  [1,2,3] 所以要带一个计数
"""

class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        # write your code here
        hash_dict = {}
        for _ in nums1:
            hash_dict[_] = hash_dict.get(_, 0) + 1
        res = []
        print(hash_dict)
        for n in nums2:
            if hash_dict.get(n, None) is not None and hash_dict.get(n) != 0:
                res.append(n)
                hash_dict[n] = hash_dict.get(n) - 1
        return res
