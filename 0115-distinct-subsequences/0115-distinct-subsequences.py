class Solution:
    def helper(self, i, j, s, t, dp):
        if j == 0:
            return 1
        if i == 0:
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        if s[i - 1] == t[j - 1]:
            dp[i][j] = self.helper(i-1, j-1, s, t, dp) + self.helper(i-1, j, s, t, dp)
        else:
            dp[i][j] = self.helper(i - 1, j, s, t, dp)

        return dp[i][j]

        
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

        return self.helper(n, m, s, t, dp)