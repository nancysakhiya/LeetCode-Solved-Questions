class Solution:
    def maxSum(self, nums: List[int]) -> int:
        positiveNumSet = set([num for num in nums if num > 0])
        return max(nums) if len(positiveNumSet) == 0 else sum(positiveNumSet)