class Solution:
    def findDisappearedNumbers(self, arr: List[int]) -> List[int]:
        n = len(arr)
        
        presentnum = set(arr)

        ans = []

        for i in range(1, n + 1):
            if i not in presentnum:
                ans.append(i)

        return ans