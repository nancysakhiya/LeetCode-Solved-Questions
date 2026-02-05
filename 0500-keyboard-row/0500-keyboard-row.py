class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        map1 = {}
        for c in "qwertyuiop":
            map1[c] = 1

        for c in "asdfghjkl":
            map1[c] = 2

        for c in "zxcvbnm":
            map1[c] = 3

        ans = []
        for w in words:
            lw = w.lower()
            r = map1[lw[0]]
            if all(map1[ch] == r for ch in lw):
                ans.append(w)

        return ans