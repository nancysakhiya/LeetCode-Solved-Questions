class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        replace_max = ''
        for c in s:
            if c != '9':
                replace_max = c
                break
        max_str = ''.join(['9' if c == replace_max else c for c in s])

        replace_min = s[0]
        min_str = ''.join(['0' if c == replace_min else c for c in s])

        return int(max_str) - int(min_str)