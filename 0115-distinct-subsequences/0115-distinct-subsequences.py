class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        prev = [0] * (m + 1)
        

        prev[0] = 1

        for i in range(1, n + 1):
            cur = [0] * (m + 1)
            cur[0] = 1
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    cur[j] = prev[j-1] + prev[j]
                else:
                    cur[j] = prev[j]

            prev = cur

        return prev[m]


        