class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        L = 0
        Lmax , Rmax = 0,0
        cursum = 0
        maxsum = nums[0]
        for R in range(len(nums)):
            if cursum < 0:
                cursum = 0
                L = R
            cursum += nums[R]
            if cursum > maxsum:
                maxsum = cursum
                Lmax , Rmax = L , R
        return maxsum