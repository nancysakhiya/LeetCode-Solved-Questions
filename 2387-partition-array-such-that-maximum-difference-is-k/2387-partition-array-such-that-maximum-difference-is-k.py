class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        rec = nums[0]
        ans = 1

        for n in nums:
            if n - rec > k:
                ans += 1
                rec = n
        return ans