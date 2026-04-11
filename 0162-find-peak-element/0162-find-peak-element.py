class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0

        if arr[0] > arr[1]:
            return 0
        if arr[n - 1] > arr[n - 2]:
            return n - 1

        l = 1
        h = n - 2

        while l <= h:
            mid = l + (h - l) // 2

            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                return mid

            elif arr[mid] > arr[mid - 1]:
                l = mid + 1

            elif arr[mid] > arr[mid + 1]:
                h = mid - 1
            else:
                l = mid + 1

        return -1        