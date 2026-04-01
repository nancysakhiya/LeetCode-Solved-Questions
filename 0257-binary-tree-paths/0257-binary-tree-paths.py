# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def allPaths(self, root: Optional[TreeNode], path, ans):
        if root.left is None and root.right is None:
            ans.append(path)
            return 

        if root.left:
            self.allPaths(root.left, path + "->" + str(root.left.val), ans)

        if root.right:
            self.allPaths(root.right, path + "->" + str(root.right.val), ans)


    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []

        ans = []
        path = str(root.val)
        self.allPaths(root, path, ans)
        return ans
        