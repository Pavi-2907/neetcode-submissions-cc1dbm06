class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sort_word = sorted(freq.items(),key=lambda x:x[1],reverse=True)
        return [item[0] for item in sort_word[:k]]
        