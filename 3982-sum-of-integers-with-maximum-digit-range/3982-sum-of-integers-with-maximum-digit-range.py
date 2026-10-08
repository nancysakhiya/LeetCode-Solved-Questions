class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        n = len(nums)
        maxdigitrang = float('-inf')

        for num in nums:
            digits = [int(i) for i in str(num)]
            rang = max(digits) - min(digits)
            maxdigitrang = max(maxdigitrang, rang)

        ans = 0

        for num in nums:
            digits = [int(i) for i in str(num)]

            rang = max(digits) - min(digits)

            if rang == maxdigitrang:
                ans += num

        return ans