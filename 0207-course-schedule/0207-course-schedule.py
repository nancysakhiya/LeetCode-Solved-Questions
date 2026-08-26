from collections import deque
class Solution:
    def canFinish(self, V: int, pre: List[List[int]]) -> bool:
        adj = [[] for _ in range(V)]
        for u, v in pre:
            adj[u].append(v)

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
            return True

        return False        