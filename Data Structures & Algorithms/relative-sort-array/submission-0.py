class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = {}

        for num in arr1:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        res = []
        for num in arr2:
            res += [num] * freq[num]
            freq[num] = 0
            
        for num in sorted(freq.keys()):
            if freq[num] > 0:
                res += [num] * freq[num]

        return res
        