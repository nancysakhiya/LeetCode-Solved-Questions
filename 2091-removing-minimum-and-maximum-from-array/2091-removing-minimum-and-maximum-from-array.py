class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        mini = float('inf')
        maxi = float('-inf')

        minidx = 0
        maxidx = 0
        cnt = 0

        for i in range(n):
            if nums[i] < mini:
                mini = nums[i]
                minidx = i

            if nums[i] > maxi:
                maxi = nums[i]
                maxidx = i

        # we will create a kind of range that has start and end
        start = min(minidx, maxidx)
        end = max(minidx, maxidx)

        # remove both from the front
        front = end + 1

        # remove both from the back
        back = n - start

        # remove one from front and one from back
        both = (start + 1) + (n - end)

        return min(front, back, both)

        