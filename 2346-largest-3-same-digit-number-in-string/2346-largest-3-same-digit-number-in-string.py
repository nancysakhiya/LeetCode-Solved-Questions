class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_digit = '\0'

        for idx in range(len(num) - 2):
            if num[idx] == num[idx + 1] == num[idx + 2]:
                max_digit = max(max_digit, num[idx])

        return '' if max_digit == '\0' else max_digit * 3
