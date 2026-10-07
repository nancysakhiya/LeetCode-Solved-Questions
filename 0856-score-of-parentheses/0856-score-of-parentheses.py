class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = [0]

        for par in s:
            if par == '(':
                st.append(0)

            else:
                val = st.pop()
                if val == 0:
                    val = 1
                else:
                    val = 2 * val

                st[-1] += val

        return st[0]