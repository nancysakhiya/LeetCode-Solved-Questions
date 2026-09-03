class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        n = len(nums)

        minodd = float('inf')

        for i in range(n):
            if nums[i] % 2 != 0:
                minodd = min(minodd, nums[i])

        if minodd == float('inf'):
            return True

        for i in range(n):
            if nums[i] % 2 == 0:
                if nums[i] <= minodd:
                    return False

        return True