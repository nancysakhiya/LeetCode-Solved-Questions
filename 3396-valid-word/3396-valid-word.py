class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowel = False
        consonant = False

        for c in word:
            if c.isalpha():
                if c.lower() in "aeiou":
                    vowel = True
                else:
                    consonant = True
                
            elif not c.isdigit():
                return False

        return vowel and consonant
