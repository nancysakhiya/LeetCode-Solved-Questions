import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        heap = []

        for i in range(n):
            heapq.heappush(heap, -stones[i])

        while len(heap) > 1:
            num2 = -heapq.heappop(heap) # largest element
            num1 = -heapq.heappop(heap) # second largest element from the heap
            

            if num1 != num2:
                heapq.heappush(heap, -(num2 - num1)) # because x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x

        if heap:
            return -heap[0]

        return 0


        