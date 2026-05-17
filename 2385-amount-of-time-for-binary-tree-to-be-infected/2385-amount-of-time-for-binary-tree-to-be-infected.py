# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findMaxDist(self, mp, target):
        q = deque()
        q.append(target)

        vis = {}
        vis[target] = 1

        maxitime = 0

        while q:
            sz = len(q)
            fl = 0

            for _ in range(sz):
                node = q.popleft()

                if node.left and node.left not in vis:
                    fl = 1
                    vis[node.left] = 1
                    q.append(node.left)

                if node.right and node.right not in vis:
                    fl = 1
                    vis[node.right] = 1
                    q.append(node.right)

                if node in mp and mp[node] not in vis:
                    fl = 1
                    vis[mp[node]] = 1
                    q.append(mp[node])

            if fl:
                maxitime += 1

        return maxitime

    def bfsToMapParent(self, root, mp, start):
        q = deque([root])
        res = None

        while q:
            node = q.popleft()

            if node.val == start:
                res = node

            if node.left:
                mp[node.left] = node
                q.append(node.left)

            if node.right:
                mp[node.right] = node
                q.append(node.right)

        return res


    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        mp = {}

        target = self.bfsToMapParent(root, mp, start)

        maxitime = self.findMaxDist(mp, target)

        return maxitime

        