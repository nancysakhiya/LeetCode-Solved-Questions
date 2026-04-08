class Solution:
    def totalFruit(self, arr: List[int]) -> int:
        n = len(arr)
        l = 0
        r = 0
        maxlen = 0

        mpp = {}

        while r < n:
            mpp[arr[r]] = mpp.get(arr[r], 0) + 1

            if len(mpp) > 2:
                if len(mpp) > 2:
                    mpp[arr[l]] -= 1
                    if mpp[arr[l]] == 0:
                        del mpp[arr[l]]
                    l += 1

            if len(mpp) <= 2:
                maxlen = max(maxlen, r - l + 1)
            r += 1

        return maxlen