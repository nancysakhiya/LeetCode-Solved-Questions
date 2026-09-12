import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mpp = {}
        for word in words:
            mpp[word] = mpp.get(word, 0) + 1

        heap = []
        for word, freq in mpp.items():
            heapq.heappush(heap, (-freq, word))

        ans = []
        for i in range(k):
            freq, word = heapq.heappop(heap)
            ans.append(word)

        return ans