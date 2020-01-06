# coding=utf-8

"""
会议室 II

描述:给定一系列的会议时间间隔intervals，包括起始和结束时间[[s1,e1],[s2,e2],...] (si < ei)，找到所需的最小的会议室数量。

思路: 扫描算法

(0, 30), (5, 15), (20, 25)

->>
(0, 1), (5, 1), (15, -1), (20, 1), (25, -1), (30, -1)

可见，每个时间段需要增加还是减少的会议室，即可得最小的会议室
"""


"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # Write your code here
        # 扫线算法真牛皮
        meeting = []
        for interval in intervals:
            meeting.append((interval.start, 1))
            meeting.append((interval.end, -1))
        meeting.sort()
        is_meeting = 0
        meeting_room = 0
        for _, i in meeting:
            is_meeting += i
            meeting_room = max(meeting_room, is_meeting)
        return meeting_room