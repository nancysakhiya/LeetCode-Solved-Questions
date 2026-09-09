class Solution:
    def countCommas(self, n: int) -> int:
        cntcomma = 0

        start = 1000
        commas = 1

        while start <= n:
            end = min(n, start * 1000 - 1)

            count = end - start + 1
            cntcomma += count * commas

            start *= 1000
            commas += 1

        return cntcomma