class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def makeCombinations(idx, comb, total):
            if total == target:
                res.append(comb[:])
                return

            if total > target or idx >= len(candidates):
                return

            comb.append(candidates[idx])
            makeCombinations(idx, comb, total + candidates[idx])
            comb.pop()
            makeCombinations(idx+1, comb, total)

            return res
        
        return makeCombinations(0, [], 0)