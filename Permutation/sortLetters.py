# codng=utf-8

"""
字符大小写排序

描述:给定一个只包含字母的字符串，按照先小写字母后大写字母的顺序进行排序。

思路: 这里是返回 先小后大， 并没有要求给给具体排序
"""

class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters_new(self, chars):
        chars.sort(key=lambda c: c.isupper())

        
    def sortLetters(self, chars):
        if chars is None:
            return
        left, right = 0, len(chars) - 1
        while left <= right:
            while left <= right and chars[left].islower():
                left += 1
            while left <= right and chars[right].isupper():
                right -= 1
            if left <= right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        return 
    
