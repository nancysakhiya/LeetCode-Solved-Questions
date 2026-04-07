class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if mid == 0 and nums[0] != nums[1]:
                return nums[mid]

            if mid == len(nums) - 1 and nums[len(nums) - 1] != nums[len(nums) - 2]:
                return nums[len(nums) - 1]
        

            if nums[mid - 1] != nums[mid] and nums[mid] != nums[mid + 1]:
                return nums[mid]

            if mid % 2 == 0:
                if nums[mid - 1] == nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                
                if nums[mid - 1] == nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1


            

        return -1
            