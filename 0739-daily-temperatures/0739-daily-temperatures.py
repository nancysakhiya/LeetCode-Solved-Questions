class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force

        n = len(temperatures)
        ans = [0] * n
        st = []

        for i in range(n):
            while st and temperatures[i] > temperatures[st[-1]]:
                prev = st.pop()
                ans[prev] = i - prev

            st.append(i)

        return ans 