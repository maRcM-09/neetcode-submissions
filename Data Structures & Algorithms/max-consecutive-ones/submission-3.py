class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_sub = 0
        sub = 0
        for num in nums:
            if num:
              sub += num
            else:
                sub = 0
            max_sub = max(sub, max_sub)                
        return max_sub