class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for num,count in freq.items():
            if count >= 2:
                return True
        return False
        