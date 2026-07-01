class Solution:
    def ladderLength(self, s: str, e: str, words: List[str]) -> int:
        q = deque()
        q.append((s, 1))
        
        st = set(words)
        
        st.discard(s)
        
        while q:
            word, steps = q.popleft()
            
            if word == e:
                return steps
            
            for i in range(len(word)):
                
                for ch in range(ord('a'), ord('z') + 1):
                    new_word = word[:i] + chr(ch) + word[i + 1:]
                    
                    if new_word in st:
                        st.discard(new_word)
                        q.append((new_word, steps + 1))
                        
                        
                    
        return 0
            
            
        