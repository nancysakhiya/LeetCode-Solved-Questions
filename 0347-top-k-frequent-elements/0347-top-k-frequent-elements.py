class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mpp = {}
        for num in nums:
            mpp[num] = mpp.get(num, 0) + 1

        heap = []
        for num, freq in mpp.items():
            heapq.heappush(heap, (-freq, num))

        ans = []
        for i in range(k):
            freq, num = heapq.heappop(heap)
            ans.append(num)

        return ans