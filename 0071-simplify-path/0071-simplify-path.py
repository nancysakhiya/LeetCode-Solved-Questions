class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)
        parts = path.split('/')

        st = []

        for part in parts:
            if part == "" or part == ".":
                continue

            elif part == "..":
                if st:
                    st.pop()

            else:
                st.append(part)

        return '/' + '/'.join(st)





        