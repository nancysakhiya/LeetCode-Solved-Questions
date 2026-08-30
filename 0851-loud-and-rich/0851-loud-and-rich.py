from collections import deque
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        ans = list(range(n))

        adj = [[] for _ in range(n)]
        for u, v in richer:
            adj[u].append(v)

        # we will calculate indegree
        indegree = [0] * n
        for node in range(n):
            for it in adj[node]:
                indegree[it] += 1

        q = deque()
        # we will add node with zero indegree to queue
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            
            # now we modify the toposort
            for it in adj[node]:
                if quiet[ans[node]] < quiet[ans[it]]:
                    ans[it] = ans[node]

                indegree[it] -= 1

                if indegree[it] == 0:
                    q.append(it)

        return ans


        

        