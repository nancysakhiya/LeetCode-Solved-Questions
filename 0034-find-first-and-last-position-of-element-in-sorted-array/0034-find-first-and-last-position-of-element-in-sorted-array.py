class Solution:
    def lowerbound(self, arr: List[int], k: int) -> List[int]:
        l = 0
        h = len(arr) - 1
        ans = len(arr)
        
        while l <= h:
            mid = l + (h-l) // 2
            
            if arr[mid] >= k:
                ans = mid
                h = mid - 1
                
            else:
                l = mid + 1
                
        return ans
        
    def upperbound(self, arr: List[int], k: int) -> List[int]:
        l = 0
        h = len(arr) - 1
        ans = len(arr)
        
        while l <= h:
            mid = l + (h-l) // 2
            
            if arr[mid] > k:
                ans = mid
                h = mid - 1
                
            else:
                l = mid + 1
                
        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if self.lowerbound(nums, target) == len(nums) or nums[self.lowerbound(nums, target)] != target:
            return [-1, -1]

        return [self.lowerbound(nums, target), self.upperbound(nums, target) - 1]
        