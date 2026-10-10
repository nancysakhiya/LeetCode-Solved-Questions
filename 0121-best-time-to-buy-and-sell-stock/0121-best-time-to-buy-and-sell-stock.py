class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0

        for i in range(len(prices)):
            minprice = min(minprice, prices[i])
            profit = prices[i] - minprice
            maxprofit = max(maxprofit, profit)

        return maxprofit