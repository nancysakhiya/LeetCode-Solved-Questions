class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 0 and n == 1:
            return 1
        count = [0] * (n+1)
        for p in trust:
            count[p[0]] -= 1
            count[p[1]] += 1

        for pp in range(len(count)):
            if count[pp] == n-1: return pp
        return -1
