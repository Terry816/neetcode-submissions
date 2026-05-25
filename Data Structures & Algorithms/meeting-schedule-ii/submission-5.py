"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x : x.start)
        minheap = [intervals[0].end]

        for i in intervals[1:]:
            if i.start >= minheap[0]:
                heapq.heappop(minheap)
            heapq.heappush(minheap, i.end)
        return len(minheap)
