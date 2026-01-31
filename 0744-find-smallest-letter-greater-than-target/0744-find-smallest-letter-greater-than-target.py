class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        res = letters[0]
        flag = False

        for letter in letters:
            if not flag:
                if letter > target:
                    res = letter
                    flag = not flag

            else:
                if letter > target and letter < res:
                    res = letter

        return res