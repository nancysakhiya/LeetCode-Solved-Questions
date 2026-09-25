class Solution:
    def countPairs(self, arr: list[int]) -> int:
        # partner = power_of_2 - current_number
        mod = 1000000007
        n = len(arr)
        mpp = {}
        cnt = 0

        for num in arr:
            power = 1

            for i in range(22):
                if power - num in mpp:
                    cnt += mpp[power - num]
                    cnt = cnt % mod

                power *= 2

            mpp[num] = mpp.get(num, 0) + 1

        return cnt