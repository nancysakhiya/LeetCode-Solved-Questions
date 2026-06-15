class Solution:
    def dfs(self, node, adj, vis):
        vis[node] = 1
       
        for it in adj[node]:
            if not vis[it]:
                self.dfs(it, adj, vis)
                
    def findCircleNum(self, edges: List[List[int]]) -> int:
        V = len(edges)
        adj = [[] for _ in range(V)]
        for i in range(V):
            for j in range(V):
                if edges[i][j] == 1 and i != j:
                    adj[i].append(j)
                    adj[j].append(i)
        n = len(adj)
        vis = [0] * V
        cnt = 0
        
        for i in range(V):
            if not vis[i]:
                cnt += 1
                self.dfs(i, adj, vis)
                
        return cnt
        