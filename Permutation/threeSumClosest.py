# coding=utf-8


"""
最接近的三数之和

描述:给一个包含 n 个整数的数组 S, 找到和与给定整数 target 最接近的三元组，返回这三个数的和

思路: 就是一个 3sum，不过问的是接近， 相减算绝对值， 谁绝对值越小，距离越小
"""


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        # 仍旧是双指针的思路
        numbers.sort()
        ans = None
        nums_len = len(numbers)
        for i in range(nums_len):
            left, right = i + 1, nums_len - 1
            while left < right:
                sum = numbers[i] + numbers[left] + numbers[right]
                if ans is None or abs(sum - target) < abs(ans - target):
                    ans = sum
                
                if sum <=target:
                    left += 1
                else:
                    right -= 1
        return ans