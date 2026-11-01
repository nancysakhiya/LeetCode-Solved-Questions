class Solution:
    def helper(self, opencnt, closecnt, curr, n, res):
        if len(curr) == 2 * n:
            res.append(curr)
            return

        if opencnt < n:
            self.helper(opencnt + 1, closecnt, curr + '(', n, res)

        if closecnt < opencnt:
            self.helper(opencnt, closecnt + 1, curr + ')', n, res)


    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        self.helper(0, 0, "", n, res)

        return res

        