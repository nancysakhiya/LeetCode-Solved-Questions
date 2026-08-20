class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        # for better solution we will store values in hash set and  we will run 2 loops
        n = len(arr)
        st = set()

        for i in range(n):
            hashset = set()
            for j in range(i+1, n):
                third = -(arr[i] + arr[j])
                if third in hashset:
                    temp = [arr[i], arr[j], third]
                    temp.sort()
                    st.add(tuple(temp))
                hashset.add(arr[j])       

        ans = list(st)
        return ans