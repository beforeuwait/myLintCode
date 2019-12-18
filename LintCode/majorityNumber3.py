# coding=utf-8

"""
主元素 III
怎么说呢，这题属于命题的时候不够严谨
给的 参数 k 从头到尾没用上
就是利用 hash表来统计主元素的个数 时间复杂度为 O(n) ，而空间复杂度为 O(n) 

"""

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        # write your code here
        # 这题跟k有什么关系?
        number = {}
        count = 0
        for num in nums:
            number[num] = number.get(num, 0) + 1
            if number[num] > count:
                count = number[num]
                majority = num
        return majority