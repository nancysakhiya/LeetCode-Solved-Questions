class Solution:
    def maxidx(self, mat: List[List[int]], col: int) -> int:
        maxval = -1
        idx = -1
        for i in range(len(mat)):
            if mat[i][col] > maxval:
                maxval = mat[i][col]
                idx = i
            
        return idx

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])

        l = 0
        h = m - 1

        while l <= h:
            mid = l + (h - l) // 2

            row = self.maxidx(mat, mid)

            left = mat[row][mid - 1] if mid - 1 >= 0 else -1
            right = mat[row][mid + 1] if mid + 1 < m else -1

            if mat[row][mid] > left and mat[row][mid] > right:
                return [row, mid]
            elif mat[row][mid] < left:
                h = mid - 1
            else:
                l = mid + 1

        return [-1, -1]
        