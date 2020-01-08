# coding=utf-8

"""
汉诺塔

描述:汉诺塔问题（又称为河内塔问题），是一个大家熟知的问题。在A，B，C三根柱子上，有n个不同大小的圆盘（假设半径分别为1-n吧），一开始他们都叠在我A上（如图所示），你的目标是在最少的合法移动步数内将所有盘子从A塔移动到C塔。
游戏中的每一步规则如下：
每一步只允许移动一个盘子（从一根柱子最上方到另一个柱子的最上方）
移动的过程中，你必须保证大的盘子不能在小的盘子上方（小的可以放在大的上面，最大盘子下面不能有任何其他大小的盘子)

思路:

移动 n-1次
把最大换到最边上
再移动 n-1次

这题挺有意思的
"""

class Solution:
    """
    @param n: the number of disks
    @return: the order of moves
    """
    def __init__(self):
        self.step = ["from A to B", "from A to C", "from B to A", "from B to C", "from C to A", "from C to B"]
        self.result = []
    def towerOfHanoi(self, n):
        # write your code here
        self.haoni(n, 'A', 'B', 'C')
        return self.result

    def haoni(self, n, a, b, c):
        if n == 1:
            self.move(a, c)
        else:
            self.haoni(n-1, a, c, b)
            self.move(a, c)
            self.haoni(n-1, b, a, c)
    
    def move(self, m, n):
        if m == 'A':
            s = 1 if n =='C' else 0
            self.result.append(self.step[s])
        elif m == 'B':
            s = 2 if n == 'A' else 3
            self.result.append(self.step[s])
        else:
            s = 4 if n == 'A' else 5
            self.result.append(self.step[s])

print(Solution().towerOfHanoi(5))