import math
class Solution:
    def isPossible(self, nums: List[int], divisor: int, threshold: int) -> int:
        sumdiv = 0

        for i in range(len(nums)):
            sumdiv += math.ceil(nums[i] / divisor)

        if sumdiv <= threshold:
            return True
        return False

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        h = max(nums)
        ans = -1

        while l <= h:
            mid = l + (h - l) // 2

            if self.isPossible(nums, mid, threshold):
                ans = mid
                h = mid - 1
            else:
                l = mid + 1

        return ans

        