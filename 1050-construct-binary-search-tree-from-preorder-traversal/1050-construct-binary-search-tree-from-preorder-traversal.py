# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def helper(i, j):
            if i >= j:
                return None
            root = TreeNode(preorder[i])
            mid = i + 1
            while mid < j and preorder[mid] < preorder[i]:
                mid += 1
            root.left = helper(i + 1, mid)
            root.right = helper(mid, j)
            return root
        return helper(0, len(preorder))
