from typing import List

class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False
        
    def insert(self, word: str):
        root = self
        for w in word:
            idx = ord(w) - ord('a')
            if root.children[idx] is None:
                root.children[idx] = Trie()
            root = root.children[idx]
        root.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self
        for w in word:
            idx = ord(w) - ord('a')
            if curr.children[idx] is None:
                return False
            curr = curr.children[idx]
        return curr.endOfWord


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        trie = Trie()
        for w in wordDict:
            trie.insert(w)

        result = []

        def backtrack(start, path):
            if start == len(s):
                result.append(" ".join(path))
                return

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if trie.search(word):
                    path.append(word)
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])
        return result