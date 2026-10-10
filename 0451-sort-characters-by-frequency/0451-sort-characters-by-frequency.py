class Solution:
    def frequencySort(self, s: str) -> str:
        n = len(s)

        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        chars = sorted(freq.keys(), key=lambda x: -freq[x])

        res = []
        for ch in chars:
            res.append(ch * freq[ch])

        return ''.join(res)


        