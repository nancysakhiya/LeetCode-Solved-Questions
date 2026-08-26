class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)

        l = 0
        h = 0
        ones = 0

        res = ""

        while h < n:
            if s[h] == '1':
                ones += 1

            while ones == k:

                curr = s[l:h+1]

                if res == "" or len(curr) < len(res) or (len(curr) == len(res) and curr < res):
                    res = curr

                if s[l] == '1':
                    ones -= 1

                l += 1
            
            h += 1

        return res 

