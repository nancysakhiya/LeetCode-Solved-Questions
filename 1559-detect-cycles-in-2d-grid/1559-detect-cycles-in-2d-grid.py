from collections import deque
class Solution:
    def bfs(self, row, col, vis, grid, delrow, delcol):
        vis[row][col] = 1
        q = deque()
        q.append((row, col, -1, -1))

        n = len(grid)
        m = len(grid[0])

        while q:
            row, col, par_row, par_col = q.popleft()

            for i in range(4):
                nrow = row + delrow[i]
                ncol = col + delcol[i]

                if nrow < 0 or nrow >= n or ncol < 0 or ncol >= m:
                    continue

                if grid[nrow][ncol] != grid[row][col]:
                    continue
                
                if not vis[nrow][ncol]:
                    vis[nrow][ncol] = 1
                    q.append((nrow, ncol, row, col))

                else:
                    if nrow != par_row or ncol != par_col:
                        return True

        return False
                    

    def containsCycle(self, grid: List[List[str]]) -> bool:
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]

        delrow = [-1, 0, 1, 0]
        delcol = [0, 1, 0, -1]

        for i in range(n):
            for j in range(m):
                if not vis[i][j]:
                    if self.bfs(i, j, vis, grid, delrow, delcol):
                        return True

        return False
