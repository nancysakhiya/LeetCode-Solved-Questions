class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        curr = 0
        for num in gain:
            curr += num
            alt = max(alt, curr)

        return alt 

            