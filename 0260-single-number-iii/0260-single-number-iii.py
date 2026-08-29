class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mpp = {}
        ans = []

        for num in nums:
            mpp[num] = mpp.get(num, 0) + 1

        for key, val in mpp.items():
            if val == 1:
                ans.append(key)

        return ans

        