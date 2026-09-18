import heapq
class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        arr = []
        for num in nums:
            arr.append(int(num))

        n = len(arr)
        heap = []

        for i in range(n):
            heapq.heappush(heap, arr[i])

            if len(heap) > k:
                heapq.heappop(heap)

        return str(heap[0])
        