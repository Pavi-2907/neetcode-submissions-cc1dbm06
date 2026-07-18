class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        i = j = 0
        while j < len(abbr):
            if abbr[j].isalpha():
                if i >= len(word) or word[i] != abbr[j]:
                    return False
                i+=1
                j+=1
            else:
                if abbr[j] == '0':
                    return False
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j+=1
                i+=num
        return i == len(word) 
        