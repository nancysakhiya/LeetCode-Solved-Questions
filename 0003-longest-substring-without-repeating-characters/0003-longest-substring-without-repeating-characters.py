class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we store each characters last seen
        mpp = {}
        l = 0
        maxlen = 0

        for r in range(len(s)):
            if s[r] in mpp:
                l = max(l, mpp[s[r]] + 1)

            mpp[s[r]] = r
            maxlen = max(maxlen, r - l + 1)

        return maxlen

