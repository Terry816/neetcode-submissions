class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row, col = len(grid), len(grid[0])
        directions = [[1,0], [0,1], [-1,0],[0,-1]]
        #from each treasure chest position do a incremental BFS
        #when to stop? when all land tiles have been modified
        time = 1
        q = deque()
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append((r,c))

        while q:
            for _ in range(len(q)):
                rval, cval = q.popleft()
                for dr, dc in directions:
                    r,c = dr +rval, dc+ cval
                    if (0 <= r < row and 0 <= c < col and 
                        grid[r][c] == 2147483647):
                        grid[r][c] = time
                        q.append((r,c))
            time += 1
        return
