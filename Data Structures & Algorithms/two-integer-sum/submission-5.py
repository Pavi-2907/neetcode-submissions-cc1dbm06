class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hash_map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in Hash_map:
                return [Hash_map[diff],i]
            Hash_map[nums[i]] = i
    
        
        