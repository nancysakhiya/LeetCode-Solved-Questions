class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nge = []
        st = []

        for i in range(2 * n - 1, -1, -1):
            while len(st) != 0 and st[-1] <= nums[i % n]:
                st.pop()

            if i < n:
                if len(st) == 0:
                    nge.append(-1)
                else:
                    nge.append(st[-1])

            st.append(nums[i % n])


        nge.reverse()

        return nge
        