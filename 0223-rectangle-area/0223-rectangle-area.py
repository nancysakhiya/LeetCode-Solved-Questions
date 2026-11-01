class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        len1 = ay2 - ay1
        width1 = ax2 - ax1

        ar1 = len1 * width1 # area of rectangle 1

        len2 = by2 - by1
        width2 = bx2 - bx1

        ar2 = len2 * width2 # area of rectangle 2

        # overlapping area

        overalp_left = max(ax1, bx1)
        overalp_right = min(ax2, bx2)

        overalp_bottom = max(ay1, by1)
        overalp_top = min(ay2, by2)

        overlap_width = max(0, overalp_right - overalp_left)
        overlap_len = max(0, overalp_top - overalp_bottom)

        oar = overlap_width * overlap_len

        return ar1 + ar2 - oar




        