class Solution:
    def minOperations(self, s: str) -> int:
        countA = 0 #start 0
        countB = 0 #start 1
        for i,ch in enumerate(s):
            if i%2==0:
                if ch!='0':
                    countA+=1
            else:
                if ch!='1':
                    countA+=1
            if i%2==0:
                if ch!='1':
                    countB+=1
            else:
                if ch!='0':
                    countB+=1
        return min(countA,countB)

        