class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjMap = defaultdict(list) # crs: [prereqs]
        for n in range(numCourses):
            adjMap[n] = []
            
        for crs, pre in prerequisites:
            adjMap[crs].append(pre)

        res = []
        seen, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in seen:
                return True
            cycle.add(crs)
            for nei in adjMap[crs]:
                if not dfs(nei):
                    return False
            cycle.remove(crs)
            seen.add(crs)
            res.append(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res
        
