import heapq
class Solution:
    def minimumEffortPath(self, mat: List[List[int]]) -> int:
        pq = []
        
        n = len(mat)
        m = len(mat[0])
        
        diffa = [[float('inf') for _ in range(m)] for _ in range(n)]
        
        diffa[0][0] = 0
        
        heapq.heappush(pq, (0, (0, 0)))
        
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        
        while pq:
            it = heapq.heappop(pq)
            
            diff = it[0]
            row = it[1][0]
            col = it[1][1]
            
            if row == n - 1 and col == m - 1:
                return diff
            
            for i in range(4):
                nrow = row + dr[i]
                ncol = col + dc[i]
                
                if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m:
                    neweff = max(abs(mat[row][col] - mat[nrow][ncol]), diff)
                    
                    if neweff < diffa[nrow][ncol]:
                        diffa[nrow][ncol] = neweff
                        
                        heapq.heappush(pq, (neweff, (nrow, ncol)))
                        
                        
                    
        return 0
        
        
