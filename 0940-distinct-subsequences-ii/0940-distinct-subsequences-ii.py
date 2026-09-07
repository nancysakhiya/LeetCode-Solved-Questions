class Solution:
    def recursion(self, i, s, dp, prev):
        n = len(s)
        if i < 0:
            return 1

        if dp[i] != -1:
            return dp[i]
        
        take = self.recursion(i - 1, s, dp, prev)
        nontake = self.recursion(i - 1, s, dp, prev)

        ans = take + nontake

        if s[i] in prev:
            j = prev[s[i]]
            ans -= self.recursion(j - 1, s, dp, prev)

        prev[s[i]] = i

        dp[i] = ans

        return dp[i]

    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        dp = [-1 for _ in range(n + 1)]

        prev = {}

        return (self.recursion(n - 1, s, dp, prev) - 1) % (10**9 + 7)
        