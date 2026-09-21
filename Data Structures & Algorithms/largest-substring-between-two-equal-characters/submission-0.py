class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        res = -1
        for i,ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            else:
                res = max(res,i-first[ch]-1)
        return res
        