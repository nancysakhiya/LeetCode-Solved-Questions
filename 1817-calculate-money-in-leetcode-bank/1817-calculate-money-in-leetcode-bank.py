class Solution:
    def totalMoney(self, n: int) -> int:
        monday = 1
        ans = 0

        while n > 0:
            for day in range(0, min(n, 7)):
                ans += monday + day
            n -= 7
            monday += 1

        return ans