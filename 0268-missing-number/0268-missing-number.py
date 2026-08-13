class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        arr.sort()
        n = len(arr)
        
        for i in range(n):
            if arr[i] != i:
                return i
                
        return n