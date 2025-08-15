from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        R, C = len(grid), len(grid[0])
        visited = set()
        DIRS = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(sr: int, sc: int) -> None:
            q = deque([(sr, sc)])
            visited.add((sr, sc))
            while q:
                r, c = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))

        count = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    count += 1

        return count
