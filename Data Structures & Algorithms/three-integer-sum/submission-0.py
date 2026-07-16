class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        triplets = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            to_find = -nums[i]
            j = i + 1
            k = n - 1
            while j < k:
                current_sum = nums[j] + nums[k]
                if current_sum > to_find:
                    k-=1
                elif current_sum < to_find:
                    j += 1
                else:
                    triplets.append([nums[i] , nums[j] , nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
        return triplets