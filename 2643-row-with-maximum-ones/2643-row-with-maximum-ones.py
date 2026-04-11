class Solution:
    
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        cntmax = 0
        idx = -1

        for i in range(len(mat)):
            cntones = sum(mat[i])

            if cntones > cntmax or (cntones == cntmax and idx == -1):
                cntmax = cntones
                idx = i

        return [idx, cntmax]

        