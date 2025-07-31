class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        curr = {0}
        for x in arr:
            curr = {x | y for y in curr} | {x}
            ans |= curr
        return len(ans)