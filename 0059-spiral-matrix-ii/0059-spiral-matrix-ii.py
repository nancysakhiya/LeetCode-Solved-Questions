class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0 for _ in range(n)] for _ in range(n)]
        l = 0 # this left pointer will tell us which coloumn we are on
        r = n - 1 # right - coloumn
        t = 0 # this top pointer will tell us which row we are working on
        b = n - 1 # bottom - row
        val = 1

        while l <= r:
            # fill every value in top row
            for c in range(l, r + 1):
                mat[t][c] = val
                val += 1

            t += 1

            # fill every value in right coloumn
            for row in range(t, b+1):
                mat[row][r] = val
                val += 1

            r -= 1

            # fill every value in bottom row (reverse order)
            for c in range(r, l - 1, -1):
                mat[b][c] = val
                val += 1

            b -= 1

            # fill every value in left colomn (reverse order)
            for row in range(b, t - 1, -1):
                mat[row][l] = val
                val += 1

            l += 1

        return mat



