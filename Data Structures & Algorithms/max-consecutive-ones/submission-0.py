class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_sub = 0
        sub = 0
        for i in range(len(nums)):
            sub += nums[i]
            if sub > max_sub:
                max_sub = sub
            elif nums[i] == 0:
                sub = 0
        return max_sub