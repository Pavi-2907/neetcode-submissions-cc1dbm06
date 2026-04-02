class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
       allow = set(allowed)
       count = 0
       for word in words:
        if all(ch in allow for ch in word):
            count+=1
       return count

        