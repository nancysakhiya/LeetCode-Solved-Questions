from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        n = len(graph)
        color = [-1] * len(graph)

        for start in range(n):
            if color[start] != -1:
                continue

            q = deque([start])
            color[start] = 0

            while q:
                node = q.popleft()
            
                for it in graph[node]:
                    if color[it] == -1:
                        color[it] = 1 - color[node]
                        q.append(it)
                    
                    elif color[it] == color[node]:
                        return False
                    
        return True
                
            
        
        