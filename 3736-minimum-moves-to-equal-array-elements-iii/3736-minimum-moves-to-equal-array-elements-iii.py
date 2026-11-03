class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)
        maxel = max(nums)
        cnt = 0

        for i in range(n):
            cnt += abs(nums[i] - maxel)

        return cnt        