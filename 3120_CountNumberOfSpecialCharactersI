class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chars = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
        word_to_set = set(word)
        count = 0
        
        for c in chars:
            if c in word_to_set and c.upper() in word_to_set:
                count += 1

        return count
        
