class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = Counter(text)
        return min(freq['b']//1,freq['a']//1,freq['l']//2,freq['o']//2,freq['n']//1)
        