class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1)

        res = []
        for n in nums2:
            if count[n] > 0:
                res.append(n)
                count[n] -= 1
        return res