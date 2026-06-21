class Solution:
    def dfs(self, row, col, vis, mat, delrow, delcol):
        n = len(mat)
        m = len(mat[0])
        vis[row][col] = 1
        
        for i in range(4):
            nrow = row + delrow[i]
            ncol = col + delcol[i]
            
            if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and not vis[nrow][ncol] and mat[nrow][ncol] == 'O':
                self.dfs(nrow, ncol, vis, mat, delrow, delcol)
        
    def solve(self, grid: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(grid)
        m = len(grid[0])
        
        vis = [[0 for _ in range(m)] for _ in range(n)]
        
        delrow = [-1, 0, 1, 0]
        delcol = [0, 1, 0, -1]
        
        
        for j in range(m):
            if not vis[0][j] and grid[0][j] == 'O':
                self.dfs(0, j, vis, grid, delrow, delcol)
                
            if not vis[n - 1][j] and grid[n - 1][j] == 'O':
                self.dfs(n - 1, j, vis, grid, delrow, delcol)
                
                
        for i in range(n):
            if not vis[i][0] and grid[i][0] == 'O':
                self.dfs(i, 0, vis, grid, delrow, delcol)
                
            if not vis[i][m - 1] and grid[i][m - 1] == 'O':
                self.dfs(i, m - 1, vis, grid, delrow, delcol)
                
            
        for i in range(n):
            for j in range(m):
                if not vis[i][j] and grid[i][j] == 'O':
                    grid[i][j] = 'X'
                    
        return grid
        
        
        