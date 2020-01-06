# coding=utf-8

"""
相对排名

描述:根据N名运动员的得分，找到他们的相对等级和获得最高分前三名的人，他们将获得奖牌：“金牌”，“银牌”和“铜牌”。
思路:就是简单排练，我用了hash map 来记录每个的位置

"""
class Solution:
    """
    @param nums: List[int]
    @return: return List[str]
    """
    def findRelativeRanks(self, nums):
        # write your code here
        hash_map = {}
        for _ in nums:
            hash_map[_] = ''
        nums.sort(reverse=True)
        n = 1
        for _ in nums:
            if n == 1:
                hash_map[_] = 'Gold Medal'
            elif n == 2:
                hash_map[_] = 'Silver Medal'
            elif n == 3:
                hash_map[_] = 'Bronze Medal'
            else:
                hash_map[_] = str(n)
            n += 1
        res = [value for value in hash_map.values()]
        return res
