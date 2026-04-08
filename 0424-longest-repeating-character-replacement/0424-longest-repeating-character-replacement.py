class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        r = 0
        maxfreq = 0
        maxlen = 0
        hashf = [0] * 26

        while r < n:
            hashf[ord(s[r]) - ord('A')] += 1

            maxfreq = max(maxfreq, hashf[ord(s[r]) - ord('A')])

            if (r - l + 1) - maxfreq > k:
                hashf[ord(s[l]) - ord('A')] -= 1
                maxfreq = 0

                for i in range(25):
                    maxfreq = max(maxfreq, hashf[i])

                l += 1

            if (r - l + 1) - maxfreq <= k:
                maxlen = max(maxlen, r-l+1)

            r += 1
        return maxlen
