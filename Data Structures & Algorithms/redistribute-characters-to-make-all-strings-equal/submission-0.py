class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        freq = Counter("".join(words))
        n = len(words)
        for count in freq.values():
            if count %n!=0:
                return False
        return True
        