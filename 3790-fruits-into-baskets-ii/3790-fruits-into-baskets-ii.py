class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = 0
        for fruit in fruits:
            unset = 1
            for i in range(len(baskets)):
                if fruit <= baskets[i]:
                    baskets[i] = 0
                    unset = 0
                    break

            count += unset
        return count