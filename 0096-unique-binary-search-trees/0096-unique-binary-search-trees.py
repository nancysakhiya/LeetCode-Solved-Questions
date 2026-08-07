class Solution:
    def helper(self, node, mpp):
        if node <= 1:
            return 1

        if node in mpp:
            return mpp[node]

        cnt = 0

        for i in range(1, node + 1):
            leftsub = self.helper(i - 1, mpp)
            rightsub = self.helper(node - i, mpp)

            cnt += leftsub * rightsub

        mpp[node] = cnt

        return cnt

    def numTrees(self, n: int) -> int:
        mpp = {}

        return self.helper(n, mpp)