import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)

        heap = []

        for i in range(n - 1):
            if heights[i] >= heights[i + 1]:
                continue

            diff = heights[i + 1] - heights[i]

            heapq.heappush(heap, -diff)
            bricks -= diff

            if bricks < 0:
                if ladders > 0:
                    bricks += -heapq.heappop(heap)
                    ladders -= 1
                else:
                    return i

        return n - 1