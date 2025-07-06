class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.cnt = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        nums2, cnt = self.nums2, self.cnt

        cnt[nums2[index]] -= 1
        nums2[index] += val
        cnt[nums2[index]] += 1

    def count(self, tot: int) -> int:
        nums1, cnt = self.nums1, self.cnt

        ans = 0
        for num in nums1:
            if (rest := tot - num) in cnt:
                ans += cnt[rest]
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)