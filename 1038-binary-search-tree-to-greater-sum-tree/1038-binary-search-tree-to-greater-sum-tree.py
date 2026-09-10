# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if node is None:
            return

        self.dfs(node.right)

        self.sum += node.val

        node.val = self.sum

        self.dfs(node.left)


    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum = 0

        self.dfs(root)

        return root