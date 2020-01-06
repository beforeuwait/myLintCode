# coding=utf-8

"""
重排后为2的幂
给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。
如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。

思路: 这题没啥可说的


"""


class Solution:
    """
    @param N: 
    @return: return true or false
    """
    def reorderedPowerOf2(self, N):
        # write your code here
        # write your code here
        count = collections.Counter(str(N))
        return any(count == collections.Counter(str(1 << b))
                   for b in range(31))