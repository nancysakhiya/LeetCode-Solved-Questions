class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def count_digit(x):
            return "".join(sorted(str(x)))

        target = count_digit(n)

        for i in range(31):
            if count_digit(1 << i) == target:
                return True
        return False