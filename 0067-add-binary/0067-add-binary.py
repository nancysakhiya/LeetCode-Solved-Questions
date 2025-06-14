class Solution:
    def addBinary(self, a: str, b: str) -> str:
        dec1 = int(a, 2)
        dec2 = int(b, 2)

        sum = dec1 + dec2

        return bin(sum)[2:]