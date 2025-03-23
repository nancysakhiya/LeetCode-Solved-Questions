class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2

        merged.sort()

        if len(merged) % 2 == 1:
            return float(merged[len(merged)//2])

        else:
            mid1 = merged[len(merged) // 2 - 1]
            mid2 = merged[len(merged) // 2]
            return (float(mid1) + float(mid2)) / 2.0