from math import isqrt
class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for a in range(1, n):
            for b in range(1, n):
                csquare = a * a + b * b
                c = isqrt(csquare)

                if c <= n and c * c == csquare:
                    cnt += 1     

        return cnt

