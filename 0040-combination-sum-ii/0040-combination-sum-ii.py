class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtracking(target, start, comb):
            if target < 0:
                return

            if target == 0:
                res.append(comb)
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                backtracking(target - candidates[i], i + 1, comb + [candidates[i]])

        backtracking(target, 0, [])
        return res