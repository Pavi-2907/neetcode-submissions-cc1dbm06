class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s = sorted(nums1+nums2)
        n = len(s)
        mid = n // 2
        if n%2==0:
            return (s[mid-1] + s[mid]) / 2
        else:
            return float(s[mid])
        