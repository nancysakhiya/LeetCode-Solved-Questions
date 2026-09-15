class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        a1, b1, a2, b2 = rec2

        # they will not overlap if one rectangle A is completly right to B or A is completly left to B
        if x2 <= a1:
            return False
        if a2 <= x1:
            return False

        # if A is compltly below B or completly above B
        if y2 <= b1:
            return False
        if b2 <= y1:
            return False

        return True