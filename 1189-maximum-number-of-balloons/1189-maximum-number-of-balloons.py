from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = float('inf')

        textCount = Counter(text)
        ballon = Counter('balloon')

        for ch in ballon:
            count = min(count, textCount[ch] // ballon[ch])

        return count






        