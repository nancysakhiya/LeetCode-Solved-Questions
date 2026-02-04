class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)

        diffArr = [0] * n
        for shift in shifts:
            if shift[2] == 1:
                diffArr[shift[0]] += 1
                if shift[1] + 1 < n:
                    diffArr[shift[1] + 1] -= 1

            else:
                diffArr[shift[0]] -= 1
                if shift[1] + 1 < n:
                    diffArr[shift[1] + 1] += 1

        res = list(s)
        numOfShift = 0

        for i in range(n):
            numOfShift = (numOfShift + diffArr[i]) % 26

            if numOfShift < 0:
                numOfShift += 26

            shiftedChar = chr(
                (ord(s[i]) - ord("a") + numOfShift) % 26 + ord("a")
            )
            res[i] = shiftedChar

        return "".join(res)