class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left,right = max(nums),sum(nums)
        while left < right:
            mid = (left + right) // 2
            count,cur_sum = 1,0
            for num in nums:
                if cur_sum + num > mid:
                    count+=1
                    cur_sum = num
                else:
                    cur_sum+=num
            if count <= k:
                right = mid
            else:
                left = mid + 1
        return left    