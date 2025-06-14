class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        ranks = {sorted_score[i]: str(i + 1) for i in range(len(score))}

        ranks[sorted_score[0]] = "Gold Medal"

        if len(score) > 1:
            ranks[sorted_score[1]] = "Silver Medal"

        if len(score) > 2:
            ranks[sorted_score[2]] = "Bronze Medal"

        return [ranks[s] for s in score]
