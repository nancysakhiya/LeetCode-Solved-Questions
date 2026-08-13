class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        n = len(nums)
        mpp = {}

        for num in nums:
            mpp[num] = mpp.get(num, 0) + 1

        max_freq = max(mpp.values())
        cnt = 0
        for freq in mpp.values():
            if freq == max_freq:
                cnt += freq

        return cnt
