class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        mpp = {}

        for i in range(n):
            a = nums[i]
            b = target - a

            if b in mpp:
                return (mpp[b], i)

            mpp[a] = i

        return []