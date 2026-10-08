class Solution:
    def maxSum(self, nums: List[int]) -> int:
        mpp = {}
        ans = -1

        for num in nums:
            digit = [int(d) for d in str(num)]
            maxdigit = max(digit)

            if maxdigit in mpp:
                ans = max(ans, num + mpp[maxdigit])

            mpp[maxdigit] = max(mpp.get(maxdigit, 0), num)

        return ans

        