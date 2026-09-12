
class Solution:
    def recursion(self, i, j, arr, dp):
        # base case
        if i == len(arr):
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        # non take
        notake = self.recursion(i + 1, j, arr, dp)

        # take
        take = 0
        if arr[i] <= j:
            take = arr[i] + self.recursion(i + 1, j - arr[i], arr, dp)

        dp[i][j] = max(take, notake)

        return dp[i][j]

    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        total = sum(stones)
        j = total // 2

        dp = [[-1 for _ in range(j + 1)] for _ in range(n)]

        best = self.recursion(0, j, stones, dp)

        return total - 2 * best
        