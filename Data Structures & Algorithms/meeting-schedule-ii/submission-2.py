"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #minheap will store the smallest end time
        #if we find a new starting value that is >= minheap[0]
        # then we just want to combine then into the same day - greedily (no need
        #to check all the other ones. always grab the smallest)
        minheap = []
        intervals.sort(key = lambda x: x.start)
        days = 0
        for i in intervals:
            if minheap and minheap[0] <= i.start:
                heapq.heappop(minheap)
                heapq.heappush(minheap, i.end)
            else:
                heapq.heappush(minheap, i.end)
                days+= 1
        
        return days