# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        summ = 0

        if root.left:
            summ += root.left.val

        if root.right:
            summ += root.right.val

        if summ == root.val:
            return True

        return False