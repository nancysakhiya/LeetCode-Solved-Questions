class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        # we use dp
        n = len(nums)
        res = [0] *  k
        dp = [0] * k

        for i in range(n):
            ndp = [0] * k # current array

            ndp[nums[i] % k] += 1

            for r in range(k):
                ndp[(r * nums[i]) % k] += dp[r]

            dp = ndp

            for r in range(k):
                res[r] += dp[r]

        return res