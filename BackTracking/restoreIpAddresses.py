# coding=utf-8

"""
恢复IP地址

描述:给一个由数字组成的字符串。求出其可能恢复为的所有IP地址。
(你的任务就是往这段字符串中添加三个点, 使它成为一个合法的IP地址. 返回所有可能的IP地址.)

思路: 所谓合法，就是不能0开头，也不能大于255
"""


class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    def restoreIpAddresses(self, s):
        # write your code here
        ips = []
        self.dfs(s, 0, ips, '')
        return ips

    def dfs(self, s, sub, ips, ip):
        if sub == 4:                    # ip 格式是4段
            if s == '':                 # 分配完毕
                ips.append(ip[1:])      # 从第一位开始，这是个深拷贝
        for i in range(1, 4):
            if i < len(s):
                if int(s[:i]) <= 255:
                    self.dfs(s, sub+1, ips, '.'.join([ip, s[:i]]))
                if s[0] == '0':
                    break 