class Solution:
    def dfs(self, node, edges, vis, pathvis, check):
        vis[node] = 1
        pathvis[node] = 1
        check[node] = 0
        
        for it in edges[node]:
            if not vis[it]:
                if self.dfs(it, edges, vis, pathvis, check):
                    check[node] = 0
                    return True
                    
            elif pathvis[it]:
                check[node] = 0
                return True
                
        check[node] = 1
        pathvis[node] = 0
        return False

    def eventualSafeNodes(self, edges: List[List[int]]) -> List[int]:
        V = len(edges)
            
        vis = [0] * V
        pathvis = [0] * V
        safenode = []
        check = [0] * V
        
        for i in range(V):
            if not vis[i]:
                self.dfs(i, edges, vis, pathvis, check)
                
        for i in range(V):
            if check[i] == 1:
                safenode.append(i)
                    
        return safenode
        