"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        if not intervals: return True

        s1, e1 = intervals[0].start, intervals[0].end

        for interval in intervals[1:]:
            s2, e2 = interval.start, interval.end
            if s2 < e1:
                return False
            s1, e1 = s2, e2
        return True
