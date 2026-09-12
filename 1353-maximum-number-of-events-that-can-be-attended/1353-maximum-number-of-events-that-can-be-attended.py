import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        i = 0
        heap = []
        day = 0
        cnt = 0

        while i < n or heap:

            #if no event is currently present in the heap, we move to the next enent
            if not heap:
                day = events[i][0]

            # we add all events to heap, that starts same day
            while i < n and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1

            # we remove the events already done
            while heap and heap[0] < day:
                heapq.heappop(heap)

            if heap:
                heapq.heappop(heap)
                cnt += 1
                day += 1

        return cnt

        
        # we attend event that ends earliest
        return n