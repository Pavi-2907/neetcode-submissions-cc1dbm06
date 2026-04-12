class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = Counter(nums)
        op = 0
        for count in freq.values():
            if count == 1:
                return -1
            op+=math.ceil(count/3)
        return op
        