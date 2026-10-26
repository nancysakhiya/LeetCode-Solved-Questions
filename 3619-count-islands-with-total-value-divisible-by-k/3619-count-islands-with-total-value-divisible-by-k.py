from collections import deque
class Solution:
    def bfs(self, row, col, vis, grid, delrow, delcol):
        vis[row][col] = 1
        q = deque()
        q.append((row, col))

        n = len(grid)
        m = len(grid[0])

        summ = 0

        while q:
            row, col = q.popleft()

            summ += grid[row][col]

            for i in range(len(delrow)):
                nrow = row + delrow[i]
                ncol = col + delcol[i]

                if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and grid[nrow][ncol] != 0 and not vis[nrow][ncol]:
                    vis[nrow][ncol] = 1
                    q.append((nrow, ncol))

        return summ

    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])

        vis = [[0 for _ in range(m)] for _ in range(n)]

        delrow = [-1, 0, 1, 0]
        delcol = [0, 1, 0, -1]

        cnt = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0 and not vis[i][j]:
                    vis[i][j] = 1
                    if (self.bfs(i, j, vis, grid, delrow, delcol)) % k == 0:
                        cnt += 1

        return cnt

