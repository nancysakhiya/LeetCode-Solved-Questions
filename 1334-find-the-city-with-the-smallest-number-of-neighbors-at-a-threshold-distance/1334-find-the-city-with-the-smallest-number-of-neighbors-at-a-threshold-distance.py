class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf') for _ in range(n)] for _ in range(n)]
        
        for it in edges:
            dist[it[0]][it[1]] = it[2]
            dist[it[1]][it[0]] = it[2]
            
        for i in range(n):
            dist[i][i] = 0
            
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] == float('inf') or dist[k][j] == float('inf'):
                        continue
                    
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                    
                    
        cntcity = n
        cityNo = -1
        
        for city in range(n):
            cnt = 0
            for adjcity in range(n):
                if dist[city][adjcity] <= distanceThreshold:
                    cnt += 1
                    
            if cnt <= cntcity:
                cntcity = cnt
                cityNo = city
                
        return cityNo