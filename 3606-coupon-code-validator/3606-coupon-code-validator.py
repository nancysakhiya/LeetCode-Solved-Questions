class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        groups = [[] for _ in range(4)]
        ans = []
        businessMap = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }
        for i in range(len(code)):
            if code[i] and self.check(code[i], isActive[i]):
                biz_line = businessLine[i]
                if biz_line in businessMap:
                    grpidx = businessMap[biz_line]
                    groups[grpidx].append(code[i])

        for group in groups:
            group.sort()
            ans.extend(group)
        return ans
        
    def check(self, code: str, isActive: bool) -> bool:
        if not code:
            return False
        for char in code:
            if char != '_' and not char.isalnum():
                return False
        return isActive