class Solution:
    def helper(self, j, i, s2, s1, dp):
        if i < 0 and j < 0:
            return True
            
        if i < 0 and j >= 0:
            return False
            
        if j < 0 and i >= 0:
            for it in range(i + 1):
                if s1[it] != '*':
                    return False
                    
            return True
            
        if dp[j][i] != -1:
            return dp[j][i]
            
        if s1[i] == s2[j] or s1[i] == '?':
            dp[j][i] = self.helper(j - 1, i - 1, s2, s1, dp)
            
        elif s1[i] == '*':
            dp[j][i] = (self.helper(j - 1, i, s2, s1, dp) or self.helper(j, i - 1, s2, s1, dp))
            
        else:
            dp[j][i] = False
            
        return dp[j][i]
            
        
    def isMatch(self, txt: str, pat: str) -> bool:
        m = len(txt)
        n = len(pat)
        
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        
        return self.helper(m - 1, n - 1, txt, pat, dp)
        