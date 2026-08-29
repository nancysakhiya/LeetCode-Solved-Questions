class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        # i need to sort the array while preserving the orginal index with that element
        n = len(nums)
        arr = [(nums[i], i) for i in range(n)]
        arr.sort()

        ans = nums[:]

        start = 0

        for end in range(1, n+1):
            #if we reach the end or found a new group
            if end == n or arr[end][0] - arr[end - 1][0] > limit:
                group = arr[start:end] #current group

                val = [x[0] for x in group]

                idx = sorted([x[1] for x in group])

                # now we put smallest val at smallest idx
                for k in range(len(group)):
                    ans[idx[k]] = val[k]

                start = end

        return ans



