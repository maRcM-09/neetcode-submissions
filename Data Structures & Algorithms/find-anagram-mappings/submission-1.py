class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m2 = {
            n2: i2 for i2,n2 in enumerate(nums2)
        }

        res = [0]*len(nums1)
        for i , numb in enumerate(nums1):
            res[i] = m2[numb]
        return res