class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            digit = [int(i) for i in str(nums[i])]

            if sum(digit) == i:
                return i

        return -1