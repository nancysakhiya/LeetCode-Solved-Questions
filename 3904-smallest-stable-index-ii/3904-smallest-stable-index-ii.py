class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        prefix = [0] * n
        prefix[0] = nums[0]
        for i in range(n):
            prefix[i] = max(prefix[i - 1], nums[i])

        sufix = [0] * n
        sufix[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            sufix[i] = min(sufix[i + 1], nums[i])

        for i in range(n):
            if prefix[i] - sufix[i] <= k:
                return i
        return -1