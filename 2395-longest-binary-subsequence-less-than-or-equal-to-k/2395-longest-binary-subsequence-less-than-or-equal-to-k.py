class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        cnt = 0
        sm = 0
        i = 0

        for ch in reversed(s):
            if ch == '0':
                cnt += 1
            elif i < 31 and sm + (1 << i) <= k:
                sm += (1 << i)
                cnt += 1
            i += 1
        return cnt