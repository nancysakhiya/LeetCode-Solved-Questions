class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # instead of increamenting n - 1 element, we can decrease 1 element
        # we need to decrease everything to the minimal. 
        # nums = [1,2,3], here minimum element is 1. so steps to reduce 1 is 0, steps to reduce 2 is 1, steps to reduce 3 is 2. so total steps 0 + 1 + 2 = 3
        n = len(nums)
        
        mini = min(nums)
        total = sum(nums)

        return total - n * mini


        