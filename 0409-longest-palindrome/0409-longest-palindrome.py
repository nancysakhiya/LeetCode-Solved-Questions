class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        res = 0
        oddfreq = False
        for fre in freq.values():
            if (fre % 2) == 0:
                res += fre

            else:
                res += fre - 1
                oddfreq = True

        if oddfreq:
            return res + 1

        return res