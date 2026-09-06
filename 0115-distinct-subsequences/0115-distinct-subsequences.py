class Solution:
    def recursion(self, i, j, dp, s, t):
        if j < 0:
            return 1
        if i < 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if s[i] == t[j]:
            dp[i][j] = self.recursion(i - 1, j - 1, dp, s, t) + self.recursion(i - 1, j, dp, s, t)
        else:
            dp[i][j] = self.recursion(i - 1, j, dp, s, t)

        return dp[i][j]

    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

        return self.recursion(n - 1, m - 1, dp, s, t)
        