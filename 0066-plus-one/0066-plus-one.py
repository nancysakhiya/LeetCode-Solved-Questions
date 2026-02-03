class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join(map(str, digits)))

        res = num + 1

        resf = [int(d) for d in str(res)]

        return resf