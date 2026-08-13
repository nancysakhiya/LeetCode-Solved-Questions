class Solution:
    def reverseWord(self, w):
        w = list(w)
        l = 0
        r = len(w) - 1

        while l < r:
            w[l], w[r] = w[r], w[l]
            l += 1
            r -= 1

        return ''.join(w)

    def reverseWords(self, s: str) -> str:
        words = s.split()
        res = []
    
        for word in words:
            rev = self.reverseWord(word)
            res.append(rev)
                
        return " ".join(res)
