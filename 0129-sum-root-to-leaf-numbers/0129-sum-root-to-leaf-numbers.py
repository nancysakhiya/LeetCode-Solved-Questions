# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumofnum(self, node, currsumm):
        if not node:
            return 0

        currsumm = currsumm * 10 + node.val

        if node.left is None and node.right is None:
            return currsumm

        left = self.sumofnum(node.left, currsumm)
        right = self.sumofnum(node.right, currsumm)

        return left + right

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        currsumm = 0
        
        return self.sumofnum(root, currsumm)
        