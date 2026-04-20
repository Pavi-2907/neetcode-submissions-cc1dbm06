class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        for char in range(len(s)):
            new = s[:char] + s[char+1:]
            if new == new[::-1]:
                return True
        return False
        