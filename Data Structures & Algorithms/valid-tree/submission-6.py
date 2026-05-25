class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        cycle = set()
        d = {i:[] for i in range(n)}
        for v1, v2 in edges:
            d[v1].append(v2)
            d[v2].append(v1)

        def dfs(v, prev):
            if v in cycle:
                return False
            cycle.add(v)
            for neighbor in d[v]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, v):
                    return False
            return True

        return dfs(0, -1) and len(cycle) == n
