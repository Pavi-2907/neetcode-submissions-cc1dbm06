class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        r1 = []
        for num in set1:
            if num not in set2:
                r1.append(num)
        r2 = []
        for num in set2:
            if num not in set1:
                r2.append(num)
        return [r1,r2]


        
        