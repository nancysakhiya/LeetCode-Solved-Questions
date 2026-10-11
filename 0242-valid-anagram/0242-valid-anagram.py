class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mpp = {}
        for ch in s:
            mpp[ch] = mpp.get(ch, 0) + 1

        for ch in t:
            if ch not in mpp or mpp[ch] == 0:
                return False

            mpp[ch] -= 1

        return True