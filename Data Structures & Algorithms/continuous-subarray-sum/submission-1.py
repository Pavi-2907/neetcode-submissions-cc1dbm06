class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n):
            total = nums[i]
            for j in range(i+1,n):
                total+=nums[j]
                if total % k == 0:
                    return True
        return False