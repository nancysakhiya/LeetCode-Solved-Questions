class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # we used bit manipulation to find subsets
        n = len(nums)
        subset = 1 << n # this is basically 2^n. because we are iterating from 0 to subset
        ans = []

        for i in range(subset):
            lis = []

            for j in range(n):
                if i & (1 << j):
                    lis.append(nums[j])

            ans.append(lis.copy())

        return ans