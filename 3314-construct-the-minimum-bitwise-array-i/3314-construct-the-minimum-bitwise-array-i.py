class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            org = num
            can = -1
            for j in range(1, org):
                if (j | (j + 1)) == org:
                    can = j
                    break
            res.append(can)
        return res