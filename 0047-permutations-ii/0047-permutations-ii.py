class Solution:
    def recursion(self, ds, mark, ans, nums):
        if len(ds) == len(nums):
            ans.append(ds.copy())
            return

        for i in range(len(nums)):
            if mark[i]:
                continue

            if i > 0 and nums[i] == nums[i - 1] and not mark[i - 1]:
                continue
                
            if not mark[i]:
                mark[i] = True
                ds.append(nums[i])
                self.recursion(ds, mark, ans, nums)
                ds.pop(len(ds) - 1)
                mark[i] = False

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ds = []
        ans = []
        mark = [False] * n

        self.recursion(ds, mark, ans, nums)

        return ans
        