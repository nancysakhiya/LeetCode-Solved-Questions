# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, diameter):
        if node is None:
            return 0

        left = self.dfs(node.left, diameter)
        right = self.dfs(node.right, diameter)

        diameter[0] = max(diameter[0], left + right)

        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]

        self.dfs(root, diameter)

        return diameter[0]
        