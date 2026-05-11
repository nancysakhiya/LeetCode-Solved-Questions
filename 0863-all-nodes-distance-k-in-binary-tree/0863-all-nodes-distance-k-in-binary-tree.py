# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def markParents(self, node, parent_track, target):
        q = deque([node])

        while q:
            curr = q.popleft()
            if curr.left:
                parent_track[curr.left] = curr
                q.append(curr.left)
            if curr.right:
                parent_track[curr.right] = curr
                q.append(curr.right)
            

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_track = {}

        self.markParents(root, parent_track, target)

        visited = {}

        q = deque([target])

        visited[target] = True

        curr_level = 0

        while q:
            size = len(q)

            if curr_level == k:
                break

            curr_level += 1

            for i in range(size):
                curr = q.popleft()

                if curr.left and curr.left not in visited:
                    q.append(curr.left)
                    visited[curr.left] = True

                if curr.right and curr.right not in visited:
                    q.append(curr.right)
                    visited[curr.right] = True

                if curr in parent_track and parent_track[curr] not in visited:
                    q.append(parent_track[curr])
                    visited[parent_track[curr]] = True

        res = []

        while q:
            curr = q.popleft()
            res.append(curr.val)

        return res