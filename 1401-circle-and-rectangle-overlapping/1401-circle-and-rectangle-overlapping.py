class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # we find the point inside the rectangle that is closest to the center of the circle
        # then we compare the distance
        closestX = max(x1, min(xCenter, x2))
        closestY =  max(y1, min(yCenter, y2))

        dx = closestX - xCenter
        dy = closestY - yCenter

        dist = dx * dx + dy * dy

        # if squared distance dist is <= radius ** 2, then they overlap
        return dist <= radius * radius
        