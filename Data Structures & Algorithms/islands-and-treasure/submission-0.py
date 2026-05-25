from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        visited = set()
        iteration = 1
        q = deque()
        
        def bfs(q, iteration):
            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            res = deque()
            print(f"this is q {q}")
            while q:
                rval, cval = q.popleft()
                for dr, dc in directions:
                    r,c  = dr +rval, dc +cval
                    if (r,c) in visited:
                        continue
                    if r in range(row) and c in range(col) and  \
                    grid[r][c] == 2147483647:
                        grid[r][c] = iteration
                        visited.add((r,c))
                        res.append((r,c))
                    else:
                        visited.add((r,c))
            return res 

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        
        while q:
            new = bfs(q, iteration)
            iteration += 1
            q = new
        
