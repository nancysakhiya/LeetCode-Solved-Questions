class Solution:
    def findsubstring(self, s):
        res = set()
        for i in range(len(s) - 1):
            res.add(s[i:i+2])

        return res

    def isSubstringPresent(self, s: str) -> bool:
        return  bool(self.findsubstring(s) & self.findsubstring(s[::-1]))