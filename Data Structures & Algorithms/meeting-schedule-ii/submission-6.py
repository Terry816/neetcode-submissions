"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

we need to squeeze as many meetings into the same room as possible to find min

0-------------40
 5--10 15-20

have a minheap sorted by their end times. whatever the earliest end time (heap[0])
we can compare

if heap[0] <= interval.start: -> yes we can input this into our minheap.
use the same room, so pop it out first and then input the new entry

else:
    the earliest end time is after this one starts
    so take a new room
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start) # sort on start time
        minheap = []
        for interval in intervals:
            start, end = interval.start, interval.end
            if minheap and minheap[0] <= start:
                heapq.heappop(minheap)
            heapq.heappush(minheap, end)
        return len(minheap)

