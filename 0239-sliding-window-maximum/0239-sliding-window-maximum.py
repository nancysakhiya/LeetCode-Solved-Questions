from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        # first window
        for i in range(k):
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)

        for i in range(k, len(nums)):
            res.append(nums[dq[0]])

            # remove elements that are not part of current window

            while dq and dq[0] <= i - k:
                dq.popleft()

            # remove smaller values
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)

        res.append(nums[dq[0]])

        return res
