class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        n = len(ages)
        mpp = {}
        for age in ages:
            mpp[age] = mpp.get(age, 0) + 1

        cnt = 0

        for i in range(1, 121):
            for j in range(1, 121):
                
                if j <= 0.5 * i + 7 or j > i or (j > 100 and i < 100):
                    continue
                cnt += mpp.get(i, 0) * mpp.get(j, 0)

                if i == j:
                    cnt -= mpp.get(i, 0)

        return cnt
