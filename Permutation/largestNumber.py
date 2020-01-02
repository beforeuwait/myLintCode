# coding=utf-8

"""
最大数
给出一组非负整数，重新排列他们的顺序把他们组成一个最大的整数。


思路: 我这里没别的思路，就想到冒泡排序的办法
"""
class Solution:
    """
    @param nums: A list of non negative integers
    @return: A string
    """
    def largestNumber(self, nums):
        # write your code here
        # 冒泡程序
        # 位数少一位，则看后补位与前一位的比较
        # 比如 66 > 6 的，但是 65 < 6的
        # 还要处理全是0的情况
        sum = 0
        for n in nums:
            sum += n
        if sum == 0:
            return '0'
        nums_len = len(nums)
        for _ in range(nums_len):
            print(nums)
            for i in range(0, nums_len -1):
                son, dad = str(nums[i]), str(nums[i+1])
                if len(son) < len(dad):
                    son += son[-1]*(len(dad) - len(son))
                    if int(son) < int(dad):
                        nums[i], nums[i+1] = nums[i+1], nums[i]
                elif len(son) > len(dad):
                    dad += dad[-1]*(len(son) - len(dad))
                    if int(son) < int(dad):
                        nums[i], nums[i+1] = nums[i+1], nums[i]
                else:
                    if int(son) < int(dad):
                        nums[i], nums[i+1] = nums[i+1], nums[i]
        res = ''
        for _ in nums:
            res += str(_)
        return res

nums = [1,20,23,4,8]
nums = [0, 0]
print(Solution().largestNumber(nums))