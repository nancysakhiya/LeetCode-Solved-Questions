class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        highPriorityPair = "ab" if x > y else "ba"
        lowPriorityPair = "ba" if highPriorityPair == "ab" else "ab"

        strAtrFstPass = self.removeSubstring(s, highPriorityPair)
        count = (len(s) - len(strAtrFstPass)) // 2

        res += count * max(x, y)

        strAtrSecPass = self.removeSubstring(strAtrFstPass, lowPriorityPair)
        count = (len(strAtrFstPass) - len(strAtrSecPass)) // 2

        res += count * min(x, y)

        return res

    def removeSubstring(self, input: str, target_pair: str) -> str:
        char_stack = []

        # Iterate through each character in the input string
        for current_char in input:
            # Check if current character forms the target pair with the top of the stack
            if (
                current_char == target_pair[1]
                and char_stack
                and char_stack[-1] == target_pair[0]
            ):
                char_stack.pop()  # Remove the matching character from the stack
            else:
                char_stack.append(current_char)

        # Reconstruct the remaining string after removing target pairs
        return "".join(char_stack)