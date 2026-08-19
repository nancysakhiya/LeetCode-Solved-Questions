class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxlen = 0
        mpp = {chr(i): -1 for i in range(256)}
        l = 0
        r = 0

        while r < n:
            if mpp[s[r]] != -1:
                if mpp[s[r]] >= l:
                    l = mpp[s[r]] + 1

            maxlen = max(maxlen, r - l + 1)
            mpp[s[r]] = r
            r += 1

        return maxlen