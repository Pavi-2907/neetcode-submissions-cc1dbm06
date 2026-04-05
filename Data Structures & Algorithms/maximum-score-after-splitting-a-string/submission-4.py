class Solution:
    def maxScore(self, s: str) -> int:
        s = s.strip('"')
        tot_one = s.count('1')
        left_zero = 0
        right_one = tot_one
        max_score = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                left_zero+=1
            else:
                right_one-=1
            score = left_zero + right_one
            max_score = max(max_score,score)
        return max_score
        