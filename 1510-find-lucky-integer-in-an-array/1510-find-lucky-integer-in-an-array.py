class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        lucky = -1

        for num, count in freq.items():
            if num == count:
                lucky = max(lucky, num)
        return lucky