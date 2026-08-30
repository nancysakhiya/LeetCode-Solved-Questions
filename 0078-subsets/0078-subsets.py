class Solution:
    def recursion(self, idx, ls, ans, arr):
        n = len(arr)
        if idx >= n:
            ans.append(ls.copy())
            return ls

        ls.append(arr[idx])
        self.recursion(idx + 1, ls, ans, arr) # take
        ls.pop()
        self.recursion(idx + 1, ls, ans, arr) # not take

    def subsets(self, nums: List[int]) -> List[List[int]]:
        # we used bit manipulation to find subsets
        ls = []
        ans = []

        self.recursion(0, ls, ans, nums)

        return ans
        