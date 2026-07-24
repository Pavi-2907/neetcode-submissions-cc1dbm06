class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1_count = Counter(s1)
        for i in range(len(s2)-n+1):
            if Counter(s2[i:i+n]) == s1_count:
                return True
        return False