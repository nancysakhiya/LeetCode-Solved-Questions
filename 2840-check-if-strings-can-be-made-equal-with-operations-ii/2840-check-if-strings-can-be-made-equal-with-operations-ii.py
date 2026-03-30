class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        count1 = [0] * 256
        count2 = [0] * 256

        for i in range(len(s1)):
            offset = (i & 1) << 7

            count1[offset + ord(s1[i])] += 1
            count2[offset + ord(s2[i])] += 1

        return count1 == count2
