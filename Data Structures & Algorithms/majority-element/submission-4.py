class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        freq = Counter(nums)
        for num,count in freq.items():
            if count > n//2:
                return num
        