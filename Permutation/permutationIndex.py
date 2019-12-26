# coding=utf-8

from copy import deepcopy

"""
排列序号

描述: 给出一个不含重复数字的排列，求这些数字的所有排列按字典序排序后该排列的编号。其中，编号从1开始。

思路:
找到首位数， 然后确定在首位数为第一位前，迭代了多少次
次数等去 len(num) -1 的阶乘
然后 次数 + 1
然后统计从当前排列到目标有多少次
"""

class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndex(self, A):
        # write your code here
        a = sorted(deepcopy(A))
        len_a = len(a)
        num_a = ''
        for _ in A:
            num_a += str(_)
        start_index = int(num_a) // 10**(len_a-1)
        a_index = a.index(start_index)
        a.remove(start_index)
        a.insert(0, start_index)
        count = self.doX(a_index, len_a) + 1
        while True:
            if a == A:
                break
            a = self.nextPermutation(a)
            count += 1
        return count
        
    def nextPermutation(self, nums):
        if nums is None or len(nums) == 0:
            return []
        n = len(nums) - 1
        while n > 0 and nums[n] <= nums[n - 1]:
            n -= 1
        if n == 0:
            return list(reversed(nums))
        for i in range(len(nums) - 1, n - 1, -1):
            if nums[i] > nums[n - 1]:
                nums[n - 1], nums[i] = nums[i], nums[n - 1]
                break
        return nums[:n] + list(reversed(nums[n:]))
    
    def doX(self,n, m):
        # n 为几次迭代
        # m 为长度
        count = 1
        for i in range(1, m):
            count *= i
        return n*count