class Solution:
    def romanToInt(self, s: str) -> int:
        val = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        tot = 0
        for i in range(len(s)):
            if i+1 < len(s) and val[s[i]] < val[s[i+1]]:
                tot-=val[s[i]]
            else:
                tot+=val[s[i]]
        return tot
        