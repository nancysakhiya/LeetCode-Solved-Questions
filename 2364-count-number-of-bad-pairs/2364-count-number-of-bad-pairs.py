class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0

        # good pair is, j - i == nums[j] - nums[i]
        # which is also equal to j - nums[i] == i - nums[i] 
        # two pair is good pair if they have same i - nums[i], we store it in hashmap
        # bad pair = total pair - good pair

        total = n * (n - 1) // 2

        mpp = {}
        good = 0

        for i in range(n):
            val = i - nums[i]

            if val in mpp:
                good += mpp[val]

            mpp[val] = mpp.get(val, 0) + 1

        return total - good
