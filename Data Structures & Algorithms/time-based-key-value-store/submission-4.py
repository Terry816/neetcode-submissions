"""
given that the timestamps are in increasing order the list is going to be sorted
and thus we can run binary search in O(logN) to get the value
"""

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) # key (str) : [(timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store: return ""

        lst = self.store[key] #(timestamp, value)
        
        l, r = 0, len(lst) - 1
        while l <= r:
            med = (r+l) // 2
            if lst[med][0] == timestamp:
                return lst[med][1]
            elif lst[med][0] < timestamp:
                l = med + 1
            else:
                r = med - 1
        return lst[r][1] if lst[r][0] < timestamp else ""

        # l - smallest value > timestamp
        # r - largest value < timestamp
