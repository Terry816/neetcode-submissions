class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        seen = set()
        q, land = deque(), 0
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append((r,c))
                    seen.add((r,c))
                elif grid[r][c] == 2147483647:
                    land += 1
        time = 1
        while q and land > 0:
            for _ in range(len(q)):
                rval, cval = q.popleft()
                for dr, dc in directions:
                    r, c = rval + dr, cval + dc
                    if (r in range(row) and c in range(col) and
                        (r,c) not in seen and grid[r][c] == 2147483647):
                        grid[r][c] = time
                        seen.add((r,c))
                        q.append((r,c))
                        land -= 1
            time += 1
        