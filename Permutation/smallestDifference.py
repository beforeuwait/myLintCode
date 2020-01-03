# coding=utf-8

"""
最小差

描述:给定两个整数数组（第一个是数组 A，第二个是数组 B），
在数组 A 中取 A[i]，数组 B 中取 B[j]，
A[i] 和 B[j]两者的差越小越好(|A[i] - B[j]|), 返回最小差。

思路: 合并为一个列表，然后前后比较取最小值
这样的有点在于，升序排列，两两比较 避开指针大和小的比较


"""
class Solution:
    """
    @param A: An integer array
    @param B: An integer array
    @return: Their smallest difference.
    """
    def smallestDifference(self, A, B):
        # write your code here
        # 这法子太棒了
        c = []
        for _ in A:
            c.append([_, 'A'])
        for _ in B:
            c.append([_, 'B'])
        c.sort(key=lambda x: x[0])
        c_len = len(c)
        res = None
        for i in range(0, c_len - 1):
            if c[i][1] != c[i+1][1]:
                if res is None:
                    res = abs(c[i][0] - c[i+1][0])
                else:
                    x = abs(c[i][0] - c[i+1][0])
                    res = min(res, x)
        return res
