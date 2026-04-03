class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)
        dis = 0
        for ch in arr:
            if freq[ch] == 1:
                dis+=1
                if dis == k:
                    return ch
        return ""

        