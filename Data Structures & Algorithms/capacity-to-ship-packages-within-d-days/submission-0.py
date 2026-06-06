class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left,right = max(weights),sum(weights)
        while left < right:
            mid = (left + right) // 2
            need , cur_sum = 1,0
            for w in weights:
                if cur_sum + w > mid:
                    need+=1
                    cur_sum = w
                else:
                    cur_sum+=w
            if need <= days:
                right = mid
            else:
                left = mid + 1
        return left
        