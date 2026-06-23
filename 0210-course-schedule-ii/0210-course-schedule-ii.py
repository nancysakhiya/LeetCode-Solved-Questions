class Solution:
    def findOrder(self, V: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(V)]
        
        for first, second in prerequisites:
            adj[second].append(first)
            
        indegree = [0] * V

        for i in range(V):
            for it in adj[i]:
                indegree[it] += 1

        q = deque()

        for i in range(V):
            if indegree[i] == 0:
                q.append(i)

        topo = []

        while q:
            node = q.popleft()
            topo.append(node)

            for it in adj[node]:
                indegree[it] -= 1

                if indegree[it] == 0:
                    q.append(it)
                
        
        if len(topo) == V:
            return topo
            
        return []
        