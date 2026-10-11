class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mpp = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in mpp:
                if not st or st[-1] != mpp[ch]:
                    return False

                st.pop()

            else:
                st.append(ch)

        return len(st) == 0

        