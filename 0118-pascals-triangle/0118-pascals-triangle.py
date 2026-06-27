class Solution:
    def generateRows(self, row):
        ans = 1
        ansrow = []

        ansrow.append(1)

        for col in range(1, row):
            ans = ans * (row - col)
            ans = ans // col
            ansrow.append(ans)

        return ansrow

    def generate(self, numRows: int) -> List[List[int]]:
        ans = []

        for i in range(1, numRows + 1):
            temp = self.generateRows(i)
            ans.append(temp)

        return ans
        