# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        # in this function we will return sum and number of nodes
        if node is None:
            return 0, 0

        # we visit left and we visit right
        leftsum, leftnodecnt = self.dfs(node.left)
        rightsum, rightnodecnt = self.dfs(node.right)

        totalsum = node.val + leftsum + rightsum
        totalnodecnt = 1 + leftnodecnt + rightnodecnt

        avg = totalsum // totalnodecnt

        if node.val == avg:
            self.cnt += 1

        return totalsum, totalnodecnt

    def averageOfSubtree(self, root: TreeNode) -> int:
        self.cnt = 0
        self.dfs(root)

        return self.cnt
