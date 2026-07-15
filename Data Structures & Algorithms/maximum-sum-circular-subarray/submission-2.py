class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        maximum = curmax = nums[0]
        minimum = curmin = nums[0]

        for num in nums[1:]:
            curmax = max(num , curmax+num)
            maximum = max(curmax, maximum)

            curmin = min(num , curmin+num)
            minimum = min(curmin, minimum)
        if maximum < 0:
            return maximum
        
        return max(maximum , total - minimum)