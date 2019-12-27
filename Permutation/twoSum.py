# coding=utf-8

"""
两数之和

描述:给一个整数数组，找到两个数使得他们的和等于一个给定的数 target。
你需要实现的函数twoSum需要返回这两个数的下标, 并且第一个下标小于第二个下标。注意这里下标的范围是 0 到 n-1。

思路: 我这里使用了 hash表，这样的时间复杂度为 O(n) 空间复杂度为 O(n)
"""

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        # 先把各个放入hash表里
        num_map = {}
        for _ in range(len(numbers)):
            if num_map.get(_):
                tmp = num_map.get(numbers[_])
                num_map[numbers[_]] = str(tmp) + str(_)
            else:
                num_map[numbers[_]] = _
        
        index1, index2 = None, None
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if num_map.get(tmp, None):
                if isinstance(num_map.get(tmp), int):
                    index2 = num_map.get(tmp)
                    index1 = i
                    break
                elif isinstance(num_map.get(tmp), str):
                    index1 = i
                    index_2_list = [int(i) for i in num_map.get(tmp)]
                    for each in index_2_list:
                        if each > index1:
                            index2 = each
                    break
        return [index1, index2]

nums = [0, 3, 4, 0]
target = 0

print(Solution().twoSum(nums, target))