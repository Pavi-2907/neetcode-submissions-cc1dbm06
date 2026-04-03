class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        nums = []
        for r in grid:
            for x in r:
                nums.append(x)
        freq =  Counter(nums)
        rep = mis = -1
        for i in range(1,n*n+1):
            if freq[i] == 2:
                rep = i
            elif freq[i] == 0:
                mis = i
        return [rep,mis]
        