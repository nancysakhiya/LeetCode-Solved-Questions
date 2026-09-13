class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # if we have 1 in img1 at the potision (row1, col1) and the one in img2 is at (row2, col2) then the overlap or new position or position shift of the img1 1 is (row2 - row1, col2 - col1)
        n = len(img1)

        one1 = []
        one2 = []

        # we store all the index of 1's from both img
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    one1.append((i, j))

                if img2[i][j] == 1:
                    one2.append((i, j))

        mpp = {}
        ans = 0

        # now we try every pair of 1
        for r1, c1 in one1:
            for r2, c2 in one2:
                dr = r2 - r1
                dc = c2 - c1

                mpp[(dr, dc)] = mpp.get((dr, dc), 0) + 1

                ans = max(ans, mpp[(dr, dc)])

        return ans

