class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        freq = Counter(nums)
        for num,count in freq.items():
            if count > len(nums) // 3:
                res.append(num)
        return res
        