class Solution:
    def dfs(self, grid, i, j):
        rows = len(grid)
        cols = len(grid[0])

        grid[i][j] = 1 #marked visited

        closed = (i != 0 and j != 0 and i != rows - 1 and j != cols - 1)

        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        for k in range(4):
            nr = i + dx[k]
            nc = j + dy[k]

            if (0 <= nr < rows and 0 <= nc < cols) and grid[nr][nc] == 0:
                res = self.dfs(grid, nr, nc)
                closed = closed and res

        return closed

    def closedIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        cnt = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    if self.dfs(grid, i, j):
                        cnt += 1

        return cnt
        