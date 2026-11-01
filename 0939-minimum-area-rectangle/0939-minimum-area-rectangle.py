class Solution:
    def minAreaRect(self, points: list[list[int]]) -> int:
        pointset = set()

        for x, y in points:
            pointset.add((x, y))

        minarea = float('inf')

        n = len(points)

        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 != x2 and y1 != y2:
                    if (x1, y2) in pointset and (x2, y1) in pointset:
                        area = abs(x2 - x1) * abs(y2 - y1)
                        minarea = min(minarea, area)

        if minarea == float('inf'):
            return 0

        return minarea

