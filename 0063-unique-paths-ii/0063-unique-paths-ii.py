class Solution:
    def helper(self, i, j, grid, dp):
        if i >= 0 and j >= 0 and grid[i][j] == 1:
            return 0
        
        if i == 0 and j == 0:
            return 1
            
        if i < 0 or j < 0:
            return 0
            
        if dp[i][j] != -1:
            return dp[i][j]
            
        up = self.helper(i - 1, j, grid, dp)
        left = self.helper(i, j - 1, grid, dp)
         
        dp[i][j] = up + left
        
        return dp[i][j]

    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        
        return self.helper(m - 1, n - 1, grid, dp) 