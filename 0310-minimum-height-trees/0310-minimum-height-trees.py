from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # we first try to find leaf nodes. 
        # leaf node has excatly one neighbour. so the len of adj list of leaf is 1
        # we will use queue to store all the leaf nodes
        q = deque()
        for i in range(n):
            if len(adj[i]) == 1:
                q.append(i)

        noofnodeintree = n # this is the number of nodes in the tree

        # now we remove leaf nodes layer by layer
        # a tree can either have one center or 2 center
        while noofnodeintree > 2:
            size = len(q)

            for i in range(size):
                leaf = q.popleft()

                for it in adj[leaf]:
                    adj[it].remove(leaf)

                    if len(adj[it]) == 1:
                        q.append(it)

            # when we remove the nodes from the tree, we reduce the number of nodes from the tree
            noofnodeintree -= size

        return list(q)
