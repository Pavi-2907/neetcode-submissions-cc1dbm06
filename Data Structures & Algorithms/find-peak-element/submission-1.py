class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i,num in enumerate(nums):
            if num == max(nums):
                return i
        return -1
        