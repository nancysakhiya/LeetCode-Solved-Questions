class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mpp = {}
        mpp[0] = 1
        cnt = 0
        prefixsum = 0

        for i in range(len(nums)):
            prefixsum += nums[i]
            remove = prefixsum - k
            cnt = cnt + mpp.get(remove, 0)
            mpp[prefixsum] = mpp.get(prefixsum, 0) + 1

        return cnt
        