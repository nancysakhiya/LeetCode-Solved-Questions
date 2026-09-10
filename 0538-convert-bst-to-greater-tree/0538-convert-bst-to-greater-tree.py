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

        # we first visit the larger value
        self.dfs(node.right)

        #then we add current node to the sum
        self.sum += node.val

        # we change the val of the current node
        node.val = self.sum

        self.dfs(node.left)

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # we will visit the largest value first

        self.sum = 0
        self.dfs(root)

        return root
