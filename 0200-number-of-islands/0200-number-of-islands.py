from collections import deque
class Solution:
    def bfs(self, row, col, vis, grid, delrow, delcol):
        vis[row][col] = 1
        q = deque()
        q.append((row, col))
        n = len(grid)
        m = len(grid[0])

        while q:
            row, col = q.popleft()

            for i in range(len(delrow)):
                nrow = row + delrow[i]
                ncol = col + delcol[i]

                if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and grid[nrow][ncol] == '1' and not vis[nrow][ncol]:
                    vis[nrow][ncol] = 1
                    q.append((nrow, ncol))


    def numIslands(self, grid: List[List[str]]) -> int:
        # we will do bfs traversal whenever we find land
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        cnt = 0

        delrow = [-1, 0, 1, 0]
        delcol = [0, 1, 0, -1]

        for i in range(n):
            for j in range(m):
                if not vis[i][j] and grid[i][j] == '1':
                    cnt += 1
                    self.bfs(i, j, vis, grid, delrow, delcol)

        return cnt