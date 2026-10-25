class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        ans = [0] * n
        pos = []

        for i in range(n):
            if s[i] == c:
                pos.append(i)

        for i in range(n):
            minidis = float('inf')

            for j in pos:
                minidis = min(minidis, abs(i - j))

            ans[i] = minidis

        return ans

