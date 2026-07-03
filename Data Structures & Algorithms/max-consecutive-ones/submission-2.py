class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_sub = 0
        sub = 0
        for num in nums:
            if num:
              sub += num
              max_sub = max(sub, max_sub)
            else:
                sub = 0
        return max_sub