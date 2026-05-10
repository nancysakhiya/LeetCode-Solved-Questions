# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', n1: 'TreeNode', n2: 'TreeNode') -> 'TreeNode':
        if root is None or root == n1 or root == n2:
            return root
            
        left = self.lowestCommonAncestor(root.left, n1, n2)
        right = self.lowestCommonAncestor(root.right, n1, n2)
        
        if left is None:
            return right
            
        elif right is None:
            return left
            
        else:
            return root