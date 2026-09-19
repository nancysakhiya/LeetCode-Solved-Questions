class Solution:
    def setZeroes(self, nums: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(nums)
        m = len(nums[0])
        row = [0] * n
        col = [0] * m
        for i in range(n):
            for j in range(m):
                if nums[i][j] == 0:
                    row[i] = 1
                    col[j] = 1

        for i in range(n):
            for j in range(m):
                if row[i] or col[j]:
                    nums[i][j] = 0

        return nums