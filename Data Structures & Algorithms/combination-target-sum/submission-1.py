class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combination = []
        res = []
        def dfs(i, current_sum):
            if current_sum == target:
                res.append(combination[:])
                return
            if i >= len(nums) or current_sum > target:
                return
            # Option 1: Include nums[i] and stay at index i
            combination.append(nums[i])
            dfs(i, current_sum + nums[i])
            # Option 2: Backtrack and move to next index
            combination.pop()
            dfs(i + 1, current_sum)
            
        dfs(0, 0)
        return res