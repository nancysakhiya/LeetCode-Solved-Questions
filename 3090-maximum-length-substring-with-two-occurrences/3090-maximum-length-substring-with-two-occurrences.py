class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        mpp = {}
        ans = 0

        l = 0
        for r in range(n):
            mpp[s[r]] = mpp.get(s[r], 0) + 1

            while mpp[s[r]] > 2:
                mpp[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
        