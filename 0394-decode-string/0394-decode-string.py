class Solution:
    def decodeString(self, s: str) -> str:
        num_st = []
        str_st = []

        num = 0
        char = ""

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == '[':
                num_st.append(num)
                str_st.append(char)

                num = 0
                char = ""

            elif ch == ']':
                repeat = num_st.pop()
                prev = str_st.pop()

                char = prev + char * repeat

            else:
                char += ch

        return char
