class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        for i,num in enumerate(s):
            if freq[num] == 1:
                return i
        return -1