class Solution:
    def getMaxArea(self, arr):
        # code here
        st = []
        maxarea = 0
        
        for i in range(len(arr)):
            
            while len(st) != 0 and arr[st[-1]] > arr[i]:
                ele = st[-1]
                st.pop()
                nse = i
                pse = -1 if len(st) == 0 else st[-1]
                
                maxarea = max(maxarea, arr[ele] * (nse - pse - 1))
                
            st.append(i)
                
        while len(st) != 0:
            nse = len(arr)
                
            ele = st[-1]
                
            st.pop()
                
            pse = -1 if len(st) == 0 else st[-1]
                
            maxarea = max(maxarea, arr[ele] * (nse - pse - 1))
                
                
        return maxarea

    def maximalRectangle(self, mat: List[List[str]]) -> int:
        n = len(mat)
        m = len(mat[0])
        maxArea = 0
        prefixsum = [[0 for _ in range(m)] for _ in range(n)]
        
        for j in range(m):
            summ = 0
            for i in range(n):
                summ += int(mat[i][j])
                
                if mat[i][j] == '0':
                    summ = 0
                    
                prefixsum[i][j] = summ
        
        for i in range(n):
            maxArea = max(maxArea, self.getMaxArea(prefixsum[i]))
            
        return maxArea