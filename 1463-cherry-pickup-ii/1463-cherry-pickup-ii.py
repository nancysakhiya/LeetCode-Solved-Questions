class Solution:
    def helper(self, i, j1, j2, grid, dp):
        n = len(grid)
        m = len(grid[0])
        if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
            return -10**9

        if dp[i][j1][j2] != -1:
            return dp[i][j1][j2]

        if i == n-1:
            if j1 == j2:
                return grid[i][j1]
            else:
                return grid[i][j1] + grid[i][j2]

        maxi = -10**9
        for dj1 in range(-1, 2):
            for dj2 in range(-1, 2):
                val = 0
                if j1 == j2:
                    val = grid[i][j1]
                else:
                    val = grid[i][j1] + grid[i][j2]

                val += self.helper(i + 1, j1 + dj1, j2 + dj2, grid, dp)
                maxi = max(maxi, val)

        dp[i][j1][j2] = maxi

        return maxi

    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        dp = [[[-1 for _ in range(m)] for _ in range(m)] for _ in range(n)]

         
        return self.helper(0, 0, m - 1, grid, dp)
        