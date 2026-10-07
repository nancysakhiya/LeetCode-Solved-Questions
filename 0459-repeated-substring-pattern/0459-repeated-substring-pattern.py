class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for length in range(1, n):
            if n % length == 0:
                substr = s[:length]

            if substr * (n // length) == s:
                return True

        return False
