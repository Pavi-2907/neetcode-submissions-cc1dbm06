class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ch_count = Counter(chars)
        tot_count = 0
        for word in words:
            word_count = Counter(word)
            if all(word_count[c] <= ch_count[c] for c in word_count):
                tot_count+=len(word)
        return tot_count
        