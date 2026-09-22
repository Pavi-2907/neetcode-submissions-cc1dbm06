class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        rep = mis = -1
        for i in range(1,len(nums)+1):
            if freq[i] == 2:
                rep = i
            elif freq[i] == 0:
                mis = i
        return [rep,mis]