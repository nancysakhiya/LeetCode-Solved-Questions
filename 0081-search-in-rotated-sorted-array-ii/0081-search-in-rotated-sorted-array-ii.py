class Solution:
    def search(self, arr: List[int], k: int) -> bool:
        l = 0
        r = len(arr) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if arr[mid] == k:
                return True
                
            if arr[l] == arr[mid] == arr[r]:
                l += 1
                r -= 1
            
            elif arr[l] <= arr[mid]:
                if arr[l] <= k < arr[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
                    
            else:
                if arr[mid] < k <= arr[r]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
        return False
                    
        