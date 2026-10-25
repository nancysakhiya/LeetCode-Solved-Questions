class Solution:
    def issubseq(self, s, t):
        i = 0
        for ch in t:
            if i < len(s) and s[i] == ch:
                i += 1

        return i == len(s)

    def findLUSlength(self, strs: list[str]) -> int:
        maxlen = -1
        n = len(strs)

        for i in range(n):
            uncomon = True

            for j in range(n):
                if i != j and self.issubseq(strs[i], strs[j]):
                    uncomon = False
                    break

            if uncomon:
                maxlen = max(maxlen, len(strs[i]))

        return maxlen