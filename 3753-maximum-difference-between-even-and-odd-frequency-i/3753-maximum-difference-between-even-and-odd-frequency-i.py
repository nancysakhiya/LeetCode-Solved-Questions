class Solution:
    def maxDifference(self, s: str) -> int:
        mapp = [0] * 26
        maxim = 0
        minim = len(s)

        for c in s:
            mapp[ord(c) - ord('a')] += 1

        for i in range(26):
            if mapp[i] % 2 != 0:
                maxim = max(maxim, mapp[i])
            if mapp[i] % 2 == 0 and mapp[i] > 0:
                minim = min(minim, mapp[i])
        return maxim - minim
