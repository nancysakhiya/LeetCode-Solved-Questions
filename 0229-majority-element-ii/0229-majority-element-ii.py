class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        eleCount = Counter(nums)
        majEle = []
        threshold = len(nums) // 3
        for ele, count in eleCount.items():
            if count > threshold:
                majEle.append(ele)

        return majEle
