import heapq
class Solution:
    def countPaths(self, V: int, edges: List[List[int]]) -> int:
        mod = 10**9 + 7
        adj = [[] for _ in range(V)]
        
        for u, v, t in edges:
            adj[u].append((v, t))
            adj[v].append((u, t))
            
        pq = []
        
        dist = [float('inf')] * V
        
        dist[0] = 0
        
        ways = [0] * V
        
        ways[0] = 1
        
        heapq.heappush(pq, (0, 0))
        
        while pq:
            it = heapq.heappop(pq)
            
            dis = it[0]
            node = it[1]
            
            for itr in adj[node]:
                adjNode = itr[0]
                edwt = itr[1]
                
                if dis + edwt < dist[adjNode]:
                    dist[adjNode] = dis + edwt
                    heapq.heappush(pq, (dis + edwt, adjNode))
                    
                    ways[adjNode] = ways[node]
                    
                elif dis + edwt == dist[adjNode]:
                    ways[adjNode] = (ways[adjNode] + ways[node]) % mod
                    
                    
                    
        return (ways[V-1]) % mod
                    
                    