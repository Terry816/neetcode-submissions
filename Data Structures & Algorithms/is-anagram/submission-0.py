class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1, d2 = defaultdict(int), defaultdict(int)

        for i in s:
            d1[i] += 1
        
        for j in t:
            d2[j] += 1
        
        for i in set(s):
            if d1[i] != d2[i]:
                return False
        return True