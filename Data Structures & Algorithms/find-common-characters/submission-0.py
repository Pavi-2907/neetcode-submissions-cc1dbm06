class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        com = Counter(words[0])
        for word in words[1:]:
            com &= Counter(word)
        res = list(com.elements())
        return res
        