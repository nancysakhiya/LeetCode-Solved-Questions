class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        n = len(nums)
        maxxor = 0

        for i in range(n):
            for j in range(n):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    xor = nums[i] ^ nums[j]
                    maxxor = max(maxxor, xor)

        return maxxor
        