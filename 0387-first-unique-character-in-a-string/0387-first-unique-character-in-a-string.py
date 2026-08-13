class Solution:
    def firstUniqChar(self, s: str) -> int:
        mpp = {}

        for ch in s:
            mpp[ch] = mpp.get(ch, 0) + 1

        for i, ch in enumerate(s):
            if mpp[ch] == 1:
                return i

        return -1

        
        

        