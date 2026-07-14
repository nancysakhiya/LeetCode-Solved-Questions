class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
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


        ans = ""
        i = n
        j = m
        while i > 0 and j > 0:
            if s1[i - 1] == s2[j - 1]:
                ans += s1[i - 1]
                i -= 1
                j -= 1

            elif dp[i-1][j] > dp[i][j-1]:
                ans += s1[i-1]
                i -= 1

            else:
                ans += s2[j-1]
                j -= 1

        while i > 0:
            ans += s1[i-1]
            i -= 1

        while j > 0:
            ans += s2[j - 1]
            j -= 1

        return ans[::-1]