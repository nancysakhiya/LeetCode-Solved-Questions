class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        n = len(num1)
        m = len(num2)

        res = [0] * (n + m)

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                a = ord(num1[i]) - ord('0')
                b = ord(num2[j]) - ord('0')

                prod = a * b

                # when we et product of a and b we will assign each number its position in res array
                pos1 = i + j 
                pos2 = i + j + 1

                total = prod + res[pos2]

                res[pos2] = total % 10
                res[pos1] += total // 10

        # we have to remove leading zeros
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1

        return ''.join(map(str, res[start:]))
