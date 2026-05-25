class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        d = {i:[] for i in range(n)}
        for a,b in edges:
            d[a].append(b)
            d[b].append(a)

        def dfs(v, prev):
            seen.add(v)
            for neigh in d[v]:
                if neigh == prev:
                    continue
                if neigh not in seen:
                    dfs(neigh, v)
            return True

        res = 0
        for i in range(n):
            if i not in seen:
                dfs(i, -1)
                res += 1
        return res
        