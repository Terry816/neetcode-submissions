import heapq
class MedianFinder:

    def __init__(self):
        self.minheap = [] #minheap of large value
        self.maxheap = [] #maxheap of small values

    def addNum(self, num: int) -> None:
        smallest = self.minheap[0] if self.minheap else float("inf")
        largest = -self.maxheap[0] if self.maxheap else float("-inf")

        if num < smallest:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)
        
        while len(self.minheap) > len(self.maxheap) + 1:
            n = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -n)
        
        while len(self.maxheap) > len(self.minheap) + 1:
            n = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -n) 

    def findMedian(self) -> float:
        #odd 
        if (len(self.minheap) + len(self.maxheap)) % 2 == 1:
            return self.minheap[0] if len(self.minheap) > len(self.maxheap) else -self.maxheap[0] 
        else:
            left = self.minheap[0] if self.minheap else 0
            right = -self.maxheap[0] if self.maxheap else 0
            return (left+right)/ 2

"""
minheap - 2.0, 2.0
maxheap - -1.0
"""
        
        