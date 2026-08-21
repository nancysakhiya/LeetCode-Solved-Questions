class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        ans = []

        for i in range(n):
            start = arr[i][0]
            end = arr[i][1]

            if ans and end <= ans[-1][1]:
                continue

            for j in range(i + 1, n):
                if arr[j][0] <= end:
                    end = max(end, arr[j][1])
                else:
                    break

            ans.append([start, end])

        return ans