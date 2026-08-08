class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        leftproduct = 1
        for i in range(n):
            res[i] = leftproduct
            leftproduct *= nums[i]

        rightproduct = 1
        for i in range(n - 1, -1, -1):
            res[i] *= rightproduct
            rightproduct *= nums[i]
            
        return res
            
