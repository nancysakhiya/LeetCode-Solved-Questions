class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        st = set()
        ans = []
        
        for i in range(n):
            mpp = set()
            for j in range(i+1, n):
                third = -(arr[i] + arr[j])
                if third in mpp:
                    temp = [arr[i], arr[j], third]
                    temp.sort()
                    st.add(tuple(temp))
                mpp.add(arr[j])

        ans = [list(t) for t in st]
        
        return ans
        