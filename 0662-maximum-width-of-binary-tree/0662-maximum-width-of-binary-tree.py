# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        
        q = deque([(root, 0)])
        max_width = 0

        while q:
            level_length = len(q)
            _, level_start = q[0]

            for i in range(level_length):
                node, idx = q.popleft()

                if node.left:
                    q.append((node.left, 2*idx))
                if node.right:
                    q.append((node.right, 2*idx+1))

            max_width = max(max_width, idx - level_start + 1)

        return max_width