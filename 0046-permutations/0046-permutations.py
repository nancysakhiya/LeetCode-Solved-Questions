class Solution:
    def recursion(self, ds, mpp, ans, nums):
        if len(ds) == len(nums):
            ans.append(ds.copy())
            return

        for i in range(len(nums)):
            if not mpp[i]:
                mpp[i] = True
                ds.append(nums[i])
                self.recursion(ds, mpp, ans, nums)
                ds.pop(len(ds) - 1)

                mpp[i] = False

    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        ds = []
        mpp = [False] * n
        self.recursion(ds, mpp, ans, nums)
        return ans
        