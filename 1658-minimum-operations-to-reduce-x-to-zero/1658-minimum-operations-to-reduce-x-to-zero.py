class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        # instead of thinking which element should i remove, we will think which element i should keep?
        # nums = [1, 1, 4, 2, 3]
        # x = 5
        # total sum of arr = 11
        # we want to remove 5 from 11, so we kepp 11 - 5 = 6
        # we keep a longest contigues sub array whose sum is 6
        n = len(nums)
        l = 0
        r = 0
        currsum = 0
        target = sum(nums) - x
        maxlen = -1

        if target == 0:
            return n

        for r in range(n):
            currsum += nums[r]

            # we shrik the window if curesum is too large
            while l <= r and currsum > target:
                currsum -= nums[l]
                l += 1

            if currsum == target:
                maxlen = max(maxlen, r - l + 1)

        if maxlen == -1:
            return -1

        return n - maxlen
