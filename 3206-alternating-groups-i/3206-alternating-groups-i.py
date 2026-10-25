class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        ans = 0

        for i in range(n):
            l = (i - 1) % n
            r = (i + 1) % n

            if colors[l] != colors[i] and colors[i] != colors[r]:
                ans += 1

        return ans
