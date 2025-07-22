class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        l = 0
        maxSum = 0
        currSum = 0

        for r in range(len(nums)):
            while nums[r] in seen:
                currSum -= nums[l]
                seen.remove(nums[l])
                l += 1
            currSum += nums[r]
            seen.add(nums[r])
            maxSum = max(maxSum, currSum)

        return maxSum