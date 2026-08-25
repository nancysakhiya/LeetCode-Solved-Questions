from functools import cmp_to_key
class Solution:
    def compare(self, a, b):
        if a + b > b + a:
            return -1
        else:
            return 1

    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))

        nums.sort(key=cmp_to_key(self.compare))

        if nums[0] == '0':
            return '0'

        return ''.join(nums)

        