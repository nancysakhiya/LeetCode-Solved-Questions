class Solution:
    def maximizeGreatness(self, nums: list[int]) -> int:
        nums.sort()

        # we use two pointers, one pointer for original array and another for tracking the max num
        n = len(nums)
        i = 0
        j = 0
        pairs = 0

        while j < n:
            if nums[j] > nums[i]:
                pairs += 1
                i += 1
                
            j += 1

        return pairs

            