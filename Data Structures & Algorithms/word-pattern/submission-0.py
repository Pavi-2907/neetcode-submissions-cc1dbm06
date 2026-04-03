class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        char = {}
        words_to = {}
        for ch,word in zip(pattern,words):
            if ch in char and char[ch]!=word:
                return False
            if word in words_to and words_to[word]!=ch:
                return False
            char[ch] = word
            words_to[word] = ch
        return True

        
        