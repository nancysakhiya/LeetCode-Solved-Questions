import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)

        i = 0
        j = 0

        heap = []

        for i in range(min(n, k)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        ans = []

        while heap and len(ans) < k:
            summ, i, j = heapq.heappop(heap)

            ans.append([nums1[i], nums2[j]])

            if j + 1 < m:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return ans



        