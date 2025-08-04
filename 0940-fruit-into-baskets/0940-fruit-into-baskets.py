class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        max_len = 0
        count = defaultdict(int)

        for end in range(len(fruits)):
            count[fruits[end]] += 1

            while len(count) > 2:
                count[fruits[start]] -= 1

                if count[fruits[start]] == 0:
                    del count[fruits[start]]
                start += 1

            max_len = max(max_len, end - start + 1)

        return max_len
