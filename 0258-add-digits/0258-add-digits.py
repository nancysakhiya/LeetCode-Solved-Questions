class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return num

        while num >= 10:
            total = 0

            for digit in str(num):
                total += int(digit)

            num = total

        return num
        