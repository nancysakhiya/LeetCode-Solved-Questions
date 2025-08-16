class Solution:
    def maximum69Number (self, num: int) -> int:
        num_copy = num
        idx = -1
        curr = 0

        while num_copy > 0:
            if num_copy % 10 == 6:
                idx = curr
            
            num_copy //= 10
            curr += 1

        return num if idx == -1 else num + 3*10**idx
