from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, edges: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        
        for u, v, wt in edges:
            adj[u].append((v, wt))
            
        q = deque()
       
        q.append((0, (src, 0)))
        
        dist = [float('inf') for _ in range(n)]
        dist[src] = 0
        
        while q:
            it = q.popleft()
            
            stops = it[0]
            node = it[1][0]
            cost = it[1][1]
            
            if stops > k:
                continue
            
            for iterr in adj[node]:
                adjNode = iterr[0]
                edgwt = iterr[1]
                
                if cost + edgwt < dist[adjNode] and stops <= k:
                    dist[adjNode] = cost + edgwt
                    q.append((stops + 1, (adjNode, dist[adjNode])))
            
            
        if dist[dst] == float('inf'):
            return -1
            
        return dist[dst]
        
            
