class Solution:
    def func(self, nums: List[int], goal: int) -> int:
        if goal < 0:
            return 0

        n = len(nums)
        l = 0
        r = 0
        summ = 0
        cnt = 0

        while r < n:
            summ = summ + nums[r]

            while (summ > goal):
                summ = summ - nums[l]
                l += 1

            cnt = cnt + (r - l + 1)

            r = r + 1
        return cnt

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.func(nums, goal) - self.func(nums, goal - 1)