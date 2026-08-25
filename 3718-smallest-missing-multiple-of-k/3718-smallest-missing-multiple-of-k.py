class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        st = set(nums)

        multiple = k

        while multiple in st:
            multiple += k

        return multiple