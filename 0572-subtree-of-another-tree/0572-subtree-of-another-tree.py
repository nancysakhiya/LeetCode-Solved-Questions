# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isIdentical(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None) or (q is None):
            return p == q
        
        return p.val == q.val and self.isIdentical(p.left, q.left) and self.isIdentical(p.right, q.right)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None or subRoot is None:
            return root == subRoot

        if root.val == subRoot.val and self.isIdentical(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    