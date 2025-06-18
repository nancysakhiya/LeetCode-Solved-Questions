class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num = ( 1 << 32) + num

        h = '0123456789abcdef'
        hex_num = ''

        while num > 0:
            rem = num % 16
            hex_digit = h[rem]
            hex_num = hex_digit + hex_num
            num = num // 16
        return hex_num

