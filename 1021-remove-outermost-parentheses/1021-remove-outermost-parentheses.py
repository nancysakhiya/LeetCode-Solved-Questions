class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        balance = 0
        res = []

        for par in s:
            if par == '(':
                if balance > 0:
                    res.append(par)
                balance += 1

            else:
                balance -= 1
                if balance > 0:
                    res.append(par)

        return ''.join(res)
                