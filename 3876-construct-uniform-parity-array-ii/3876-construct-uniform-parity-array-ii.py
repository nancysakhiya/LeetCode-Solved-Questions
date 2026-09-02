class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        n = len(nums)

        minodd = float('inf')

        # we will find the smallest oddd number and we will count all the odd number
        for i in range(n):
            if nums[i] % 2 != 0:
                minodd = min(minodd, nums[i])
        
        # if there is no odd number everything is even, we can return
        if minodd == float('inf'):
            return True

        # Case 2: if only one number is odd
        for i in range(n):
            if nums[i] % 2 == 0:
                if nums[i] <= minodd:
                    return False

        return True
        