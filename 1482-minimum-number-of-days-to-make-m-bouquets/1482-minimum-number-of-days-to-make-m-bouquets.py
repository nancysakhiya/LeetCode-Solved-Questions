class Solution:
    def isPossible(self, bloomDay: List[int], days: int, m: int, k: int) -> int:
        cnt = 0
        nob = 0

        for i in range(len(bloomDay)):
            if bloomDay[i] <= days:
                cnt += 1
            else:
                nob += (cnt // k)
                cnt = 0

        nob += (cnt//k)
        if nob >= m:
            return True
        return False


    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l = min(bloomDay)
        h = max(bloomDay)
        ans = -1

        while l <= h:
            mid = l + (h - l) // 2

            if self.isPossible(bloomDay, mid, m, k):
                ans = mid
                h = mid - 1
            else:
                l = mid + 1

        return ans

        