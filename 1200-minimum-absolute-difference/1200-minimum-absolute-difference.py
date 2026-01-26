class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        minDif = 2e6 + 1
        res = []

        for i in range(1, n):
            diff = arr[i] - arr[i - 1]
            if diff < minDif:
                minDif = diff
                res = [[arr[i - 1], arr[i]]]
            elif diff == minDif:
                res.append([arr[i-1], arr[i]])

        return res