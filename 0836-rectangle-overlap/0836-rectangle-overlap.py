class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        a1, b1, a2, b2 = rec2

        # overlap on x-axis
        x_overlap = min(x2, a2) > max(x1, a1)

        # overlap on y-axis
        y_overlap = min(y2, b2) > max(y1, b1)

        return x_overlap and y_overlap