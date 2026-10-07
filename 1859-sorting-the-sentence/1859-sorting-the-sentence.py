class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        res = [""] * len(words)

        for word in words:
            pos = int(word[-1])
            originalword = word[:-1]

            res[pos - 1] = originalword

        return " ".join(res)


        

        