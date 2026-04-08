class Solution:
    def helper(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        r = 0
        mpp = {}
        cnt = 0

        while r < n:
            mpp[nums[r]] = mpp.get(nums[r], 0) + 1

            while len(mpp) > k:
                mpp[nums[l]] -= 1

                if mpp[nums[l]] == 0:
                    del mpp[nums[l]]

                l += 1

            cnt = cnt + (r - l + 1)
            r += 1

        return cnt

        

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.helper(nums, k) - self.helper(nums, k-1)


        