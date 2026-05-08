# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node: Optional[TreeNode], level: int, ds: List[int]):
        if node is None:
            return None
            
        if level == len(ds):
            ds.append(node.val)
        self.helper(node.right, level + 1, ds)
        self.helper(node.left, level + 1, ds)

       
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ds = []

        self.helper(root, 0, ds)

        return ds

        