class Solution:
    def check(self, nums: List[int]) -> bool:
        arr = nums * 2

        length = 1

        if len(nums) == 1:
            return True

        for i in range(1, len(arr)):
            if arr[i - 1] <= arr[i]:
                length += 1

            else:
                length = 1

            if length == len(nums):
                return True

        return False


        

        