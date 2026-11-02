class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0

        while i < len(s) and s[i] == " ":
            i += 1

        sign = 1
        if i < len(s) and s[i] == '-':
            sign = -1
            i += 1

        elif i < len(s) and s[i] == '+':
            sign = 1
            i += 1

        num = 0
        while i < len(s) and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')

            num = num * 10 + digit

            i += 1

        num = num * sign

        # handle overflow
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num
