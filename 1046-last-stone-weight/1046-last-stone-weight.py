import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone) # maxheap in python

        while len(heap) > 1:
            # first we get largest element
            # then we get second largest element
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)

            if x != y:
                heapq.heappush(heap, -(y - x))

        if heap:
            return -heap[0]

        return 0