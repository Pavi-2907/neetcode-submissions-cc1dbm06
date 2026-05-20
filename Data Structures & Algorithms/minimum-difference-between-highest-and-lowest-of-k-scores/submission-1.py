class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_dif = float('inf')
        for i in range(len(nums)- k + 1):
            diff = nums[i + k -1] - nums[i]
            min_dif = min(min_dif,diff)
        return min_dif
        