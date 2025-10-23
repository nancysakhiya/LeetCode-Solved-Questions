class Solution:
    def hasSameDigits(self, s: str) -> bool:
        n = len(s)
        slist = list(s)
        for i in range(1, n-1):
            for j in range(n - i):
                dig1 = ord(slist[j]) - ord("0")
                dig2 = ord(slist[j+1]) - ord("0")
                slist[j] = chr(((dig1 + dig2) % 10) + ord("0"))
        return slist[0] == slist[1]