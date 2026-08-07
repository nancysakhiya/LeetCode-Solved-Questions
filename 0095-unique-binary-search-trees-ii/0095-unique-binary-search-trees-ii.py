# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, start, end, mpp):
        res = []
        if start > end:
            res.append(None)
            return res

        if (start, end) in mpp:
            return mpp[(start, end)]

        for i in range(start, end + 1):
            leftsubtree = self.helper(start, i - 1, mpp)
            rightsubtree = self.helper(i + 1, end, mpp)

            for left in leftsubtree:
                for right in rightsubtree:
                    root = TreeNode(i, left, right)
                    res.append(root)

        mpp[(start, end)] = res
        return res


        
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        mpp = {}

        return self.helper(1, n, mpp)