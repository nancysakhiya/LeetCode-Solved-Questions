class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        for num in nums:
            idx = abs(num) - 1

            if nums[idx] < 0:
                ans.append(abs(num))
            else:
                nums[idx] = -nums[idx]

        return ans