class Solution:
    def insert(self, curr: List[List[int]], new: List[int]) -> List[List[int]]:
        res = []
        n = len(curr)

        for i in range(n):

            # case 1: where curr interval come before new interval
            if curr[i][1] < new[0]:
                res.append(curr[i])

            # case 2: where curr interval comes after new interval
            elif curr[i][0] > new[1]:
                res.append(new)
                new = curr[i]

            # case 3: where curr and new intervals overlap somewhere
            else:
                new[0] = min(new[0], curr[i][0])
                new[1] = max(new[1], curr[i][1])

        res.append(new)

        return res

