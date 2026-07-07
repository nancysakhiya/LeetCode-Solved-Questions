class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        arr.sort(key = lambda i : i[0])
        n = len(arr)
        ans = []

        for i in range(n):
            if not ans or arr[i][0] > ans[-1][1]:
                ans.append(arr[i])
            else:
                ans[-1][1] = max(ans[-1][1], arr[i][1])

        return ans
        