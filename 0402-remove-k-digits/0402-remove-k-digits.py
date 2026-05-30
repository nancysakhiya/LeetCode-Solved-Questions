class Solution:
    def removeKdigits(self, s: str, k: int) -> str:
        st = []
        
        for i in range(len(s)):
            
            while len(st) != 0 and k > 0 and (int(st[-1]) > int(s[i])):
                st.pop()
                k -= 1
                
            st.append(s[i])
            
        while k > 0:
            st.pop()
            k -= 1
            
        if len(st) == 0:
            return "0"
            
        res = ""
        
        while len(st) != 0:
            res = res + st[-1]
            st.pop()
            
        while len(res) != 0 and res[-1] == "0":
            res = res[:-1]
            
        res = res[::-1]
        
        if len(res) == 0:
            return "0"
            
        return res
        
        