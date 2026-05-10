class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        positive = []
        for x in nums:
            if x > 0:
                positive.append(x)

        negative = []
        for x in nums:
            if x < 0:
                negative.append(x)
        
        res = []
        i = j = 0
        while i < len(positive) and j < len(negative):
            res.append(positive[i])
            res.append(negative[j])
            i+=1
            j+=1
        return res
        