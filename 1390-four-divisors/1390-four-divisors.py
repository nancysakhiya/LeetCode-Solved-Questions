import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        totalsum = 0
        for num in nums:
            divisorcount = 0
            divisorsum = 0

            for i in range(1, math.isqrt(num) + 1):
                if num % i == 0:
                    divisorcount = divisorcount + 1
                    divisorsum = divisorsum + i

                    if i != (num // i):
                        divisorcount = divisorcount + 1
                        divisorsum = divisorsum + (num // i)

                if divisorcount > 4:
                    break

            if divisorcount == 4:
                totalsum = totalsum + divisorsum
        return totalsum
            
