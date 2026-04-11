class Solution:
    def isPossible(self, arr: List[int], capacity: int, d: int) -> int:
        weights = 0
        nod = 1

        for i in range(len(arr)):
            if (weights + arr[i]) > capacity:
                nod += 1
                weights = arr[i]
            else:
                weights += arr[i]

        if nod <= d:
            return True
        return False

    def shipWithinDays(self, arr: List[int], days: int) -> int:
        l = max(arr)
        h = sum(arr)
        ans = -1

        while l <= h:
            mid = l + (h-l) // 2

            if self.isPossible(arr, mid, days):
                ans = mid
                h = mid - 1
            else:
                l = mid + 1

        return ans
        