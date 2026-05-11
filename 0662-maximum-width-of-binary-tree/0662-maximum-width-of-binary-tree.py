# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
            
        q = deque([(root, 0)])
        maxWidth = 0
        
        while q:
            levelSize = len(q)
            mini = q[0][1]
            first = last = 0
            
            
            for i in range(levelSize):
                node, idx = q.popleft()
                curr_idx = idx - mini
                if i == 0:
                    first = curr_idx
                if i == levelSize - 1:
                    last = curr_idx
                if node.left:
                    q.append((node.left, curr_idx*2 + 1))
                if node.right:
                    q.append((node.right, curr_idx*2 + 2))

            maxWidth = max(maxWidth, last - first + 1)
                    
        return maxWidth