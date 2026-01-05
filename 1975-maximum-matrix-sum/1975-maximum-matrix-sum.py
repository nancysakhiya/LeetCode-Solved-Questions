class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        totalsum = 0
        minAbsVal = float("inf")
        negcount = 0

        for row in matrix:
            for val in row:
                totalsum += abs(val)
                if val < 0:
                    negcount += 1
                minAbsVal = min(minAbsVal, abs(val))

        if negcount % 2 != 0:
            totalsum -= 2 * minAbsVal

        return totalsum
