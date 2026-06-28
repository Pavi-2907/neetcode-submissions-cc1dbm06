class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        freq = Counter(nums)
        for num,count in freq.items():
            if count == 1:
                res.append(num)
        return res
        