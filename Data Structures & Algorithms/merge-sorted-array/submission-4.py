class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        length = m + n
        while j < n and i < m + n:
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                nums1[i+1 : j+m+1] = nums1[i:m+j]
                nums1[i] = nums2[j]
                j+=1
        while j < n:
            nums1[m+j] = nums2[j]
            j+=1


        