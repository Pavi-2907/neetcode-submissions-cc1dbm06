class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num in nums1:
            idx = nums2.index(num)
            grt = -1
            for j in range(idx+1,len(nums2)):
                if nums2[j] > num:
                    grt = nums2[j]
                    break
            res.append(grt)
        return res



        