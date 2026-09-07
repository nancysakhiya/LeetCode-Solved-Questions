class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        small = min(nums)
        largest = max(nums)

        present = set(nums)
        res = []

        for i in range(small, largest + 1):
            if i not in present:
                res.append(i)

        return res


