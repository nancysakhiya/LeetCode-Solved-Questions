class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        total = 0
        res = list(s)

        for i in range(len(s) - 1, -1, -1):
            total = (total + shifts[i]) % 26
            res[i] = chr((ord(s[i]) - ord('a') + total) % 26 + ord('a'))

        return ''.join(res)