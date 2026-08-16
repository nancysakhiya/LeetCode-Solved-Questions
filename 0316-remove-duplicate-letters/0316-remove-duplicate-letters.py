class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        st = []
        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in s:
            count[ch] -= 1

            if ch in st:
                continue

            while st and st[-1] > ch and count[st[-1]] > 0:
                st.pop()

            st.append(ch)

        return "".join(st)