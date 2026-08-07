class Solution:

    def nthUglyNumber(self, n: int) -> int:
        ugly = set()

        ugly.add(1)
        curr = 1

        for i in range(n):
            curr = min(ugly)

            ugly.remove(curr)

            ugly.add(curr * 2)
            ugly.add(curr * 3)
            ugly.add(curr * 5)

        return curr
        



        