class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0 
        while len(nums) > 1:
            isAscending = True
            minSum = float("inf")
            targetIdx = -1

            for i in range(len(nums) - 1):
                pairSum = nums[i] + nums[i + 1]

                if nums[i] > nums[i + 1]:
                    isAscending = False
                
                if pairSum < minSum:
                    minSum = pairSum
                    targetIdx = i

            if isAscending:
                break

            count += 1
            nums[targetIdx] = minSum
            nums.pop(targetIdx + 1)

        return count