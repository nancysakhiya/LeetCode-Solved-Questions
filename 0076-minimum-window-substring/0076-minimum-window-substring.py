class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashf = [0] * 256
        for ch in t:
            hashf[ord(ch)] += 1

        n = len(s)
        l = 0
        r = 0
        minlen = float('inf')
        stidx = -1
        cnt = 0

        while r < n:
            if hashf[ord(s[r])] > 0:
                cnt += 1

            hashf[ord(s[r])] -= 1

            while cnt == len(t):
                if (r-l+1) < minlen:
                    minlen = r - l + 1
                    stidx = l

                hashf[ord(s[l])] += 1

                if hashf[ord(s[l])] > 0:
                    cnt -= 1
                l += 1

            r += 1

        if stidx == -1:
            return ""

        return s[stidx:stidx+minlen]



        