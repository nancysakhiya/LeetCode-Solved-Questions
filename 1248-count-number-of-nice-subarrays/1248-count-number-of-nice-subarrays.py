class Solution:
    def helper(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        r = 0
        summ =0
        cnt = 0

        while r < n:
            summ = summ + (nums[r] % 2)

            while summ > k:
                summ = summ - (nums[l] % 2)

                l += 1

            cnt = cnt + (r - l + 1)
            r += 1

        return cnt

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.helper(nums, k) - self.helper(nums, k - 1)