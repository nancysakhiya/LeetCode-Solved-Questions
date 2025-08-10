class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        memo = {}
        cut = [0] + sorted(cuts) + [n]

        def cost(l, r):
            if (l, r) in memo:
                return memo[(l, r)]
            if r - l == 1:
                return 0
            ans = min(cost(l, mid) + cost(mid, r) + cut[r] - cut[l] for mid in range(l+1, r))
            memo[(l, r)] = ans
            return ans

        return cost(0, len(cut) - 1)