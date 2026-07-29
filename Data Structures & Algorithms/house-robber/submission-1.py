class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1]*(len(nums))
        def dp(i):
            if i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]
            skip = dp(i+1)
            rob = nums[i] + dp(i+2)
            cache[i] = max(skip , rob)
            return cache[i]
        return dp(0)