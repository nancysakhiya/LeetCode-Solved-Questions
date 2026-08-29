class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0

        for i in range(n):
            xor = xor ^ nums[i]

        return xor
