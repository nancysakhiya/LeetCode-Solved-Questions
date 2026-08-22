# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binarySum(self, node, curr):
        if not node:
            return 0
        
        curr = curr * 2 + node.val

        if node.left is None and node.right is None:
            return curr
            
        left = self.binarySum(node.left, curr)
        right = self.binarySum(node.right, curr)

        return left + right


    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        return self.binarySum(root, 0)
        