from collections import deque

class Solution:
    def findOrder(self, V: int, pre: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(V)]
        for v, u in pre:
            adj[u].append(v)

        # calculating indegree
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

            # the node is in the topo so we remove it from the indegree
            for it in adj[node]:
                indegree[it] -= 1
                if indegree[it] == 0:
                    q.append(it)

        if len(topo) != V:
            return []

        return topo

        
