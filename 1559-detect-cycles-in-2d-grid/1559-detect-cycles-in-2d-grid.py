from collections import deque
class Solution:
    def bfs(self, row, col, vis, grid, delrow, delcol):
        vis[row][col] = 1
        n = len(grid)
        m = len(grid[0])

        # our queue should store parent-row and parent-col because when we are checking in all 4 direction, we need to make sure that the parent is not being part of any loop
        q = deque()
        q.append((row, col, -1, -1))

        while q:
            row, col, par_row, par_col = q.popleft()

            for i in range(len(delrow)):
                nrow = row + delrow[i]
                ncol = col + delcol[i]

                if nrow < 0 or nrow >= n or ncol < 0 or ncol >= m:
                    continue

                # we only need to move to same character
                if grid[nrow][ncol] != grid[row][col]:
                    continue

                # now if neighbor is not visited
                if not vis[nrow][ncol]:
                    vis[nrow][ncol] = 1
                    q.append((nrow, ncol, row, col))
                # if neighbor is already visited but it is not our parents and it has the same value as us then cycle detected
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

        