class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]

        for j in range(0, m):
            dp[0][j] = matrix[0][j]

        for i in range(1, n):
            for j in range(0, m):
                up = matrix[i][j] + dp[i - 1][j]
                ld = matrix[i][j]
                if j - 1 >= 0:
                    ld += dp[i - 1][j - 1]
                else:
                    ld += 10**9
                rd = matrix[i][j]
                if j + 1 < m:
                    rd += dp[i - 1][j + 1]
                else:
                    rd += 10**9

                dp[i][j] = min(up, ld, rd)

        minii = dp[n - 1][0]
        for j in range(1, m):
            minii = min(minii, dp[n - 1][j])

        return minii


