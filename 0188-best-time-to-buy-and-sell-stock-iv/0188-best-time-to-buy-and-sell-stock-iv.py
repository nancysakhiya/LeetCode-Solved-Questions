class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0 for _ in range(k + 1)] for _ in range(2)] for _ in range(n+1)]

        
        for i in range(n - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, k+1):
                    if buy:
                        dp[i][buy][cap] = max(-prices[i] + dp[i + 1][0][cap], 0 + dp[i + 1][1][cap])
                    
                    else:
                        dp[i][buy][cap] = max(prices[i] + dp[i+1][1][cap-1], 0 + dp[i+1][0][cap])

        return dp[0][1][k]

                
            
        
       
