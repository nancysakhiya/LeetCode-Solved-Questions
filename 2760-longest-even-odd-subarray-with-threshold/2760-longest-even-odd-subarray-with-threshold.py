class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        maxlen = 0
        l = 0
        r = 0

        while r < n:
            if nums[r] % 2 == 0 and nums[r] <= threshold:
                l = r
                r += 1
                while r < n and nums[r] <= threshold and nums[r] % 2 != nums[r - 1] % 2:
                    r += 1
                maxlen = max(maxlen, r - l)

            else:
                r += 1

        return maxlen

