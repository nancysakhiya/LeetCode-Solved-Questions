# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node, arr):
        if node is None:
            return

        self.inorder(node.left, arr)
        arr.append(node.val)
        self.inorder(node.right, arr)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # we first create a arr of node from inoder traversal because inorder traversal gives sorted arr
        arr = []
        self.inorder(root, arr)

        l = 0
        r = len(arr) - 1

        while l < r:
            mid = arr[l] + arr[r]

            if mid == k:
                return True

            elif mid < k:
                l += 1
            else:
                r -= 1

        return False


            

