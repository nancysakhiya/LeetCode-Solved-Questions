class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        rowcnt = [0] * n
        colcnt = [0] * m

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    rowcnt[i] += 1
                    colcnt[j] += 1

        cnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if rowcnt[i] > 1 or colcnt[j] > 1:
                        cnt += 1

        return cnt

