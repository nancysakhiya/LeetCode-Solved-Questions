from collections import deque
class Solution:
    def updateMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        dis = [[0 for _ in range(m)] for _ in range(n)]

        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append(((i, j), 0))
                    vis[i][j] = 1

        nrow = [-1, 0, 1, 0]
        ncol = [0, 1, 0, -1]

        while q:
            (row, col), step = q.popleft()

            dis[row][col] = step

            for k in range(4):
                neirow = row + nrow[k]
                neicol = col + ncol[k]

                if (
                    0 <= neirow < n
                    and 0 <= neicol < m
                    and vis[neirow][neicol] == 0
                ):
                    vis[neirow][neicol] = 1
                    q.append(((neirow, neicol), step + 1))

        return dis