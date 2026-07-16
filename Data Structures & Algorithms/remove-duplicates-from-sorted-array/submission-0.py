class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        table = {}
        L = 1
        R = 1
        n = len(nums)

        while R < n:
            if nums[R] != nums[R-1]:
                nums[L]=nums[R]
                L+=1
            R+=1
        return L 
            