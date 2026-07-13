class Solution:
    def lcs(self, s1, s2):
        # code here
        n = len(s1)
        m = len(s2)
        
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        
        for j in range(m):
            dp[0][j] = 0
            
        for i in range(n):
            dp[i][0] = 0
            
        for idx1 in range(1, n + 1):
            for idx2 in range(1, m + 1):
                if s1[idx1 - 1] == s2[idx2 - 1]:
                    dp[idx1][idx2] = 1 + dp[idx1 - 1][idx2 - 1]
            
                else:
                    dp[idx1][idx2] = max(dp[idx1 - 1][idx2], dp[idx1][idx2 - 1])
        
        return dp[n][m]

    def longestPalindromeSubseq(self, s: str) -> int:

        return self.lcs(s, s[::-1])
        