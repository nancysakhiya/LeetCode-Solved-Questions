# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def arrTraversal(self, node, arr, ans):
        if not node:
            return
        
        arr.append(str(node.val))
        
        # if leaf node
        if not node.left and not node.right:
            ans.append("->".join(arr))
        
        # recursive calls
        self.arrTraversal(node.left, arr, ans)
        self.arrTraversal(node.right, arr, ans)
        
        # backtrack
        arr.pop()

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        arr = []
        
        self.arrTraversal(root, arr, ans)
        
        return ans