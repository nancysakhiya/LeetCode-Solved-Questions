class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hashf = [-1] * 256
        l = 0
        r = 0
        maxlen = 0

        while r < n:
            if hashf[ord(s[r])] != -1:
                if hashf[ord(s[r])] >= l:
                    l = hashf[ord(s[r])] + 1

            hashf[ord(s[r])] = r

            
            maxlen = max(maxlen, r - l + 1)
            r += 1

        return maxlen

