# classic two heap problem, we maintain 2 heap. maxheap for left half of the number
# minheap, for right half of the number
import heapq
class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []     

    def addNum(self, num: int) -> None:
        # put number in left maxheap
        heapq.heappush(self.left, -num)

        # we want all the element in left to be smaller than all the element in right
        if self.right and -self.left[0] > self.right[0]:
            x = -heapq.heappop(self.left)
            y = heapq.heappop(self.right)

            heapq.heappush(self.left, -y)
            heapq.heappush(self.right, x)

        # we will maintain the heap size
        if len(self.left) > len(self.right) + 1:
            x = -heapq.heappop(self.left)
            heapq.heappush(self.right, x)

        elif len(self.right) > len(self.left) + 1:
            y = heapq.heappo(self.right)
            heapq.heappush(self.left, -y)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]

        return (-self.left[0] + self.right[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()